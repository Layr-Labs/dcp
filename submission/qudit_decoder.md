# QUDIT-L16-LARGE: explicit finite-vector measurement

This file is part of the same algorithm/proof as proof.md. All parameters,
cost conventions and the adaptive model are those there. This lemma is
used only on clean reference roots; proof.md18 compares the adaptive run.

## 1. Known finite vectors and the collision identity

For the actual data block let1<=b<=b0=floor(H/2)-1024u,
q=2^b,noise=ceil(log2(n^5)),r=b+noise,D=2^r. Thus
q*n^5<=D<2q*n^5. Both q and D may be exponential in H. A completed fine root has a known integer table
W_a,0<=a<D,withW_0=0 and|W_a|<=2^(Y+b),and the physical state

    |psi_v>=D^(-1/2) sum_a exp(2pi i J W_a v/q+i eta_a)|a>,

wherev is the unknown block residue,J is a known odd integer and
|eta_a|<=1/(16n^4). In the two-adic vector branch eta_a=0.
Condition on the entire low-bit structural transcriptG,including root
completion. It excludes unused top labels and root decoding outcomes.
Distinct entries correspond to distinct0/1 incidence vectors on disjoint
source-copy coordinates. Thus for eacha!=c,the differenceW_a-W_c has
at leastone coefficient+1 or-1 on an independent uniform unused top
label inZ/q. Holding all other such labels fixed proves

    Pr(J(W_a-W_c)=0 modq |G)=1/q.                 (Q1)

OddJ is invertible moduloq. No joint independence of theW_a is required.
Capping/retrying only reads structural decisions,so conditioning on a
particular completeG retainsQ1. Each later root call uses fresh source
systems; this claim is uniform over prior clean reference histories.

Putz_a=J W_a modq,c_z=#{a:z_a=z},p_z=c_z/D. Allcounts and permutations
below are computed by finite classical scans of this explicitD-row table.
They are not a subset-sum oracle. Since sum_z c_z² counts ordered equal
frequency pairs,Q1 gives

    E[sum_z p_z² |G]=1/D+(D-1)/(Dq),
    E[q sum_z(p_z-1/q)² |G]=(q-1)/D.             (Q2)

The first identity includes theD diagonal pairs explicitly. It holds even
when an individualW_a has a biased marginal (in particularW_0=0).

## 2. Exact ideal measurement and every-secret guarantee

Ignoreeta temporarily. Enumerate each bin in increasing original indexa;
rank(a) is its zero-based position. Coherently map

    |a>|0> -> |z_a>|rank(a)>.

This is an isometry on theD source indices. To implement it,compute
(z_a,rank(a)) by explicit XOR scan lookup on the original addressa,then
lookup its inversea from the pair and XOR it into the original register,
clearing that register on the image. Define the inverse lookup0 on
invalid pairs. Each XOR lookup is a unitary on its WHOLE address space;
the zero-on-invalid convention supplies a finite circuit also on bad states.
The ideal transformed state is

    sum_(z:c_z>0) sqrt(p_z) exp(2pi iz v/q)|z>|u_(c_z)>,
    |u_c>=c^(-1/2) sum_(t=0)^(c-1)|t>,

withrank padded tor qubits. Conditional onz,apply a known unitaryU_c^dagger
whoseforward action maps|0^r> to|u_c>. Forc=0 useidentity; that bin has
zero ideal amplitude. This clearsrank and leaves

    sum_z sqrt(p_z) exp(2pi iz v/q)|z>|0^r>.

Apply inverse Fourier transformF_q^dagger on theb-bitz register,where
F_q|v>=q^(-1/2)sum_z exp(2pi izv/q)|z>,then measure theb bits as the
residuea. For EVERYv the correct-output probability is exactly

    P_v=(sum_z sqrt(p_z))²/q.                    (Q3)

It is independent ofv,not merely an average over unknown secrets. This
is the covariant frequency-bin/pretty-good measurement construction. We
need its explicit success formula,not a claim of optimality.

LetA=sum_z sqrt(p_z/q). Cauchy gives0<=A<=1. Then

    1-A²<=2(1-A)=sum_z(sqrt(p_z)-1/sqrt(q))²
       <=q sum_z(p_z-1/q)²,                     (Q4)

because the squared denominator(sqrt(p_z)+1/sqrt(q))² is at least1/q.
ByQ2,expected ideal error for EVERYv,conditionalG,is at most
(q-1)/D<=n^-5. This expectation is over the unused top labels; conditioning
onG does not additionally fix those labels or the frequency table.
The circuit,however,is classically chosen using the actually known table.

