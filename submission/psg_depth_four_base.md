# Complete source and semantic proof for PSG-D4

This required appendix is used jointly with psg_depth_four.md,
psg_depth_four_compiler.md and psg_depth_four_family.md. All five claims
cite all four proofs. The ONE actual program fixes depth d=4 and uses
n_4=2^256. This appendix reproduces the complete original source identities,
collective extraction, exact disjoint-pair primitive, unused-block and
characteristic proofs, both decoders, virtual-record/finite analysis and
literal helpers. Only the selected four-level profile, guards, record
counts and their proved interfaces replace the earlier parameter rules.

The immediate local semantic source is psg_depth_two_base.md,
SHA-256 f58e64e83594a4258b40632973ca8e3fb9e042e3290b5441415894d1a961c268,
which reproduces the S371 semantic source at
bba18b26ef7260f1ec1a1c834baa9f545659bf1e887d8c81df8b5fb263562599.
The original PSG14C proof hash is
2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6.
Exact local-first/public-later source identities and inherited credits
are in the main and family appendices. No verdict is a premise.
The complete selected parameter rule is

    d=4, n_4=2^256, C_4=7, q0=(2R+1)^4,
    Qroot=7168q0, Wroot=8192*2^R,
    K=2^17n, Proot=7168n^4, Hmax=8192K=2^30n,
    Qtot=7*2^40n^5=7696581394432n^5 exactly,
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4).

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

Write N=2^a2 M with M odd, D0=floor(log2 N), omega=exp(2 pi i/N),
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


EXTRACT uses precision budget P_label: Qroot inside a main-branch root,
and P_label_old=2^40n^4 in each finite-branch record, as fixed in Section 8. Put J_e=n+4,

    h=ceil(log2(2^16 P_label (n+5))), F=2^21 h.

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

with O(n) qubits, O(n^2) classical bits. Since P_label=O(n^4) by Section9, h=O(log n)=O(L),
and L^2=O(n), this is O(n^2 L) for the complete profile.
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
4(n+5)2^-h <= 1/(2^14 P_label). The union bound for at most P_label adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n h L+n^2 L)=O(n^2 L) core operations under the actual
profile budgets, O(n) qubits and O(n^2) classical bits. Store the n+5 six-bit
directions and their empirical counters explicitly. All loops have fixed bounds.

## 4. Exact selected four-level profile

For n>=n_4=2^256, put ell=ceil(log2 n). Scan integer trials starting
at R=ceil(n/8). For each trial compute

    c=ceil(log2(3(2R+1))), v_i=R-(4-i)c, i=1,...,4.

Take the first trial with v_1>=ceil(R/2) and 8R-12c>=n. No capacity
monotonicity is used. The feasible trial
Rtest=ceil(n/8)+ceil(3(ell+2)/2) proves

    n/8<=R<=n/8+(3/2)log2 n+13/2,
    2^R<=2^(13/2)n^(3/2)2^(n/8), R<n/3,
    v_i>=R/2>=u=floor(R/4)>=R/8,
    n<=8R<=64u, 2R+1<=n, q0=(2R+1)^4<=n^4.

All ceilings, positivity and scalar bounds are proved for this entire
range in psg_depth_four_family.md Section 3 with fixed d=4. The search
uses O(log(n+2)) trials and explicit integer arithmetic. For each
1<=D<=n and 0<=B<D, allocate b_i=min(2v_i,remaining) from i=4 down
to 1, then reduce remaining. Capacity makes the final remainder zero.
Set r_i=b_i+1 and p_i=sum_(j<i)b_j. Skip a zero width; B=0 returns
one leaf. Each positive width uses k=b_i+1 children, the exact primitive
below, and its nominal weight 2^v_i. Every returned tree has at most
product_active r_i<=q0 nominal leaves. Its full signed label is 2^B W,
with |W|<2^(D-B)q0 and a nonzero signed incidence on disjoint leaves.
All fields have n+ceil(log2 q0)+4=O(n) bits. High and zero labels are
not filtered. These rules cover every partial and zero-width tree.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, b=b_i, p=p_i. Their joint state is

 2^(-k/2) sum_(y in{0,1}^k) exp(2pi i th A(y))|y>, A(y)=sum_j y_j a_j.

