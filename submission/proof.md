# Robust Fourier-score search with polynomial space

This is one uniform algorithm for every integer N>=2 and every s in Z/NZ,
with n=ceil(log2 N). It has the joint worst-case envelopes

\[
 T=O(2^{n/2}n^3\log_2 n),\qquad S_C=O(n^2),\qquad S_Q=O(n),\qquad
 Q=M=2^{18}(n+1)=O(n).
\]

The exact growth indices of these representative envelopes are respectively
1,0,0,0. In particular, the coefficient 1/2 in the exponent of the time
envelope is explicit: it is not an unspecified inner big-O constant.
The algorithm tolerates the malformed fraction epsilon(n)=83/250, for all n>=1,
under the following complete adaptive error model, with epsilon(n)=83/250
and the deterministic acquisition count Q=M=2^26(n+1). Its context text is
quoted verbatim for exact model comparison:

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

Model-text attribution: this exact context is materially adopted from the
official reviewed metric of peer submission d0c6b9b9-d80e-4bd7-95e1-e6267b61f2f0.
Its SHA256 is fd67d2af7a9a9733f2422981afd4a6ce00bb9ceac8c29d345f29535cc0156475.
The algorithm and the stronger 83/250 proof below are independently derived;
no scientific novelty or organizer acceptance is asserted.

## 1. Fourier records using exact gates

Write
\[
 |\chi_k\rangle=N^{-1/2}\sum_{x=0}^{N-1}e^{-2\pi i kx/N}|x\rangle,
 \quad |\phi_{k,s}\rangle=(|0\rangle+e^{2\pi i ks/N}|1\rangle)/\sqrt2.
\]
Direct substitution in the source definition gives the exact identity
\[
 \rho_s={1\over N}\sum_{k=0}^{N-1}
 |\phi_{k,s}\rangle\langle\phi_{k,s}|\otimes
 |\chi_k\rangle\langle\chi_k|.
\]
Thus k is a uniform latent classical variable. Translation U_a on the residue
register, defined as modular addition by a on y<N and the identity on y>=N,
has eigenvalue exp(2 pi i ka/N) on chi_k. Its controlled version is an exact
reversible arithmetic circuit: comparisons, carry addition, subtraction and
selection on O(n) bits give O(n) Boolean gates and intermediate bits; compute,
copy, uncompute, and the inverse modular permutation give O(n) reversible
gates and ancillas. Toffoli, CNOT, X, H, and S have exact fixed Clifford+T
implementations. Constants 2^j mod N are computed by repeated doubling with
ordinary binary arithmetic. The extension on invalid residues makes every
operation unitary, including on malformed inputs.

Here is a complete finite-precision label extractor; it requires no QFT,
arbitrary rotation, synthesis theorem, source inverse, or coherent source
control. Set
\[
 \delta={1\over 2^{16}M},\quad
 w=\lceil\log_2(4n/\delta)\rceil,\quad r=512w.
\]
For j=0,...,n-1, perform r X Hadamard tests and r Y
Hadamard tests of controlled U_(2^j mod N) on the same residue register.
Each test uses a fresh control |+>, measures it in the stated Pauli basis, and
discards that control. Measuring Y uses exact S-dagger followed by H.
On chi_k the control has phase exp(2 pi i 2^j k/N), and the residue eigenstate is unchanged on every
branch. Thus conditional on k these are independent +/-1 variables with
means c_j=cos(2 pi 2^j k/N) and d_j=sin(2 pi 2^j k/N).

Hoeffding's inequality for averages of r variables in [-1,1] gives failure
probability at most 2 exp(-r/512) for either estimate to err by more than 1/16.
The union bound over the 2n estimates is at most
4n exp(-r/512)=4n exp(-w)<=delta, since w>=ln(4n/delta).

For each j choose alpha_j in {0,1/4,1/2,3/4} maximizing the estimated dot
product with its corresponding coordinate direction. If both coordinate
errors are at most 1/16, the true selected dot product is at least
1/sqrt(2)-1/8>1/2. Consequently the circular distance from alpha_j to
2^j k/N mod 1 is strictly less than 1/6.