For physical phaseseta_a,choose the common phase ofentry0. The norm
distance to the unperturbed vector is at most max_a|eta_a|<=1/(16n^4),
using|exp(ix)-1|<=|x|. Pure-state trace distance is at most that vector
norm distance; measurement contracts it. Thus phase perturbation adds
at most1/(16n^4) error to any outcome probability. The perturbations may
depend onW; only their uniform absolute bound is used.

## 3. Finite known-angle preparation and Clifford+T synthesis

The idealU_c is explicitly defined by a binary prefix tree on[0,c).
At a prefixp oflengthj<r,letd_p count integers in[0,c) with that prefix,
and letd_(p0),d_(p1) be the two child counts. They are computed by integer
interval intersections. Ifd_p=0 use angle0. Otherwise perform the
controlled real rotationRy(2theta_p) on the next bit,where
cos(theta_p)=sqrt(d_(p0)/d_p),sin(theta_p)=sqrt(d_(p1)/d_p),
0<=theta_p<=pi/2,controlled on the current prefix. Induction on theprefix
length gives equal amplitude1/sqrt(c) on everyinteger belowc andzero
elsewhere. This defines a full unitary as a fixed ordered product of
controlled rotations,not a postselected preparation. Use the inverse
product to unprepare. For eachz,controls includez's bits as well as the
rankprefix. At mostqD suchprefix nodes suffice (indeed fewer are needed).
Conditioned rotations act coherently onz; z is not measured.

Multi-bit controls use an AND computed intoO(b+r) fresh ancillas by
Toffoli gates,with X on negative control literals,then are uncomputed.
A controlledRy(angle) is implemented by Ry(angle/2),CNOT,
Ry(-angle/2),CNOT (choose the chronological orientation consistently).
When the control iszero the two rotations cancel; whenone the relation
X Ry(t) X=Ry(-t) doubles the desired angle,up to choosing its sign/order.
Thus only UNcontrolled single-qubit SU(2) rotations require synthesis.
Any global phase in their compiled implementations is a global circuit
phase,not an uncontrolled relative phase on the AND wire.

F_q^dagger uses the ordinary b-qubit Fourier circuit: Hadamards,bit swaps
and controlled phasesdiag(1,1,1,exp(i phi)),withknown dyadicphi. A
controlled phase can be written,up to a GLOBAL phase,using
Rz(phi/2) on eachwire,CNOT,Rz(-phi/2) on the target,CNOT. This gives
relative diagonal phases(1,1,1,exp(i phi)),as a direct four-basis-state
calculation verifies. Negatephi for inverse Fourier. The resulting number
of known single rotations plus counted reversible gates is bounded by
G=2^20 qD(b+r+1)^2; this loose deterministic bound covers the bin lookups,
AND computation/uncomputation,uniform preparations,Fourier gates andresets.

For every uncontrolled rotation use the explicit finite-precision
compiler proved in Section5 below, based on Dawson--Nielsen's
balanced commutator construction, quant-ph/0505030v2 Sections2..4,
https://arxiv.org/abs/quant-ph/0505030 . That paper omits numerical
arithmetic costs; Section5 supplies the additional bound here.
Choose tau=1/(16G n^10), including target-entry and numerical errors.
The predetermined compiler precision and circuit cutoff are stated in5.

Telescoping the product,at mostG unitary approximations of error<tau add
operator error<G*tau<1/(16n^10). Target-entry approximation is included
in that allowance by the chosen safety factors. Thus for any input state,
including one entangled with spectators,the compiled circuit's outcome
probabilities differ by at most1/(16n^10) from the ideal bin/Fourier circuit.
Use this uniform precision for every fine measurement,also on incorrect
histories. It requires no condition on balanced bin counts or on success.
Combining withQ2..Q4 and the physical phase bound gives error

    <=n^-4+1/(16n^4)+1/(16n^10)<2/n^4.           (Q5)

No free postselection or repeated quantum preparation is used inU_c.
All measurements here are computational-basis measurements after the
fully specified compiled circuit. T/T^dagger are permitted elementary
gates in the challenge's uniform Clifford+T model and are charged.

## 4. Complete charged bounds and scope

