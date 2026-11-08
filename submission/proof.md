# PFD-15: few-copy Fourier decoding with linear quantum space

This is a research construction, not a claim of literature priority or
hosted acceptance. It uses standard Fourier states, Grover reflections
and phase estimation. The contribution being audited is the complete
uniform compilation, phase convention and joint resource accounting.

## Joint claim

For every N>=2 and every fixed s modulo N, let n=ceil(log2 N). From
exactly m=n+2 independent clean DCP source copies, the fixed algorithm
below recovers the entire secret with probability at least 241/320>3/4.
On every branch its joint envelopes are

    T = O(2^(n/2) n^2 log(n+2)),
    S_C = O(n^2),  S_Q = O(n),  Q = n+2.

For n>=2 the supported representative uses log2 n in place of log(n+2).
Its time index is 1, and the three other resource indices are 0.
There is no malformed-copy guarantee beyond fraction zero. All source
acquisitions, bad extraction outcomes and implementation errors remain
in the unconditional claim. There are no retries or free postselection.

The n=1 branch acquires exactly three copies. Fourier-transform the
one-bit data register by H and measure its label. If any label is one,
measure that copy's phase qubit in X and output its parity; otherwise
output zero. Acquire all three copies even after obtaining an answer.
For either secret success is at least 7/8. Everything below concerns n>=2.

## 1. Fourier-label extraction without a general-modulus QFT oracle

Put omega=exp(2 pi i/N) and

    |chi_a> = N^(-1/2) sum_u omega^(a u)|u>,
    |p_a(s)> = (|0>+omega^(a s)|1>)/sqrt(2).

After X on the first source register, the source state is exactly the
uniform mixture of |p_a(s)> tensor |chi_a>, for a in Z_N. This follows
by expanding the supplied coset-state mixture in the Fourier basis;
cross terms vanish by character orthogonality. Independent source copies
give independent latent labels, without assuming a source purification.

The known modular shift L:u -> u-1 mod N has eigenvalue omega^a on
|chi_a>. Extend the shift by the identity on invalid n-bit encodings.
Its power L^(2^r) is one modular subtraction by the known constant
2^r mod N, not 2^r separate source or shift calls.

Let

    q_lab = n + ceil(log2 m) + 10,
    M_lab = 2^q_lab.

Our phase-estimation convention is

    PE(U) = (F_M^dagger tensor I)
            (sum_j |j><j| tensor U^j) (H^q tensor I),
    F_M|j> = M^(-1/2) sum_l exp(2 pi i j l/M)|l>.

The middle operation uses controlled powers U^(2^r). The power-of-two
Fourier transform has q Hadamards, q(q-1)/2 controlled dyadic phases
and a bit reversal, obtained by factoring its binary output amplitudes.
Thus its decomposition and gate generation are polynomial in q.

Perform ordinary q_lab-bit phase estimation on L. Measure j and set
a_hat=floor(N j/M_lab+1/2) mod N, fixing ties upward. Discard
the data and estimation registers but retain the phase qubit.

For phase alpha, the phase-estimation probability at j is

    |M_lab^(-1) sum_(r=0)^(M_lab-1)
          exp(2 pi i r(alpha-j/M_lab))|^2.

If d_j is circular distance between alpha and j/M, then for d_j>0
the probability is at most 1/(4 M^2 d_j^2), using
|sin(pi x)|>=2|x| for |x|<=1/2. At most four grid points occur in
each unit-width bin of M d_j. Consequently, for M e>=2,

    Pr[d_j>=e] <= 1/(floor(M e)-1).                 (1)

Taking e=1/(2N), M_lab>=1024 m N gives error at most
1/(512m-1)<=1/(256m). Thus the probability any of the m extracted
labels differs from its latent value is at most 1/256.

This is an unconditional coupling with ideal uniform labels. We do
not condition on correct extraction and then claim the labels remain
uniform. Conditional on each latent label, extraction touches only
its product data register, so its phase qubit is unchanged. Circuit
approximation is budgeted separately below.

## 2. The ideal fiber readout and its ensemble success

