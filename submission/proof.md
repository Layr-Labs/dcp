# GV2: wide-base phase-vector Grover sieve with counted table scans

## 0. Joint theorem and provenance

For every N>=2 and s in Z/NZ put n=ceil(log2 N), L=log2 n. The ONE
algorithm below, including its finite fallback and both cutoffs, recovers
all of s with unconditional probability at least 1-2^-8>2/3 from independent
ideal copies. On EVERY branch its simultaneous uniform envelopes are

 T=O(2^((43/100)sqrt(nL))), S_C=O(2^((2/7)n^(1/3))),
 S_Q=O(n), Q=O(2^((3/10)sqrt(nL))).

These formulas apply for n>=2; a specified finite branch covers n=1.
All outer constants are absolute, independent of N,s and every outcome.
The exact indices are [1/2,1/3,0,1/2]. Fractional tolerance is0, with the
independent ideal-copy promise. No optimality or cube-root-time result is
asserted. The exponential classical memory is real, explicitly charged.

Immediate source: GV1 submission ea4b1150-1536-4894-b829-d4f30362a2b5,
which was hosted-validating when this draft was created. Its exact local
snapshot had passed genuine atomic review, but that verdict is not a premise.
GV2 changes its quarter-base profile to a three-tenths base and tightens all
three exponential coefficients. Exact circuits and both budgets are retained.

Direct material sources, whose verdicts are NOT premises:
* PSG4 b9c350f5-4330-4b53-95b4-a0e85f000033, source archive
  6b3e9f7942a2ca5a95edff3f422e243884dcbf78: wide base, source identities,
  collective label extraction, held-out-block stride decoder and two budgets.
* MWG 76d06063-f670-4712-8f30-d52b4c665084, source archive
  59bdf3c06652a7b54d3e0d8dde2c5af269a1cf7a: separate-register Grover
  listing and measured-fiber moments. Its schedules are not executed here.
* CS1-WINDOW e9fc2eca-9d1c-469b-a629-a43e0f7ce928, source archive
  45d9985c85813b2f3d30c62c717faba3621eb57a: exact cyclic-window selection
  and conditioning only on low-block selection transcripts.
All needed arguments are reproduced. These sources themselves acknowledge
upstream work; this declaration identifies the materials directly used here.

The new configuration combines lambda-bit vectors, an overshoot-tolerant
listing rule, a linear base and explicit table-scan costs. In particular,
there is no coherent random-access memory. The fiber-success bound is
averaged over fresh low blocks BEFORE generating children, never claimed
pointwise after conditioning on their entire full-label tables. Every
failed attempt regenerates complete fresh children. Positive subset sums
are retained throughout, so unused-block laws follow from distinct binary
incidences without an unjustified independence assumption on table entries.

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

## 4. Exact profile, phase vectors and the merge instrument

Put lambda=max(1,floor(floor(cuberoot(n))/8)), kappa=4, with all roots
computed by integer comparison/binary search. For integer v>=1 define

 bcap(v)=2max(0,v-8lambda-64),
 rmax(v)=ceil((2v+lambda+kappa)/lambda),
 delta(v)=ceil(log2(2rmax(v))).

For R=1,...,n put u=max(1,floor(3R/10)). Starting at v=R, retain v and replace
v by v-delta(v) until v<u. Reverse the retained list, obtaining
u<=v_1<...<v_mstar=R. Its capacity is sum_i bcap(v_i). Choose the FIRST R
whose capacity is at least n. If none exists, run the exhaustive branch
of Section8. This search uses only polynomially many O(n)-bit operations;
no exponential array is constructed in choosing the profile.