All decoder preprocessing, gates, classical synthesis and execution cost
O(2^(2b)n^128) work and bits, with O(b+r)=O(n) accessible qubits,
as proved in5. It applies also to the direct-product B=0 branch.
No quantum table, QRAM, subset-sum list or uncharged compilation is used.
All loops have deterministic cutoffs on arbitrary malformed input states.
Material PGM source: Bacon,Childs andvanDam,Optimal measurements for the
dihedral hidden subgroup problem,quant-ph/0501044v2 Sections4,5,8,
https://arxiv.org/abs/quant-ph/0501044 . Q1/Q2 and the explicit
collimated-vector circuit specialize that construction. No acceptance
verdict or finite diagnostic is a premise of Q1..Q5.

## 5. Explicit bit-cost lemma for the larger decoder

The precision analysis here is additional to Dawson--Nielsen: their
paper expressly omits finite-precision arithmetic costs. We use their
balanced group-commutator construction and prove the coarse bit bound
needed here. All constants below are absolute, independent of N and s.

For a known one-qubit SU(2) target and p-bit accuracy, the following
algorithm uses O((n+p+1)^64) charged classical bit operations and bits,
and O((p+1)^8) elementary gates, on n>=2^128 and p<=16n.
The input entries are supplied as certified rational balls computable
to L bits in O(L^3) bit operations. The count/phase targets above have
this property: integer-ratio square roots use bisection, and dyadic
sines/cosines use Machin's rational pi series and Taylor series.
Zero counts and zero angles are handled exactly.

Normalize the fixed inverse-closed Clifford+T alphabet to SU(2).
Choose once and for all a certified epsilon0/2 covering net, with
 epsilon0=2^-32.
A finite such net of gatewords exists by universality and compactness.
It is generated by finite enumeration: refine a fixed rational quaternion
mesh, enumerate all words through each length, and stop at the first
finite covering certificate. Each mesh point has certified operator
distance <epsilon0/4 from a word; the certified mesh radius is
<epsilon0/4. Strict inequalities ensure finite termination. This is a
constant computation, repeated and charged, rather than instance advice.
Let Cnet>=1000 include its finite cost, storage, word lengths and
certificate precision. Its size affects only absolute outside constants.
At the base case select the first word with certified error <epsilon0;
the epsilon0/2 coverage leaves a fixed numerical margin.

Use dyadic target exponents
 a0=32, a_(j+1)=floor(3a_j/2)-7.
They increase by at least a factor5/4. Stop at the least d with
ad>=p+4; thus d=O(log(p+1)), 5^d=O((p+1)^8), and the number
of recursive calls is O((p+1)^5). A depth-j invocation first obtains
Uprev with error<=2^-a_(j-1), and sets Delta=U Uprev^dagger.
For j>=1, if a certified upper bound on ||Delta-I|| is <=2^-aj/2,
return Uprev. Otherwise compute a balanced commutator. Choose the
branch with overlapping thresholds: if the snap test does not certify,
use a certified lower bound >=2^-aj/4. The error bounds below ensure
one of these tests always certifies; the two admissible regions overlap.
There is no numerical search with an input-dependent iteration limit.

Here is a stable algebraic commutator construction. Write
Delta=a I+i x.sigma, r=|x|. In the non-snap branch a>0 and
r>=2^-aj/8. Set
 t=r/sqrt(2(1+sqrt(1-r^2))),
 V0=sqrt(1-t) I+i sqrt(t) sigma_x,
 W0=sqrt(1-t) I+i sqrt(t) sigma_y.
Their commutator has scalar part 1-2t^2=a and vector length r,
since r=2t sqrt(1-t^2). Map its unit vector to x/r by conjugation.
To construct that conjugation, for each unit vector v choose a coordinate
e_i with |v_i|<3/4, form the frame
 ( (e_i-v_i v)/sqrt(1-v_i^2), v cross first, v ).
A coordinate with |v_i|<=1/sqrt3 exists, so interval tests with the
3/4 threshold have a uniform margin. The product of the two frames
is a rotation mapping the vectors. Lift it to SU(2) using any quaternion
chart whose component square is >1/8. Some component square is >=1/4,
again giving overlap and bounded chart denominators. Conjugate V0,W0
by that lift to obtain V,W. These formulas avoid antipodal singularities.
Direct substitution gives Delta=VWV^dagger W^dagger and
||V-I||,||W-I||<=2 sqrt(epsilon), where epsilon=2^-a_(j-1).
Recursively approximate V,W to epsilon and assemble the five wordpieces
 Vtilde Wtilde Vtilde^dagger Wtilde^dagger Uprev.
Dawson--Nielsen Lemma14 bounds the commutator perturbation by
 8 epsilon delta+4 epsilon delta^2+8 epsilon^2
       +4 epsilon^3+epsilon^4,