Starting with beta_(n-1)=alpha_(n-1), work backward. Of the two preimages
under doubling of beta_(j+1), choose as beta_j the one closest on the circle
to alpha_j. This choice is unique on the good event: the preimage near the
true phase is within 1/12 of it, its distance to alpha_j is strictly below
1/4, and the other preimage is distance 1/2 away. Inductively beta_j is
within 2^{-(n-1-j)}/6 of 2^j k/N. In particular beta_0 is within
2^{-n}/3<1/(2N) of k/N. Round N beta_0 to the nearest integer modulo N to
recover k exactly. All alpha and beta values are dyadic rationals with O(n)
bits. Ties outside the good event follow a fixed rule. Hence extraction
always terminates and outputs a residue, with probability of a wrong clean
label at most delta, uniformly in k.

After extraction choose a fresh private unbiased b in {X,Y}, measure the
first source qubit in that basis, and record the ACTUAL (khat,b,z), with
z in {+1,-1}. The adversary continues to receive exactly the actual past
measurement information permitted by the quoted model.

Conditional on any pre-delivery history and a clean decision, the delivered
register is a fresh product rho_s. The one-copy extractor analysis couples
its output to an ideal uniform Fourier label with the same phase qubit,
with wrong-label probability at most delta. Because a score lies in [-1,1],
its actual conditional mean differs from its ideal conditional mean by at
most 2 delta. This is a local expectation estimate, without conditioning on
correct extraction or substituting ideal labels into the transcript. Section
2 uses it directly in a martingale over actual records, including adaptive
malformed decisions and entangled private adversarial systems.

## 2. Robust separation by a bounded score

For an ideal record define, for every candidate t in Z/NZ,
\[
 h_t(k,b,z)=\begin{cases}
 z\cos(2\pi kt/N),&b=X,\\
 z\sin(2\pi kt/N),&b=Y.
 \end{cases}
\]
Always -1<=h_t<=1. Conditional expectations of z are cos(2 pi ks/N) and
sin(2 pi ks/N), respectively. Therefore
\[
 E[h_t\mid k]={1\over2}\cos(2\pi k(s-t)/N),\qquad
 E h_s={1\over2},\quad E h_t=0\ (t\ne s),
\]
where the final identity is the finite geometric-series character sum. This
also covers nonprime N and every proper divisor of N; there is no assumption
that k is invertible or that a difference of two secrets is a generator.

### 2.1. Physical conditional-mean bound for a malformed record

For a recorded residue `k`, write `phi=2*pi*k*t/N`. Conditional on the past,
and on any current extractor transcript that has nonzero probability, the
retained first qubit has some density matrix `omega`. This remains true if it
is entangled with future malformed registers or the source environment; take
the reduced density matrix after conditioning. The extractor produces its
label before the independent fair measurement choice `b` is generated.

The score `h_t` uses the measured sign `z`: it is `z*cos(phi)` for X and
`z*sin(phi)` for Y. Therefore its conditional expectation, averaging over the
fresh fair choice and the resulting Pauli measurement, is

    (1/2) Tr[omega (cos(phi) X + sin(phi) Y)].

The Hermitian observable in parentheses squares to the identity, because
`X^2=Y^2=I` and `XY+YX=0`. Its eigenvalues are `+1` and `-1`, so this
expectation belongs to `[-1/2,1/2]`. Averaging over the current extractor
transcript preserves that interval. No correct-label or spectral-eigenstate
assumption was made for the malformed register. The proof also covers the
extractor's identity action on invalid residues.

### 2.2. Actual-score drift under predictable adaptive decisions

The adversary's actual information and interaction are never changed in
this proof. In particular, it sees every actual previous extractor outcome,
actual extracted label, basis coin, and measurement sign allowed by the
model. Define `C_i=1` if delivery `i` is malformed and `0` otherwise. Its
selection can depend on that entire actual past and its private quantum
system. The algorithm is not told `C_i`.