For each PS_TREE(D,B), where 0<=B<D<=n, greedily allocate b_i from root
level down, assigning min(remaining B,bcap(v_i)); sum b_i=B. There is at
most one positive partial level. Zero-width nonroot levels simply return
the child. If B=0 return one supplier phase qubit with its full label.
All other nonroot outputs have 2^lambda entries; the root has two entries.
Positive root width is necessary and holds because the allocation begins
at the root and capacity is positive. For a positive-width node put t=lambda
(nonroot) or t=1 (root), and r=ceil((b_i+t+kappa)/lambda). It calls r fresh
children. The base children are lambda supplier qubits tensored together,
indexed by a lambda-bit subset. Their full table contains all 2^lambda
POSITIVE subset sums, including the zero sum. Store these sums explicitly.
The state with table a is

 2^(-lambda/2) sum_x exp(2pi i a[x] th)|x>.

All indices have their own original supplier leaves. Every table entry is
a distinct binary incidence vector on those leaves. These incidence vectors
are analytic proof objects and are not stored. Different entries can have
equal NUMERICAL labels, which is allowed. Every table at a level cancelled
to p bits has entries congruent modulo2^p, not necessarily all zero.
All full positive labels are retained; no unknown-phase offset is removed.

MERGE(b,t) on r child vectors, collimated to p bits, is as follows.
Let a(x) be the sum of the r selected child entries, let k=r lambda,
M0=2^k, mu=2^(k-b), C=4mu, T0=2^t and J=2^ceil((b+1)/2).
Because of the arity rule,

 2^(t+kappa)<=mu<2^(t+kappa+lambda),
 C<2^(2lambda+kappa+2), k<b+2lambda+kappa.

Compute bits p,...,p+b-1 of a(x) into a b-bit target and uncompute all
other arithmetic; measure that target to get e. The untouched index then
has uniform-amplitude phases on the fiber E={x: these bits equal e}.
Call its size F. The measurement law is F/M0. It is independent of th.
The full label tables are classical and known to the controller.

Using SEPARATE query registers, do exactly

 Ntrial=64 C (kappa+ceil(log2(C+1))+1)

independent discovery trials. In each trial a fair classical bit chooses:
(1) prepare H^k|0>, measure x directly; or (2) draw j uniformly in [0,J)
using log2 J fair bits, prepare H^k|0>, do j Grover iterations marking
membership in E and measure x. Check the result classically against e.
Store all verified results, sort lexicographically after the fixed trials,
deduplicate, and retain the first C distinct tuples. Call this list Lst
and its length F0. No search predicate depends on previously found tuples.
The original phase-bearing index is untouched by these trials.

If F0<T0 discard all inputs and FAIL. Otherwise project the original index
onto Lst: compute its membership by a scan into a flag, measure the flag,
and FAIL if outside. Conditional on success its amplitudes on Lst are
exactly F0^(-1/2) exp(2pi i a(x) th). Map x bijectively to its known rank
q in [0,F0), clearing x by the known inverse list. Prepare a uniform t-bit
index j0. Compute z=(q-j0) mod F0 into a sufficiently wide clean register,
measure z, and clear q by q=(z+j0) mod F0. Keep j0, and output its table
of T0 labels a(Lst[(z+j0) mod F0]). This is an EXACT cyclic window even
when F0 is not a power of two: for each z the same T0 terms occur, and
Pr(z)=1/F0. The finite valid-domain permutations have reversible extensions
to all padded encodings. No amplitude synthesis is needed beyond H gates.
The output has exactly uniform magnitudes and the advertised phases.

On FAIL discard/reset the entire current input collection and regenerate
all fresh children. No free postselection is used. Every accepted branch,
even with an incomplete discovered list, is an exact phase vector. At the
root its two positive labels a0,a1 give, up to a global phase, the qubit
(|0>+exp(2pi i(a1-a0)th)|1>)/sqrt2. Return its signed difference x=a1-a0.

### 4.1 Counted circuits and fixed widths

