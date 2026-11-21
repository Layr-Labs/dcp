# Robust coherent Grover search with a retained linear DCP batch

## 1. Theorem and fixed configuration

For every integer N>=2 and s in Z/NZ, define n=ceil(log2 N),
q=128(n+1), r=q/4, m=n+3, L=2^m, and

    k = floor(3 sqrt(L)/4) = isqrt(9 * 2^(n-1)).

Here isqrt is exact integer square root. Algorithm RCG-1/4 below acquires
exactly q source registers once. Under Section 2's static error model it
outputs the entire s with unconditional probability strictly greater than
5/6. On every execution branch, simultaneously,

    T(N,s) = O(sqrt(N) n^2 log2(n+2)),
    S_C(N,s) = O(n) classical bits,
    S_Q(N,s) = O(n^2) qubits,
    Q(N,s) = 128(n+1) = O(n).

The constants are independent of N, s and the allowed joint source state.
Supported asymptotic envelopes for n>=2 are
[2^(n/2) n^2 log2 n, n, n^2, n], with growth indices [1,0,0,0].
The operational bound covers n=1. The guaranteed malformed fraction is 1/4.

The runtime improves the N search factor in our predecessor RCR-1/4 to
sqrt(N), preserving the sample count, asymptotic spaces and error model.
The time growth index is STILL 1, not 1/2: the coefficient of n in the
exponent has changed, not its power. This does not reach 2^{O(n^{1/3})}
and is not a claim to improve known subexponential DCP algorithms.

## 2. Exact error model and source access