Let `G_i^-` be the classical history just after the adversary chooses `C_i`
and commits the next delivered register, before local processing of that
register. Include all actual previous measurement transcripts and previous
decisions, as well as `C_i`. Let `G_i^+` additionally include this position's
actual local measurement outcomes. No latent labels or future private coins
are included. These are alternating increasing sigma-fields:

    G_i^- subset G_i^+ subset G_(i+1)^-.

The extra decision variable is used only for analysis. Conditional on this
classical history, private quantum systems have their conditional density
operators; we do not condition on a fictitious classical specification of a
quantum state. All measurement outcomes are countable by the exact model.
Zero-probability histories can be omitted from the conditional statements.

For each candidate `t`, let `X_(i,t)=h_t(khat_i,b_i,z_i)` be its exact real
score on the ACTUAL observed record. Put
`mu_(i,t)=E[X_(i,t)|G_i^-]`. At a clean delivery, the register is a fresh
`rho_s` in tensor product with everything else, conditional on the current
history and decision. Only within this single conditional clean experiment,
use the spectral mixture to couple its actual output to the ideal output
with a uniform Fourier label. The first qubit is unchanged conditional on
that label; the actual label differs with probability at most `delta`.
The actual and ideal scores both lie in `[-1,1]`, so their expected values
differ in absolute value by at most `2 delta`. The ideal expected values
were computed above by character orthogonality. Consequently

    mu_(i,s)>=1/2-2 delta,
    mu_(i,t)<=2 delta            (t != s),                 if C_i=0.

This is a conditional expectation estimate for the actual record. It does
not replace a label in the actual transcript, introduce latent variables
across deliveries, or condition on extraction success. Future adversarial
choices therefore continue to follow the exact actual history.

At a malformed delivery, condition further on its completed actual extractor
transcript and output label. The first-qubit conditional density matrix can
be arbitrary and entangled with the adversary's remaining system. The fresh
private X/Y coin is generated next, so the physical conditional-mean bound
in subsection 2.1 gives, by the tower property,

    -1/2<=mu_(i,t)<=1/2          (every t),                 if C_i=1.

Processing the adversary's remaining system cannot signal into a delivered
register: a trace-preserving channel on the remaining system leaves the
register's reduced density matrix unchanged. No access to the delivered
register or algorithmic systems is allowed after delivery. Thus arbitrary
private quantum processing and correlations among malformed copies do not
invalidate this conditional-mean statement.

Since `C_i` is known in `G_i^-`, the bounds combine pathwise to

    mu_(i,s)>=1/2-C_i-2 delta,
    mu_(i,t)<=C_i/2+2 delta      (t != s).

Let `K=sum_i C_i`. The adaptive count promise is `K<=floor((83/250)M)` on
every branch. Without conditioning on the final decision vector, we have

    sum_i mu_(i,s)>=M/2-K-2M delta,
    sum_i mu_(i,t)<=K/2+2M delta (t != s).

### 2.3. Conditional Hoeffding for the actual adaptive transcript

Every actual score belongs to `[-1,1]`. The conditional Hoeffding lemma is

    E[exp(lambda*(X_(i,t)-mu_(i,t)))|G_i^-]<=exp(lambda^2/2).

For completeness, the log moment generating function of `X-E X` on any
conditional distribution has value and first derivative zero at zero. Its
second derivative is the variance of an exponential tilt supported in
`[-1,1]`, at most one. Integrating twice proves the bound for every real
`lambda`. With `Z_i=X_(i,t)-mu_(i,t)`, the earlier sum of the `Z_j` is
`G_i^-`-measurable because `G_(i-1)^+ subset G_i^-`. Iterated conditional
expectation over the alternating histories therefore yields

    E exp(lambda sum_i Z_i)<=exp(M lambda^2/2).

Exponential Markov, optimized at `lambda=a`, and the same argument for the
negative sum show

    Pr[|sum_i Z_i|>M a]<=2 exp(-M a^2/2).

No independence of actual scores, malformed decisions, or different
candidates is assumed. Use `a=1/3072` and `M=2^26(n+1)`, so

    M a^2/2=(32/9)(n+1).

