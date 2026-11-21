# Robust coherent reuse of a linear batch of DCP samples

## 1. Theorem and fixed configuration

For every integer N >= 2 and s in Z/NZ, put n=ceil(log2 N),
q=128(n+1), and r=q/4=32(n+1). Algorithm RCR-1/4 below acquires
exactly q source registers once and reuses them for sequential candidate tests.
Under the error promise in Section 2 it recovers the entire s with unconditional
probability greater than 49/64, hence greater than 2/3. Simultaneously, on every
execution branch, its worst-case resource bounds are

    T(N,s) = O(N n^2 log2(n+2)),
    S_C(N,s) = O(n) classical bits,
    S_Q(N,s) = O(n^2) qubits,
    Q(N,s) = q = 128(n+1) = O(n).

Constants are independent of N, s, and the allowed source state. The supported
bit-length envelopes are [2^n n^2 log2 n, n, n^2, n], with growth indices
[1,0,0,0]. The logarithmic envelope is asymptotic for n>=2; log2(n+2) in the
operational bound covers n=1. The guaranteed malformed fraction is 1/4.

This is an exponential-time algorithm. It does not achieve the research target
2^{O(n^{1/3})}. Compared with the provided baseline's stated guarantees it
improves sample count, classical space, and work. No claim of a new best-known
DCP algorithm or new underlying state-detection principle is made.

## 2. Exact error model

All q registers, each one qubit plus an n-qubit residue, are acquired before
any candidate test. Their joint density operator omega is fixed before the
algorithm's measurements. There must exist an unknown fixed subset B of
positions, |B|<=floor(epsilon(n) q), such that the joint reduced state on the
other positions is exactly rho_s^{tensor (q-|B|)}, with rho_s as defined in
the challenge. The state on B and its correlations with other registers may
be arbitrary subject to this clean marginal, and may depend on N and s.
Malformed registers may contain residue basis states y>=N. No measurement
feedback is given to a source that can change the promised joint state.

All q positions, including B, count as acquired samples. At epsilon=0 the
promise is exactly independent ideal samples. The guarantee is uniform over
every omega and B satisfying this condition, not an average over error
locations or a per-sample error probability. An inaccessible purification is
used only in the mathematical proof; the algorithm never receives one.

## 3. Projectors and executable algorithm

On the full n-qubit residue space define the permutation

    f_t(y) = (y-t) mod N  if 0<=y<N;
             y            if N<=y<2^n.

Let C_t apply f_t conditioned on the register's first qubit being 1, and
let V_t=(H tensor I) C_t. Set W_t=V_t^{tensor q}. Let D_r be the
computational-basis projector onto states with at most r ones among the q
first qubits, with no restriction on residue registers. Define

    P_t = W_t^dagger D_r W_t.

These are orthogonal projectors for every N, including on malformed inputs.
Implement the instrument {P_t,I-P_t} as follows:

1. Apply W_t, processing source registers one at a time with reusable scratch.
2. Reversibly count the first-qubit ones in a ceil(log2(q+1))-qubit counter.
   Compute the predicate count<=r into a flag, then uncompute the counter.
3. Measure ONLY the predicate flag, not the individual first qubits or count.
4. Apply W_t^dagger regardless of the outcome. Reset the measured flag using
   its classical outcome and reuse all cleared scratch.

The two Kraus operators on the retained batch are exactly P_t and I-P_t.
Measuring individual test outcomes would give a different instrument and is
not part of this algorithm.

    RCR-1/4(N):
        n := bit_length(N-1)
        q := 128(n+1); r := q/4
        acquire and retain all q source registers
        for t := 0,...,N-1:
            perform the instrument {P_t,I-P_t} on this same batch
            if accepted: output t and halt
        output 0

The fallback makes the output total. There are no fresh-sample retries or
free postselection. Every rejection probability is included below.

## 4. Each projector on the original state

On an ideal component, C_t maps the input to

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

For t=s this is |+>|x>, and H makes the first qubit zero. Thus all good
first qubits are zero after W_s. Correlations with malformed registers do
not change this support statement. In general, if a marginal is supported
on a subspace, any joint extension is supported on that subspace tensor
the other systems: for its complementary projector E, Tr(E omega)=0
implies E omega^{1/2}=0. With at most |B|<=r bad positions, this proves

    P_s omega P_s = omega.                                (1)

