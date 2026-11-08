# Exact-gate Fourier-label extraction for every cyclic modulus

This auxiliary lemma uses the source and the charged computation model of
`../rules.md`. It is an extraction primitive, not by itself a complete DCP
algorithm. All logarithms in resource bounds are base two. Trace distance means
one half of the trace norm.

## Lemma and quantitative guarantee

Let N >= 2, n = ceil(log2 N), s in Z/NZ, and let q >= 1 be an integer
precision parameter, supplied in binary (or computed by the controller).
There is a uniform, bounded-duration channel E_(N,q), using one source copy,
which outputs a classical n-bit label K and one retained qubit. Its output on
rho_s has trace distance at most 2^(-q) from

    Omega_s = (1/N) sum_(k=0)^(N-1) |k><k| tensor |phi_(k,s)><phi_(k,s)|,
    |phi_(k,s)> = (|0> + exp(2 pi i k s/N)|1>)/sqrt(2).

More precisely, there is a conceptual uniform latent k such that the retained
qubit is exactly |phi_(k,s)> on every measurement branch, and the classical
label equals that k with probability at least 1 - 2^(-q), for every k.
Conditioning only on an observed label need not produce an exact pure qubit:
mislabelled branches can contribute. No claim of exactly uniform labels after
conditioning on successful extraction is needed or made.

With input and output included, the primitive has the following uniform
worst-case bounds, including gate generation, classical bit operations,
initialization, measurement, modular constants, addressing and source cost:

    T = O(n^2 (q + log(n+1)) log(n+q+2)),
    S_C = O(n + log(q+2)) bits,
    S_Q = O(n) qubits,
    Q = 1.

Absolute constants are independent of N, s, q and all outcomes. In particular,
the weaker bounds S_C = O(n+q), S_Q = O(n+q) also hold. All quantum gates are
exact Clifford+T gates. There is no approximate-rotation synthesis, real-number
oracle, arbitrary-modulus QFT, postselection or inverse source preparation.

## Exact spectral decomposition of the mixed source

Write omega = exp(2 pi i/N) and

    |chi_k> = (1/sqrt(N)) sum_(y=0)^(N-1) omega^(-k y) |y>.

For U|y> = |(y+1) mod N> on y<N, U|chi_k> = omega^k|chi_k>.
Expanding |x> and |x+s> in this basis and averaging over the inaccessible x
eliminates every k != l cross term, because
(1/N) sum_x omega^((k-l)x) equals 1 for k=l and 0 otherwise. Therefore exactly

    rho_s = (1/N) sum_k |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.

This identity is an analysis of a mixed state, not a request for its purification
or for the hidden x. The circuit never prepares |chi_k>.

## An explicit exact-gate phase estimator

Set ell = ceil(log2(4n)) and r = 512(q+ell). For j=0,...,n-1 perform r
Hadamard tests measuring X and r measuring Y on a fresh test ancilla, with
controlled U^(2^j) acting on the residue register. Reset or discard each test
ancilla after its measurement. A Hadamard test is: initialize |0>, apply H,
apply the controlled translation, and measure X (H then computational
measurement) or Y (S-dagger then H then computational measurement).
Encode outcomes as +1 and -1. Let c_hat_j and d_hat_j be their respective
sample means. Division need not be implemented: all comparisons below use
the signed integer sums, whose denominators are the same r.

Conditional on the spectral component k, put theta_j = 2^j k/N modulo 1.
The X and Y means are respectively cos(2 pi theta_j) and sin(2 pi theta_j).
The residue eigenstate and the retained first source qubit are unchanged on
every test branch. Thus the repeated outcomes are independent conditional on
k, despite reusing the same source copy.

For an average of r independent random variables in {-1,+1} with mean mu,

    Pr[ |mean - mu| > a ] <= 2 exp(-r a^2/2).

For completeness, let F(t)=log E exp(t(X-E X)). Then F(0)=F'(0)=0,
and F''(t) is the variance of X under the exponentially tilted distribution.
Every distribution supported in [-1,1] has variance at most 1, so integrating
twice gives F(t)<=t^2/2. Independence gives the corresponding r-term bound;
Markov's inequality and minimization at t=a give exp(-r a^2/2) for the
upper tail, and applying the same argument to -X gives the lower tail.
This proves the stated two-sided bound without an external theorem.
The argument applies separately to every fixed k; there is no distributional
assumption about k in this bound.

At a=1/16, a union bound over the 2n estimates gives failure probability at
most

    4n exp(-r/512) <= 4n 2^(-(q+ell)) <= 2^(-q).

On the complementary event, construct alpha_j in {0,1/4,1/2,3/4} by selecting
the largest of c_hat_j, d_hat_j, -c_hat_j, -d_hat_j, respectively. Break ties
by the displayed order. These are the four cardinal unit vectors. The largest
true cardinal dot product is at least 1/sqrt(2); changing either the selected
or the maximizing dot product by at most 1/16 shows that the true dot product
of the selected direction is at least

    1/sqrt(2) - 1/8 > 1/2.

Hence the circular distance between alpha_j and theta_j is strictly less
than 1/6. Only integer comparisons and two-bit alpha_j values are used; the
trigonometric functions in this paragraph occur solely in the proof.