To evaluate a child entry, scan its entire classical table. For each row,
compare its known row address to the quantum lambda-bit index, controlled
XOR its W0-bit label into a clean accumulator, and clear the equality flag.
Then add all r selected labels; uncompute temporary values and comparisons.
Extract only the desired b-bit slice to the output and reverse the sum.
All r scans, arithmetic, addresses and gate generation cost
O(poly(n)2^lambda) sequential work per SUM, with O(n) scratch. We may
conservatively use O(n^4 2^lambda) in the full ledger. Labels need not be
reduced modulo2^D; carries are correctly computed on positive integers.
The mark is compute slice, compare to e, phase flip, reverse. Reflection
about H^k|0> is H^k, a reversible all-zero test, phase flip, reversal, H^k.
Both use exact Clifford+T gates with O(n) scratch. J and Ntrial are fixed.

A list scan realizes membership and rank by comparisons, controlled writes
and their inverses. Its inverse scans the list by rank and XORs the tuple.
Each costs O(poly(n)C). Cyclic rank arithmetic is exact reversible modular
addition; lookup scans Lst, costs O(poly(n)C T0) if performed separately
for each output table entry, and all these terms fit O(poly(n)2^(3lambda)).
Classical mergesort of Ntrial O(n)-bit records is charged, including address
bits. Ntrial=O(poly(n)2^(2lambda)) and log Ntrial=O(n). It uses
O(poly(n)2^(2lambda)) bits and polynomial overhead per retained record.
It is also permissible to do repeated scans instead of sorting; we fix
mergesort so no squared-list factor is hidden. Record widths are fixed.

Use W0=D+ceil(log2(q0+1))+2ceil(log2(n+1))+32 for all full labels,
where q0 is defined in Section5. Every nominal tree uses at most q0
supplier leaves, each label below2^D. This width covers every positive
sum, every signed root difference and intermediate arithmetic. Even wrong
EXTRACT outputs remain in their fixed D-bit range (or are rejected by the
supplier), so every actual branch respects the width. All loop indices,
records and physical wire addresses have O(n) bits. No source inverse,
controlled source, QRAM or uncharged arithmetic oracle is available.

### 4.2 Fresh-block fiber bound and discovery success

Condition on the transcript consisting of ORIGINAL source labels only
modulo2^p, all choices selecting child incidence tables, and independent
external history from BEFORE the fresh children were generated. Do not
condition on their higher full numerical tables. Each child's selection
kernels used only these low p bits: this is immediate at the base and
preserved by the merge instrument, whose query and physical measurement
kernels depend only on the new low slice. Thus the remaining b-bit blocks
of the original supplier labels are independent uniform in Z/2^b.

The tuple incidence vectors z_x are distinct binary vectors, because
children use disjoint leaf sets and each child has distinct binary rows.
Fix a reference tuple x. For y!=x the linear difference z_y-z_x has an odd
coefficient, so a(y)-a(x) is uniform modulo2^b after fixing low parts.
For distinct y,w!=x, these two differences reduced modulo2 are nonzero
and distinct: XOR by the fixed z_x is injective. They are linearly
independent over F2, so some 2-by-2 minor is odd. Solving for those two
fresh leaf blocks shows the differences jointly uniform modulo2^b, even
with their fixed low-part carry offsets. Consequently the collision
indicators are pairwise independent, each with probability2^-b.

For a uniformly chosen reference tuple the size of its fiber is
F=1+sum_(y!=x) I_y. Choosing the measured fiber with probability F/M0
has exactly this size-biased distribution. Therefore

 E F=1+(M0-1)2^-b=mu+1-2^-b, Var F<=mu.

If F is outside [mu/2,2mu], it is at least mu/2 away from its mean
(mu>=32). Chebyshev gives bad-fiber probability at most4/mu<=1/8.
This argument averages over fresh b-bit blocks and the measured residue.
It makes no false assertion of a pointwise fixed-table success probability.

On a good fiber write f=F/M0 and theta=arcsin(sqrt(f)). If f<=1/2,
J sin(2theta)>=1, since f>=2^(-b-1) and
sin(2theta)=2sqrt(f(1-f))>=sqrt(2f). The average success of random-length
Grover is

 (1/J)sum_(j=0)^(J-1)sin^2((2j+1)theta)
 =1/2-sin(4Jtheta)/(4J sin(2theta))>=1/4.