For t!=s, the two displayed residue basis states are distinct for every x.
The reduced first qubit is I/2 both before and after H. On the g=q-|B|
good positions the promised product marginal makes their measured first
bits independent fair bits. Whatever the bad outcomes or correlations,
total weight<=r implies good-position weight<=r. Therefore

    Tr(P_t omega) <= Pr[Bin(g,1/2)<=r].                    (2)

Here is the elementary tail estimate, included to specify its hypotheses.
For independent fair bits X_j,
E exp(lambda(1/2-X_j))=cosh(lambda/2)<=exp(lambda^2/8).
The inequality follows from log cosh u<=u^2/2, since tanh u<=u for
u>=0 and the functions are even. Independence and Markov's inequality give

    Pr[sum X_j <= g/2-a] <= exp(-lambda a + g lambda^2/8).

Setting lambda=4a/g gives exp(-2a^2/g). Since g>=3q/4, r=q/4,
a=g/2-r>=q/8, and g<=q, (2) yields, for every wrong t,

    Tr(P_t omega) <= exp(-q/32) =: eta.                    (3)

These assertions refer to the ORIGINAL omega. Rejected tests may disturb
the batch, so independence is not assumed again in the sequential proof.

## 5. Sequential disturbance and unconditional success

Choose any mathematical purification |Omega> of omega. Operators below
act identically on the inaccessible reference. Equations (1) and (3) imply

    P_s|Omega> = |Omega>,
    ||P_t|Omega>|| <= sqrt(eta) for t!=s.

Write A_t=I-P_t and K_s=A_{s-1}...A_0, with K_0=I. The
unnormalized branch vector for rejecting 0,...,s-1 and accepting s is
P_s K_s|Omega>. Its squared norm is that branch's unconditional probability.
All A_t and P_s are contractions. The exact telescoping identity

    A_{s-1}...A_0-I
      = sum_{j=0}^{s-1} A_{s-1}...A_{j+1}(A_j-I)

contains no prefix to the right of (A_j-I). Hence

    ||(K_s-I)|Omega>|| <= sum_{j<s} ||P_j|Omega>||
                       <= s sqrt(eta).

The reverse triangle inequality and P_s|Omega>=|Omega> give

    ||P_s K_s|Omega>|| >= 1-s sqrt(eta)
                       >= 1-(N-1) exp(-q/64).

This argument includes mixed inputs, the permitted correlated errors, and
all disturbances, without normalized postselection or renewed independence.
With q=128(n+1), N<=2^n, e>2, and n>=1, the loss is at most

    2^n exp(-2(n+1)) < 2^n 2^{-2(n+1)}
                     = 2^{-n-2} <= 1/8.

The correct branch therefore has probability greater than
(7/8)^2=49/64>2/3. Other branches outputting s can only increase success.
False acceptance and the fallback are already covered by this lower bound.

## 6. Uniform exact Clifford+T implementation

No QFT, approximate rotation, QRAM, subset-sum oracle, or inverse/coherent
source access is used. Arithmetic, addressing, and circuit generation are
charged explicitly.

Ordinary ripple comparisons, addition/subtraction and bitwise selection on
O(n) bits have Boolean circuits with O(n) gates and wires. For f_t compare
y with N and t, select y-t if valid and y>=t, y+N-t if valid and y<t,
and y otherwise. O(n+1) intermediate bits avoid overflow. Its inverse adds
t modulo N on the valid range and is identity elsewhere, also of Boolean
size O(n). The first-qubit condition is included in bitwise selection.
This is not an iteration t times.

To evaluate each Boolean circuit reversibly, retain each intermediate gate
value in a clean ancilla, XOR its output into a target, and reverse its
gates. NOT/XOR/AND use X/CNOT/Toffoli. For a permutation, compute into a
zero register, swap input and output, then XOR-compute the inverse to clear
the old input. This implements the controlled permutation with O(n) gates
and O(n) reusable ancillas, on the full Hilbert space. The inverse has the
same costs. No gate list or source labels are supplied for free.

For completeness, Toffoli has an exact constant-size Clifford+T realization.
The integer identity for bits a,b,c

    4abc = a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c)

implements CCZ using T or T^dagger phases on these seven parities, with
CNOT computation/uncomputation and one reusable parity ancilla.
Conjugating the target by H gives Toffoli. T^dagger=T^7, so only the
allowed finite gate set is used, with constant overhead.

