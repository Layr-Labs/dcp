# PSG4-THIRDBASE-REFINED: variable-width streaming sieve with a weighted work cutoff

## 0. Joint theorem and provenance

For every integer N>=2 and every s in Z/NZ, let n=ceil(log2 N) and
L=log2 n. The single algorithm PSG4-THIRDBASE-REFINED below recovers the entire s from
independent ideal source copies with unconditional probability at least
1-2^-8>2/3. On every execution branch, including failed attempts, rejected
copies and both cutoff branches, it has the simultaneous bounds

 T=O(2^((3/4)sqrt(nL)+sqrt(n)L^(-3/8))),
 S_C=O(n^2) classical bits, S_Q=O(n) qubits,
 Q=O(2^((1/2)sqrt(nL)+sqrt(n)L^(-3/8))).

These asymptotic representatives apply for n>=2; the explicit finite branch
covers n=1 as well. All constants are absolute and independent of N,s and
outcomes. The exact resource growth indices are [1/2,0,0,1/2]. The fifth
claim is fractional tolerance0 with the baseline's exact clean-copy model.
This is not a cube-root-time or optimality claim.

Immediate complete program source: PSG4-THIRDBASE,
b9d09a8b-8f16-4bc1-9e47-0e95256fa792, published commit
6ab863cadb6f56ddb590a155ea284bbb75be5dc2. Its exact program, third-base
threshold, source/decoder, memory and two caps are unchanged and restated.
This candidate also uses the refined lower-order capacity/gap theorem of
PSG4-SEVENELEVEN-REFINED,33a7495f-9510-45b2-b1e4-2b5f82f05b3c,
restating its method for q=1/2. The improvement is an analytical upper
bound with G=sqrt(n)L^(-3/8), not a claim that unchanged circuits run faster.
The complete source credits C4096 010beaf6-a810-46ed-997f-6213f4424a50
for the exact instrument and cutoff framework. Section9 proves the exact
two-term bounds without hiding the lower-order term in an outside constant.
The measured-bank interpreter is not used in this configuration.

The source credits PSR2 16bb6065-c3ca-45fb-b514-86106a310646,
SLS 59facd77-4082-40d9-910e-9060c197e72a,
CS1 f1481815-9577-4990-abe3-7b79fa5d9284, collective tests
844c0fd2-9b1c-4e84-a37c-f402e109985f and stride decoding
50a9f13c-eda5-4239-a3c8-28ed83e8ce83. These historical credits
are retained; no prior verdict or provisional attribution edge is a
mathematical premise. The full proof is self-contained.

The historical Regev class is established, not a cube-root breakthrough.
Grover search is from quant-ph/9605043; random iteration search is analyzed
in Boyer, Brassard, Hoyer and Tapp, quant-ph/9605034v1, Sections3-4.
The needed search formula, capped algorithm, state projection, label law
and full gate costs are derived here. No oracle query is treated as free.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, comparison, copy or
increment has O(w) Boolean gates using ripple carry, with O(w) scratch.
Reversibly compute a Boolean circuit, copy out its answer, then reverse it;
a permutation can be computed into a fresh register, swapped, and erased by
its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has an exact constant
Clifford+T decomposition. Wire counters, generation, initialization, resets,
measurements and classical reads/writes are counted. Every indexed action
also pays O(log(S_C+S_Q+2)) bit operations. Gates are generated in streaming
order; no circuit description of exponential length is stored.

Only H, S, S-dagger and these exact reversible gates are used. In particular,
there is no arbitrary-N QFT circuit or approximate rotation to synthesize.
Fourier LABELS are inferred by nondestructive translation tests, with their
precision, tests and global error budget charged below. The source is used
only for fresh mixed copies; no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole algorithm
is a linear (adaptive) quantum instrument applied to independent copies. So
the joint law of all its classical outcomes equals the law obtained by first
drawing, for every copy, an independent uniform latent label k, and then
running on the product state phi_k(s) (x) chi_k. All probabilities below use
this model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (3.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which EXTRACT recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation with
alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 3. Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)


EXTRACT uses Qcap fixed in Section 8. Put J_e=n+4,

    h=ceil(log2(2^16 Qcap (n+5))), F=2^21 h.

It runs RUN(F) below once, without verification, fallback or restart.
Conditional on the latent label k, the data register is unchanged by every
test. Afterward discard that register and keep its control qubit, applying X
when the positive phase convention is needed. The latent-label mixture makes
this procedure valid for the mixed source, without access to its purification.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

### Level-wise extraction RUN(F)