Set c_j=(a_j/2^p) mod2^b. Reversibly compute f(y)=sum_j y_j c_j mod2^b,
measure it to obtain e, and reset that measured register. The remaining
phase state has equal magnitudes on C_e={y:f(y)=e}.
Hold this original register untouched during discovery on SEPARATE query
registers. The discovery procedure below returns at most64 distinct,
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

Fix C=64. If k<=7, enumerate at most128 strings and retain the first64
solutions; this has constant enumeration length. If k>=8, use at most64
search blocks. Each block makes at most64 trials, stopping at its first
new verified solution, which is added to the list. Stop discovery after an
empty block or after64 found solutions. The list never contains a duplicate
or a false solution. On each trial:

 * Set J0=2^ceil(k/2), draw uniform j in[0,J0) with ceil(k/2) fair bits.
 * Prepare a fresh k-qubit query in |+>^k. Apply j Grover iterations for
   membership in C_e minus the found list. Measure its candidate string.
 * Verify its residue and novelty classically. Reset query registers before
   the next trial. The original phase-index register is not touched.

Membership is a COUNTED circuit. Controlled additions of the known b-bit
constants c_j compute f(z) in O(kb) gates; compare with e, exclude at most64
known strings with equality flags, apply Z on the computed flag, then
uncompute. This uses O(kb+64k) gates and O(k+b) scratch up to fixed constants.
Diffusion about |+>^k is H^k, a multi-controlled sign flip and H^k; a clean
Toffoli chain implements the sign flip in O(k) gates and scratch. Z=S^2.
All are exact Clifford+T. Known weights and strings are read by a classical
loop emitting gates; no quantum-addressed lookup, QRAM or stored circuit of
exponential length occurs. Gate generation, verification, fair bits, counters,
measurements, resets and all oracle work are charged.
### 4.2.1 Complete selected online implementation

The required psg_depth_four_compiler.md G.2--G.4 specifies every padded
DATA row, ready operand, indexed known-bit read, carry head, marked strip,
loop test, exact gate, inverse and release. It implements the exact
circuits above, with O(k+b) live arithmetic/index helpers and no kb-node
quantum history. Each paid attempt costs O(R^2 L2^v) on every branch.
The full proof, including every partial row and one-off signed output,
is contained there; Section 9 below and the required family appendix
count every other work term. No gate-generation oracle is assumed.

### 4.3 Discovery probability and the measured-fiber moment

Suppose the measured fiber has at most64 members. At any search trial with
1<=m<=64 remaining solutions, let A=2^k and sin^2(gamma)=m/A. In the
normalized good/bad two-dimensional basis the marking reflection and
uniform-state reflection rotate by2gamma; therefore success after j
iterations is sin^2((2j+1)gamma). Summing the cosine geometric progression
for uniform j gives

 mean success=1/2-sin(4J0*gamma)/(4J0*sin(2gamma)).

For k>=8, m<=64<=A/2, hence sin(2gamma)>=sqrt(2/A) and J0>=sqrt A.
The mean is at least1/2-1/(4sqrt2)>1/4. A64-trial block consequently misses
while solutions remain with probability at most(3/4)^64<2^-16.
Over at most64 relevant blocks, premature stopping has probability at most
64*2^-16=1/1024. Once no solutions remain a block simply finds none;
no counting oracle is used. Small k is enumerated exactly up to the list cap.

