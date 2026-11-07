# Complete joint-input, channel, statistical and endpoint proof

This is required evidence with [the main proof](linear_quantum_marginal.md),
[the full filter proof](linear_quantum_marginal_filter.md), and
[the literal controller](linear_quantum_marginal_controller.md).
All five claims cite all four current proof files. This file proves the
exact selected joint-input model, local compression channel with arbitrary
reference, good-first record law and concentration, coherent answer law,
known undo and complete endpoint. All literal filter/module/controller
proofs are present in the other current files, not supplied by an external
review or theorem. Main Section 10 gives actual direct and inherited sources.

## 1. Result and fixed scope

Use the exact LQ-MARGINAL deterministic-filter algorithm and the single
parameter rule in main Section 0.
For every N>=2 and s in Z/NZ, the same physical algorithm has

    Q=3*2^16*(n+32), n=ceil(log2 N), r=Q/3,
    T=O(2^(n/2)*n^(7/2)*(log2 n)^2),
    S_C=O(n^2), S_Q=O(n), success>=11/16, epsilon=1/3.

The displayed time envelope applies for n>=2. N=2 has finite absolute cost
with this same Q rule. All resource bounds hold on every branch.

The complete current filter appendix supplies the literal all-input
unitaries, codes, probe-inclusive reflections, deterministic success and
verifier hybrid. The current controller appendix and main Section 9 supply
the complete literal stream and resource proof. These are required evidence.
The channel/statistical/endpoint interfaces are proved in full below.

The selected input specification is exactly the following structured text
from the direct E source credited in main Section 10.4:

> Among the Q acquired copies, an adversary fixes a set B of at most
> floor(epsilon(n) Q) malformed positions, possibly depending on N and s.
> The joint state is arbitrary subject to its reduced state on all other
> positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be
> correlated or entangled with each other and with other systems subject to
> that marginal promise. No source control, purification access, or
> preparation inverse is supplied.

Here rho_s is the ideal coset mixture defined in main Section 0. For a fixed component, write
H for the good set (to distinguish it from the gradient modulus G), and R
for any inaccessible reference. The promise is

    sigma_(HBR)>=0, Tr sigma=1,
    Tr_(BR) sigma=rho_s^(tensor |H|), |B|<=r.            (J1)

No tensor product between H and BR is assumed. A convex mixture of such
components with different B is allowed. A uniform success bound extends to
that mixture by linearity. The resource bounds do not depend on its choice.

## 2. Delivery, memory, and exact comparison of the models

The Q registers in (J1) are prepared jointly before the first delivery.
The inaccessible source holds the unread registers passively. It releases
one register on each of the algorithm's Q fixed acquisition steps. It makes
no replacement, measurement, feedback choice or further transformation.
The algorithm applies its unchanged local compression, then releases the
position/probe work before it asks for the next register. A state change
in a conditional description of an unread register is not a source action.

This uses the input promise above without change. It does not assert that
the unread conditional good marginal remains ideal after earlier outcomes.
In general it does not. The promise applies to the original joint input.

The rules state: "State held by the inaccessible source is excluded."
Thus the unread raw registers are excluded. The Q acquired rows, all
classical labels and prefixes, and the one current n-qubit position register
are included. Each of the Q deliveries still incurs n+1 source work units.
There is no extra call, source control, source inverse or change to the
fixed streaming schedule. E's choice to acquire and retain all Q raw
registers before it acts is a choice of E's algorithm, not a condition in
the structured input text above. That choice is not copied here.

The public linear source has a different, interactive specification. Its
next clean delivery is a fresh rho_s in tensor product with everything
else, and its malformed choices may depend on earlier public outcomes.
For a fixed B its clean tensor requirement excludes some inputs in (J1).
For example, purify one clean rho_s into a malformed register (rho_s has
rank N, whereas a malformed register has dimension 2^(n+1)>=N), and tensor
all other good rho_s states. This satisfies (J1), but the selected clean
register is entangled with the later malformed register. It cannot be a
fresh clean tensor factor in that delivery protocol. Thus the new statement
does cover additional entangled inputs. An interactive feedback promise
and a fixed joint-state promise are distinct specifications; no inclusion
of all adaptive feedback laws into (J1) is asserted.

If all unread raw registers had to be resident algorithm inputs at once,
they would contribute Q(n+1)=Theta(n^2) qubits. That would prevent this
space claim under that different convention. The quoted rule permits the
passive-source convention used here, so it causes no barrier in this task.