For each basis take F collective ROUNDS. In one round prepare J_e+1=n+5
ancillas in |+>, representing x=sum_(j=0)^J_e x_j2^j. Compute z=x modN
coherently, apply the register-controlled translation u<-u-z modN to the
data, and uncompute z and reduction scratch. This equals the product of
all individually controlled translations Tr_(-2^j). To compute the remainder,
x<2^(n+5)<64N since N>2^(n-1); six compare/conditional-subtract steps with
32N,16N,...,N suffice, keeping their six borrow flags for reversal.
All arithmetic has O(n) wires and O(n) exact reversible gates. On the
Fourier eigenstate chi_k the ancilla state is EXACTLY

    tensor_(j=0)^J_e (|0>+omega^(k2^j)|1>)/sqrt2,

while data and spectators are unchanged. Measure all ancillas in the chosen
X or Y basis, add each outcome to its own empirical counter, and reset the
ancillas before the next round. Conditional on k these outcomes are
independent across levels and rounds, with exactly the same means as the
separate tests. Thus each level still has F tests per basis and the same
concentration and unwrapping proof. No approximate QFT or rotation is used.

The n+5 counters each have O(log F) bits. Updating all of them costs
O(n log F) per round even with conservative ripple increments; their total
storage is O(n log F)<=O(n^2). Round-loop and gate-generation bookkeeping
are charged as well. Here log F=O(log n)=O(L), since h=O(R+log n)=O(n).
The quantum translation costs O(n) per round. Decoding and unwrapping add
O(n^2) core operations. Consequently a full call costs

    O(n h L+n^2 L) core operations,

with O(n) qubits, O(n^2) classical bits. Since R=O(sqrt(nL)), h=O(R+log n)
and L^(3/2)/sqrt n is bounded, this is O(n^2 L) for the complete profile.
All finite exceptions are absorbed by an absolute constant, using the
same fixed round counts. The source label error bound below is unchanged.

Decoding each level. Pick the least dr in [0,64) maximizing
x_j Cos[64 dr] + y_j Sin[64 dr].
- If |x_j - cos| and |y_j - sin| are at most 1/1024, each computed dot product
  differs from cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256.
- The nearest direction has true dot >= cos(pi/64) >= 511/512.
- Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
- The gap 15/512 exceeds 2/256. So alpha_j = dr/64 is within circular distance
  1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be
whichever of g_(j+1)/2 and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j
(ties: the first).
- Suppose g_(j+1) is within e < 1/16 of 2^(j+1) k/N. The correct preimage is
  within e/2 of 2^j k/N, hence within 1/16 + e/2 < 3/32 of alpha_j.
- The other preimage is at least 1/2 - e/2 from 2^j k/N, hence more than 13/32
  from alpha_j.
- So the choice is correct and the error halves. Finally g_0 is within
  2^-(J_e)/16 = 2^-(n+8) < 1/(2N) of k/N.

RUN(F) outputs floor(N g_0 + 1/2) mod N, which then equals k. On any input it
returns a value in [0,N) after its fixed number of tests.

Concentration. For F independent +-1 variables, the centered log-moment
generating function has second derivative at most 1 (a tilted variance) and
vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and
F = F(h) this is 2 exp(-h). So RUN(F(h)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h) = 4 (n+5) e^(-h), uniformly in k.
RUN(F(h)) uses 2F(h) collective rounds supplying 2(J_e+1)F(h)
individual outcomes, at the charged cost proved above.


Since e^-h <= 2^-h, the per-call probability of an incorrect label is at most
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n h L+n^2 L)=O(n^2 L) core operations under the actual
profile budgets, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. Work-balanced profile and bounded-search combiner

Main-branch parameters are computed once for n>=256. Fix C=4096,
cancel b bits using r=b+6 children, and use beta=21/20. The exact decrement is

    delta(v)=min{d>=0:20*2^d>=21*(2v+6)}.

This is ceil(log2((21/20)(2v+6))), computed by integer bit length
and one exact comparison. Section 4.3 proves advancing probability at
least 3963/4096>20/21, so this beta bounds the expected attempts.
The exact certificate is 3963*21=83223>81920=4096*20.

The success/decrement proof is the retained C4096 one. The larger base
is a different actual schedule trading paid time for source copies;
no smaller-height or all-axis-dominance assertion about the quarter-base
configuration is made.

Starting at a positive trial R put u=max(1,floor(R/3)). Descend by
v<-v-delta(v), retaining only values v>=u and stopping as soon as the
next value is below u. Reverse the retained values to obtain
v_1,...,v_mstar=R, with sum S_u(R). For i>=2 the usual decrement relates
v_i and v_(i-1), while the base v_1 directly combines fresh leaves.
Choose the least positive R with 2S_u(R)>=n. Search sequentially; no
monotonicity is assumed. It terminates by R<=ceil(n/2), since2S_u(R)>=2R.
Generate profiles and counters with counted polynomial-time integer
arithmetic. Put

    q0=(2u+6)*2^(R-u).

