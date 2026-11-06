# Polynomial classical space with linear quantum space

This is a resource tradeoff, not a cube-root-time algorithm and not a claim
that polynomial-space sieving is new. Its main ingredients are a dyadic
subset-sum sieve and a reduction that uses only the supplied mixed coset
states. In particular, the reduction never calls a hiding-function oracle,
an inverse source, or a purification.

## Joint theorem

There is one uniform algorithm, specified below, which for every integer
N >= 2 and every s in Z/NZ outputs all of s with probability at least 2/3.
Put n = ceil(log2 N). On every execution branch its joint bounds are

\[
\begin{split}
T&=O\left(n^{10}2^{\,2n^{1/2}(\log_2 n)^{1/2}
                                  +(5/2)n^{1/2}}\right),\\
S_C&=O(n^2),\qquad S_Q=O(n),\\
Q&=O\left(n^6 2^{\,n^{1/2}(\log_2 n)^{1/2}
                                  +(5/2)n^{1/2}}\right).
\end{split}
\]

These are big-O envelopes, with absolute outer constants. The four exact
growth indices are respectively 1/2, 0, 0, 1/2. The malformed-sample
fractional guarantee is 0: all acquired copies are independent ideal copies
of the state in the challenge. No positive corruption tolerance is claimed.
For n=1 use the exhaustive two-candidate test with seven copies per candidate,
accepting a candidate only if all seven X tests return +;
all the definitions below concern n>=2. Finite smaller sizes in subsequent
estimates are covered by the absolute outer constants, not by a different
asymptotic algorithm.

This trades time and samples for polynomial classical storage. It does not
dominate a bound with time 2^{a sqrt(n)}. Its classical-space envelope is
strictly smaller than any envelope containing a positive sqrt(n) exponential
term, while retaining a linear quantum-space envelope.

## 1. Phase states and a dyadic combination operation

For a modulus P=2^m and unknown d in Z/PZ write

\[
|k;d,P\rangle=2^{-1/2}(|0\rangle+
                  e^{2\pi i dk/P}|1\rangle).
\]

Fourier transform the second register of a mixed coset copy over Z/PZ and
measure its Fourier label. The result is a uniformly random, known k in
Z/PZ and the displayed one-qubit state. This follows separately for every
offset x: its Fourier amplitude contains a common phase depending on x,
which disappears from the one-qubit density operator. Therefore mixing over
x has no effect on this assertion.

Ideal Fourier measurement is an analysis reference only. The actual circuit
uses the exact-gate label extractor proved in the accompanying
`label-extraction.md`. Section 6 specifies its precision and accounts for
its possible label error inside each good trial. No QFT circuit or
approximate-angle gate is needed.

Suppose r=w+4 independent input phase states have labels uniformly
distributed among multiples of 2^c modulo P, where c+w <= m-1. Write
k_j=2^c a_j, with a_j in Z/2^{m-c}Z. Tensor the r qubits, coherently compute

\[
f(x)=\sum_{j=1}^r a_j x_j\pmod {2^w},\qquad x\in\{0,1\}^r,
\]

and measure f(x), obtaining z. Let F_z be its fiber in lexicographic order,
and let h=|F_z|. Pair entries of F_z consecutively: entries 0 and 1 form a
pair, entries 2 and 3 another, and so on. An odd final entry is unpaired.
Compute the rank of x in F_z reversibly, measure floor(rank/2), and reject
only if the measured group is the unpaired final entry. Otherwise the state
has exactly two basis terms x_0,x_1. Reversible elementary Boolean operations
map those terms to |0> and |1>, leaving one phase qubit with known label

\[
k'=2^c\sum_j (x_{1j}-x_{0j})a_j\pmod P.
\]

This label is divisible by 2^{c+w}.

The success probability is at least 15/16 for **every** assignment of the
low w bits of the input labels. Indeed at most one basis string is discarded
in each of 2^w fibers, and all 2^r computational basis strings have equal
probability. Thus the discarded probability is at most 2^w/2^r=1/16.
No random-subset-sum heuristic or fiber-size assumption enters this bound.

Conditional on success and the measured pair, k'/2^{c+w} is uniform modulo
2^{m-c-w}. To see this, write a_j=l_j+2^w u_j. The selection and every
computational-basis outcome used above depend only on l_j and on uniformly
weighted basis strings, not on u_j or on d. The u_j remain independent
uniform residues modulo 2^{m-c-w}. The two bit strings are distinct, so at
least one coefficient x_{1j}-x_{0j} is +1 or -1. Consequently their linear
combination, plus the known carry from the l_j, is uniform in that ring.
This also proves that different calls using disjoint source copies have the
independence required by the recursive construction.