Unwrap these coarse phase estimates backwards. Set beta_(n-1)=alpha_(n-1).
For j=n-2,...,0, choose, from the two numbers beta_(j+1)/2 and
(beta_(j+1)+1)/2 modulo 1, the one with smaller circular distance to alpha_j.
Ties may be broken arbitrarily. All beta_j are dyadic rationals with at most
n+1 fractional bits.

Here is a direct correctness proof of the unwrapping. If beta_(j+1) has
circular error e_(j+1) from theta_(j+1), one of its two preimages has
circular error e_(j+1)/2 from theta_j. Its distance to alpha_j is strictly
less than 1/6 + (1/6)/2 = 1/4. The other preimage is half a turn away and
therefore has distance strictly greater than 1/4. The algorithm selects the
correct preimage. Inductively,

    dist(beta_0, k/N) < (1/6) 2^(-(n-1))
                         = 2^(-n)/3 < 1/(2N).

Return round(N beta_0) modulo N as the classical label, and retain the first
source qubit. Rounding and reduction include the case where the nearest
integer is N and the true label is 0. The strict bound proves that the label
is k. This handles every modulus, including non-powers of two, and n=1.

For each latent k, couple the actual output with the ideal output carrying
that same k and exact qubit. They differ only when the label is wrong, an
event of probability at most 2^(-q). Convexity of trace distance, or direct
comparison of these classical blocks, proves the lemma's trace-distance
bound. In particular, for L independent ideal source calls, using q on each
call makes the joint output at most L 2^(-q) away from L ideal labelled
phase qubits. The same hybrid bound holds when subsequent processing is
adaptive, by contractivity of trace distance. Choose
q >= ceil(log2(L/eta)) to budget total extraction error eta. This is not an
extra source failure or an extra acquired copy.

## Uniform reversible translations and charged resources

Implement the controlled power directly as modular addition of the classical
constant a_j = 2^j mod N. Do not implement it as 2^j separate increments.
Generate all a_j successively by doubling, comparison with N, and conditional
subtraction, using O(n) bits and O(n^2) total elementary bit work.

For each a<N extend y -> (y+a) mod N on y<N to the identity on n-bit
strings y>=N. This is a permutation on all 2^n basis states. Its inverse is
similarly extended subtraction. Comparisons, addition, subtraction, and
selection are ordinary ripple Boolean circuits with O(n) bounded-fanin
gates and O(n) intermediate bits. Include the test ancilla as a Boolean
control choosing this permutation or the identity. Reversibly evaluate its
Boolean circuit into a zero n-bit target, swap input and target, and reversibly
XOR the inverse permutation of the new input into the old-input register,
clearing it. Each Boolean evaluation is made clean by retaining its O(n)
gate values, copying the result, and reversing the calculation. This gives
O(n) NOT/CNOT/Toffoli gates and O(n) qubits per controlled translation, with
all temporary wires clean at the end. For explicit exact synthesis, on bits a,b,c the integer identity

    4abc = a+b+c - (a xor b) - (a xor c) - (b xor c)
                     + (a xor b xor c)

holds. Compute the four displayed nontrivial parities with CNOTs into four
zero scratch qubits; apply T to a,b,c and the triple parity, and T-dagger to
the three pair parities; then uncompute the parities. The phase is
exp(i pi abc), exactly CCZ. Conjugating its target by H gives Toffoli.
This supplies a constant-length exact Clifford+T decomposition with a
constant number of reusable clean scratch qubits. There are no gates
depending on an approximate angle. The extension to
invalid residues also makes the channel well-defined on malformed input
states.

There are exactly 2nr tests, regardless of outcomes. Their exact quantum-gate
count is O(n^2 r); the first source qubit is never acted on. Signed running
sums require O(log(r+2)) classical bits. Store the n two-bit alpha_j values;
reuse arithmetic workspaces and generate gates as a stream. Backward
unwrapping and rounding use O(n)-bit dyadic integers; schoolbook integer
multiplication costs O(n^2) bit operations and O(n) working bits here.
The input q and the test counters need O(log(q+2)+log(n+1)) bits. No complete
circuit list, truth table, real approximation table or sample history is
stored. The total peak allocated memory is
M=O(n+log(r+2)) bits and qubits. Classically addressed gates and memory
accesses therefore pay O(log(M+2)) bit work apiece, as required by the rules.

A uniform ripple-circuit generator uses bit counters and reads O(n)-bit
constants. Emitting each constant-size gate and its wire indices costs
O(log(M+2)) bit operations; test bookkeeping and updating the signed sums
cost O(log(r+2)) per test even with conservative non-amortized arithmetic.
Consequently a convenient joint upper bound is

    O(n^2 r log(n+r+2))

charged work. It also covers generation of modular constants, classical
unwrapping, multiplication/rounding, all Clifford+T decomposition output,
the n+1 source charge, initialization, measurement and disposal. Substituting
r=512(q+ceil(log2(4n))) gives the stated T envelope. The peak classical and
quantum spaces are as stated above. The loop count is fixed before the first
sample measurement; no expectation, uncharged restart or cutoff is involved.

Finally, this is a fixed CPTP map. Arbitrary malformed input states are sent
to some (possibly malformed) classical-label/qubit output. Applying the map
does not convert a corruption-count promise into an independent-error
promise. A larger algorithm must state its own corruption model and account
for the L 2^(-q) approximation budget on its ideal inputs. This lemma alone
claims no positive malformed-sample tolerance or full-secret-recovery bound.