A PS_TREE(D,B) call,1<=D<=n,0<=B<D, has independent ideal leaves with
uniform known labels in[0,2^D). When B=0 return one leaf. Unless explicitly
stated otherwise (the odd-part decoder), calls use B=D-1. Otherwise allocate
actual widths b_mstar,...,b_1 greedily from the root down, b_i=min(2v_i,
B-already_allocated). Then sum_i b_i=B. Set r_i=1 for b_i=0, and r_i=b_i+6 for b_i>0, and
p_i=sum_(j<i)b_j. Level0 returns a leaf. A zero-width level just returns
its child. For b_i>0, recursively build r_i fresh child outputs, then check
and add weight2^v_i to the global weighted-attempt counter before executing
the combiner below. If that would exceed Wcap, abort. On FAIL discard ALL
inputs and query scratch, and build fresh children before trying again.
No output label, including zero, is rejected inside the tree merely because
of its higher bits or value.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+6, b=b_i, p=p_i. Their joint state is

 2^(-k/2) sum_(y in{0,1}^k) exp(2pi i th A(y))|y>, A(y)=sum_j y_j a_j.

Set c_j=(a_j/2^p) mod2^b. Reversibly compute f(y)=sum_j y_j c_j mod2^b,
measure it to obtain e, and reset that measured register. The remaining
phase state has equal magnitudes on C_e={y:f(y)=e}.
Hold this original register untouched during discovery on SEPARATE query
registers. The discovery procedure below returns at most4096 distinct,
classically verified members of C_e, using only c_j,e and fresh random bits.
It need not certify completeness. Sort the found strings and pair adjacent
ones, dropping an unpaired singleton. Reversibly compute on the original y
a success flag and a constant-size pair ID from equality tests with the
known list, then measure them. If y matches no pair, FAIL and discard.
Otherwise it is now an equal-magnitude superposition of exactly two known
strings y0,y1, with their original phases. Reset measured flags from their
known values. XOR y0 into y, choose a differing pivot, and use CNOTs from
that pivot to clear every other differing position. The surviving qubit has
label a'=A(y1)-A(y0), a FULL signed integer, not reduced modulo2^D or N.
Every successful branch is exactly this phase qubit, up to global phase,
regardless of whether discovery found the entire fiber.

The output is divisible by2^(p+b), since both selected strings have residue e.
It has a nonzero symbolic incidence vector in{-1,0,1} over distinct original
leaves: y0!=y1 differs in some child, child incidence vectors are nonzero,
and child leaf sets are disjoint. This induction starts at a single leaf.
Full labels are stored, but ALL choices of found strings and pairs, and
all success probabilities, factor through input residues modulo2^(p+b).
The unknown phase th is absent from this selection kernel. Computing a
full output label after selection does not add a selection rule on its high
bits. This distinction is used in the marginal argument of Section5.

### 4.2 Bounded discovery, exact Clifford+T circuits

Fix C=4096. If k<=12, enumerate at most4096 strings and retain the first4096
solutions; this has constant enumeration length. If k>=13, use at most4096
search blocks. Each block makes at most4096 trials, stopping at its first
new verified solution, which is added to the list. Stop discovery after an
empty block or after4096 found solutions. The list never contains a duplicate
or a false solution. On each trial:

 * Set J0=2^ceil(k/2), draw uniform j in[0,J0) with ceil(k/2) fair bits.
 * Prepare a fresh k-qubit query in |+>^k. Apply j Grover iterations for
   membership in C_e minus the found list. Measure its candidate string.
 * Verify its residue and novelty classically. Reset query registers before
   the next trial. The original phase-index register is not touched.

Membership is a COUNTED circuit. Controlled additions of the known b-bit
constants c_j compute f(z) in O(kb) gates; compare with e, exclude at most4096
known strings with equality flags, apply Z on the computed flag, then
uncompute. This uses O(kb+4096k) gates and O(k+b) scratch up to fixed constants.
Diffusion about |+>^k is H^k, a multi-controlled sign flip and H^k; a clean
Toffoli chain implements the sign flip in O(k) gates and scratch. Z=S^2.
All are exact Clifford+T. Known weights and strings are read by a classical
loop emitting gates; no quantum-addressed lookup, QRAM or stored circuit of
exponential length occurs. Gate generation, verification, fair bits, counters,
measurements, resets and all oracle work are charged.
There are at most16777216 trials, each with fewer than J0 iterations. Since
k=b+6<=2v_i+6, J0<=2^(v_i+3). Thus one complete attempt costs
O(v_i^2 L2^v_i+n v_i L) core operations, simplified below, and O(n)
quantum scratch. For explicit generation, enumerate the k controlled b-bit ripple additions
and their reversals in nested loops, and enumerate at most4096 k-bit equality
comparisons. Each elementary-gate template and its wire indices use O(L)
core bookkeeping, including classical operand reads and loop counters.
There are O(kb+4096k+n)=O(v_i^2+n) elementary operations per iteration.
Verification and the bounded-list sort cost O(v_i^2 L); the single full
signed-label update adds at most k<=2v_i+6 n-bit labels, in O(n v_i L).
This full-label work is outside the Grover loop. Since n<=2R^2 and
v_i>=u=floor(R/3)>=R/8 on the main branch, n<=128v_i^2. Therefore
n v_i<=128v_i^3<=128v_i^2 2^v_i, and the entire complete attempt costs
O(v_i^2 L2^v_i)<=O(R^2 L2^v_i) core work on every branch.
This proves a tighter bound for the same streamed circuits and loops. The factor L in the displayed bound
includes this conservative bookkeeping; the model's separate logarithmic
address charge is still applied globally in Section9.
The fixed-size found list needs O(n) classical bits. All these are
branchwise limits, independent of search success.