A union bound over `N<=2^n` candidates gives simultaneous failure at most

    2N exp[-(32/9)(n+1)]
      <=2^(n+1) exp[-(32/9)(n+1)]
      <=4 exp(-64/9)<1/256,                         every n>=1.

The middle expression decreases in n, and the final inequality follows
from `10 ln2<7<64/9`. The elementary estimate `ln2<7/10` follows from the
positive Taylor sum `exp(7/10)>482921/240000>2`.

### 2.4. Finite separation including clean extraction bias

On that simultaneous concentration event, put the random
`beta=K/M<=83/250`. The actual record averages satisfy

    A_s>=1/2-beta-a-2 delta,
    A_t<=beta/2+a+2 delta                     (t != s).

The finite deterministic score evaluation changes each average by less
than `tau=1/16384`. Thus

    computed A_s>=138219697995401/824633720832000-2 delta,
    computed A_t<=137207964762487/824633720832000+2 delta   (t != s),
    theta=167/1000=137625600000000/824633720832000.

Before the small clean extraction bias, both margins are exactly
`593804232914/824633720832000`. Since `n>=1`, `M>=2^27` and
`delta=1/(2^16 M)<=2^-43`. Hence

    593804232914/824633720832000-2 delta>1/1700.

The true secret is therefore marked and all wrong residues are unmarked,
with margins greater than `1/1700`. Strings `t>=N` are rejected explicitly,
so the predicate has exactly one marked n-bit string on the good event.
This argument directly analyzes actual scores; no global label-success
event or associated failure-probability charge is needed.

For every fixed good record list, the unchanged capped search fails with
probability at most `(3/4)^16<1/64`. Fresh search preparations and coins are
independent of the earlier adaptive record-generation process. Therefore
the unconditional full-secret success probability is at least

    1-1/256-1/64=251/256
      >1-1/256-2^-16-1/64=64255/65536>2/3.

The latter, conservative expression is the common guarantee retained in
all five claims. The proof is uniform for every N>=2, every secret, and
every adversary permitted by the complete quoted adaptive model.


## 3. A uniform, exact reversible score oracle

The quantum search never evaluates a transcendental operation as a free gate.
Fix the following finite arithmetic procedure once for the entire algorithm.
Given t,k, compute v=kt mod N by schoolbook binary multiplication and long
division on O(n)-bit numbers. Compute u=floor(2^24 v/N)/2^24. Compute a fixed
rational approximation P to pi from Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), using 20 terms of each alternating Taylor
series. The alternating-series bound gives |P-pi|<2^-80. This identity follows
by the tangent addition formula and the quadrant of the two positive angles.
This fixed calculation, including its rational numerator and denominator, is
performed and charged; there is no table or instance-dependent advice.

Evaluate the sine or cosine Taylor polynomial through degree 255 at 2Pu,
using exact rational arithmetic; then round to the nearest multiple of 2^-12
and clip to [-1,1]. The polynomial has fixed degree and all its intermediate
rational bit lengths are absolute constants. Its truncation error on |x|<=7
is bounded by 7^256/256!<2^-100 (the elementary product bound
256!>=128^128 suffices). The error in the argument is below 2^-20 and sine
and cosine are 1-Lipschitz. Rounding to the nearest multiple of 2^-14
contributes at most 2^-15, and the argument error contributes at most 2^-20.
Thus the result, including multiplication by z, is a dyadic number h_tilde_t
in [-1,1] satisfying |h_tilde_t-h_t|<2^-15+2^-20<1/16384, uniformly in all
k,t,N. Clipping cannot increase the error because the exact target belongs to
[-1,1].

Add these exact dyadic scores over all M records. Mark a candidate exactly
when
\[
 t<N\quad\hbox{and}\quad {1\over M}\sum_i\widetilde h_t(k_i,b_i,z_i)
 \ge {167\over1000}.
\]
Each exact dyadic score is an integer multiple of 1/16384. Let A be the
signed sum of these score integers; the threshold comparison is exactly
`125*A >= 342016*M`, as implemented below. On the good events of section 2
the true secret's computed mean is at least 138219697995401/824633720832000-2*delta, whereas
every wrong secret's computed mean is at most 137207964762487/824633720832000+2*delta. The threshold is
137625600000000/824633720832000. Therefore there is exactly one marked n-bit string, namely s.
Strings t>=N are rejected explicitly.

