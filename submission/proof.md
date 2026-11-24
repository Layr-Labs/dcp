# Reusable threshold reflection for the dihedral coset problem

## 1. Statement and parameters

Let $N\ge2$, $s\in\mathbb Z/N\mathbb Z$, and $n=\lceil\log_2 N\rceil$.
The robust source is the adaptive malformed-copy model stated in the fifth
claim. Take the fixed constants and parameters

```text
epsilon = 333333 / 1000000
Q = 2^46 (n + 16)
B = floor(epsilon Q)
R = Q - B
D = 2^n
L = 2^(ceil(n/2) + 1)
trials = 16.
```

Acquire all $Q$ source copies in order, before drawing private bits or
performing any measurement. Retain them on individually addressed wires.
The algorithm reuses these same qubits in every trial and verification.
Its joint bounds are $O(2^{n/2} n^2\log_2 n)$ charged work, $O(n)$
classical bits, $O(n^2)$ qubits, and exactly (Q=O(n)) source copies.
The asymptotic work bound treats the finite case $n=1$ separately from
the eventual representative. The unconditional full-secret success
probability is greater than $3/4$, uniformly over the allowed adversaries.

## 2. Per-copy projectors and a coherent threshold test

For a candidate $t<N$, define $V_t$ on a row bit $b$ and a residue
register $y$. Controlled by $b=1$, subtract $t\bmod N$ from valid
residues $0\le y<N$. Leave invalid residues unchanged, and apply
Hadamard to $b$ after the subtraction. Define
$P_t=V_t^\dagger (|0\rangle\langle0|\otimes I)V_t$. This is the
projector onto the one-copy pass subspace over the whole physical
register. In particular it is defined even on malformed inputs with
out-of-range residues.

For a clean pure summand with shift $s$, after subtraction the two
row branches have positions $x$ and $x+s-t\pmod N$. The squared
norm for the Hadamard row outcome zero is one for $t=s$, and exactly
one half for $t\ne s$, because in the latter case the two positions
are orthogonal. This remains true for the mixed ideal source. Moreover
the clean source is supported inside the range of $P_s$, since each
pure summand has pass probability one.

Write $\Pi_t$ for the spectral projector indicating at least $R$
passes among the $Q$ commuting projectors (P_t^{(i)}), one per source
register. Set $\Pi_t=0$ for $N\le t<D$. Implement the exact unitary
$I-2\Pi_t$ on the source copies controlled by the candidate register.
First compute the candidate validity bit. For each valid candidate
transform all source registers by $V_t$. Increment a reversible
counter for each transformed row bit equal to zero, using
$\lceil\log_2(Q+1)\rceil$ counter bits. Compute the threshold flag,
phase flip if it is set and the candidate is valid, then uncompute the
flag, the counter, validity and all transformations. Compute and erase
each arithmetic workspace before processing the next copy. The
candidate is never modified. Every invalid candidate sees the identity.
To implement the same reflection conditional on one extra qubit, control
only the threshold phase flip. This uses the same preceding computation
and exact uncomputation. Thus control of source preparation is never used.

### Gate and controller implementation

The controlled modular subtraction and its inverse are reversible
permutations. To implement them at linear size, first describe the
ordinary Boolean circuit computing the updated residue from the unchanged
(b,t,N,y). Compare $y<N$, compute the binary subtract with carry/borrow,
add $N$ in the borrow case, and select the original $y$ if the row or
validity control is off. Ripple arithmetic and selection require
$O(n)$ scalar gates using $O(n)$ temporary bits. Compute into a clean
register by evaluating gates into scratch, copying the result and
reversing the evaluation. Swap old and new values and erase the old
register by XORing the output of the analogous inverse Boolean function,
controlled modular addition, into it. For both operations the validity of
the residue is preserved, so the inverse covers the entire Hilbert space
for each valid candidate, including invalid residues. The exact
constructions use NOT, CNOT, Toffoli and controlled swaps. One may apply
the row Hadamard irrespective of candidate validity and rely on the
phase-flip guard, because the surrounding computation is reversed for
every candidate. This requires no controlled-Hadamard synthesis. Toffoli
is exact in Clifford+T.