### 4.3 Discovery probability and the measured-fiber moment

Suppose the measured fiber has at most C=4096 members. At a search
trial with 1<=m<=C remaining solutions let A=2^k and sin^2(gamma)=m/A.
The two-dimensional good/bad rotation gives success sin^2((2j+1)gamma).
Summing over uniform j in [0,J0) yields exactly

    mean success=1/2-sin(4J0*gamma)/(4J0*sin(2gamma)).

For k>=13, m<=4096<=A/2, so sin(2gamma)>=sqrt(2/A) and
J0>=sqrt A. Each fresh search trial succeeds with probability greater
than 1/4 while any undiscovered solution remains. Each 4096-trial block
therefore misses with probability at most (3/4)^4096<(3/4)^128<2^-32.
There are at most 4096 relevant blocks, so premature stopping probability
is below 2^-20<=1/1024. Small k<=12 is enumerated exactly and has at
most 4096 basis strings in its entire space. No counting oracle is used.

Now the r=k=b+6 low residues are independent uniform in Z/2^bZ.
The actual residue outcome has the law of f(Y) for a uniform binary Y.
For each z!=Y, a coefficient of f(z)-f(Y) is +1 or -1, so its residue
is uniform. Thus the SIZE-BIASED fiber expectation is

    E |C_(f(Y))|=1+(2^k-1)/2^b<65.

By Markov, the probability of a measured fiber larger than 4096 is below
65/4096. On complete discovery the mass lost by dropping unmatched
strings is at most #fibers/2^k<=2^b/2^k=1/64. Therefore

    Pr[success]>=1-65/4096-1/1024-1/64=3963/4096>20/21. (4.1)

This is an average over fresh low labels and search coins before each
whole attempt, not a pointwise guarantee conditional on arbitrary full
labels. The successful pair's exact correctness and low-only selection
kernel remain valid even when a fiber is large or discovery is incomplete.

## 5. Unused blocks, termination and the root frequency

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Equation(4.1) gives conditional success at least1/3 before child generation,
whatever the earlier external past. Every failure releases its inputs and
restarts with fresh children. The geometric bound proves almost-sure
termination and finite expected attempts at this level.

It remains to prove the output law that closes the induction. Fix any
finite successful selection transcript through this level, containing all
used leaf values modulo2^(p+b), search choices/outcomes, residue and pair
measurements, and retry choices. Its probability kernel is a function ONLY
of those low parts, by4.1 and4.2; quantum searches used separate registers.
Write each original leaf as k_l=u_l+2^(p+b)H_l, with H_l independent uniform
in Z/2^(D-p-b). The selected output has a symbolic signed incidence vector
z_l in{-1,0,1}, not allzero, determined by the low transcript. Consequently

 x/2^(p+b) mod2^(D-p-b)=c+sum_l z_l H_l mod2^(D-p-b).

Here c is an integer determined by the low parts. At least one z_l is a
unit +1 or-1, so the sum is uniform on that cyclic group. Marginalizing over
all finite successful low transcripts proves the output law. Fresh disjoint
leaf sets give the conditional independence for successive child calls.
This conditioning does NOT include irrelevant high-valued EXTRACT records
or all full labels stored by the controller; the ideal process marginalizes
those records and uses exact latent labels. It does not condition on the
event that all actual extractions were correct. The real/ideal comparison
later uses an additive error coupling. Computing/storing full labels does
not change that marginal law: decisions at this level use only the stated
low residues, and do not filter a zero or other high output value. QED.

For every stage above the base, (21/20)r_i<=(21/20)(2v_i+6)<=2^delta(v_i).
Telescoping gives product_(i>=2)((21/20)r_i)<=2^(R-v_1). The base has
r_1<=2v_1+6. Since (2x+6)2^-x decreases for integer x>=1 and v_1>=u,

 q_D=product_i r_i<=(2v_1+6)2^(R-v_1)<=q0.

A returned tree has q_D nominal distinct leaves. Its label is2^B W with
integer |W|<2^(D-B)q0. All stored labels and sums have O(n+log q0)=O(n) bits,
including incorrect numerical-label branches. No incidence vector is stored.
Lemma U is unchanged at the new base: its inputs are independent fresh
uniform leaves and the same low-bit selection proof applies to its b_1 bits.