The pairing operation uses polynomial space even when 2^r is large. After z
is known, scan all r-bit strings y classically. When f(y)=z, add [y<x] to a
quantum rank accumulator; each comparison flag is uncomputed after the
controlled addition. This calculates the rank on the support F_z using
O(r) extra qubits. After the pair index is measured, scan again to recover
its two classical members. They give an explicit reversible map clearing
all but one qubit: XOR x_0, choose a coordinate where x_0 and x_1 differ,
and use that coordinate to clear the others. The remaining rank registers
are cleared from that same branch bit and the known pair index.
There are O(2^r) scan iterations and polynomially many counted bit/gate
operations per iteration; no list of 2^r strings is stored.

## 2. A bounded dyadic solver

The following parameters depend on the original input bit length n, even
when solving a smaller dyadic modulus:

\[
b=\lceil\sqrt{n\log_2 n}\rceil,\quad r=b+4,\quad
A=\frac{16r}{15},\quad
D=\left\lceil\frac{m-1}{b}\right\rceil,\quad
V=\left\lceil100 n^2 A^D\right\rceil.
\]

All parameters are computable by integer arithmetic. For example the least
integer b with b^2 >= n log2 n is found by comparing 2^{b^2} with n^n;
the latter integer needs O(n log n) bits. Rational powers A^D here have
integer exponent D, so their ceilings are also ordinary integer arithmetic.

Build a recursive generator. Level zero obtains one Fourier phase state.
Subsequent levels remove successive blocks of at most b low label bits,
using Section 1, retrying failed combinations. Traverse this recursion depth
first. Stop after removing m-1 bits. Its label is then uniform in
{0,2^{m-1}}. If the label is zero discard it and repeat; otherwise an X
measurement gives d mod 2 with certainty.

After finding d mod 2^j, use a new source copy, subtract that known residue
from the second register on branch 1, and measure the low j bits of the
second register. If those j bits were correct, both branches have the same
measured residue. Dividing the remaining second-register value by 2^j
produces an independent ideal coset state over Z/2^{m-j}Z with shift
(d-(d mod 2^j))/2^j. There is no rejection or source overhead for this
quotient operation. Repeat the parity procedure until all m bits are known.

A node is a start of a recursive generator invocation, including a base
invocation, a failed combination attempt, and every retry. Terminate this
whole dyadic solve with a failure flag if it would start more than V nodes.
This is an explicit worst-case cutoff, not an expected-resource claim.

For clarity, the expected-size bound used to justify the cutoff is as
follows. Let a_i be the expected number of nodes required for one successful
level-i output without cutoff. With a_0=1 and success at least 15/16,

\[
a_i\le A a_{i-1}+16/15\le(4/3) A^i.
\]

The second inequality follows by summing the geometric series and using
A>=16/3. The final nonzero-label loop has mean two iterations, so at most
(8/3)A^D expected nodes suffice per bit. There are at most n bits, and all
smaller quotient moduli use at most D levels. Thus the expected number is
at most 3n A^D. Markov's inequality bounds cutoff probability by
3/(100n), in particular by 3/100. Whenever the ideal solver finishes, its
answer is exact. It uses at most V dyadic coset copies on every branch.

## 3. Producing approximately dyadic copies from an arbitrary modulus

Let P=2^m be the largest power of two at most N, so P<=N<2P. For any chosen
t in Z/NZ, apply controlled subtraction of t to a fresh original coset
copy. Its shift becomes delta=s-t mod N. Project the second register onto
I={0,...,P-1}, retain the copy on that outcome, and identify I with Z/PZ.
The success probability is exactly P/N>=1/2, because the diagonal marginal
on the second register was uniform. Accepted copies are independent copies
of a state tau_delta.

If delta has an integer representative with 0<=delta<=B<P, then

\[
\tfrac12\|\tau_\delta-\rho^{(P)}_\delta\|_1
       \le \frac{2\delta}{P}.
\]

Here is a direct density-matrix proof. Both normalized states have identical
diagonal entries 1/(2P). Their off-diagonal pairs agree for
x=0,...,P-delta-1. At most delta ideal wraparound pairs and at most delta
original-modulus wraparound pairs remain different. Each such Hermitian
off-diagonal pair has trace norm 1/P. The triangle inequality even gives
the stronger trace-distance bound delta/P; the displayed weaker bound is
sufficient. For N=P the two states agree exactly.