Incrementing a $k$-bit counter conditionally is reversible addition
modulo (2^k) by its condition bit. A ripple circuit for the increment
and its inverse, with the same clean-output, swap, and erase method,
uses (O(k)) gates and scratch. On the forward count a wrap cannot occur
because its maximum is (Q<2^k); the implementation is still unitary
on unused counter states. Comparing the count to $R$, comparing a
candidate to $N$, and flipping a phase on the flags use linear size
in the corresponding word lengths. Signs and comparisons include the
endpoint (N=2^n) by storing $N$ as an (n+1)-bit value.

These circuits can be emitted as fixed passes of ripple steps, with gate
addresses computed from the current register offset and bit index. A
counter, address, and offset have $O(\log(n+2))$ bits, and the
controller advances or resets them with at most that much bit work per
gate. For a fixed classical input bit of $N$ or $R$, it emits the
appropriate gate or omits it. This does not require a stored gate list.
Operations with the source array use classical indices, independent of
the superposed candidate. All scratch is shared serially.

## 3. Threshold bounds in the adaptive model

At acquisition the algorithm only receives each fixed-size register,
without measurements or source-dependent control. Thus it has no
outcomes for the adversary to use in changing later decisions.
Condition on a classical record of the adversary's decisions, or just
its resulting set of malformed positions. Conditional on this set
of size $m\le B$, the joint marginal of the (g=Q-m) clean copies is
$\rho_s^{\otimes g}$. In fact the clean registers factor from the
rest on each such branch: each of them was delivered in fresh product
form, and subsequent delivery choices and adversary operations cannot
access them or any system correlated with them. This also follows by
inducting over deliveries with the private adversary instrument restricted
to its own systems and classical records. Nonselective mixing over
these records preserves any common bound proved on each branch.
Neither factorization of the malformed registers nor a measurement of
the malformed flags by the algorithm is needed.

For true $t=s$, all $g\ge R$ clean registers are supported in their
pass subspaces. Consequently $\Pi_s$ acts exactly as identity on the
support of the actual source state. This holds on a purification too.
For a fixed wrong $t<N$, testing just the clean copies gives independent
Bernoulli variables of parameter $1/2$, as the projectors act on
separate factors of the clean marginal. With at most $m$ malformed
registers, the event defining $\Pi_t$ requires at least (R-m)
clean passes. This implication is an inequality of commuting projectors
and is valid even on the unmeasured joint state. The required excess
above the clean mean is
$$
R-m-g/2=(Q-2B-m)/2\ge (Q-3B)/2\ge Q/(2\cdot10^6).
$$
The last inequality uses $3\epsilon=1-10^{-6}$. Hoeffding's bound
for the clean Bernoulli sum therefore gives
$$
\operatorname{Tr}(\Pi_t\rho_{\rm source})
 \le \exp[-2(Q/(2\cdot10^6))^2/g]
 \le \exp[-Q/(2\cdot10^{12})]
 \le 2^{-20(n+16)}.
$$
For the last inequality, $2^{46}/(2\cdot10^{12})>35>20\ln 2$.
All these bounds are unconditional after averaging over the possible
malformed sets.

## 4. Search, verification, and coherent reuse

In each of 16 trials, initialize the $n$-wire candidate register in
the uniform superposition by Hadamards. Draw a uniform integer
$j\in[0,L)$ with exactly $\log_2 L$ private fair bits. Run $j$ Grover
iterations using the source threshold reflection and the diffusion
reflection on the uniform candidate. Measure the candidate and verify
it by a Hadamard test on the candidate-controlled threshold reflection,
using a fresh control wire (Hadamard, controlled reflection, Hadamard,
measure). Interpret control bit one as success. Record the first
verified candidate and execute every remaining trial. Return the recorded
candidate, or zero if none has verified. The ideal comparison algorithm
replaces every reflection by the exact mark on $t=s$ acting as identity
on the sources, and does the same replacement in verification.

For the ideal search let $\sin\theta=D^{-1/2}$, $0<\theta\le\pi/4$.
The Grover two-dimensional rotation gives ideal single-trial success
$\sin^2((2j+1)\theta)$, since the initial amplitudes in the marked and
unmarked directions are $\sin\theta,\cos\theta$. The uniform average
over $j$ is at least
$1/2-1/(2L|\sin(2\theta)|)\$,
by summing the unit-modulus geometric progression in the doubled-angle
expression. Here $L\ge2\sqrt D$ and
$\sin 2\theta\ge\sqrt2/\sqrt D$ since $D\ge2$. Thus the chance is
at least $1/4$. Ideal verification accepts exactly the true candidate.
The independent ideal trials fail together with probability at most
((3/4)^{16}<1/64).