For the root write h=D-B>=1 and each accepted leaf as
k_l=u_l+2^B tau_l, with independent uniform blocks tau_l in[0,2^h).
Condition on low parts u_l, residue/search/pair outcomes, retry choices and
independent previous roots. All these kernels use only bits below B and
are phase independent. Thus the tau_l remain independent uniform blocks.
Its nonzero signed incidence vector gives

 W=c+sum_(l in S+)tau_l-sum_(l in S-)tau_l, |S+|+|S-|>=1.

Lemma5.1. With A=2^h, for every real y, conditional on that low transcript,

 |E exp(2pi i yW)|<=D_A(y)=|(1/A)sum_(t=0)^(A-1)exp(2pi i yt)|,
 D_A(y)<=|cos(pi y)|,
 D_A(y)<=min(1,1/(2A*||y||)) when ||y||>0,                (5.2)
 Pr[W odd]=1/2.                                         (5.3)

Proof. Each independent block contributes D_A(y); at least one is present
and all factors are at most1. Writing a uniform block as its independent
fair binary digits factors its characteristic modulus into
product_(j=0)^(h-1)|cos(pi2^j y)|, giving the first bound. The geometric sum
has modulus |sin(pi A y)|/(A|sin(pi y)|). For circular distance x=||y||
in(0,1/2], the sine chord gives |sin(pi y)|>=2x, proving the second bound.
At y=1/2 the fair lowest bit makes the characteristic function zero, so
parity is fair. This is about the full signed integer W, not a claim that
its full integer distribution is uniform. Irrelevant high EXTRACT records
and future budget survival are marginalized, not conditioned on. QED.

## 6. Odd-part recovery by free-frequency decoding

If M=1, put s1=0, K=0, Sodd=0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta=s1/M in[0,1). Define

 hmax=1+floor(u/8), h=min(d-a2,hmax), B=d-h>=a2,
 stride=max(1,h-4), D=d, nq=2^(h-1)q0,

and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j=0,...,J, where J is least nonnegative with
2^((J+1)*stride+2)>2M. Put Sodd=J+1. Because stride>=1, Sodd<=n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^(j*stride) (2^(B-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^B W th = W 2^(B-a2) alpha_j s / M = 2^(j*stride) W s1 / M   (mod 1),            (9.1)

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a PS_TREE(d,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. For i = 1..K:
- run PS_TREE(d,B);
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1}
  together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^(j*stride) W_i.

Candidates. Put P_j = j*stride + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j*stride+2) of the previous center z_(j-1). This is one or two explicit
  integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of 2^-(P_j),
  so the two arc endpoints are themselves candidates.
- There are at most 2^(ceil(log2 nq)+7) + 2 <= 2^(ceil(log2 nq)+8) candidates.

The candidate set is fixed by information available at the start of the stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have
fixed lengths, and the decoder returns a candidate on every branch.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j*stride+stride+2) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 5 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the held-out blocks of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (4.1), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^(j*stride) 2 nq,

    |f_i Delta0| < 2^(j*stride+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j*stride+stride+2). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j*stride+1). Hence xx=2^(j*stride)|Delta| lies in[2^(-stride-2),1/2]
for each far candidate. Fresh trees are independent of Fs_(i-1), conditional
on its low transcript. Averaging the fair basis and the full signed root
frequency gives

 E[xi_i | Fs_(i-1)] <=(1/2)D_(2^h)(2^(j*stride)Delta).

If h<=4, stride=1 and xx>=1/8, so the cos bound is at most cos(pi/8).
If h>=5, stride=h-4 and xx>=2^(-h+2); the block bound is at most
1/(2*2^h*2^(-h+2))=1/8<cos(pi/8). Thus the SAME old far-point score
upper bound (1/2)cos(pi/8) holds uniformly for every stage and modulus.
The larger frequency range is already included through nq=2^(h-1)q0.

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is a
martingale whose increments lie in intervals of length 2. By Azuma-Hoeffding
it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every far
candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count bound. The chosen hmax is Theta(R) as R grows, since
u=floor(R/3). If h=hmax, stride=Theta(R), so Sodd=O(1+log M/R).
If h<hmax, then h=d-a2=floor(log2 M), hence log2 M<h+1. For h>=5,
h/(h-4)<=5; for h<=4, stride=1. Thus Sodd=O(1) in this case.
In all cases Sodd=O(1+n/R), K=O(log nq+log n)=O(R), because h<=hmax=O(R)
and R>=sqrt(n/2). Consequently Sodd*K+2n=O(n), with absolute constants.
These are bounds for the fixed stage counts before execution, not favorable
outcome counts. No factorization of the odd M is needed.

## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run PS_TREE(wd,wd-1). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (5.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.


## 8. Complete algorithm, two cutoffs and success