Endpoints f=1 use the direct branch. If f>=1/2, the direct branch alone
has mixed success at least1/4. Thus in all cases the mixed trial succeeds
with probability at least1/8. Permutation symmetry within marked tuples
makes its output uniform on E conditional on success. Every particular
marked tuple has discovery probability at least1/(8F)>=1/(8C), because
good F<=2mu<C. The trials are independent for fixed tables and e.
The probability that some marked tuple is missed is at most

 F exp(-Ntrial/(8C)) <= C exp(-8(kappa+ceil(log2(C+1))+1)) <2^-kappa.

On a complete good list F0=F>=mu/2>=T0. The projection succeeds with
probability1 and the window always succeeds. Averaged over all fresh
children, failure is at most 4/mu+2^-kappa<=3/16. In particular success
is at least1/2. This uniform-before-generation bound is what is used
for geometric retry sums. It is not conditioned on an attempt's cost,
nor on already generated full tables. All three kinds of failures are
included, and incomplete-list acceptance never affects exactness.

## 5. Unused blocks, termination and signed root law

Inductively every nonroot vector consists of distinct binary incidences on
disjoint original supplier leaves, selected by a kernel involving only
bits below its cancelled depth p. The physical merge outcomes have this
property even though the phase vector depends on th: measurements are of
diagonal functions of its index, discovery uses separate registers, list
projection is diagonal, and the cyclic-window measurement has probability
1/F0. No interference depending on th is used for selection. Full labels
can be stored without being conditioned on. The ideal process ignores
EXTRACT's internal records; it will be coupled to the actual process later.

At a positive level the proof in4.2 applies before fresh child generation.
It yields success>=1/2, uniformly over independent external past, and the
same property holds in each fresh retry. Hence each call terminates almost
surely by induction on its finite level. Distinct fresh calls use disjoint
supplier leaves. Any finite successful selection transcript has a kernel
only of low-p parts. Conditional on it, original higher blocks remain
independent uniform. This proves the induction needed in4.2 jointly with
termination. We never assert that all entries in a vector are independent.

Write r_i for the arities actually used at positive levels. Since
2r_i<=2rmax(v_i)<=2^delta(v_i), the exact adjacent profile gaps give

 product_(j>i)(2r_j)<=2^(R-v_i).

The base vector has lambda supplier leaves. For i=1,
lambda r_1<=2v_1+2lambda+kappa. The function
(2v+2lambda+kappa)2^-v decreases for integer v>=1. Define

 q0=(2R+2lambda+kappa)2^(R-u).

The number of distinct leaves in any NOMINAL returned root (ignoring retries)
is lambda product_i r_i<=q0. With zero-width levels skipped this only
decreases. For B=0 there is one supplier, also covered. A root difference
x is divisible by2^B, and |x/2^B|<2^(D-B)q0. The W0 width of4.1 follows.

For the root put h=D-B>=1. Condition on all original leaf labels modulo2^B,
selected incidences, query choices/outcomes, residues, list projection,
window outcomes and retry history, and independent PREVIOUS root history.
Do not condition on the remaining high blocks or later budget survival.
The selected two root entries are distinct binary incidence vectors, so
their difference z has entries in{-1,0,1} and at least one unit entry.
Writing original labels k_l=u_l+2^B tau_l gives

 W=x/2^B=c+sum_l z_l tau_l,

where tau_l are independent uniform in [0,A), A=2^h, and c is fixed by
this low transcript. Therefore, for every real y,

 |E exp(2pi i yW)|<=D_A(y)=|(1/A)sum_(t=0)^(A-1)exp(2pi i yt)|,
 D_A(y)<=|cos(pi y)|,
 D_A(y)<=min(1,1/(2A||y||)) for ||y||>0,
 Pr(W odd)=1/2.                                                   (5.2-3)