All q registers, each one first qubit and an n-qubit residue, are acquired
before the search. Their joint density operator omega is fixed. There is an
unknown fixed subset B, |B|<=floor(q/4), whose complementary JOINT marginal
is exactly rho_s tensor-powered over g=q-|B| good positions. Here

    rho_s = (1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    |psi_(x,s)> = (|0,x> + |1,(x+s) mod N>)/sqrt(2).

The malformed registers and their correlations with all good registers can
be arbitrary subject to that exact joint marginal. They may depend on N,s
and include residue states y>=N. The source does not adapt to measurement
feedback. Every register counts toward Q. This is a fraction of the acquired
batch, not an independent per-copy error probability. Clean inputs correspond
to B empty. Correct individual marginals without the joint product promise
would not suffice and are not claimed.

The algorithm has no source labels x, purification, source inverse, or coherent
source control. A reference system introduced below is purely an analysis
device; it is inaccessible and not an algorithm resource.

## 3. Threshold projectors and the actual phase oracle

For 0<=t<N define a permutation on the FULL residue space:

    f_t(y) = (y-t) mod N if y<N, and y otherwise.

Let C_t apply f_t if the first qubit is 1, and otherwise do nothing. Define
V_t=(H tensor I) C_t and W_t=V_t tensor-powered over all q source registers.
Let D_r project onto computational basis states with at most r first-qubit
ones, unrestricted on all residue registers. Set

    P_t = W_t^dagger D_r W_t.

These are orthogonal projectors, including on malformed inputs. The candidate
register has m=n+3 qubits and L basis labels. The actual joint oracle is

    O = sum_(t<N) |t><t| tensor (I-2P_t)
        + sum_(N<=t<L) |t><t| tensor I.                 (1)

It is a unitary involution. Its construction does NOT enumerate its L blocks:

1. Reversibly compute v=[t<N] from the quantum candidate into a flag. For
   arithmetic, use its low n bits u. Apply V_u to each source register,
   using u as a quantum input to modular arithmetic. When u>=N use the
   identity permutation before H; this defines V_u everywhere.
2. Reversibly count the q first-qubit ones, compute h=[count<=r], apply CZ
   to v and h, then reverse the comparison and counting circuit.
3. Reverse every V_u and erase v by reversing its comparison.

For t<N this gives I-2P_t; for all other labels the middle phase is identity
and the other operations cancel. All scratch returns to zero on every input,
even when t and the batch are entangled. No first-qubit outcome, weight,
threshold flag or candidate label is measured during this process.

The diffusion operation on the candidate only is

    D = (2|a><a|-I) tensor I,  |a> = H^tensor m |0^m>.

This is an exact Clifford+T circuit: conjugate 2|0^m><0^m|-I by H gates.
The phase reflection can be synthesized with X, a multi-controlled Z and
an overall minus sign. An overall sign is physically irrelevant; choosing
that representative makes the analysis exact. A multi-controlled Z uses a
linear chain of Toffoli-computed ANDs, a Z phase and uncomputation, O(m)
gates and O(m) clean scratch. It never reflects about an unknown source state.

    RCG-1/4(N):
        n := bit_length(N-1)
        q := 128(n+1); r := q/4; m := n+3; L := 2^m
        k := isqrt(9 * 2^(n-1))
        acquire and retain q source registers
        initialize m candidate qubits to |a> with Hadamards
        repeat exactly k times:
            apply O from (1) to candidate and retained batch
            apply D to candidate
        measure candidate t in the computational basis
        output t if t<N, and otherwise output 0

There are no restarts, postselection or additional sample acquisitions. The
fallback is total and cannot reduce the probability of measuring the true s.

## 4. Projector bounds on the original batch

On an ideal source component, C_t produces

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

At t=s, H makes every good first qubit zero. A joint extension of a marginal
supported on a subspace is supported on that subspace tensor the other
systems: if E projects onto its complement, Tr(E omega)=0 implies
E omega^(1/2)=0. This applies to arbitrary correlations with bad registers.
There are at most r bad first bits, hence

    P_s omega P_s = omega.                               (2)

For t!=s, the two residue states displayed above are distinct. The first-qubit
marginal is I/2 before and after H. The good registers' exact product marginal
therefore gives g independent fair first bits under W_t. No assumptions on
bad outcomes are needed: total weight<=r implies good-position weight<=r.
Thus

    Tr(P_t omega) <= Pr[Bin(g,1/2)<=q/4].                 (3)

For completeness, independent fair bits X_j satisfy
E exp(lambda(1/2-X_j))=cosh(lambda/2)<=exp(lambda^2/8).
Indeed log cosh u<=u^2/2 follows by integrating tanh u<=u for u>=0;
both sides are even. Markov's inequality and lambda=4a/g, for a>=0,
give Pr[sum X_j<=g/2-a]<=exp(-2a^2/g). Here g>=3q/4 and

    2(g/2-q/4)^2/g = g/2-q/2+q^2/(8g) >= q/24.

The expression is increasing for g>=3q/4, because its derivative is
1/2-q^2/(8g^2)>0; its value at 3q/4 is q/24. Therefore

    Tr(P_t omega) <= exp(-q/24) =: eta  for t!=s.         (4)

These bounds concern the ORIGINAL joint state only. The actual evolving
batch need not retain independent good marginals.

## 5. Hybrid bound for coherent reuse

Choose any mathematical purification |Omega> of omega, including its
inaccessible reference. Equations (2),(4) give P_s|Omega>=|Omega> and
||P_t|Omega>||<=sqrt(eta) for t!=s. For any normalized candidate vector
|alpha>=sum alpha_t|t>, define the ideal comparison oracle

    O_s = (I-2|s><s|) tensor I.

Orthogonality of candidate labels, exact preservation at s and identity on
dummy labels imply

    ||(O-O_s)(|alpha> tensor |Omega>)||^2
        = 4 sum_(t<N,t!=s) |alpha_t|^2 ||P_t|Omega>||^2
        <= 4 eta.                                      (5)

This is only a bound on product states with the ORIGINAL |Omega>, not an
operator-norm approximation on arbitrary states. That is sufficient. Put
U=DO and U_s=DO_s. The exact noncommutative telescoping identity is

    U^k-U_s^k = sum_(j=0)^(k-1) U^(k-1-j)(U-U_s)U_s^j.

Every ideal prefix U_s^j preserves the batch |Omega> and changes only the
candidate vector. Every actual suffix is unitary. Applying (5) term by term
proves the Euclidean distance between actual and ideal final purifications is

    ||U^k(|a>|Omega>)-U_s^k(|a>|Omega>)||
        <= 2k sqrt(eta) = 2k exp(-q/48).                 (6)

No independence is asserted for actual intermediate states; no sample reset,
reflection about |Omega>, inverse preparation, or source oracle is invoked.

## 6. Ideal search and a uniform success constant

Let sin(theta)=1/sqrt(L), 0<theta<pi/2, and let |b> be the uniform
superposition over all L-1 labels except s. In the ordered basis (|s>,|b>),
|a>=(sin(theta),cos(theta)), O_s=diag(-1,1), and direct multiplication gives

    D O_s = [[cos(2theta), sin(2theta)],
             [-sin(2theta), cos(2theta)]].

Induction shows the marked amplitude after k iterations is
sin((2k+1)theta). This explicitly proves the used Grover rotation formula.
We choose k with exact integer arithmetic, not numerical evaluation of theta.

Since L>=16 and k=floor(3sqrt(L)/4), let A=(2k+1)theta. The integral
formula for arcsin gives x<=arcsin x<=x/sqrt(1-x^2). Therefore

    A >= 3/2-1/sqrt(L) >= 5/4,
    A <= (3/2+1/sqrt(L))/sqrt(1-1/L) <= 7/sqrt(15).

Both endpoint inequalities remain valid with the floor. Using 3<pi<22/7,
7/sqrt(15)<11/6 and 9/28<1/3 gives |A-pi/2|<1/3. Since
cos z>=1-z^2/2, the ideal marked amplitude is strictly greater than 17/18.

The error in (6) is at most

    (3/2) 2^((n+3)/2) exp(-8(n+1)/3).

This decreases with integer n>=1: its successive ratio is
sqrt(2) exp(-8/3)<1. At n=1 it is 6 exp(-16/3)<1/32. The last
inequality is elementary: exp(16/3)>sum_(j=0)^12 (16/3)^j/j!>192,
where the finite inequality can be checked in rational arithmetic.

Project onto candidate label s and use contraction and the reverse triangle
inequality in (6). Actual marked amplitude norm is strictly greater than

    17/18-1/32 = 263/288.

Its squared norm is the UNCONDITIONAL measurement probability. Since
263^2=69169>69120=5*288^2/6, full-secret success is strictly greater than
5/6. This covers every N>=2, s and allowed mixed/correlated omega, including
small n and all malformed positions. Fallback outputs can only add success.

## 7. Uniform exact gates and charged classical work

All gates are exact Clifford+T with computational-basis final measurement.
There is no QFT, arbitrary-angle synthesis, QRAM or hidden oracle. Crucially,
quantum u is an OPERAND of explicit arithmetic gates, not a quantum address
into a table of candidate circuits.

Ripple comparisons, addition/subtraction and bitwise selection on O(n) bits
have O(n)-gate Boolean circuits with O(n) intermediate bits. For u<N, f_u
selects y-u when y<N and y>=u, y+N-u when y<N and y<u, and y otherwise.
Use O(n+1) intermediate bits to avoid overflow. For u>=N select y. Include
the source first-qubit condition in the selection. The inverse adds u modulo
N when valid and is identity otherwise; it has the same linear Boolean size.
Both u and y can be quantum inputs; these formulae are Boolean permutations
coherently controlled by u, not measurement-and-feedforward constructions.

Compute each Boolean gate reversibly into fresh scratch (NOT/XOR/AND via
X/CNOT/Toffoli), XOR the output into a target, and reverse the computation.
For a permutation, compute into zero output, swap input/output, and XOR-
compute the inverse to erase the old input. The control u is unchanged.
This implements each C_u with O(n) gates and O(n) clean reusable ancillas,
unitarily on the full residue and control spaces.

Toffoli has a constant-size exact Clifford+T realization. For bits a,b,c,

    4abc = a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c).

