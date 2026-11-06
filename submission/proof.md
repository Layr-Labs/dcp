# RWT25: threshold witness search with one-quarter malformed copies

One fixed algorithm for every integer N>=2 and s in Z/NZ has unconditional
success at least 95/128>2/3 and simultaneous worst-case charged bounds

    T=O(2^(n/2) n^3), S_C=O(n), S_Q=O(n^2), Q=32(n+16)=O(n),

where n=ceil(log2 N). The exact growth indices are 1,0,0,0. The guaranteed
malformed fraction is epsilon(n)=1/4 under the following error model.

## 1. Precise adversarial promise

Q=k=32(n+16) copies are acquired, exactly once each. Write h=k/4=8(n+16),
and a=3k/4. For every N,s, an adversary may fix a set B of b<=h malformed
positions, possibly depending on N and s. The full joint state sigma of all
k copies may be any state whose reduced density matrix on the remaining
g=k-b positions is exactly rho_s^(tensor g). The malformed systems may have
arbitrary correlations or entanglement with each other and with other systems
subject to this marginal promise. No source control, purification access or
inverse preparation is provided. The promise includes the original clean
input by taking B empty. All guarantees below are uniform over every B and
sigma meeting the promise.

The structured error-model text is exactly:
"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

Here Q=k deterministically, epsilon(n)=1/4, and floor(epsilon(n)Q)=h is exact.
No interpretation as independent per-copy corruption probability is used.

## 2. Exact test projectors and the threshold lemma

For a candidate t<N, define C_t to subtract t modulo N from a source copy's
data y when its first qubit b is 1, and to act identically when b=0. On
invalid n-bit data encodings y>=N, extend it to identity. Define

    P_t=C_t^dagger (|+><+|_b tensor I_y) C_t.

For an ideal source component with offset x, C_t produces
(|0,x>+|1,(x+s-t) mod N>)/sqrt(2). Therefore P_s acts as identity on the
support of rho_s, whereas Tr(P_t rho_s)=1/2 for t!=s. On independent ideal
copies the corresponding test outcomes are independent Bernoulli(1/2) for
each wrong t.

Let Pi_t be the orthogonal projector for at least a=3k/4 plus outcomes among
the k commuting single-copy P_t measurements. For invalid t>=N set Pi_t=0.
The following hold for every sigma permitted in Section 1:

    Pi_s sigma=sigma,
    Tr(Pi_t sigma) <= exp(-k/32) <= 2^(-k/32)=2^(-n-16) (t!=s).    (1)

For the first assertion, every good copy is supported on P_s. The joint state
is therefore supported on the tensor product of the good P_s supports and
arbitrary bad systems: indeed the expectation of the complementary good
support projector is zero, so positivity forces that support condition on
the full joint state. There are at least k-h=a such good positions. Even if
every bad position fails, the threshold is met deterministically. This
support argument does not assume independence between good and bad systems.

For the second assertion, threshold acceptance implies at least a-b good
positions pass. Let Z be their count. The good marginal is exactly the product
ideal state, hence Z is Binomial(g,1/2), regardless of correlations with bad
systems. Formally the threshold projector is bounded above by the good-count
projector for Z>=a-b, tensored with identity on bad positions. Its deviation
from the good mean obeys

    (a-b)-g/2 = k/4-b/2 >= k/8.

For independent fair bits and any lambda>0,

    E exp(lambda(Z-g/2)) = cosh(lambda/2)^g <= exp(g lambda^2/8).

The inequality follows by integrating tanh(x)<=x. Markov's inequality with
lambda=4u/g yields Pr[Z-g/2>=u]<=exp(-2u^2/g). Taking u>=k/8 and g<=k gives
exp(-k/32). Finally e>2 gives exp(-k/32)<=2^(-k/32). This proves (1) without
an external concentration theorem, assumed random errors or a hidden adversary
independence premise.

## 3. Complete fixed algorithm

Compute n,k,h,a and acquire exactly k copies, retaining them as witness W.
If N=2, perform the known test for t=0 on every copy, count the plus outcomes,
and output 0 if their count is at least a, otherwise output 1. Equation (1)
gives certainty when s=0 and failure at most 2^(-17) when s=1. All k copies
are acquired even if early stopping could otherwise be possible.