With public labels a_1,...,a_m define

    K=2^m,  f(x)=sum_i a_i x_i mod N,
    eta_t = |{x:f(x)=t}|,
    |u_t> = eta_t^(-1/2) sum_(f(x)=t) |x>.

Compute f into a fresh n-bit register T, without measuring x or T.
On ideal labels the state is

    sum_(t:eta_t>0) sqrt(eta_t/K) omega^(s t)|u_t>|t>.

A phase-correct controlled unpreparation of each |u_t> to zero would
leave the target state

    |zeta_s> = sum_t sqrt(eta_t/K) omega^(s t)|t>.

Measurement in the Fourier basis has true-secret probability

    p_a = (sum_t sqrt(eta_t))^2/(NK).

Let Z_a=sum_t eta_t^2. Holder gives
(sum_t sqrt(eta_t))^2 >= K^3/Z_a. Distinct binary selectors have a
difference coefficient +1 or -1, so under independent uniform labels
their sums collide modulo N with probability 1/N, for any N. Therefore

    E Z_a = K + K(K-1)/N,
    E p_a >= K^2/(N E Z_a) = K/(N+K-1) >= 4/5.   (2)

The last inequality uses m=n+2, hence K>=4N. This holds for every
fixed secret. Empty and badly unbalanced fibers have not been omitted.

This measurement/interface is inherited from the Bacon-Childs-van Dam
PGM construction and our earlier dcp-exa-structural-route/PROOF.md,
Section 4. The present task is its charged implementation, not a new
information-theoretic success statement.

## 3. A phase-correct square-root Grover rotation

Let |a0>=K^(-1/2) sum_x |x>, Pi_t project onto f(x)=t, and define

    R_a0 = 2|a0><a0|-I,
    R_bad,t = I-2 Pi_t,
    G_t = R_a0 R_bad,t.

These are known circuits. The first is a reflection about a known
uniform state, not about the unknown supplied DCP phase state.

For 0<eta_t<K, put sin(theta)=sqrt(eta_t/K), and let |v_t> be the
normalized uniform complement. In the basis (u_t,v_t),

    |a0> = (sin(theta),cos(theta)),
    G_t = [[cos(2theta),sin(2theta)],
           [-sin(2theta),cos(2theta)]].

The vectors e_+=(u_t+i v_t)/sqrt(2) and e_-=(u_t-i v_t)/sqrt(2)
have eigenphases 2theta and 2pi-2theta. On the circle with the cut at
zero, define f_phase(phi)=i exp(-i phi/2), for 0<phi<2pi.
Applying this function to G_t maps |a0> to |u_t> with exactly the
same positive phase for every occupied fiber. This follows from

    <e_+|a0> = -i exp(i theta)/sqrt(2),
    <e_-|a0> =  i exp(-i theta)/sqrt(2).

For eta_t=K, the relevant eigenvalue is -1 and the same operation is
the identity on |a0>=|u_t>. Empty fibers carry no amplitude in Section 2.
No normalization of arbitrary unknown vectors outside the uniform-fiber
span is asserted. Target T remains present, preserving orthogonality
between different fibers.

## 4. Explicit phase-estimation filter and error

Use

    q_G = ceil(m/2)+15,   M_G=2^q_G.

Let PE_G be ordinary phase estimation of G_T on a fresh q_G-bit
register, with T retained coherently. This Grover phase register is
never measured; it is coherently uncomputed. The known phase diagonal is

    D|j> = i exp(-i pi j/M_G)|j>.

Define U_tilde=PE_G^dagger D PE_G. Its inverse is obtained by
reversing this exact known circuit. D is a product of fixed dyadic
one-qubit phases and a common global i, which can be implemented on
a known auxiliary qubit if a literal phase convention is wanted.
It has no label- or fiber-dependent unknown phase.

For a G eigenphase 2pi alpha, PE leaves the data eigenvector unchanged.
Its filter error squared is exactly

    sum_j P_alpha(j) |i exp(-i pi j/M_G)
                       -i exp(-i pi alpha)|^2.              (3)