## Streamed exact score implementation

Within this implementation section let D=16384, the fixed dyadic score
denominator. Section 4 separately uses D=2^n for the search-domain size.

Fix a classical record label k. The n-qubit candidate t can be in an arbitrary
superposition and ranges over every n-bit string, including t >= N. Introduce
an n-qubit accumulator R initialized to zero. For j=0,...,n-1 compute the
classical constant

```
c_j = 2^j k mod N,
```

and add c_j modulo N to R, controlled by the candidate bit t_j. At every
stage R is a valid residue, so at completion it equals k t mod N for every
basis value of t. Linearity establishes the same coherent calculation for
superpositions and entangled candidates. Neither k nor t needs to be
invertible modulo N.

Each controlled addition is the permutation which acts as addition modulo N
on R<N and as the identity on R>=N. A ripple addition, comparison and
conditional subtraction evaluate this permutation with O(n) Boolean gates
and O(n) intermediate bits. Evaluate it cleanly into an n-bit target, swap
input and target, and XOR the inverse permutation of the new input into the
old input. The last register becomes zero. Clean Boolean evaluation stores
each of its O(n) gate outputs, copies its result, and reverses its gates.
The resulting controlled permutation has O(n) exact NOT/CNOT/Toffoli gates
and O(n) reusable scratch qubits. This is the construction proved explicitly
in `label-extraction.md`; its identity extension ensures a unitary on the
entire n-qubit register.

There are n additions. Therefore coherent modular multiplication uses O(n^2)
gates and O(n) qubits, with no accumulated history across additions. It can
be reversed by applying the same controlled additions backwards with their
signs reversed. All scratch registers are zero between additions.

The constants c_j are generated by n successive classical modular doublings,
using O(n^2) elementary Boolean work. For convenient forward and backward
access, store the n constants for the current record in an O(n^2)-bit
classical array. This array is reused for each record. Its accesses have
classical addresses; candidate bits never address this array. This storage
fits within the O(n^2) space already required by the M records.

## A clean, linear-space single-record evaluation

The finite score procedure in this proof starts from r=k t mod N and
forms

```
u = floor(2^24 r/N) / 2^24.
```

This quotient needs only 24 restoring-division steps. Start a scratch
remainder at r. In each step double the current remainder, compare it with N,
emit one quotient bit, and subtract N when necessary. The remainder is again
in [0,N). Each step has O(n) Boolean gates and intermediate wires. Keeping
the histories of all 24 steps therefore still takes O(n) wires and O(n)
gates, since 24 is an absolute constant. Its clean reversible evaluation
copies the 24 quotient bits and uncomputes this history. There is no need to
retain the O(n^2) history of a general n-bit-by-n-bit division.

The remaining Machin-series calculation, rational Taylor polynomial through
degree 255, rounding to multiples of 1/16384, and clipping all use absolute
constant bit lengths: their inputs have only 24 fractional bits, and all
degrees, coefficient numerators and coefficient denominators are fixed
independently of n. Their finite Boolean circuits consequently have absolute
constant size and space. Those possibly large constants are counted; they
are not instance advice or an uncharged real-arithmetic oracle. Computing
the fixed rational pi approximation is charged once during preprocessing.

Thus there is a clean reversible evaluation V_i for the i-th record,

```
|t>|0_score>|0_work> -> |t>|a_i(t)>|0_work>,
```

with O(n^2) gates and O(n) scratch qubits. Here a_i(t) is the exact signed
integer in [-D,D] returned by the prescribed approximation procedure, and
the signed score register has a fixed 14 bits. To implement V_i, compute r,
evaluate and copy the finite score, reverse the score calculation, and
reverse the modular multiplication to clear r. The sign and choice of sine
or cosine are literal classical record bits. V_i has an exact inverse and
uses only exact Clifford+T gates. Its O(n) workspace includes the n-qubit
candidate and modular arithmetic registers, the constant-size finite-score
circuits, and all clean ancillas.