The actual query is allowed to disturb its source memory and entangle
it with the candidate. To bound the cumulative effect, purify the
source state as $ |\Psi\rangle$ and put
(p=2^{-20(n+16)}). On the ideal input to any query the source and its
reference are still in $ |\Psi\rangle$, factorized from the
candidate, control and algorithm records. If the ideal candidate
amplitudes are arbitrary vectors $ |u_t\rangle$ in the other algorithm
registers, the squared norm of the difference between actual and ideal
query outputs is at most
$$
4 \sum_{t\ne s}\langle u_t|u_t\rangle
            \|(\Pi_t\otimes I)|\Psi\rangle\|^2\le4p.
$$
This follows by orthogonality of the candidate labels and the exact
true-candidate equality just proved. For a controlled reflection the
same inequality holds by restricting to the control-on subspace.
For a query skipped by the trial's counter, the two operations agree.
The bound also holds in the presence of any private registers used to
purify the controls, randomness and measurements.

Form a length-bounded comparison by allowing $L$ query positions per
trial and treating skipped positions as the identity. This is a proof
convention. The physical algorithm simply loops $j$ times. Include an
additional verification query per trial. The hybrid that uses ideal
queries up to the replaced query and actual channels after it bounds the
final trace distance by $16(L+1)\,2\sqrt p$. Indeed each changed query
on the ideal prefix has vector distance at most $2\sqrt p$, an upper
bound on its trace distance, and the common suffix is contractive.
This calculation makes no claim that a later actual-prefix source state
is independent of the observed history. Retaining a purification is an
analytical device and allocates no physical algorithm memory.
Since $L\le 4\sqrt D$, the distance is at most
$160\,2^{n/2}2^{-10(n+16)}<1/64$.
The total actual failure probability is below $1/32$, in particular
the success probability is greater than $3/4$.

## 5. Joint worst-case resource bounds

The source array contains (Q(n+1)=O(n^2)) qubits and is acquired once
at cost (Q(n+1)). Even if transfers to stable wire addresses are
needed, they take at most (O(Qn)) swaps. The candidate, verifier control,
diffusion workspace, recycled arithmetic ancillas and threshold counter
need $O(n+\log(Q+1))=O(n)$ additional qubits. Copy disposal or reset
at the end costs at most the same order as allocation. The classical
controller stores the input modulus, counters and current offsets,
fixed parameters, trial iteration index and a constant number of
$n$-bit outcomes. The trial random bits take $O(n)$ classical bits.
A stream of elementary gates suffices and no list of source labels,
outcomes from the sources, or circuit descriptions is retained.

The number of elementary gates per threshold reflection, controlled or
uncontrolled, is $O(Q(n+\log(Q+1))+n)=O(n^2)$. Diffusion uses $O(n)$
Hadamards, X and a many-controlled sign with a linear-size Toffoli chain
and clean ancillas. Every branch executes at most (16(L+1))
reflections, (O(L)) diffusion steps and only polynomial setup,
measurement and cleanup work. Parameter construction uses ordinary
integer arithmetic on $O(\log(n+2))$-bit words besides parsing the
(n+1)-bit input. The number of allocated bits and qubits is
(M=O(n^2)), so addresses cost $O(\log(n+2))$ per counted access or
gate. The bit work for uniform gate generation has the same overhead.
Total work is $O(2^{n/2} n^2\log_2 n)$ as $n\to\infty$.
This bound includes all trials and failed verifications. No run
requires additional copies. All constants including the source
multiplier and fixed count of trials are absolute.

The time representative satisfies
$\log_2 B_T=n/2+2\log_2 n+\log_2\log_2 n\$ eventually, so its
growth index is exactly one. The classical, quantum and sample
representatives (n,n^2,n) each have growth index zero. The fifth
claim's constant $333333/1000000$ bounds the malformed fraction of
the exact acquisitions, as used in Section 3.

## 6. Provenance

The adaptive error model is reproduced from ROB-G2, Yukon submission
55a6ce76-34af-468f-b735-a1197f3d3459. Its measured-shadow oracle is
a comparator for the work and space claims. The candidate test is the
usual controlled cyclic subtraction and Hadamard used by the checkout's
exhaustive baseline. The threshold here is a coherent reflection on the
raw copies, with a query hybrid in place of a classical record oracle.