## 3. The complete local compression channel

Use the Fourier convention of main Section 2:

    chi_k=N^(-1/2) sum_(x<N) exp(-2*pi*i*k*x/N)|x>,
    phi_(k,s)=(|0>+exp(2*pi*i*k*s/N)|1>)/sqrt(2),
    rho_s=(1/N) sum_(k<N)
        |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.   (J2)

Main Section 1's fixed repeated label test has J0=max(1,n-2),
L_F=bitlength(16*(J0+1)*Q*2^60), and R_F=200*L_F.
It first measures position validity. On valid positions its probe words
use only controlled modular translations and gates on fresh probes.
For a complete probe outcome string a, the corresponding operator on the
position is

    K_a=sum_(k<N) c_a(k)|chi_k><chi_k|.

It is the identity on the row. Let d(a) be its total deterministic label
decoder and put p(ell|k)=sum_(a:d(a)=ell)|c_a(k)|^2. Its established uniform
bound is

    p(k|k)>1-delta_F, delta_F=2^-60/Q, for every k.     (J3)

This follows from the label test, not from a distribution for malformed k.
All decoded words are total even when tests fail. Store only the valid
flag v, decoded label ell, and exact classical prefix
e=floor(2^(n+p)*ell/N). The remaining measurement outcomes are used for
their charged count/reset operations, then ignored by all later gates.
Measuring, conditionally resetting and releasing position work is a trace
over position for the retained row and R.

For an arbitrary input tau on row, position and any reference R, the valid
branch of the retained local channel therefore has the exact form

    A_ell(tau)=sum_(k<N) p(ell|k)
        (I_rowR tensor <chi_k|) tau
        (I_rowR tensor |chi_k>).                    (J4)

The output order in (J4) is row,R. Indeed expand K_a tau K_a^dagger in
the chi basis. Partial trace of position multiplies the (k,l) term by
<chi_l|chi_k>=1_[k=l]. Sum a with the selected label. This also proves
(J4) after tensoring the channel with identity on arbitrarily many other
registers. The invalid branch is the partial trace of the padded-position
block, with v=0 and ell=e=0. The measured validity flag removes its cross
terms with the valid block.

Equation (J4) is a full channel statement, not just a mean-score bound.
It gives an exact mathematical refinement with a hidden true label k.
Forget k to obtain the actual retained compressed state. The algorithm
does not read k. No hidden label is assigned to an invalid position.
The refinement is used after unused reset records are traced out; it is
not an assertion about conditional laws after fixing those unused records.
That trace changes no later algorithm outcome.

On a clean rho_s, (J2)--(J4) give uniform hidden k, row phi_(k,s), v=1,
and the stated decoded-label law. Across all good slots, their joint
hidden-label/retained-row marginal is a product of this local law, because
the input marginal in (J1) is a product and each local channel is applied
once. Arbitrary extension to B and R is retained. For endpoint analysis,
one may further fix all the good hidden k. Their row marginal is then the
pure product of the phi_(k,s), hence factors from the remaining systems:
a density operator with a pure subsystem marginal has support only on
that subsystem vector. This factorization is a derived conditional fact,
not an extra clean/bad tensor premise.

For a good slot J3 bounds the error even conditional on its true k. By a
union bound on the product good marginal,

    Pr[any good decoded label differs from hidden k]<2^-60.  (J5)

This is unconditional. Conditioning all labels on successful decoding
would change the good parity law and is not done.

## 4. Record law and the score bound on arbitrary bad states

Append the unchanged fresh |+> axis qubit to each retained row, apply
Sdag to the row under axis=1, and apply H to the row. Axis and row now
hold computational records (a,b). In the mathematical measured version,
a is a fresh fair X/Y choice and y=(-1)^b is its outcome. Actual records
remain coherent. Combine this instrument with the slot's local acquisition
channel from Section 3. This is a local instrument on one raw input and
its fresh independent ancillas only.

For clarity, the full joint probability of local record outcomes x_j is

    Pr[x_1,...,x_Q]
      =Tr[(tensor_(j=1)^Q I_(j,x_j) tensor id_R)(sigma)],  (J6)

where each I_(j,x_j) is its trace-decreasing local instrument. Local maps
on different slots commute, including on entangled inputs. Thus (J6)
is exactly the law of the physical streaming acquisition followed by
deferred row records. It is also the law if the complete good-slot
instruments are applied first in any fixed order, then the complete bad
instruments. This is an order for the proof only. It does not give B to
the algorithm and does not change its delivery or storage schedule.