T and T^dagger phases on these parities, computed/uncomputed with CNOTs
and a reusable parity ancilla, implement CCZ. H conjugation on the target
gives Toffoli; T^dagger=T^7. Thus no synthesis error is being omitted.

Count q first bits in a ceil(log2(q+1))-bit counter by reversible controlled
increments, compare to r, apply the phase and uncompute. Increments and
comparison have O(log(q+1)) size with reusable carries, giving
O(q log(q+1)) gates and O(log(q+1)) scratch. The initialized counter never
overflows on reached inputs, and each reversible gate is unitary everywhere.
Candidate validity comparison and diffusion add O(n) gates/scratch.

Each iteration therefore has O(qn+q log(q+1)+n)=O(n^2) gates. The uniform
controller streams these regular ripple circuits using a constant number
of loop indices; inverses traverse the same gate pattern backwards. It does
not store a gate list. All wire addresses refer to O(n^2) allocated storage,
so each classically addressed gate costs O(log(n+2)) bit operations. Index
updates, reading constant bits of N,r and emitted gate specifications fit
this charge. Quantum candidate bits are always operated on with counted gates.
The outer repetition counter has O(n) bits and costs O(n log(n+2)) work per
update, which is absorbed in O(n^2 log(n+2)) per iteration.

The integer k is computed once by the binary digit-pair square-root algorithm:
scan the O(n)-bit radicand from high pairs, shift the partial remainder,
compare with/subtract the trial divisor, and append one root bit. There are
O(n) steps on O(n)-bit numbers, O(n^2) bit operations and O(n) storage;
including indexed accesses this is O(n^2 log(n+2)) work. This exact
preprocessing, construction of n,q,r, source acquisition and initialization
fit the same additive bound. No real arithmetic or advice is provided free.