For the Hamming count, add each source first-qubit bit into a
ceil(log2(q+1))-bit counter. Controlled increment, comparison, and their
inverses have O(log(q+1)) Boolean/reversible size with reusable carries.
The counter never overflows on reached inputs. Copy the comparison to the
flag and uncompute the count before measuring the flag. Total size is
O(q log(q+1)), with O(log(q+1)) scratch. The actual reversible gates are
unitary also on unused counter states.

The uniform controller emits gates as it traverses these regular ripple
circuits. A constant number of loop counters, operand bits, node addresses,
and flags suffices; reverse traversals count down instead of storing a gate
list. Addresses into O(n^2) allocated bits/qubits have O(log(n+2)) bits.
Reading bits of the classical constants N,t, updating such indices, emitting
a gate, and the required classically addressed operation each cost at most
O(log(n+2)) bit operations per Boolean/reversible gate. A constant number
of O(n)-bit classical integers and O(log(n+2))-bit counters suffice. There
are no instance-dependent preloaded tables or uncharged advice.

Per candidate, W_t and its inverse have O(qn)=O(n^2) gates. Counting adds
O(q log(q+1))=O(n log(n+2)). Exact fixed-size gate decompositions, generation,
and the address charge therefore cost O(n^2 log(n+2)) work per candidate.
Incrementing t, loop termination, handling a flag, and output fit this bound.

## 7. Joint worst-case resources and structured envelopes

Exactly q=128(n+1) copies are acquired once, at charge q(n+1)=O(n^2).
There are at most N candidate tests, with no random retries or unbounded
compilation. Initialization, resets, measurement, and disposal are covered.
Thus total work is O(N n^2 log(n+2)) on every execution branch.

Quantum storage is q(n+1)=O(n^2) retained source qubits, O(n) reusable
arithmetic scratch, O(log(n+2)) counting scratch, and O(1) flags.
Classical storage consists of N,t,n,q,r, a constant number of O(n)-bit
working integers, O(log(n+2))-bit wire indices/counters, and O(1) measured
flags: O(n) bits. Neither a table of outcomes nor a circuit description is
stored. All four bounds concern this same algorithm and configuration under
every allowed input, including malformed ones and all failure branches.

For n>=2, N<=2^n and log(n+2)=O(log n), giving supported envelopes

    [time, classical_space, quantum_space, samples]
       = [2^n n^2 log2 n, n, n^2, n].

For time, log2 B=n+2 log2 n+log2 log2 n, so the challenge's double-log
growth index is 1. For n and n^2 the double logarithm is O(log log n),
so its ratio to log2 n tends to zero. Constants do not change the indices.
The operational bounds cover the finite small cases; the asymptotic expression
does not assert log2 1>0. The fifth declaration is the fraction 1/4 under
Section 2's model. It has no score and claims no optimal corruption threshold.

## 8. Provenance, scope and evidence status

The source and baseline format are Layr-Labs/dcp revision
5f141ca57dc41fe431770ea153fc4c0af6a05aea. Its single-candidate controlled-shift
test is the starting primitive. This candidate uses it coherently on a retained
batch, replaces all-plus acceptance by a threshold projector, and analyzes
sequential disturbance directly. No other Yukon submission's proof, code or
note supplies a premise.

Polynomial-sample/exponential-processing approaches and quantum state detection
are established ideas. Contextual references: Mark Ettinger and Peter Hoyer,
"On Quantum Algorithms for Noncommutative Hidden Subgroups,"
arXiv:quant-ph/9807029v1 (1998), https://arxiv.org/abs/quant-ph/9807029v1;
and "Quantum State Detection Via Elimination," arXiv:quant-ph/9905099v1
(1999), https://arxiv.org/abs/quant-ph/9905099v1. No theorem from either paper
is required as an unproved premise here. The probabilistic, disturbance and
circuit arguments and all their input hypotheses are given above. Acceptance
would not establish novelty or a best-known result.

validation.py supplies supplementary finite-dimensional checks on toy batches
small enough to simulate, and exact binomial-tail checks for the prescribed
q. The toy quantum runs do not execute the full asymptotic configuration and
do not prove the theorem. The proof above is the mathematical evidence. The
submission declares no hosted executable experiments.