Main Section 4 specifies the complete exact prefix/score circuit. To state the needed all-input
interface, let U_t add t modulo N on row 1 on valid positions and fix
padding. Let R_t=U_t X_row U_t^dagger, A=(R_t-R_u)/2, and

    M_tu=(7A-2A^3)/5
       =[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.

It is zero on padding, antisymmetric in t,u, and has norm <=1. For
nonantipodal distinct t,u, its means on rho_t and rho_u are +/-11/20.
These facts follow from R_t^2=I, R_t R_u R_t=R_(2t-u) and the monotone
polynomial (7x-2x^3)/5 on [-1,1]. On the k block its row observable is
Re(h_tu(k)) X+Im(h_tu(k)) Y, where

    h_tu(k)=[11(exp(2*pi*i*k*t/N)-exp(2*pi*i*k*u/N))
        +exp(2*pi*i*k*(2t-u)/N)
        -exp(2*pi*i*k*(2u-t)/N)]/20,
    |h_tu(k)|<=1.

The unchanged rational score Z(t,u) is in [-2,2], including on arbitrary
labels and row records. The exact prefix/table computation approximates
each trigonometric component within

    eta=3*pi*2^-14+2^-24.

Its clamped h-component error on a correct label is <=(6/5)*eta.
Averaging the fresh X/Y axis gives a row-observable error <=(12/5)*eta.
For an incorrect label, the norm difference is <4. Apply J3 in each
diagonal block of J4. The expected-score observable O_tu of the complete
local instrument obeys, on the full raw input space,

    ||O_tu-M_tu||<=beta=(12/5)*eta+4*delta_F<1/320.   (J7)

Padding contributes zero. In particular J7 holds for every conditional
density matrix on a bad slot, with any residual reference entanglement.
It is not a claim that a bad label is uniform or correct. It is not
obtained by conditioning on previously measured bad labels. All outcomes
of this next local instrument, including its fresh axis, are averaged.

## 5. Good-first concentration, without a conditional-input assumption

Fix B and use the good-first order in J6. The joint good record marginal
is the product clean law by J1. Hence each successive good slot has its
clean law conditional on earlier good records. At this point no bad
record has been revealed. A good measurement can steer B and R; that
does not change the product marginal law of the remaining good outcomes.
After all good records have been revealed, take bad records one at a
time. Their conditional states are arbitrary; J7 applies to each one.
Its axis is drawn locally at this step and is fresh. The prior bad
outcome history cannot condition a future independently supplied axis.

For a pair (s,u) with u outside the true class, let mu_i be the mean
of its score conditional on all preceding records in this order. Then

    mu_i>=11/20-beta on good slots,
    mu_i>=-1-beta on bad slots,
    sum_i mu_i>=Q/30-Q*beta.                        (J8)

For the reverse pair use the reversed inequalities. These are uniform
pathwise bounds on conditional means; only the original good marginal
was assumed to be a product. In particular do not reveal all physical
acquisition labels before applying the first inequality. Bad labels can
steer a good row and make that different conditioning invalid.

For completeness, put D_i=Z_i-mu_i. Each centered increment has interval
width 4 and conditional mean zero. If a centered variable lies in an
interval [a,a+w], convexity bounds its exponential moment by that of the
two endpoints with the same mean. With p=-a/w and h=lambda*w its log is

    f(h)=-p*h+log(1-p+p*exp(h)).

Here f(0)=f'(0)=0 and f''(h)<=1/4, so f(h)<=h^2/8. Applying this at
each conditional history, iterating, and optimizing Markov's bound gives

    Pr[|sum_i D_i|>=x]<=2 exp(-2*x^2/(16Q)).       (J9)

Choose x=Q/64. A union bound over fewer than K^2 needed ordered pairs,
K=2^n, yields simultaneous sign failure less than

    2*K^2*exp(-Q/32768)
      =2*K^2*exp(-6*(n+32))<2^-80.                (J10)

The final inequality uses e>2 and n>=1. Outside that event,

    Q^-1 sum_i Z_i(s,u)
      >=1/30-beta-1/64>7/480>0,                  (J11)

with strict reversed sign in the other orientation. The fixed class
tournament therefore has the true class as its unique source. No
independence of bad records, bad-good tensor product, or transitivity
of false-class edges has entered this proof. N=2 has no distinct classes,
so its coarse sign/selector work is omitted as specified.

## 6. Coherent records and the exact coarse-bank interface

At a fixed retained acquisition transcript ell, apply the row-record
unitary. Let x denote its full axis/row computational word. Every later
filter and answer gate preserves x. Thus the selector word is

    S_ell=sum_x |x><x| tensor S_(ell,x),             (J12)

where each block is the full actual unitary from the current filter proof.
It is defined on every logical input, including arbitrary stopping codes,
probes and shared-verifier leakage. The read-only records may be
entangled with the external R and with other work. For an answer
probability, expand the input density in x,x'. Since the answer effect
is identity on the retained record register, its trace sets x=x'.
Consequently the answer law is exactly the average of the block answer
laws under J6. This is an operator calculation, not an assumption that
records are physically measured. No off-diagonal coherence can increase
this failure probability.

On every good record block, the fixed deterministic selector gives a
fresh-attempt source probability >1/16. Its 1024 disjoint fresh attempts
have miss probability <(15/16)^1024<2^-64 in the comparison circuit.
Its shared verifier has initial-inner-zero vector error <2^(-4n-127)
per call, uniformly over candidate superpositions and reference systems.
The preceding ideal calls leave the shared inner work zero. The same
telescoping hybrid as in current filter Section 8 therefore has vector error
<2^-121 and probability loss <2^-120 for n>=1. Actual shared leakage
is retained; the estimate is never applied to a later actual leaked input.
Arbitrary x blocks use the total physical word without a success premise.

J10 and J12 now give the actual unconditional coarse failure

    e_c<2^-80+2^-64+2^-120<2^-60.                 (J13)

This is the same numerical interface as in the current filter proof. It
has now been proved for J1 with arbitrary good-bad/reference entanglement.

Let U_ell include row-record creation, the fixed filter/verifier words,
and the total first-verified answer logic. No source operation is in U.
For a purification psi of the compressed bank, zero logical work and
ideal gradient, let Pi_z=U_ell^dagger P_z U_ell. Copy only the answer and
apply the literal inverse of U_ell. The resulting vector is

    sum_z |z> Pi_z psi.

If z_* is the true class, the squared distance from |z_*>psi is exactly
2(1-<psi|Pi_(z_*)|psi>). The correct component contributes
||(Pi_(z_*)-I)psi||^2=1-p and all other orthogonal answer components
contribute 1-p. Make a direct-sum purification over the actual retained
transcript ell, with an orthogonal environment copy. Average this identity
using J13. The actual bank, all residual old work, ideal gradient and
copied class are within trace distance

    d_undo<=sqrt(2*e_c)<2^-29                    (J14)

of the original compressed bank and work with the correct fixed class.
The bound also holds with any inaccessible reference retained. Acquisition
measurements and source preparation are not inverted. All residual old
work, logical probes and shared-verifier leakage remain allocated.
Any later endpoint instrument, with fresh helpers, contracts this distance.
No correctness conditioned on every transcript is asserted or needed.

## 7. Endpoint on the compressed joint bank

For odd N, J14 already gives the secret. For even N, put h=N/2 and
t=s mod h. First compare to the original compressed bank in J14, with
the correct class t and an ideal independent gradient. Use the exact
hidden-label extension J4 for this comparison bank.

Use the fixed physical endpoint: on row 1, subtract

    a_j=floor(G*((ell_j*t) mod N)/N),
    g=bitlength(2^80*(Q+1)), G=2^g,

from the gradient. On its ideal Fourier state gamma this is a phase
exp(-2*pi*i*a_j/G), leaving gamma unchanged. Compare it to the exact
row phase exp(-2*pi*i*ell_j*t/N). Their operator norm difference is
<2*pi/G<8/G for every ell_j, including arbitrary bad labels and row
states. A telescoping bound across Q rows gives vector distance <8Q/G.
An outcome probability differs by at most twice that distance. Thus
endpoint probability loss is bounded by

    d_round<16Q/G<2^-76.                          (J15)

This estimate is uniform for entangled banks; bad rows need no purity
or independence. The invalid flag only changes the later trit rule.

In the exact-phase comparison, measure each row in X. A slot gives C
if its flag is invalid or its decoded label is even. Otherwise it gives
L for X sign +1 and U for X sign -1. All bad trits may be arbitrary.
They number at most r, so the number of false trits is at most r on
every outcome of this comparison instrument.

Define a mathematical second endpoint instrument using the same hidden
label refinement. Change only good slots: use their hidden k in their
phase correction and parity test. Leave all bad instruments unchanged.
On the block where every good ell_j=k_j, these two endpoint instruments
are identical. Their success probabilities can thus differ by at most
the weight of the other blocks, which is <2^-60 by J5. This is an
unconditional coupling of classical hidden-label/decoded-label blocks.
It does not condition the clean parity law on accurate estimation.

In this second instrument the product good marginal in J1 gives uniform
independent k_j in [0,N). Exactly half are odd. A good row is phi_(k,s).
After correction it is |+> if s=t, and has row phase (-1)^k if s=t+h.
Hence each good slot gives C/correct with probabilities 1/2,1/2 and
never gives a false trit. The correct-good count is Bin(|H|,1/2) and
dominates X~Bin(2r,1/2). Good outcomes can be correlated with bad
outcomes, but this good-count marginal is unchanged. Bad outcomes cannot
give more than r false trits, regardless of those correlations.

Use the fixed total decision: return t if L>r; else return t+h if U>r;
else use a fresh fair coin. Give L priority if both exceed in other
comparison branches. In the true-label reference a false threshold
cannot be crossed. Thus success is at least

    1/2+(1/2)*Pr[X>r]
      =3/4-(1/4)*binom(2r,r)/4^r>=23/32.          (J16)

For completeness, b_r=binom(2r,r)/4^r obeys
b_(r+1)/b_r=(2r+1)/(2r+2) and b_r<=1/sqrt(r+1).
Squaring the induction step gives 3r+2>=0. Here r>=64, so b_r<1/8.
This argument needs no conditional binomial law after the bad outcomes.
It uses only the original good marginal and the pathwise false-count cap.

## 8. Gradient, triangle bound, and N=2

Main Section 7's complete 80-attempt gradient routine is local and independent of the
input bank and all its acquisition outcomes. Its reduced output, including
failure flag, is within distance

    d_grad<=2^-80+2^-100

of success with the ideal pure gamma. Fresh local randomness supplies
that routine. Therefore it is a product channel with the input bank,
even if that bank has an arbitrary reference extension. Trace-distance
contraction charges d_grad once through all later operations. A failure
branch has already acquired all Q copies and is included in this bound.

Combine J14, J5, J15, and this gradient comparison. The total success loss
against J16 is less than

    2^-29+2^-60+2^-76+2^-80+2^-100<1/256.         (J17)

Full-secret success is therefore >183/256>11/16>2/3. The actual disturbed
bank need not have a literal bad-trit cap; that cap is used only in the
unchanged comparison bank, then J14 contracts through the full endpoint.

At N=2 the fixed algorithm omits U, the selector and all selector probes.
Its class is t=0, Q=3*2^16*33 and r=2^16*33. Acquisition, the exact same
gradient routine, trit threshold and fresh final coin remain. Sections
3 and 7 apply with the two Fourier labels 0 and 1. Half are odd, the
good marginal still gives independent parities, and J16 holds. J17
applies with zero undo loss (and the stated conservative rounding loss).
Thus N=2 has the same success bound and a fixed finite absolute resource
cost. It is not replaced by E's Q=192 branch or by a new special circuit.

## 9. Resource and integration consequence

No gate, seed, acquisition test, precision, number of attempts, threshold,
gradient parameter, filter scale, code rule, module, inverse or verifier
changes. The deterministic schedule still has no selector seed bank.
All Q raw deliveries are compressed once before gradient preparation.
The input may be entangled across future slots, but the same local channel
uses one current position/probe workspace. Its output stores Q rows and
the same Q classical labels/flags/prefixes. Malformed conditional states
cannot change the loop caps, allocated widths or emitted circuit stream.

The complete current filter/controller proof supplies the resource count.
Its S_Q includes all Q retained rows and axes, all 1024 retained logical
attempts/probes/output bits, the shared verifier with leakage, reusable
arithmetic, gradient, answer copy, residual old work and fresh endpoint
helpers. It is O(n) in total. Its S_C=O(n^2) includes every classical
record and public controller word. Its complete stream has charged time
O(2^(n/2)n^(7/2)(log2 n)^2), and exactly Q source acquisitions on every
branch. No good-first reorder is physically executed or allocated.

The selected model is exactly the joint clean-marginal specification in
main Section 0. Sections 3--5 supply the full record/score proof, and
Sections 6--8 supply known undo and the endpoint. The acquisition, score
arithmetic, filter, gradient and endpoint implementation proofs are all
present in the four required current proof files. The historical adaptive
specification is distinct and is not a selected input requirement here.