For n<256 use exhaustive shift testing. For t=0,...,N-1 use at most n+10
fresh copies, subtract t modulo N controlled by the first qubit, and measure
that qubit in X. Reject t at the first minus and output the first candidate
passing every test, or0 if none. The true t=s always passes; each wrong
candidate passes a fresh test with probability1/2. Thus wrong output has
probability<(N-1)2^(-n-10)<2^-10. It uses at most N(n+10) copies,
O(n) qubits and O(n^2) classical bits. All charged work is O(Nn^4).
The fixed finite prefix is absorbed in the stated asymptotic bounds.

For n>=256 compute the profile of Section4, all decoder parameters and K.
Define integer budgets

    H0=Sodd*K+2n,
    Qstar=6*(2u+6)*2^(R-u)*H0+2n, Qcap=1024Qstar,
    Wstar=3*mstar*2^R*H0, Wcap=1024Wstar.

The fixed H0 overbounds Sodd*K+2a2 for every modulus; when M=1, Sodd=K=0.
Initialize the acquisition counter and the weighted-attempt counter to zero.
Before any acquisition that would exceed Qcap, abort, release all registers
and output0. Before a combiner attempt, after building its inputs, check
whether adding its nominal weight2^v_i would exceed Wcap; if so abort
likewise, otherwise add it and execute the complete attempt. EXTRACT uses
this fixed Qcap. Run the odd-part decoder followed by the2-adic procedure,
then output(s1+M*s2) mod N. No circuit execution is hidden in either counter.

Expected source bound. In the ideal uncapped run each accepted leaf costs
at most two source copies. By Lemma U and(4.1), before each attempt generates fresh children it
succeeds with probability at least20/21. Thus, uniformly over previous history,
E_i<=(21/20)r_i E_(i-1). Zero-width shortcuts only reduce this bound.
Above the base the factors(21/20)r_i telescope. The base uses at most
(21/20)r_1 leaf calls, each costing at most two source copies in expectation.
Consequently

 E_root<=(21/10)(2v_1+6)2^(R-v_1)<=6(2v_1+6)2^(R-v_1)<=6(2u+6)2^(R-u)=6q0.

No independence of attempt cost and success is required. The event of
reaching an attempt depends on earlier attempts; its fresh child calls
have the same uniform conditional cost bound. Summing their geometric
upper bound, with failure at most1/21 before each fresh attempt, gives the
displayed recurrence. Conditioning on fixed child labels is not used. Odd-part decoding uses at
most Sodd*K roots; each of at most n2-adic bits needs two roots in expectation
by parity fairness, or two direct copies when wd=1. Thus ideal expected
acquisitions are at most Qstar, irrespective of earlier decoder outcomes.

Expected weighted-attempt bound. For a root call, the expected number of
leveli attempts is at most (21/20) product_(j>i)((21/20)r_j). The same conditional
geometric-sum argument proves this by induction, including attempts in
failed ancestors. Telescoping the profile gives

 product_(j>i)((21/20)r_j)<=2^(R-v_i).

Hence the expected sum of weights at that level is at most
(21/20)*2^(R-v_i)*2^v_i<3*2^R, and at most3*mstar*2^R over all levels.
Zero-width shortcuts contribute zero. Summing over all roots, with the
same conditional argument for odd-W repeats, bounds ideal expected total
weighted attempts by Wstar.

Apply Markov separately to source count and weighted attempts in this
ideal uncapped process. Each cutoff changes it only on an event of
probability at most1/1024. In particular, a work cutoff before the next
attempt implies the uncapped weighted total would exceed Wcap; children
already built are already charged. There is no assumption that caps and
decoder events are independent. The odd-part error is at most2^-20, and
conditional on its correctness the2-adic measurements make no error.
On the actual capped run the probability of any EXTRACT label error is
at most2^-14 by Section3. Couple the actual and ideal processes until
a label error or cutoff. Total failure is at most

    2^-10+2^-10+2^-14+2^-20 < 2^-8.

The finite branch meets that bound as well. This proves unconditional
full-secret success at least1-2^-8. All trials, failures and aborts remain
in the resource counts; nothing is postselected free of charge.

## 9. Every-branch resources and explicit envelopes

### Exact profile estimate and an explicit lower-order term

Put F=sqrt(nL) and G=sqrt(n)L^(-3/8), for n>=2. Each retained v has
an adjacent interval (v-delta(v),v] and D_R=maxdelta(v)<=log2 R+4.
For R=1 this bound is direct; for R>=2,
(21/20)(2R+6)<= (21/4)R and the ceiling logarithm is below log2R+4.
For R>=3, u=floor(R/3)<=R/3. The intervals cover [u,R],
so integrating t<=v gives

    2S_u(R)>=(R^2-u^2)/D_R>=(8/9)R^2/D_R.             (9.1)

Use the ANALYSIS trial Rtest=ceil((3/4)F+(1/2)G). Eventually Rtest<=F:
the ratio of the unrounded trial to F is 3/4+(1/2)L^(-7/8), and the
rounding contributes at most 1/F. Both positive remainder terms decrease
to zero. Thus D_Rtest<=L/2+(log2 L)/2+4. On the other hand

 (8/9)Rtest^2 >= nL/2+(2/3)n L^(1/8).