Every relevant alpha lies in [a_cut,1-a_cut], where
a_cut=1/(4 sqrt(K)), since theta>=1/sqrt(K) and pi<4. With d_j the
circular distance, the summand's phase difference squared is at most
pi^2 d_j^2 plus four times the indicator of wrapping across the cut.
Such wrapping requires d_j>=a_cut. The pointwise probability bound above
also gives E d_j^2<=1/(4M_G). Applying (1),

    error^2 <= 4/M_G + 4/(floor(M_G a_cut)-1)
             <= 2^(-15) + 4/(2^13-1) < 1/1024.             (4)

Here m>=3 suffices. Thus the norm error is less than 1/32 uniformly
on the relevant eigenvectors and their span. Different eigenvectors
and target registers remain orthogonal, so this is also a uniform
bound on arbitrary superpositions in the stated uniform-fiber span,
with references attached to that span.

Apply U_tilde^dagger to the selector and estimation registers, then
H^m to the selector. Equation (4) and unitarity give norm error at
most 1/32 from |0^m,0^q_G>|zeta_s>. No success flag is postselected.
Any residual selector/estimation state is discarded only after this
whole-state error has been charged.

The filter uses exactly 2(M_G-1) controlled applications of G or its
inverse, plus polynomially many QFT and phase gates. Powers of G are
implemented by that many repetitions; they are not fast-forwarded or
charged as unit-cost high powers.

## 5. Final arbitrary-modulus Fourier measurement

To measure |zeta_s> in the N-point Fourier basis, reuse the shift
phase-estimation measurement of Section 1 on T with M_lab grid points.
For each Fourier eigenstate it reports the correct index except with
probability <=1/(256m)<=1/256. For an arbitrary target state, discarding
the target makes this a classical mixture over its Fourier components.
The same bound therefore compares its outcome law with ideal Fourier
measurement. No arbitrary-modulus QFT unitary is supplied for free.

## 6. Finite gates, precision, and total success

All subset-sum arithmetic, comparisons, diffusion reflections and
controlled powers of G use exact Clifford+T gates. The only approximate
gates are fixed dyadic rotations in the polynomially many source,
filter and readout QFTs and in D.

For a concrete uniform allocation, let

    A=10(m+4)(q_lab+q_G+2)^2.

After ordinary controlled-phase decomposition this exceeds the number
of non-Clifford one-qubit rotations. Synthesize each to error at most
1/(128A) up to a global phase, and use actual reversed words for inverse
circuits. All these one-qubit words are applied unconditionally after
the controlled-phase decomposition, with a fixed sequence depending
only on n. Their global factors combine into one common circuit phase,
never a target-, label- or eigenphase-dependent phase. Controlled Grover
calls themselves are exact and include the diffusion sign above.
Uniform finite-gate compilation has work
polynomial in the required precision bits. Those bits are O(log(n+2));
gate descriptions are generated and discarded one at a time. These
costs and classical compilation are counted, not treated as an oracle.

The complete adaptive instrument then differs from the ideal-gate one
by outcome error at most 1/128. The source-label coupling costs at most
1/256, final rounding at most 1/256, and the fiber-filter norm error
costs at most 1/32 in any outcome probability. For normalized pure
vectors this follows from 1-|<u|v>|^2 <= ||u-v||^2; mixture averaging
and subsequent channels cannot increase the trace-distance bound.
Thus (2) gives

    P[correct] >= 4/5 - 1/256 - 1/256 - 1/32 - 1/128
                = 241/320 > 3/4.                            (5)

All allowances are unconditional. There is no division by a heralded
probability. Wrong label estimates still follow the same bounded circuit.

## 7. Uniform arithmetic, addressing and storage

An in-place controlled modular addition by a known constant can be
implemented in O(n) exact gates and O(n) reusable scratch. One explicit
construction evaluates F_c(u)=(u+c mod N) for u<N and F_c(u)=u otherwise:
compute an (n+1)-bit ripple sum, compare/subtract N once, and select the
correct result, with an additional valid-range test. Controlled addition
selects F_c(u) or u. Each Boolean evaluation has O(n) intermediate bits.
Compute/copy/uncompute, SWAP, then XOR an evaluation of F_-c clears the
old input. This is a permutation on every encoding, including invalids.

Compute f(x) by m controlled modular additions into one n-bit register.
Each addition clears its scratch before the next. A marking reflection
computes f, compares with the retained target, applies its controlled
phase, and reverses all arithmetic. It costs O(mn) gates and O(n+m)
qubits; it does not retain m addition histories.