Now suppose c_j are independent uniform residues in G=Z/2^b and
k=b+1. Complete adjacent DISJOINT pairing has averaged success at least3/4,
as the following exact parity-support calculation proves. Fix the first
b weights, and let c_e be their subset counts for e in G. Let O be the
set of residues with odd c_e and o=|O|. For the last independent uniform
weight a, the full fiber count at e is c_e+c_(e-a). Thus its odd-count
support is O symmetric-difference(O+a). Averaging a gives

 E_a #odd_full_fibers=2o-2o^2/|G|
                    =2o(|G|-o)/|G|<=|G|/2.

The actual residue measurement assigns a fiber its size divided by2^k.
Complete pairing loses exactly one basis state from every odd fiber, so
its averaged lost mass is at most(|G|/2)/2^k=1/4. This is NOT a
3/4 guarantee for a fixed arbitrary list of all child labels.

The measured fiber has the same size-biased law as C_(f(Y)), with Y an
independent uniform index in{0,1}^k. Conditional on Y write
X=|C_(f(Y))|-1=sum_(z!=Y)I[f(z)=f(Y)]. Each row z-Y has nonempty
support and coefficients0 or a sign fixed by Y at that coordinate.
Two distinct nonzero rows have distinct supports. Choosing one coordinate
in their support difference and a coordinate in the other nonempty support
gives a2x2 minor of determinant+1 or-1. Therefore the two linear forms
of independent uniform weights are jointly uniform modulo2^b. In particular,

 E binom(X,2)=binom(2^k-1,2)/2^(2b)<2.

When the fiber exceeds64, X>=64 and binom(X,2)>=2016. Hence
Pr[|C_(f(Y))|>64]<2/2016=1/1008. This applies also at small k;
it does not assume a Poisson law or independence of all subset sums.

On fibers of size at most64, the preceding fixed-fiber discovery estimate
bounds premature stopping by1/1024 (zero in the small enumeration branch).
If discovery is complete the SAME old adjacent-pair projection is performed.
Consequently, without assuming independence of the failure events,

 fresh node success >=3/4-1/1008-1/1024>37/50.             (4.2)

We use a=50/37 as a conservative expected-attempt factor. This estimate is
averaged BEFORE fresh children are generated, not conditional on arbitrary
fixed child labels. Every accepted pair still has the exact phase even
when discovery was incomplete. Section5 supplies the fresh uniform weights
and almost-sure termination jointly. No cyclic operation is added.

## 5. Unused blocks, termination and the root frequency

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Equation(4.2) gives conditional success at least37/50 before child generation,
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

There are exactly four nominal levels and each active r_i<=2R+1. A
shortcut contributes factor one. Therefore

 q_D=product_(active i) r_i<=(2R+1)^4=q0.

A returned tree has at most q_D nominal distinct leaves. Its label is2^B W
with integer |W|<2^(D-B)q0. All stored labels and sums have
O(n+log q0)=O(n) bits, including incorrect numerical-label branches.
No symbolic incidence vector or exponential subset list is stored.
Lemma U applies to the base with its independent fresh leaves.

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

## 6. Odd-part recovery with isolated records

Factor N=2^a2 M, M odd, by removing trailing zero bits only; no odd
factorization is needed. Set D0=floor(log2N), hmax=1+floor(u/8),
K=2^17n. A ROOT RECORD uses the local source/work caps and padding of
Section8. On a root abort it returns the neutral score0 for every candidate.
Otherwise measure its root in a fresh fair X or Y basis and store the
frequency, basis beta and sign Z. Clamp every numerical trigonometric score
to[-1,1]. All records use fresh reset workspace; there is no root reuse.

If M=1, put s1=0, Sodd=0 and skip ONLY this odd-part section.
The shared K=2^17n remains positive and unchanged for Section7 and padding. Otherwise M >= 3, so N >= 3 * 2^a2
and D0 - 1 >= a2. Put theta=s1/M in[0,1). Define

 hmax=1+floor(u/8), h=min(D0-a2,hmax), B=D0-h>=a2,
 stride=max(1,h-4), D=D0, nq=2^(h-1)q0,