For N>=3, let L=2^n and r=floor(3 sqrt(L)/4), computed by integer binary
search as the largest integer with 16r^2<=9L. On an n-qubit register A,
prepare the uniform state |u>=L^(-1/2)sum_t|t> using Hadamards. Implement

    R=I-2 sum_{t=0}^{L-1}|t><t|_A tensor Pi_t,
    D=(2|u><u|-I)_A tensor I_W.

Apply D R exactly r times. Measure A and output its value if below N;
otherwise output 0. There are no restarts, verification passes, conditional
repetitions, extra source calls or unbounded loops.

The reflection R is an explicit circuit. Compute a valid flag [t<N]. For
each witness copy coherently apply its C_t and then H to its first qubit.
Reversibly count how many of those k first qubits are zero. Apply a minus
phase if the valid flag is true and the count is at least a. Reverse the
counting computation, all Hadamards and all arithmetic, and clear the flag.
This is the threshold projector reflection exactly. It measures or postselects
no test outcomes. The inverse arithmetic is modular addition, not inverse
preparation of the witness.

D is the usual n-Hadamard conjugation of the zero-string phase reflection,
with an irrelevant global sign fixed consistently. All gates are exact
Clifford+T; Section 5 gives charged implementation details.

## 4. All witness disturbance and uniform success

For analysis only define R_s^*=(I-2|s><s|)_A tensor I_W. This unknown ideal
oracle is not implemented. Take any mathematical purification |Omega> of
sigma on a reference E which the algorithm never accesses. Equation (1)
implies Pi_s|Omega>=|Omega> and, for every wrong t,

    ||(Pi_t tensor I_E)|Omega>||^2 <= 2^(-n-16).

For any normalized |v>=sum_t v_t|t>, orthogonal candidate support gives

    ||(R-R_s^*)|v,Omega>||^2
      =4 sum_{t!=s}|v_t|^2 Tr(Pi_t sigma) <=4*2^(-n-16).           (2)

Let V=D R and V*=D R_s^*. In the ideal computation W and E stay fixed, so
each ideal intermediate state factors as |v_j> tensor |Omega>. A telescoping
expansion and unitarity therefore give

    ||V^r|u,Omega>-(V*)^r|u,Omega>||
      <=sum_{j=0}^{r-1}||(V-V*)(V*)^j|u,Omega>||
      <=2r 2^(-(n+16)/2) <=1/128.                                (3)

No factorization or nondisturbance is assumed for the actual intermediate
states. Their entanglement and all repeated-use errors are covered by (3).
A purification is used only in this proof, not supplied as an algorithm input.

Put sin(theta)=1/sqrt(L). Multiplying the two reflection matrices in the basis
formed by |s> and the uniform superposition of other candidates gives ideal
success sin^2((2r+1)theta). For L=4, r=1 gives probability 1. For L=8, r=2
gives probability 121/128, since sin(5theta)=11/(4sqrt(8)). For L>=16,

    1/sqrt(L)<=theta<=1/sqrt(L-1)<=16/(15sqrt(L)),
    5/4 <= (2r+1)theta <=28/15.

The arcsin upper bound follows by integrating its increasing derivative.
The angle interval lies in [pi/3,2pi/3], using 3<pi<22/7, so ideal success
is at least 3/4. These cases cover all N>=3.

The trace distance of normalized pure states is at most their vector norm
difference, and it cannot increase under partial trace or measurement.
Equation (3) changes the probability of A=s by at most 1/128, proving actual
success at least 95/128. The N=2 branch has a larger guarantee. This establishes
unconditional full-secret correctness for every allowed joint corrupted state,
not only for clean inputs or for an average secret.

## 5. Exact implementation and jointly charged resources

For each fixed b,t, controlled subtraction is a permutation of all n-bit
encodings: it subtracts t modulo N on y<N and acts identically otherwise.
Define it also as identity for t>=N. Its inverse uses modular addition on
the same valid range. A fixed number of ripple additions, subtractions,
comparisons and bitwise selections computes these maps with O(n) Boolean
gates and intermediate bits, on n+2-bit scratch. Quantum t is retained and
used as an input to those gates, never read classically.