## Accumulate one score at a time

Use a signed two's-complement accumulator A of

```
w_A = 2 + ceil(log2(D M + 1)) = O(log(n+1))
```

bits, initially zero. For i=1,...,M, perform V_i, add its signed 14-bit score
to A by a reversible ripple adder, and apply V_i inverse to clear the score
register. The addition costs O(w_A) gates and O(w_A) reusable scratch
qubits. Every partial mathematical sum lies in [-MD,MD], so this accumulator
does not overflow; its modular bit implementation represents the intended
signed integer on every branch. The output of the loop is the exact integer
sum A(t), with every other work register zero.

Compute the predicate

```
F(t) = [t < N and 125*A(t) >= 342016 M],
```

apply its phase, and uncompute that comparison. Finally reverse the entire
accumulation loop, using subtraction in place of addition, to clear A. Since
D=16384 and 125*D*(167/1000)=342016, this is precisely the score predicate.
The sum accumulator retains its stated width w_A. For the comparison use
a separate signed scratch register of width

```
w_C = 24 + ceil(log2(M+1)) = O(log(n+1)).
```

Sign-extend A into this workspace and form 125*A by a 7-bit left shift
and subtraction (125 = 128 - 3). Every partial sum obeys |A|<=16384M. Thus
|125*A|<=2048000M, and 125*A-342016M lies in [-2390016M,1705984M]. All these
signed values fit within w_C bits, whose magnitude capacity exceeds 8388608M.
The threshold 342016M is computed classically and charged. No modular overflow or rounding
of the rational threshold occurs; negative sums fail the positive-threshold
test. Compute, copy/use, and uncompute the comparison workspace cleanly.
The extra arithmetic uses O(w_C) gates and scratch bits, so each comparison
still uses O(n+w_A+w_C)=O(n) gates and scratch bits. Its strict or
non-strict choice at equality has no effect on the proved good event,
whose separation is greater than 1/1700 on both sides of the threshold;
the displayed non-strict comparison is used consistently, including in
the final classical candidate checks.

There are O(M) clean record evaluations and reversible additions in the
phase oracle. The gate count is

```
O(M (n^2 + log(M+1))) = O(n^3).
```

The peak quantum allocation is O(n + log(M+1)) = O(n), since all record
workspaces are reused. In particular, the sum's history is not retained.

## Streaming, addresses, and joint charged work

Keep all M classical records, which take M(n+2)=O(n^2) bits. Keep the input,
loop counters, O(n^2)-bit current modular-constant array, and fixed rational
constants. These together use O(n^2) bits. No list of the full oracle's gates
is stored. Ripple circuits, the fixed 24-stage division circuit, comparisons,
and the fixed finite-score circuit have gate-by-gate generators using binary
counters and explicit wire-index formulas. Their inverse circuits are emitted
by traversing their indices in reverse order. This does not require storing
the output circuit or its quantum computation history.

The whole memory allocation is O(n^2), so each ordinary indexed access or
classically addressed gate incurs O(log(n+1)) charged bit operations.
Generating a ripple gate's indices and reading a constant bit also takes
O(log(n+1)) bit work. The arithmetic schedules are regular; no search or
quantum-addressed lookup is hidden in gate generation. Regenerating the
current record's modular constants as needed costs O(n^2 log(n+1)) charged
work, which is within the same per-record envelope. Thus each exact oracle
execution, including all classical generation and memory access, costs

```
O(n^3 log(n+1)).
```

Reflection about the uniform n-qubit state costs O(n) exact gates with O(n)
clean ancillas, so it fits within this bound. The fixed 16-trial search makes
at most 16*2^(ceil(n/2)+1)=O(2^(n/2)) oracle iterations, including every
failed trial and any record set with zero or multiple marked candidates.
Its counters need O(n) classical bits. The final at-most-16 classical
predicate checks fit within the same charged-work bound and O(n^2) storage.