The stages are j=0,...,J, where J is least nonnegative with
2^((J+1)*stride+2)>2M. Put Sodd=J+1. Because stride>=1, Sodd<=n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^(j*stride) (2^(B-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^D0 (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^D0), each copy is
accepted with probability 2^D0/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^B W th = W 2^(B-a2) alpha_j s / M = 2^(j*stride) W s1 / M   (mod 1),            (9.1)

because 2^(B-a2) alpha_j = 2^(j*stride) (mod M) and s = s1 (mod M). So a PS_TREE(D0,B) root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^(j*stride) W.

Measurement. Obtain K isolated ROOT RECORDS for PS_TREE(D0,B), each
using this stage's leaf supplier. The record routine performs the ONE fair
basis choice and root measurement, followed by padding/reset. On success
it stores f_i=2^(j*stride)W_i, beta_i and Z_i; on abort it is neutral.
No second measurement is applied after receiving a record.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^(j*stride) W_i.

Candidates. Put P_j = j*stride + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j*stride+2) of the previous center z_(j-1). This is one or two explicit
  integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of 2^-(P_j),
  so the two arc endpoints are themselves candidates.
- Stage 0 has exactly 2^(ceil(log2 nq)+8) candidates. At j>=1 there
  are at most 2^(ceil(log2 nq)+7)+2<=2^(ceil(log2 nq)+8). The smaller
  arc count applies only to j>=1; the final common bound covers both.

The candidate set is fixed by information available at the start of the stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * clamp(tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ),-1,1),
with contribution0 from an aborted record.

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have
fixed lengths, and the decoder returns a candidate on every branch.

Ideal gap calculation. Suppose theta is in the stated input arc.
Analyze one EXACT, UNCAPPED clean root, before isolation/corruption.
The following proves a uniform ideal near/far gap; Section11 transfers
it to actual capped, possibly contaminated records and proves concentration.

Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 5 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the held-out blocks of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

For these exact UNCAPPED records only, the clamped-table score differs
from sum_i xi_i by at most K/625. Capped/contaminated effects are deferred
to Section11; no such bound is asserted for arbitrary actual records here.

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

The ideal near/far mean gap is at least
(1/2)(cos(pi/128)-cos(pi/8))>0.0379. Actual clamped-table and
isolated-record effects are treated quantitatively in Section11.

For stage j+1 the hypothesis of the near/far geometry is the conclusion of stage j, since
2^-(j*stride+stride+2) = rad_(j+1). On the simultaneous good stage events proved in Section11, theta
lies within 2^-((J+1)*stride+2) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


Stage-count bound. The selected main profile has R>=256 and n<=8R.
If h=hmax, stride>=R/64 gives Sodd<=64n/R+1<=513. If h<hmax,
log2 M<h+1 and the stride rule gives Sodd<=8. These bounds do not
assume that earlier estimates are correct. M=1 has no odd stages.

## 7. Multi-bit2-adic recovery

After the odd estimate s1, maintain g=0 and t0=0, representing the known
low g bits of s2=(s-s1)/M modulo2^a2 when previous estimates are correct.
While g<a2, put wd=a2-g, h=min(wd,hmax), sh=(s1+M*t0) modN.
For this block generate K ROOT RECORDS for PS_TREE(wd,wd-h), with leaves:
acquire a fresh source, apply Shift_sh, run EXTRACT, apply X for the
positive phase convention and use kk=k mod2^wd as its classical label.
All source calls and attempts obey their local root caps. A success record
contains W=label/2^(wd-h), a fair basis beta, and its measured sign Z;
an abort is a neutral record. Each record is padded/reset as in Section8.

Enumerate r=0,...,2^h-1. For a success record use score
 Z*clamp(tab_beta(((W*r) mod2^h)/2^h),-1,1), and0 for an abort.