Each unit block contributes the factor D_A and all other factors have
modulus at most1. Factoring a uniform block into independent fair binary
digits gives D_A=product_(j=0)^(h-1)|cos(pi2^j y)|. The geometric sum and
|sin(pi y)|>=2||y|| give the second bound. The lowest fair bit gives
parity fairness. The law concerns the full signed integer W; it does not
claim its entire integer distribution is uniform. This provides exactly
the frequency facts used in Sections6-7 for ALL moduli, not just powers
of two. Rejected supplier copies and previous failed attempts use disjoint
independent leaves. Their unused high blocks are marginalized.

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
u=floor(3R/10). If h=hmax, stride=Theta(R), so Sodd=O(1+log M/R).
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


## 8. Complete algorithm, both cutoffs and unconditional success

For n<256, or if the finite profile search found no feasible R, use
exhaustive shift testing: for t=0,...,N-1 acquire at most n+10 fresh copies,
subtract t controlled by the first qubit, and measure that qubit in X.
Reject t at the first minus, output the first t passing all tests or0 if
none. The true s always passes. Every wrong t has plus probability1/2
per fresh copy, since the nonzero translation has trace0. Wrong output
probability is less than(N-1)2^(-n-10)<2^-10. It uses at most N(n+10)
copies, O(n) qubits, O(n^2) classical bits, O(Nn^4) charged work. Section9
proves this branch is taken for only a FIXED FINITE set of n, independent
of N,s and outcomes, so its full costs fit all claimed asymptotic bounds.

Otherwise compute all decoder parameters, including q0 and K, before
execution. For M=1 use Sodd=K=0. Define

 H0=Sodd K+2n,
 Qstar=4q0 H0+2n, Qcap=1024Qstar,
 Wstar=2mstar 2^R H0, Wcap=1024Wstar.

Before any acquisition exceeding Qcap abort, release registers and output0.
Before a merge attempt, AFTER its fresh children have been built, test
whether adding2^v_i to the weighted counter exceeds Wcap. Abort likewise
if so; otherwise charge2^v_i and execute the complete attempt. Every
acquisition, including rejected/failed/discarded copies, is charged.
EXTRACT uses this exact fixed Qcap. Execute the odd-part decoder then the
2-adic decoder and output(s1+M s2) mod N. The root computation is PS_TREE
of Section4 with the appropriate D,B and supplier of Sections6-7.

In the ideal uncapped process each supplier qubit costs at most two copies
in expectation. A base vector therefore costs at most2lambda. For every
positive merge, before complete fresh child generation, success>=1/2
uniformly over prior external history. Summing a geometric tail of
attempts gives E_i<=2r_i E_(i-1). No independence between cost and
success within the same attempt is assumed: reaching a given attempt
depends on previous attempts, and then its fresh child cost is bounded
conditionally. Thus E_root<=2lambda product_i(2r_i)<=4q0. For B=0 its
supplier costs at most2. All odd decoder roots and the expected two roots
per 2-adic bit give total expected copies<=Qstar.

At level i the expected number of attempts, including all failed ancestor
attempts, is at most2 product_(j>i)(2r_j)<=2*2^(R-v_i). Its expected
weighted contribution is at most2*2^R. Over at most mstar levels and the
H0 expected root count this yields total expected weight<=Wstar. The same
conditional geometric argument handles odd-W repeats. Zero-width shortcuts
have zero merge weight; their classical bookkeeping is charged separately.

Apply Markov separately to the ideal uncapped source and weighted totals.
Each cap changes the process with probability at most2^-10. An abort
before a next merge means the uncapped total WOULD exceed Wcap; its
already-built children are already charged. No cap/decoder independence
is asserted. The ideal odd decoder error is at most2^-20; conditional on
correct s1, ideal2-adic recovery is exact. EXTRACT errors have total
probability<=2^-14 by Section3. Couple until first error or cutoff,
without conditioning the ideal unused-block law on numerical extraction
success. Total failure<=2^-10+2^-10+2^-14+2^-20<2^-8. This includes every
failure and abort. The finite branch also meets this success guarantee.