## 8. Joint bounds and structured indices

Exactly q=128(n+1) source copies are acquired, costing q(n+1)=O(n^2).
There are exactly k=O(2^(n/2)) iterations, irrespective of the input state
or measurement outcome. Since 2^(n-1)<N<=2^n, also k=O(sqrt(N)). Counting
all charged work from Section 7, final measurement, comparison and output
proves T=O(sqrt(N) n^2 log2(n+2)) on every branch.

Quantum storage consists of q(n+1)=O(n^2) retained source qubits, n+3
candidate qubits, O(n) arithmetic/diffusion scratch, O(log(n+2)) counting
scratch and constant flags. All scratch can be reused. Classical storage
holds N,n,q,r,k, the repetition counter, a constant number of O(n)-bit
working integers, and O(log(n+2))-bit wire/loop indices: O(n) bits. No
classical outcomes from the batch or exponentially sized circuit are stored.
These counts include preparation, all malformed copies and all failure outcomes.

For n>=2, the supported bound for time is B_T=2^(n/2) n^2 log2 n;
log2 B_T=n/2+2log2 n+log2 log2 n. Its double logarithm divided by log2 n
tends to 1. The corresponding indices for n,n^2,n are all 0 because
log2 log2(n^c)=O(log log n). The exponential structured coefficient is the
exact rational 1/2, while the time score is the exact rational 1. Finite
n=1 is covered by the operational log2(n+2) bound. The fifth fraction is
1/4 under precisely Section 2's model and has no numeric score.

## 9. Attribution, external context and evidence limits

The protected challenge revision is 5f141ca57dc41fe431770ea153fc4c0af6a05aea;
the pinned verifier is 204fdf8fb640704da0a3972d97831de09bfb1c7a.
The baseline's single-register shift test is the original primitive. This
entry directly builds on our previous RCR-1/4 submission,
bea41c5b-5ac3-4e10-a882-9e74aef9aa64,
https://github.com/Layr-Labs/dcp/pull/1905 . It reuses its static marginal
model, retained batch, threshold projectors, support argument and reversible
arithmetic analysis. It replaces sequential measured tests with a coherent
controlled reflection and Grover search, sharpens the tail bound, and proves
a new hybrid/success analysis. This dependency is declared at submission.
No previous acceptance is a mathematical premise: every needed argument
is supplied here, and there are no prior_results references.

Grover search is established work: Lov K. Grover, "A fast quantum mechanical
algorithm for database search," https://arxiv.org/abs/quant-ph/9605043v3 .
The rotation formula actually used is derived in Section 6. Polynomial-sample
state detection is also established; see Ettinger and Hoyer,
https://arxiv.org/abs/quant-ph/9807029v1 and
https://arxiv.org/abs/quant-ph/9905099v1 . Known subexponential DCP-related
algorithms include Kuperberg, https://arxiv.org/abs/quant-ph/0302112v2,
and Regev, https://arxiv.org/abs/quant-ph/0406151v1 . These references give
context and credit, not imported unproved premises. This exponential-time
construction does not supersede their subexponential runtime results.
Novelty and frontier placement have not been established.

validation.py contains supplementary finite-dimensional simulations and
scalar/rational checks. Quantum simulations use explicitly TOY batches,
not q=128(n+1). Some purifications entangle bad registers with good ones
while preserving the exact product good marginal. These are selected cases,
not an exhaustive check of general correlations. Floating-point checks do
not prove asymptotic or universal inequalities. The submission is proof-based,
not a full hardware implementation or formal proof-assistant certificate.
Its hosted executable experiment plan is empty; mathematical evidence is
this self-contained proof.