Keep the least maximizing r. Set t0<-t0+2^g r and g<-g+h, then continue.
After all blocks output (s1+M*t0) modN. No individual parity test or
odd-W postselection is performed. All loops run even if earlier estimates
were wrong; their length and allocation remain bounded.

To prove the ideal score gap assume the earlier estimates are correct.
Then s-sh=M2^g rem moduloN for an integer rem modulo2^wd. A uniform
source label k gives phase exp(2pi i k rem/2^wd), which depends only on
kk=k mod2^wd. Since2^wd divides N, kk is uniform on[0,2^wd).
The exact uncapped root has label2^(wd-h)W and phase
exp(2pi i W rem/2^h). Lemma U makes W modulo2^h UNIFORM, conditional
on all past before this fresh call. Thus the fair-basis exact score for r
has expectation

 (1/2)E cos(2pi W(rem-r)/2^h)
   =1/2 if r=rem mod2^h, and0 otherwise,

by the finite character sum. The true grid point therefore has a1/2 mean
gap over every wrong point. Section11 proves that the actual isolated,
possibly contaminated records retain a unique maximizing true r with high
probability. Inducting over the blocks recovers all bits of s2.
This proof never reduces a phase by a noninteger multiplier: the identity
using kk requires the correct earlier prefix, exactly as assumed here.
Other branches only need the unconditional resource analysis.

The number of blocks is ceil(a2/hmax)<=32n/R+1<=257,
because hmax>R/32 and n<=8R. Each grid has 2^h<=2^(1+R/32)
points. Together with the at most 513 odd stages, there are at most
770 actual stages. In the case a2=0 this section
has no blocks. If wd-h=0, the tree is just a leaf and the same uniform
quotient and cap bounds apply.

## 8. Complete actual record and finite interfaces

Compute Qtot and the separate P_label_old before branching. Select exactly

    d=4, n_4=2^256, C_4=7, q0=(2R+1)^4,
    Qroot=7168q0, Wroot=8192*2^R,
    K=2^17n, Proot=7168n^4, Hmax=8192K=2^30n,
    Qtot=7*2^40n^5=7696581394432n^5 exactly,
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4).

For n<2^256 make mF=2^20(n+16) original-source one-copy shadow records,
using EXTRACT(P_label_old), positive phase, one fresh fair X/Y basis and
one sign. Reset all work between records. Scan all t in [0,N) using
exact kt mod N and clamped table scores. Save the least maximizer,
acquire/discard to exactly Qtot, and only then return it. Since
mF<=2^25n<=Qtot, padding is nonnegative also for n=1,N=2.

For n>=2^256 execute the exact profile and the two decoders above.
Every stage takes K records. A root starts with reset scratch and fresh
local source/weighted counters. Check before each source acquisition.
After its children are built, check and charge a positive attempt's 2^v_i
before parent query/array setup. A failed check aborts only that root;
prior children and work remain counted. Neutral roots contribute score 0.
A successful root is measured only once, in one fresh fair basis. Store
only its bounded classical record. Then pad to Proot using a distinct
record-padding counter, not the Qroot guard, and reset all nonrecord work.
All later stages run also after wrong earlier estimates. Keep K positive
when M=1. Only s1 and Sodd are then zero. If a2=0 there are no 2-adic
blocks. B=0 returns a leaf with the same record and cap interfaces.

There are at most 770K active records, less than Hmax=8192K. After saving
(s1+M*t0) mod N, consume enough Proot-copy dummy records to fill Hmax.
Return the saved classical residue afterward. Thus every branch has
exactly Hmax*Proot=7*2^40n^5 acquisitions. The same count is used in the
finite branch, and floor(epsilon(n)Qtot)=128n for every n>=1.
Rejected leaves, neutral roots, record padding and dummies are included.