The controlled diffusion reflection must include its global sign.
Use H^m around a zero-state phase flip and apply Z to the phase-estimation
control to obtain controlled (2|a0><a0|-I), rather than its negative.
Multi-controlled phases use clean AND chains and their reverses. This
costs O(m) gates and O(m) scratch. Omitting the sign would change the
Grover eigenphases and invalidate Section 3.

There are O(2^(n/2)) Grover calls, each costing O(n^2) gates. The
classical controller stores N, the m n-bit labels, loop counters and a
streamed descriptor, for O(n^2) bits. Every addressed bit or gate pays
O(log(n+2)) address work under the challenge model. Gate generation,
constant reads and ripple control can be streamed within the same
O(n^2 log(n+2)) allowance per Grover call. The exponentially long loop
counter has only O(n) bits. No exponential circuit list is stored.

Here the controller is specified at the bit level. Keep the fixed-many
short wire-index fields and current descriptor on sequential work tapes.
Their additions, offsets and increments use O(log(n+2)) local bit steps,
not a fresh arbitrary indexed lookup for each bit of their own addresses.
Every genuine indexed coefficient access and every indexed quantum gate
still pays the required O(log(n+2)) debit. A template needs only a constant
number of such accesses per emitted gate. Read coefficients as binary
fields; compute inverse constants N-a_i once, and do not charge a long
integer shift or division as a unit-cost operation inside the Grover loop.
Maintain each coefficient-row base by adding n between rows, instead
of multiplying the row index by n separately for every accessed bit.

The generator in arithmetic.py streams one O(n)-gate modular-addition
subroutine at a time. Materializing that small subroutine takes
O(n log(n+2)) classical bits, within O(n^2). A full Grover word is collected
only in the finite diagnostic, not in the asymptotically specified
controller. Its exponentially long repetition loop is never materialized.
The sequential-field accounting follows the published saved-copy proof
b45accfa-78b4-45f0-a9aa-b8e82ed22fd4, Section 5.1; this use is recorded in
sources.md. That submission's judgment is not a proof premise.

Source/readout shifts and the approximate QFTs have polynomial total
work, hence are asymptotically absorbed in 2^(n/2)n^2 log(n+2). Their
uniform compiler needs only polynomial-logarithmic scratch beyond the
listed registers, also absorbed in O(n^2) classical bits. Quantum
registers comprise m retained phase qubits, the n-bit target, one phase
estimation register of O(n) bits, and O(n) arithmetic/synthesis scratch.
During source extraction, only one n-bit data register and its O(n)
phase-estimation register are live in addition to retained phase qubits.
Thus peak accessible quantum memory is O(n).

Exactly m original source copies are acquired. The entire schedule is
fixed and bounded for every measured label list. There are no restart,
verification-copy or successful-only resource omissions.

## 8. What the sample and space claims mean

At N=2^n, a procedure capped at m copies on every branch needs m>=n
for worst-secret success at least 2/3, even without a work restriction.
Indeed, the
Fourier labels form secret-independent orthogonal blocks. Conditioned
on one label block, m copies occupy a K=2^m dimensional phase space.
For any N-outcome POVM, averaging over uniform secrets gives

    (1/N) sum_s Tr(M_s |psi_s><psi_s|)
      <= (1/N) sum_s Tr(M_s) = K/N.

Off-diagonal label-block entries of a measurement never contribute to
the input probabilities, so this bounds arbitrary measurements on the
original mixed copies as well. If m<n, K/N<=1/2. Thus n+2 is within
two copies of this necessary bound, not a proof of exact optimality.

The source itself supplies an accessible n+1-qubit register, making
linear peak quantum space optimal in order under the stated accounting.
No matching lower bound for the O(n^2) classical storage is asserted.
The exponential work remains the price of this few-copy construction.

## Status

Independent mathematical review has not yet been performed. This package
requests hosted joint review of the five claims.
Finite diagnostics check components and phase conventions; they cannot
execute the full asymptotic circuit or certify its bounds. Comparison
with public rows is separate from the proof and supplies no premise.