At L=2^48, (2/3)L^(1/8)-(log2 L)/2-4
=128/3-24-4=44/3>0. Its derivative is positive thereafter:
multiplying the derivative by L gives L^(1/8)/12-1/(2 ln2)>0,
using ln2>1/2 and L^(1/8)>=64. Consequently (9.1) is at least n
on this eventual range. All inequalities are analytic proofs; the
physical controller uses only the exact integer profile search.

The first-feasible height is therefore

    R<=ceil((3/4)F+(1/2)G) eventually.                 (9.2)

At every smaller input the same ordinary first-feasible search is used;
it terminates by ceil(n/2). The finite exceptional prefix changes only
an absolute outside constant in the uniform asymptotic claims. No advice,
real-arithmetic oracle, special fast branch or uncharged trial is used.
The actual algorithm does not test the analytic threshold.

As before n<=2S_u(R)<=2R^2 implies R>=sqrt(n/2), and (9.2) gives
R=O(sqrt(nL)). Also u=floor(R/3)>=R/8 on the main branch. For R>=64,
every decrement is at least log2u>=log2R-3>=(log2R)/2, so
mstar=O(R/log R)=O(R/L). These estimates concern the actual new profile.

### Original source copies

The same literal source cap is Qcap=1024[6q0 H0+2n], now with
q0=(2u+6)2^(R-u), u=floor(R/3), and all decoder parameters recomputed.
The unchanged decoder proof gives H0=Sodd*K+2n=O(n), since hmax=Theta(R).
Thus Qcap=O(n(2u+6)2^(R-u)). Furthermore

 R-u<=(2/3)R+1 <=(1/2)F+(1/3)G+5/3 eventually.

The log of every prefactor is O(log n)=o(G). The positive difference
between G and (1/3)G absorbs it, proving exactly

    Q=O(2^((1/2)F+G)).

All failed and discarded copies remain included. Counters and extraction
confidence have O(R+log n)=O(n) bits/precision, so the source and coupling
arguments remain those proved for this newly computed cap.

### Space

A depth-first tree keeps at most sum_i(r_i-1)+1=B+5m_active+1<=6n+1,
where m_active<=B counts only the positive-width levels source-phase qubits
as siblings/current outputs. Each combiner uses O(r_i+n)=O(n) scratch,
and source extraction/transforms use O(n) more. Released registers are
reused, so S_Q=O(n).

A successful leveli label is a signed sum of its distinct original leaf
labels, with coefficients in{-1,0,1}. Its magnitude is less than
q0*2^D, so O(n+R)=O(n) bits suffice even for incorrect numerical label
branches. O(n) retained phase qubits require O(n^2) label bits. Recursion
counters and budget snapshots use O(mstar*(R+log n))=O(R^2+R log n)
=O(nL)<=O(n^2) bits. The profile, bounded search-loop counters, at most4096 found strings,
EXTRACT scratch and modular arithmetic fit O(n^2) as well. K decoder frequencies and residues have O(n) bits each with
K=O(n), giving O(n^2). The found-solution list has at most4096 entries; no exponential list is stored. Therefore
S_C=O(n^2) and every address/gate pays O(log n)=O(L).

### Work, on every actual branch

Each leveli attempt uses at most16777216 bounded Grover trials, or a
constant enumeration for small k. Its residue oracle, diffusion, verification,
projection and affine phase compression are explicit circuits. Section4.2
gives O(R^2 L2^v_i) core work and polynomial scratch on every branch;
it never enumerates2^r_i strings at large r_i.
The new counter checks/updates need O(R+log n)=O(n) bit operations per
attempt and are covered by the same bound. Thus the weighted cutoff gives

 all combiner core work <=O(R^2 L Wcap)=O(nR^3 2^R)
                                     =O(n^(5/2)L^(3/2)2^R),

because mstar=O(R/L) and H0=O(n) imply Wcap=O(nR2^R/L).
This argument holds even if a source cutoff occurs inside a child call.
A completed attempt was charged before it began; an unexecuted attempt
performs only the already charged children and one polynomial check.

Each batched EXTRACT takes O(n^2 L) core operations as shown in Section3.
Its source transforms and acquisition also fit that bound. Since
q0<=4*2^R, total leaf work is at most
O(n^2 L Qcap)=O(nR*n^2 L2^(R-u)), lower than
O(n^(5/2)L^(3/2)2^R), since u grows linearly with R.
Classical decoder grids cost at most O(n^4 nq)=O(n^4 q0*2^h) core
operations by Section6's explicit grid and per-record arithmetic. Since
h<=1+u/8 and q0=(2u+6)2^(R-u), this is at most
poly(n)*2^(R-7u/8). As u=floor(R/3) and R>=sqrt(n/2), that negative
stretched-exponential factor absorbs every fixed polynomial; this cost is
therefore lower than O(n^(5/2)L^(3/2)2^R). This explicitly charges the
larger grid rather than treating the stride improvement as free.
Preprocessing uses O(n^6) core operations, also covered eventually by the
same bound; finite exceptions enlarge an absolute outside constant.
Resets, aborted allocations,
source counters and loop control are covered by these bounds.
Multiplying by the full O(L) address charge, and adding the n+1 cost per
acquisition, gives

 T=O(n^(5/2)L^(5/2)2^R)
  =O(2^((3/4)F+G)).