The unused-block induction and the 37/50 fresh success in Sections 4--5
at four levels give expected root acquisitions <=2(50/37)^4q0<7q0 and
expected weight <=8*2^R. The complete geometric/weight proof is included
in psg_depth_four_family.md Section 6. The two local guards above each
lose at most 1/1024 on an ideal uncapped clean root. EXTRACT(Qroot)
adds at most 2^-14 label error. The clean capped/uncapped coupling loss
is p0=33/16384. The mean allowance is 2p0+1/625. It is unconditional
before a fresh record, including neutral aborts; it is not conditioned
on extraction, root survival or the actual record remaining clean.

## 9. Joint charged implementation

The actual complete controller is psg_depth_four_compiler.md G.2--G.4.
Each paid attempt costs O(R^2 log2(n+2)2^v_i), including all failed and
partial work. Hard weighted guards bound a root's sum by 8192*2^R.
Across O(n) records the combiner time is O(nR^2 log2(n+2)2^R), hence
O(n^(9/2)log2(n+2)2^(n/8)). All remaining costs, hard guards and
simultaneous O(n^2) classical/O(n) quantum storage are proved in full
in the compiler and in family Sections 9--10. Source/extraction/padding
costs total at most O(n^7 log2(n+2)^2), grids have polynomial(n)2^(R/32)
work, and recursion metadata has polynomial(n)2^(R-u) work. Their positive
exponential gaps absorb these charged terms. The explicit n<2^256 scan
has a finite worst-case loop count and changes only an absolute constant.
There is no expected-resource substitution for any hard bound.

## 10. Exact adaptive model

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

## 11. Virtual records, contamination and full-secret success

### Reset coupling and deterministic contamination bound

At the start of each actual root record the quantum workspace is reset,
with only N, stage parameters and classical history retained. Extend the
outcome probability space by a virtual fully clean capped root record,
with fresh ideal inputs and fresh coins. Until the first malformed delivery
couple it to the actual computation: their active workspace states agree,
and a clean delivered copy is rho_s in tensor product with everything else.
After the first malformed delivery, finish the virtual record with independent
ideal inputs and analysis randomness. A neutral abort and the measurement
are included in the virtual law. Padding has no effect on a candidate record.
No physical cloning, algorithmic extra sources or purification access is used;
these are couplings of distributions of classical measurement transcripts.

Conditional on all earlier real and virtual history, the next virtual run
is the same fresh clean capped root for fixed stage parameters. Its mean
score bound of Section 8 therefore holds uniformly, regardless of the
adversary's conditional private state. The adversary may decide adaptively
when to corrupt from earlier outcomes within the current record. Before
that event all copies are fresh ideal products; afterward virtual inputs
are independent. This does not change the unconditional virtual law.
We NEVER condition that mean bound on the actual record remaining clean.
The same construction applies to each finite-branch one-copy shadow record.

Each malformed copy contaminates at most one record, conservatively including
padding and dummy records. There are at most Bbad=128n such copies globally.
For any main stage K=2^17n, so at most Bbad records are contaminated, even
if the adversary concentrates all its budget on this one stage. Every score
is in[-1,1]; actual and virtual scores match on uncontaminated records.
Thus, SIMULTANEOUSLY for all stage candidates, their average-score difference
is at most2Bbad/K=1/512. This bound does not depend on the corrupted
frequencies or phases and requires no independence of contamination events.

### A bounded-score concentration estimate

For a fixed stage candidate, virtual scores X_i have conditional means m_i
and range[-1,1]. Hence the centered martingale increments X_i-m_i lie in
history-dependent intervals of length2. Conditional Hoeffding's lemma gives
E exp(lambda(X_i-m_i))<=exp(lambda^2/2). This follows from convexity of the
exponential on the bounded interval and the zero conditional mean; equivalently
the second derivative of its tilted log moment is a variance at most1.
Iterating and optimizing lambda yields

 Pr[|sum_i(X_i-m_i)|>=Kt]<=2exp(-Kt^2/2).