Make Boolean evaluation reversible by retaining gate values, XORing the
result to a target and reversing evaluation. X, CNOT and Toffoli suffice,
and Toffoli has an exact fixed Clifford+T decomposition with constant scratch.
Compute the permutation into zero Z, swap Y,Z, and XOR its inverse from Y
into Z to clear the old input. This gives O(n) exact gates and scratch per
copy operation, including arbitrary-N invalid encodings and coherent controls.

For the threshold, sequentially add each zero-test indicator to an O(log k)-bit
counter, compare the result with a, apply the controlled phase, uncompute the
comparison and reverse all additions. Ripple controlled increments take
O(log k) exact gates and O(log k) reusable scratch each. Thus threshold work
is O(k log k), smaller than O(k n) for the present k=O(n). No array of
classical outcomes or irreversible observation is used on the search branch.

The k(n+1)=O(n^2) witness qubits are all counted even when idle. Candidate,
arithmetic scratch, phase flags and threshold counter add O(n) qubits.
Thus peak S_Q=O(n^2). Classically store N,n,k,a,r, iteration/copy/ripple counters
and one gate descriptor, using O(n) bits. Gates are streamed: fixed offsets
and ripple positions determine each wire number, and reverse passes are
regenerated rather than stored as complete circuits. Exact computation of r
by schoolbook multiplication and binary search uses O(n) bits. Hence S_C=O(n).

Total allocated memory is O(n^2), so the charged address length is
O(log(n+2)). Allow O(log(n+2)^2) bit operations per emitted arithmetic gate,
including index generation, reading input-constant bits, and the stipulated
address costs for both the controller and quantum gates. One R, its inverses,
D, and loop bookkeeping therefore cost

    O(k n log(n+2)^2)=O(n^2 log(n+2)^2)=O(n^3).

At most sqrt(L) iterations cost O(2^(n/2)n^3). The k acquisitions each cost
n+1 and add O(n^2) work. All initialization, final disposal, output and exact
polynomial preprocessing fit the same envelope. The N=2 branch costs a fixed
finite amount and is absorbed by absolute outer constants. No synthesis
accuracy, arbitrary QFT, preparation inverse, QRAM or subset-sum primitive
is used. No parallel work is discounted. All loops have deterministic lengths,
so bounds include every wrong-answer branch and all acquired copies.

## 6. Claims, provenance and comparison limits

The representatives are 2^((1/2)n)n^3, n, n^2, n. Their exact growth indices
are 1,0,0,0: log2 of the time envelope is n/2+3log2 n, while all the other
envelopes are polynomial. The fraction1/4 has no numerical score.

This is a threshold refinement of the immutable RWG-16 proof at local commit
e61eb55065946f72b78a3e3abd6acafd4c405318. It materially reuses the streamed
arithmetic also present in our CST-128 submission
f95bb4e2-3d08-4ca0-a34f-99841dca855a. The original exact shift test comes from
the prepared seed cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a. Full arguments are
reproduced; no acceptance or reviewer artifact is a proof premise. Any later
published identifier for the RWG-16 parent must be declared by the central
sender. Unavailable parents must be disclosed, not replaced by an independence
claim. No rival submission supplied the threshold lemma.

Primary search/hybrid context: Grover, arXiv:quant-ph/9605043v3 Sections 2-3,
https://arxiv.org/pdf/quant-ph/9605043 ; Bennett, Bernstein, Brassard and
Vazirani, arXiv:quant-ph/9701001v1 Theorem 3.3,
https://arxiv.org/pdf/quant-ph/9701001 . The former assumes an available
condition oracle; ours is explicitly built. The latter treats oracle-query
perturbation; we reproduce the specific mixed-witness telescoping bound rather
than assert literal application outside its hypotheses. The concentration
calculation and search rotation needed here are fully reproduced.

The error-model text DIFFERS from the seed/RWG-16 clean model, so the hosted
fractional comparator treats those rows as incomparable. This is not a claimed
backend dominance or formal supersession of RWG-16. Scientifically, the new
promise includes clean inputs and permits a genuine global adversarial fraction
of malformed copies with the same asymptotic envelopes. It is not a maximal
corruption-tolerance theorem, a cube-root time result or a literature-best sieve.
All local checks are development evidence only. Hosted acceptance is fallible
mathematical review, not formal proof.