The new configuration trades a slightly larger feasible height for a
smaller source exponent, while the tighter raw memory ledger supports
coefficient2/7. Its declared time coefficient43/100<7/16, source
coefficient3/10<1/3 and classical coefficient2/7<1/3 all strictly improve
the immediate source's full envelopes with the same O(n) quantum bound.
This is a simultaneous tradeoff sharpening, not an index breakthrough.

## 9. Profile estimates and EVERY-BRANCH resource bounds

### 9.1 The exact first-feasible rule

Let lambda_n~n^(1/3)/8. For R~c sqrt(nL), fixed c>0, all retained v are
in [3R/10+O(1),R] and rmax(v)=Theta(R/lambda_n). Uniformly there,

 delta(v)=log2(R/lambda_n)+O(1)=(1/6+o(1))L.

The spacing is log2(R/lambda_n)+O(1). Comparing each descending step
with its integral rectangle, whose error is O(R delta_max) in total,
gives sum_i 2v_i=(R^2-u^2)/log2(R/lambda_n)*(1+o(1)). Explicitly, bounds
between the min and max spacings, which differ by O(1), sandwich the
sum; missing endpoint intervals have length O(delta_max), negligible
relative to R. Subtracting 2(8lambda+64) per retained point is a relative
O(lambda/R)=o(1). Clamping is absent on these trial profiles eventually.
Hence their capacity is

 sum_i bcap(v_i)~(273/50)c^2 n.

For c=857/2000 the ratio is200504577/200000000>1. Thus a feasible profile exists eventually
with R<=ceil((857/2000)sqrt(nL))<=n. Exhaustive fallback occurs only for finitely
many n. Since choosing the FIRST feasible profile does not require capacity
monotonicity, the displayed upper bound holds for the actual selected R.

Conversely capacity<=2 sum_i v_i<=2R^2, so actual feasible R>=sqrt(n/2).
This already implies lambda/R=o(1), and log2(R/lambda)>= (1/6+o(1))L.
For actual R between sqrt(n/2) and the trial upper bound, all retained
v=Theta(R), and delta(v)=Theta(L). Therefore mstar=O(R/L). These bounds
are for the SAME exact first-feasible configuration as all other estimates.
They also imply log q0=O(R), K=O(R), H0=O(n), W0=O(n).

### 9.2 Source and weighted budgets

The literal source cap is O(n(R+lambda)2^(R-u))=O(nR2^(R-u)).
Since u=floor(3R/10) eventually,

 log2 Qcap <=(7/10)R+O(log n)
 <=(5999/20000)sqrt(nL)+O(log n).

The strict inequality5999/20000<3/10 absorbs the polynomial into
Q=O(2^((3/10)sqrt(nL))). All acquisitions are counted by the literal cap,
including erroneous labels and partially built trees at a work abort.
Weighted cap is O(n mstar 2^R), and therefore polynomial times2^R.

### 9.3 Classical bits and quantum wires

Per active merge, at most r child tables of2^lambda W0-bit labels are
retained, and Ntrial records of O(n) bits plus sort scratch. The recursion
has at most n levels and r<=O(n). Empirical EXTRACT counters, decoder roots,
full labels, source registers, budgets and gate-generation counters fit

 S_C=O(n^4 2^(2lambda)).

The peak includes rejected lists before release, sorting scratch and all
suspended ancestor tables. Larger fixed polynomial bounds would give the
same pure envelope; the displayed one covers log Ntrial=O(n), records of
O(n) bits, r<=O(n), at most O(n) frames, and the O(n^2) decoder records.
Since 2lambda<=n^(1/3)/4+2, the strict gap2/7>1/4 absorbs n^4. Thus
S_C=O(2^((2/7)n^(1/3))). Address charge is log(S_C+S_Q+2)=O(n), and is
included in the work bounds below; it is never log of merely the index set.