At t=1/512 and K=2^17n this is2exp(-n/4)<2^(1-n/4),
since e>2. In particular the endpoint n=2^256 keeps a strict tail bound.
Independence of the actual records or the adversary is not assumed.
The virtual conditional means already include the local cutoff and label
errors; there is no conditioning on all virtual roots succeeding.

In an odd stage with a correct input arc the ideal near/far mean gap is
at least0.0379. Each actual average score differs from the applicable exact
ideal near lower or far upper mean by at most

 eta=2p0+1/625+1/512+1/512<0.009535.

The terms are clean-root coupling, table precision, virtual concentration
and deterministic contamination. Since2eta<0.01907<0.0379, every maximizer
is within the next required radius on the good concentration event.
In a2-adic block with a correct earlier prefix, the ideal true/wrong gap
is1/2, so the same error bound makes its exact true residue the unique
maximizer. These statements remain valid for random input arcs: condition
on the entire history at stage start, where the candidate set is fixed.

For either stage type there are at most2^(n/8+12) candidates. For the odd
grid, log2nq<=h-1+log2q0<=n/64+4L<=n/8 and Section6's count plus
ceilings fits this bound. The2-adic grid has2^h<=2^(1+n/64) points.
At most 770<2048 actual stages are run. A conditional union bound and induction
on successful earlier stages therefore give main-branch failure

 failure <2^11*2^(n/8+12)*2^(1-n/4)
        =2^(24-n/8)<=2^-8,

for all n>=2^256. The next-arc induction and exact final rounding in Section6
recover s1; the block induction of Section7 recovers all s2. The output is
the entire s moduloN, not merely a parity or a partial secret.

### Finite branch under the same adaptive budget

For n<2^256 the actual budget is still Bbad=128n. The finite branch uses
mF=2^20(n+16) one-copy records, so at most Bbad records are contaminated
and2Bbad/mF=n/[4096(n+16)]<1/4096<1/512. Construct virtual clean shadow records as above.
With exact latent labels, the fair-basis trigonometric score for t has
mean1/2 if t=s and0 otherwise, by the uniform character sum in Z/NZ.
Each virtual EXTRACT call has error at most1/(2^14P_label_old), uniformly before
the fresh ideal copy, so changing that record to an exact-label one alters
a mean by at most2/(2^14P_label_old)<=2^-13. Table error is below1/625.
Consequently each virtual conditional mean is greater than3/8 for s and
less than1/8 for every wrong t. This includes the stochastic extraction
outcomes visible to the adversary; no exact-label event is conditioned on.

Use the same martingale estimate with t=1/16 and mF records. Union over
N<=2^n candidates gives probability at most
2^(n+1)exp(-mF/512)<=2^(n+1-2048(n+16))<2^-20.
Otherwise virtual scores average at least5/16 for s and at most3/16 for
wrong t. Adding at most1/512 actual/virtual perturbation leaves s uniquely
maximal. Padding malformations may be counted as contaminated records but
cannot change the saved candidate. Finite-branch full recovery succeeds
with probability at least1-2^-20>1-2^-8 under every admissible adversary.

Both branches have the exact fixed source count and branchwise envelopes
of Section9. With the full selected compiler and family proofs, the five current claims
hold jointly for this single algorithm and exact adaptive model, including
the no-corruption case.

## 12. Literal helpers and total record/output interfaces

The Boolean gates in Section 1 have a literal exact implementation. A fresh
zero z can compute NOT(a) by X(z),CX(a,z), XOR(a,b) by CX(a,z),CX(b,z), and
AND(a,b) by CCX(a,b,z). For repeated inputs use AND(a,a)=a and XOR(a,a)=0.
Copy output bits and reverse the actual node gates to clear every helper,
for any input and arbitrary XOR-output target. One Toffoli on a,b,c is

    H(c),CX(b,c),Tdag(c),CX(a,c),T(c),CX(b,c),Tdag(c),
    CX(a,c),T(b),T(c),H(c),CX(a,b),T(a),Tdag(b),CX(a,b).