For any adaptive procedure acquiring at most V accepted copies, replacing
these tau_delta copies by ideal rho_delta^(P) copies changes the final
outcome distribution by at most 2V delta/P. This is the usual telescoping
hybrid: replace one fresh input density matrix at a time, tensoring does
not change its trace norm, and all intervening channels contract trace
distance. This statement applies to the entire adaptive dyadic solver,
including its known-residue quotient operations; it does not assume that
the imperfect copies remain ideal after conditioning on later outcomes.

## 4. The complete arbitrary-N algorithm and its success probability

Use the parameters of Section 2 for this P. Set

\[
B=\left\lfloor\frac{P}{1000V}\right\rfloor,\qquad
R=\lceil20000V\rceil,\qquad
q=\lceil\log_2(100R)\rceil.
\]

Perform at most R trials. In each trial:

1. Generate n+q independent random bits as a uniform integer U and set
   t=U mod N. This has bounded work, without a rejection-sampling loop.
2. Run the V-node dyadic solver, supplying its source requests by the
   projection in Section 3. Independently cap the number of original source
   acquisitions for this trial at 200V; exhausting either cap fails the
   trial. If the solver finishes, let its answer be d_hat in Z/PZ.
3. Form c=t+d_hat mod N. Verify c with q fresh original copies: controlled
   subtraction of c followed by X measurement of the first qubit. Accept
   and output c only if all outcomes are +. A failed trial or verification
   advances to the next trial. If all R trials fail, output 0.

The verification has acceptance probability one when c=s and exactly
2^{-q} when c!=s. This follows directly from the mixed coset state: for an
incorrect shift the two second-register basis states are distinct, so the
first qubit has reduced density matrix I/2. Fresh verification copies
remain independent conditional on the entire preceding history.

Call a trial good when delta=s-t mod N belongs to {0,...,B}. Every residue t
has probability at least (1-2^{-q})/N >= .99/N. Also

\[
\frac{B+1}{N}>\frac{P}{1000VN}\ge\frac1{2000V}.
\]

This remains true when B=0. In that case the good event is simply t=s;
there is no need for P/(1000V) to exceed one.

On a good trial the ideal dyadic solver fails its node cutoff with
probability at most .03. The expected number of original copies needed
for V accepted projections is at most 2V; Markov's inequality bounds
failure of the 200V acquisition cap by .01. The hybrid error is at most
2VB/P <= .002. The extractor error from Section 6 is at most .01 per
good trial. Therefore the actual exact-gate algorithm on a good trial
returns the correct candidate with probability at least .948, and we use
the weaker lower bound .9. Conditional on any earlier history, a trial
therefore produces the correct candidate with probability at least
1/(3000V). The probability that none of R trials does so is at most
exp(-20/3)<.002. The union bound for all incorrect verification acceptances
is at most R 2^{-q}<=.01. Thus the actual exact-gate algorithm has
success probability greater than .988, in particular at least 2/3.

All trials, projection rejections, failed combinations, restarts, and
verification copies are charged. No success probability in this argument
is a free postselection probability.

## 5. Space and exact exponential envelopes

Depth-first evaluation holds at most O((b+4)D)=O(n) phase qubits at once.
Only the active combination uses rank, comparison, and modular-sum quantum
registers; these have O(n) qubits. A source copy, controlled arithmetic,
quotient operation, and label extraction also use O(n) qubits. Their
spaces are reused. Thus S_Q=O(n).

The labels of all pending phase qubits use O(n^2) classical bits. Frame
counters, subset enumeration counters, the two selected strings, node and
trial counters, modular constants, and arithmetic workspaces fit within
O(n^2) additional bits. Classical ranks and label lists are never expanded
to size 2^r. Section 6 generates the gate descriptions as a stream and
also fits in O(n^2) classical bits. Thus S_C=O(n^2). Address charges are
therefore O(log n) per indexed access and per classically addressed gate;
they are included in the polynomial time estimate below.

There are O(V) trials, at most V nodes and 200V source requests per trial,
and q=O(n) verification copies per trial. Because V>=100n^2,

\[
Q=O(V^2).
\]

Every combination scans at most 2^r strings. Computing the subset residue
from scratch costs O(rn)=O(n^2) elementary bit operations per string.
Reversible comparison against the quantum input and rank accumulation use
O(r) elementary gates per string. After charging O(log n) per memory
access, gate address, and emitted wire index, a combination costs
O(2^r n^2 log n). Section 6 bounds a base extraction by O(n^3 log n).
The inequality 2^r>=n (from b>=log2 n for n>=2) absorbs that base cost.
We use the conservative O(2^r n^4) charged bound per node, including
controller bookkeeping. All conversion attempts and verification work
have smaller total cost. Consequently

\[
T=O(V^2 2^b n^4).
\]

