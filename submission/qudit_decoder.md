# QUDIT-L16: explicit finite-vector measurement

This file is part of the same algorithm/proof as proof.md. All parameters,
cost conventions and the adaptive model are those there. This lemma is
used only on clean reference roots; proof.md18 compares the adaptive run.

## 1. Known finite vectors and the collision identity

Letb<=floor(log2n),q=2^b,r=ceil(log2(n^5)),D=2^r,so
q<=n,n^5<=D<2n^5. A completed fine root has a known integer table
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
(q-1)/D<=n^-4. This expectation is over the unused top labels; conditioning
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

For every single-qubit target rotation use the constructive Solovay-Kitaev
algorithm of Dawson andNielsen,quant-ph/0505030v2,Sections2..4,
https://arxiv.org/abs/quant-ph/0505030 . On the fixed inverse-closed universal
Clifford+T instruction set,it gives operator-error tau with gate count
O(log^4(1/tau)); explicit circuit generation and arithmetic have polynomial
cost in log(1/tau). The absolute initial net is generated by enumerating
fixed-length gatewords and certified against a fixed finite constant mesh;
its cost/storage are absolute and charged each run,not instance advice or
an input-dependent preloaded table. This is a standard constructive
compilation theorem used with known angles,not a rotation or real oracle.

Choose tau=1/(16G n^10). Compute target matrix entries by rational interval
bisection/square roots and convergent sine/cosine series to error attau/4;
use the compiler at target error tau/4 with numerical working precision
increased to certify error<tau. Alltargets are determined byintegercounts
or dyadic phases. Rational bisection ofsquare roots in[0,1] usesO(log1/tau)
steps; angles can instead be specified by their sine/cosine pair to the
compiler,so no inverse-trigonometric oracle is needed. Fixed-dimensional
matrix calculations in the constructive compiler can be performed with
certified interval arithmetic at polynomial bit precision. At degenerate
zero rotations returnidentity. Use deterministic tie choices when intervals
permit more thanone valid approximation. There is a fixed polynomial
bound on its recursion/precision from the constructive theorem; choose
that bound as the cutoff,not an unbounded approximation search.

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

The phase table hasD<2n^5 rows ofO(n) bits. Frequency counts,ordered bins,
rank and inverse maps are computed by direct scans/sorts on finite integers.
Each lookup may scan all its declared polynomial-size address table;
classical bit access and indexed gates pay their address cost as inproof.md2.
The inversepair table has at mostqD<2n^6 entries. The compiler's precision
and gateword lengths are polynomial inlogn becauseG is polynomial inn.
It follows,conservatively,that all measurement preprocessing,synthesis,
lookup gates,known-angle gates,generation,execution and cleanup cost a
fixed polynomial inn and classical bits,withO(logn) accessible qubits:
originalr index wires,z/rank wires,O(b+r) AND/lookup scratch,andone active
compiled gate at a time. Circuit words can be streamed by a classical
controller; their polynomial classical storage is nevertheless counted.
No quantum table,QRAM or uncharged subset-sum solution list is supplied.

These fixed polynomial additions over at mostO(n) calls are absorbed by
proof.md's explicit n^11*2^(n/(16log2n)) time and exponential classical
space on its main n>=2^128 range,allowing absolute constants. Polynomial
bit/gate costs need not be smaller at every main input; uniform big-O over
that range absorbs any finite exception into an absolute constant. Quantum
scratch remainsO(logn),so it fits the jointly declaredO(n) envelope.
The main algorithm's Ct/global-attempt guards hold even on arbitrary
malformed states. Synthesis and measurement loops have deterministic
cutoffs/precision; no expected-work assumption enters these resources.

Material intellectual sources: the covariant PGM/frequency-bin construction
is from Bacon,Childs andvanDam,Optimal measurements for the dihedral hidden
subgroup problem,quant-ph/0501044v2,Sections4,5,8,
https://arxiv.org/abs/quant-ph/0501044 . We enumerate our polynomial-size
collimated table explicitly and proveQ1/Q2 using its retained unused-top
labels. This is a specialized accounted implementation,not a discovery
of a new PGM or a black-box solution to subset sum. The constructive
Clifford+T compilation theorem is credited separately above. No prior
submission's acceptance or finite diagnostic is a premise ofQ1..Q5.