For quantum space use a POINTWISE path bound, not average tree size.
At a positive nonroot level, retained siblings consume at most
r lambda < b_i+2lambda+kappa; during child generation their total can
be bounded by (r-1)lambda < b_i+lambda+kappa. Along a stack add these
last quantities, plus the current node's O(n) registers and leaf lambda.
Greedy allocation has at most one partial positive level. For full levels
bcap>=lambda, charge lambda+kappa<=(kappa+1)b_i. Full levels with
0<bcap<lambda lie in an interval of integer v of length<lambda and so
there are at most lambda+1 of them. Include the partial level to get

 sum retained indices + leaf
 <=(kappa+2)B+(lambda+2)(lambda+kappa)+lambda=O(n).

Here lambda^2<=n and kappa=4. Adding O(n) reversible arithmetic, the
current tuple, source data, extraction ancillas, Grover workspace, rank
and window registers preserves S_Q=O(n). Repeated attempts release all
old inputs. At B=0 a single supplier uses O(n) wires. No classical label
arrays are silently counted as quantum memory.

### 9.4 Charged sequential work, all outcomes

A merge uses at most Ntrial*J=O(poly(n)2^(2lambda+b/2)) query iterations;
each uses O(n^4 2^lambda) work, inclusive of scans, wire addresses and
streaming gate generation. Classical trial generation, verification,
sorting, projection, rank, clearing and the output table use at most
O(poly(n)2^(3lambda)) additional work. Choose conservatively
O(n^6 2^(b/2+3lambda+16)) per complete attempt. For a positive level,
b/2<=v-8lambda-64, so this is O(n^6 2^v), with absolute constants.
The weighted cap bounds the sum of2^v on EVERY branch by Wcap. Merge
work is thus O(n^6 Wcap)=O(poly(n)2^R). Counter checks, failures and
aborts cost polynomial per started node or source acquisition, including
checks before partly built ancestor attempts. Positive attempted nodes
are weighted; zero-width levels are short-circuited when building the
parameter list. The profile preprocessing is polynomial.

Leaf vectors, which are not charged as merge attempts, cost
O(poly(n)2^lambda) to materialize their tables. Each leaf vector starts
with supplier acquisitions, and the number started is at most Qcap+1.
Each call to EXTRACT costs polynomial in n with h=O(R+log n); the
source transforms, table initialization, partial leaves and resets also
cost polynomial times Qcap*2^lambda. Its exponent is at most
R-u+lambda+O(log n), strictly below R eventually, since u=Theta(R) and
lambda=o(R). Decoder enumeration costs poly(n)2^(R-u+h), with
h<=1+u/8. This too is exponentially below2^R. The at most H0 records
have polynomial width. These terms include the actual physical-address
charge and the finite trigonometric table construction of Section3.
An intentionally conservative combined envelope is O(n^12 2^R).

Substituting the actual height bound gives

 log2 T <= (857/2000)sqrt(nL)+O(log n).

The strict gap43/100>857/2000 absorbs n^12 and all other fixed polynomials.
Hence T=O(2^((43/100)sqrt(nL))) on every branch, including incorrect-label
branches and either abort. No worst-case resource statement relies on
expected retries. Expectations were used ONLY to prove that the literal
caps preserve success probability.

### 9.5 Exact indices and finite constants

For pure envelope2^(a n^p L^q), a>0,p>0, log2 log2 of its value divided
by log2 n tends to p. Thus the stated pure time, classical space and
sample envelopes have indices1/2,1/3,1/2. A polynomial O(n) envelope
has index0. These are the exact indices of the declared representatives,
not claims that unknown optimal complexities equal those functions.
All finite exceptional n are handled by the specified exhaustive branch
or the specified finite profile; there are finitely many such integers,
so their finite maxima are absorbed by absolute outer constants. No
nonuniform advice, unspecified n-dependent schedule or hidden oracle is
used to implement the branch or choose those constants.

## 10. Malformed copies

The guaranteed malformed-sample fraction is epsilon(n)=0. Every acquired
copy is assumed to be an independent ideal coset state. No positive
corruption, adversarial noise or heralded erasure tolerance is claimed.
Under that promise the same algorithm has the full-secret probability
and all four joint every-branch bounds proved above. This does not assert
that greater tolerance is impossible.