For completeness, record extraction also meets these tighter storage
bounds. With error per copy delta=1/(2^16 M), the exact-gate extractor uses
q=O(log(n+1)) precision, O(n) qubits and O(n+log(q+2)) temporary classical
bits per copy. At most one sample is acquired and processed at a time.
Its n controlled-translation scales each need O(log(n+1)) repeated tests,
and each translation needs O(n) gates. With the global record-storage
address charge included, total charged extraction and collection work is

```
O(M n^2 (log(n+1))^2) = O(n^3 (log(n+1))^2).
```

It acquires exactly M source copies; repeated tests of a retained source
copy are not additional acquisitions. Acquisition itself contributes
M(n+1)=O(n^2) charged work. Initialization, measurement, disposal and all
finite fixed preprocessing fit within the displayed bounds. Processing a
bad sample can change its transcript but cannot change any loop bound,
register width or gate-count envelope.

Combining these calculations gives the more informative work expression

```
O(2^(n/2) n^3 log(n+1) + n^3 (log(n+1))^2).
```

It is bounded by O(2^(n/2)n^3 log_2 n), uniformly for every integer n>=1.
Write L=log_2 n. For the first term, log_2(n+1)<=log_2(2n)=1+L<=2L for
n>=2, so that term is at most 2*2^(n/2)n^3 L. For the second term, the
elementary inequality log_2(n+1)^2<=2^(n/2)L holds for every n>=3: at n=3
it reads 4<=4.482, and both sides are eventually increasing with the
right-hand side growing by the factor 2^(1/2) per unit step while the left
grows only logarithmically, so it persists. At n=2 the second term is
absorbed by the same absolute constant. Hence the proved expression is at
most a fixed multiple of 2^(n/2)n^3 L for all n>=2, which is exactly the
assertion T=O(2^(n/2)n^3 log_2 n). The exact
coefficient 1/2 in the exponential is unchanged. For this representative
time envelope, log2 B_T=n/2+3 log2 n+log2 log2 n, hence its growth index is 1. The
polynomial envelopes n^2, n, and n have index 0. All five claims, including
the constant fraction 83/250 under the complete adaptive malformed-copy
model, concern the same finite algorithm and deterministic acquisition
count.


## 4. Capped search, including all bad branches

Put D=2^n and R=2^(ceil(n/2)+1). Perform at most 16 trials. In each trial,
choose an independent uniform integer q in {0,...,R-1} using exactly
ceil(n/2)+1 measured |+> qubits. Prepare the uniform superposition of all D
strings with n Hadamards. Apply q Grover iterations for the predicate above;
each is the clean phase oracle followed by reflection about the uniform
state. The latter uses H gates, X gates, and a multiple-controlled Z built
from O(n) exact Toffoli gates with clean ancillas. Measure t, check the same
integer predicate classically, and return t if it is marked. If all 16 trials
fail, return 0. No more source copies are ever acquired.

On the good record event there is exactly one marked string. With
theta=arcsin(1/sqrt D), one trial's success probability, averaged over q, is
\[
 {1\over R}\sum_{q=0}^{R-1}\sin^2((2q+1)\theta)
 ={1\over2}-{\sin(4R\theta)\over4R\sin(2\theta)}>{1\over4}.
\]
Indeed sin(2theta)=2 sqrt(D-1)/D>=sqrt(2)/sqrt D for D>=2 and
R>=2 sqrt D, so the absolute correction is at most 1/(8 sqrt2)<1/4.
The displayed sum is an exact finite geometric-series identity. Conditional
on a fixed good record set, the fresh preparations and random q's make the
16 trial failures independent, so total search failure is at most
(3/4)^16<1/64. A successful marked result is necessarily s. Combining the
actual-record concentration and search bounds gives unconditional
success at least
\[
 1-1/256-1/64>1-1/256-2^{-16}-1/64>2/3.
\]
On every other record set, with zero, one, or many marked strings, the same
16-trial cutoff applies. In particular there is no hidden expected-time
loop, rejection sampling, postselection, or source restart.


The declared representative envelopes are 2^(n/2)n^3 log_2 n, n^2, n and n. Their exact growth indices are 1,0,0,0. This theorem does not achieve the cube-root research target.