We now eliminate the algorithmic parameters without concealing any
coefficient inside an exponent. For n>=16 put L=log2 n and x=sqrt(nL).
Then b<=x+1, A=(16/15)(b+4)<=2x, and D<=n/x+1. Hence

\[
\begin{split}
\log_2 V
&\le \log_2 101+2L+(n/x+1)(L/2+(\log_2 L)/2+1)\\
&\le x/2+(5/4)\sqrt n+3L+8.
\end{split}
\]

For the last line use L>=4, log2 L <= (3/2)sqrt L, and log2 L<=L.
The first inequality log2 L <= (3/2)sqrt L follows, for example, by
maximizing log2 L/sqrt L by differentiation. Thus

\[
V=O\left(n^3 2^{x/2+(5/4)\sqrt n}\right),
\]

and substitution gives exactly the theorem's stated T and Q envelopes.
For 2<=n<16 all quantities are finite and the same formulas still define
the algorithm, so enlarging the absolute outer constants suffices.

## 6. Uniform exact Clifford+T implementation and label precision

All operations above other than the ideal reference measurement are
computational-basis measurements,
Hadamards, X gates, and reversible bounded-integer arithmetic. NOT, CNOT,
and Toffoli implement this arithmetic; Toffoli has an exact constant-size
Clifford+T decomposition. Modular subtraction for y<N is extended by the
identity for y>=N, giving a permutation on the full register; its reversible
implementation uses comparison, addition/subtraction, and uncomputation.
Counters, comparisons, rank accumulation, and the two-string compression
use polynomially many such gates and at most O(n) temporary qubits.

To obtain a labelled phase qubit from each accepted and, when appropriate,
quotiented coset copy, apply the channel in `label-extraction.md` with

\[
q_{\rm label}=\left\lceil\log_2(100RV)\right\rceil.
\]

That file is part of this proof. It proves from the mixed source's exact
spectral decomposition that a bounded sequence of Hadamard tests of
controlled modular translations produces the ideal retained phase qubit
with a classical label incorrect with probability at most 2^{-q_label}.
The translations, X/Y measurements, and integer phase decoder all use
exact Clifford+T gates. The stated classical-label/qubit trace-distance
bound is at most 2^{-q_label} per ideal coset input. The copy supplied to
this channel is the already acquired copy; there is no extra source call.

For explicit error accounting, fix a good trial. First compare its at most
V accepted tau_delta inputs with ideal rho_delta^(P) inputs, as in Section
3. In the latter ideal-source reference, use a telescoping comparison
between the actual extractor and ideal Fourier-label measurement. Until a
replacement changes the output, the known-residue quotients are correct
and their fresh source inputs are ideal dyadic cosets. Conditional on
every such ideal history the extractor lemma applies. Summing over at
most V calls gives error at most V 2^{-q_label} <= .01/R <= .01.
This argument requires no bound on the extractor channel's diamond norm
on arbitrary states. On bad trials, its output may be arbitrary; exact
candidate verification is what controls those trials. The underlying
channels and all cutoff bounds are nevertheless well-defined for them.

The extractor has fully charged cost
O(n^2(q_label+log(n+1)) log(n+q_label+2)), O(n) qubits, and O(n+log(q_label+2))
classical bits. Here q_label=O(n), so its time is O(n^3 log n), which is
within Section 5's O(2^r n^4) allowance. Streaming ripple circuits
and subset enumeration require no stored long circuit descriptions or
rotation tables. All quantum-addressed operations are explicit scanned
comparisons and controlled arithmetic, with every constituent gate
counted. There is no QRAM, approximate rotation, or synthesis subroutine.

## 7. Indices, scope, and provenance

For a bound with positive leading exponent a sqrt(n log2 n), the logarithm
of its logarithm divided by log2 n tends to 1/2. The positive sqrt(n)
term and polynomial factors do not change that limit. Polynomial space
has index zero. This proves the four indices stated in the theorem.

The algorithm is related to Regev's polynomial-space sieve in Section 3
of *A Subexponential Time Algorithm for the Dihedral Hidden Subgroup
Problem with Polynomial Space*, arXiv:quant-ph/0406151v1 (21 June 2004):
https://arxiv.org/abs/quant-ph/0406151v1 . The proof above specifies its own
pairing rule, uniform-label induction, constants, cutoff, space schedule,
and arbitrary-modulus source reduction; no unquoted distributional lemma
or oracle access from that paper is used. The auxiliary proof
`label-extraction.md` supplies the exact-gate extraction primitive and is
included with this evidence.

The results are for the clean independent mixed-coset source of this
challenge. They assert neither a maximum possible tolerance of zero nor
an improvement over established algorithms in time exponent growth.