The parity phase identity 4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)
+(a XOR b XOR c) verifies the phase-free action. Replace Tdag by seven T,
S by two T, Sdag by six T, and Z by four T. Thus these finite words use
only the allowed gate set. H followed by computational measurement gives
X measurement; Sdag,H followed by measurement gives Y measurement. H on
a zero bit and measurement gives a fresh fair bit. Resets measure each
work bit and apply X if its outcome is 1. All gates and outcomes are charged.

Ripple addition uses s_i=a_i XOR b_i XOR c_i and
c_(i+1)=a_i b_i XOR (a_i XOR b_i)c_i. These are a fixed number of Boolean
nodes per bit. Subtraction uses the analogous borrow recurrence; its final
borrow compares unsigned words. Keeping one bit of carry/borrow history per
position and reversing it gives O(w) gates and O(w) clean scratch for w bits.
The controlled versions include the fixed enable among unchanged inputs.
Inside an oracle, each row addition is in place and clears its O(b) carry
scratch before the next row. The oracle inverse reverses these same row
words. No history for an entire O(kb)-node oracle is retained; the active
index/query/arithmetic helpers use O(k+b) qubits as in the selected compiler.
Known-constant modular addition first computes valid-position status,
forms x+c on one extra carry bit, compares with N and conditionally subtracts
N. It fixes x>=N. The resulting function is a permutation on the complete
padded word space, with inverse addition of -c mod N. Compute it into a
clean output, swap and XOR-evaluate that inverse to clear the old input.
Its guard inputs are preserved; helpers clear for every source word.
For a register shift, first use c mod N, obtained by the same fixed division
or compare/subtract templates. The exact sum/subtract selection remains
O(n) for an already reduced c. These constructions implement the collective
translation and literal validation shifts on the whole declared domain.

Classical products, quotient/remainder and extended Euclid use explicit
schoolbook bit arithmetic. A w-bit product adds w shifted rows. Restoring
division processes one numerator bit at a time with compare/subtract.
Euclid iterates remainder divisions. After at most two divisions the larger
positive argument falls by at least a factor of two, so O(w) divisions suffice. These
finite algorithms use polynomial work and O(w^2) classical bits. CRT uses
the resulting Bezout coefficients and exact remainder operations. Only
units with the stated gcd condition are inverted. These setup/classical
costs are included in the explicit polynomial allowances in Sections 4,
8 and 9. They provide no unit-cost real or integer oracle. Quantum
Mult_alpha uses the n known controlled modular additions and its known
inverse as specified in Section 2; it needs only O(n) quantum scratch.

For the actual quantum collective remainder, x<64N uses the fixed six
compare/subtract passes of Section 3, with O(n) quantum helpers. The general
restoring division and Euclid above are classical setup/numerical work; no
O(n^2) quantum divider is allocated. Full signed labels use
n+ceil(log2q0)+4 bits. A row's low-residue conversion is a counted signed
bit slice, including negative divisible values, not an n-bit search per gate.

Every root cap returns only a neutral record, never an output phase to
measure again. Success records contain the one measured frequency/basis/sign.
The finite main output is a least maximizing t in [0,N). The odd estimate
is reduced modulo M or set to 0; each 2-adic r has h bits, so t0 stays within
its accumulated bit width. Final output is (s1+M*t0) mod N. Thus every branch
returns a classical residue, even after malformed inputs or earlier wrong
scalar/numerical decisions. No whole-run abort changes the padding schedule.

The exact shared K remains positive when M=1. Source, weighted, record
padding and whole-run counters are distinct. Root padding begins only after
that root has returned and does not use its smaller Qroot guard. The complete
new cap certificate, count identities, K-dependent concentration, finite old
precision and exact model are in psg_depth_four_family.md. The complete
actual controller and all simultaneous space/remaining-work charges are in
psg_depth_four_compiler.md. The main proof includes every source credit.