with delta<=2sqrt(epsilon). For epsilon<=2^-32 this is less than
32 epsilon^(3/2). Our target 2^-aj is at least
128 epsilon^(3/2), leaving a factor-four margin for numerical errors.

For completeness the precision and operation counts are fixed as follows.
Every recursive target denotes an EXACT SU(2) matrix defined by the
algebraic formulas, with certified enclosing balls as its representation.
Rounded nonunitary midpoints are never substituted as exact targets.
The frame/quaternion formulas are evaluated for the exact target inside
its ball; overlap choices are certified for all members of that ball.
Use L=(n+p+Cnet+100)^4 fractional bits throughout; all ball radii are
rounded outwards. An elementary balanced-commutator macro uses fewer
than 1000 scalar additions, multiplications, divisions and square roots.
All values have absolute size <=16; the only potentially small divisor
comes from r or its square roots, with r>=2^-aj/8. A square root is
used either on a strictly positive argument >=2^(-4aj-20), or as the
exact zero branch. The derivatives of division and square root on these
intervals, along with multiplication and sums, bound the macro error
amplification by 2^(10000(aj+1)); the deliberately loose coefficient
covers all 1000 scalar operations even if their losses are multiplied.
Frame/chart choices retain the margins just stated. Since every aj is
<=2p+64 and the depth is at most 8 log2(p+2)+8, total amplification
along any recursive path is at most
 2^(1000000(p+100)(log2(p+2)+1)).
There are O(Cnet(p+1)^8) rounded operations and word products.
For n>=2^128,p<=16n the displayed L dominates that loss and
p+100+log2(Cnet+1)+16log2(p+2), with ample strict slack.
One may check the endpoint using log2 n<=n^(1/4), and thereafter
n^3/log2 n is increasing. Increasing Cnet only increases the left
quartic faster than the right logarithm. Thus every node's numerical
uncertainty is <2^-aj/1000, and the assembled error fits the factor-four
margin. Snap tests, chart choices and base net choices all terminate
within their predetermined arithmetic loops.

Matrix products of gatewords are evaluated as unitary norm balls.
For each exact unitary factor with approximation error eta, update the
radius by R+eta+R eta+rounding. Consequently a word of length W
accumulates O(W 2^-L) error (with absolute fixed gate constants),
rather than multiplying a naive interval wrapping factor W times.
Each partial exact product is unitary. This justifies the polynomial
operation/radius count used above. Finish by certifying operator error
<2^-p using the target ball and the final word ball; the proved margin
ensures this check succeeds. There is no exhaustive instance-dependent
word search. Any failed certificate causes a declared abort, counted
as failure; the bounds show this cannot occur on the main range.

At L bits, grade-school arithmetic and bisection use O(L^3) bit work.
The call tree and all stored/evaluated words together use at most
O(Cnet(p+1)^16) fixed-dimensional operations, including certification.
Since L=O(n^4),p<=16n, this is O(n^28) bit work before address costs;
allowing generation, tape/index addresses, resets and storage gives
O(n^64), with an absolute constant depending on Cnet. All compilation
is classical. Inverse words are literal reversed words with inverse
gates; gates can be streamed. The physical normalized alphabet differs
from permitted gates only by whole-circuit scalar phases, because
controlled rotations were first decomposed into uncontrolled rotations
and exact reversible gates. No relative phase on a control is discarded.

For this decoder G<=2^23 2^(2b)n^7. Choose
 tau=1/(16G n^10), p=ceil(log2(16/tau)); then p<=16n on the
main range since 2b<=H<=n and log2 G<=2b+7u+23.
The rounding and target allowances above give error<tau per rotation.
Preprocessing may use even the simple quadratic scan of the D input
rows, costing O(D^2 n^4). The inverse permutation uses a sparse list
of the D valid pairs, with value zero otherwise; its reversible XOR
lookup scans that list once. The qD prefix nodes use classically known
counts, so no extra D-row quantum lookup is performed per node.
Multiplying G by the compiler bound, and including all integer/address
work, bounds the ENTIRE decoder by
 O(2^(2b)n^128)
charged work and classical bits. Quantum wires are O(b+r); none of the
classical compiler's arithmetic is carried out in quantum workspace.
This deliberately coarse bound is sufficient because the algorithm
sets 2b<=H-2048u. Over O(u) decoder calls the work and storage are
O(2^H/n^1900), absorbed by the declared tree work and H2^H memory.
This bound is deterministic on arbitrary states, not merely ideal roots.