This uses the strict lower-order gap G-(1/2)G=(1/2)G in (9.2),
not freedom to drop a polynomial at the leading coefficient. Since
G/log n -> infinity, the gap absorbs every fixed polynomial factor
already counted in the full work ledger. The separate source gap is
proved above. Every retained source, circuit-generation, address, reset,
preprocessing and decoder cost stays included on every branch.

All four bounds apply jointly to this single parameter rule and both caps.

### Exact growth indices and the resource trade

The declared representatives are 2^((3/4)F+G), n^2, n, and
2^((1/2)F+G). Because G=o(F) and log2 F=(log2 n)/2+
(log2log2 n)/2, both exponential envelopes have exact growth index 1/2.
Both polynomial storage envelopes have index zero. This proves the
four exact indices [1/2,0,0,1/2] for one actual schedule and both caps.

Compared with the quarter-base C4096 row, the main time coefficient
3/4 is larger, and the main sample coefficient 1/2 is smaller. The
positive subleading G is explicitly retained in each declaration.
These bounds are not pure leading-coefficient claims. Neither row
dominates the other; no global frontier, optimality, or cube-root-time
assertion follows from this theorem.

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N>=2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a rigorous implementation/accounting tradeoff of
known sieve ideas, not a new exponent breakthrough. Hosted mathematical
acceptance, if obtained, remains fallible review rather than formal proof.


## 11. Rational family and the range of lower-order powers

Fix any rational q with 0<q<1/sqrt(2), and any fixed rational alpha with
0<alpha<1/2. Put

 F=sqrt(nL), G_alpha=sqrt(n)L^(-alpha),
 c=q/2+1/(4q), f=(1-2q^2)/(1+2q^2).

Then 0<f<1, c(1-f)=q, (1-f^2)c^2=1/2. Use threshold
u=max(1,floor(fR)), recomputing every profile, root, precision and literal
cap. The ONE corresponding configuration has joint bounds

 T=O(2^(cF+G_alpha)), S_C=O(n^2), S_Q=O(n),
 Q=O(2^(qF+G_alpha)),

with the same full-secret success at least 1-2^-8 and clean fraction0.
Constants may depend on fixed q and alpha, never on N,s or outcomes.
The selected claims are only q=1/2, alpha=3/8, with absolute constants.
They do not combine different algorithms in one resource row.

Proof. The source, signed-incidence, low-bit, decoder and two literal-cap
arguments are unchanged and uniform in the selected integer profile.
Search terminates by ceil(n/2). For all sufficiently large R, the retained
intervals give 2S_u(R)>=(1-f^2)R^2/D_R, D_R<=log2R+4.
Try Rtest=ceil(cF+G_alpha/2). Eventually Rtest<=(c+1)F, giving
D_Rtest<=L/2+(log2L)/2+C_q for a fixed constant C_q. By the exact leading
identity and positive cross term,

 (1-f^2)Rtest^2 >= nL/2+(1/(2c))n L^(1/2-alpha).

Because 1/2-alpha>0, L^(1/2-alpha)/log2L tends to infinity. Thus this
numerator eventually exceeds n[L/2+(log2L)/2+C_q], proving feasibility.
The actual first-feasible R<=ceil(cF+G_alpha/2), with no monotonicity
assumption in the integer search and no real-arithmetic physical oracle.

For large R, u>=fR/2, mstar=O_q(R/L), hmax=Theta_q(R), H0=O_q(n).
Exactly the reproduced branchwise ledger gives T<=poly_q(n)2^R and
Q<=poly_q(n)2^(R-u), where

 R-u<=(1-f)R+1<=qF+((1-f)/2)G_alpha+O_q(1).

Since G_alpha/log n tends to infinity, the positive gaps to the declared
G_alpha absorb both polynomial prefactors. Depth-first storage still uses
O(n^2) bits and O(n) qubits. Caps and coupling have the same failure
constants; every smaller finite input changes only an outside constant.
The exponential indices remain 1/2 and space indices remain0.

This is a family of complete analytical upper envelopes for the supplied
programs. The argument does not establish alpha=1/2: its capacity surplus
then has only constant order n while the denominator includes n log2 L.
No endpoint, matching lower bound, global optimality or improved time
index is claimed. In particular, this sharper upper bound is not a claim
that the physical runtime changed when only its analysis changed.
