# NONPOWER-ROBUST16: adaptive malformed-copy tolerance with constant-size source microbanks

## 0. Joint theorem, exact bank configuration and error model

For every N>=2 and secret s moduloN put n=ceil(log2N). The single
NONPOWER-ROBUST16 algorithm below acquires exactly Qbank copies,computed
fromN alone. For every adversary of the error model below,including the
clean case,it recovers the entire secret with unconditional probability
at least2/3. On EVERY branch jointly,with absolute constants,

    T=O(n^10 l 2^F64(n)),
    S_C=O((n^9/log2n)2^F64(n)),
    S_Q=O(n), Q=O(n^17),
    epsilon(n)=log2n/(238263 n^17).

F64 is the exact64-term rational-coefficient exponent in15.
Logarithmic resource envelopes atn=1 usepositive n=2 values; the tolerance
has its natural value0 atn=1. Growth indices are1,1,0,0; tolerance is a fraction
among all acquired copies,not a per-copy probability or a count score.

Error model (exact adaptive specification): Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

For n>=2^128 compute exact parameters

    ell=RLOG(n),m=ceil(16ell),u=ceil(log2n),w=64u,
    base=ceil(n/(m+1)-m/2)+2,dl=base,H=base+m-1,
    lambda_i=base+i,delta_i=2^(i-m-2),
    M_i=2^lambda_i-2^(lambda_i+i-m-2) for0<=i<m,
    lambda_m=d,M_m=2^d,
    d=1 for coarse roots,d=r for fine vector roots,
    Kc=36864u,g_w=ceil(log2dl),
    b0=floor(H/2)-1024u,Lblk=ceil(n/b0),E=8u,noise=ceil(log2(n^5)).
For each actual data block b set r=b+noise; coarse roots use d=1.

The consumed-slot capQcap is defined in13 before access; Qbank=1024*Qcap.
For the main branch each reference source request in3..12 uses a fresh
microbank ofKraw=1024 raw copies: hold core workspace idle while they are
acquired,then draw10 fresh fair bits and select exactlyone uniformly.
Unchosen copies are reset/released. The main core never uses the wrapper's
selection or cleanup outcomes. After the core stops,pad with unused
microbanks until exactlyQcap microbanks have been acquired. Thus actual
Q=Qbank=1024Qcap is fixed byN,including all discarded and padding copies.
For n<2^128 use the whole-bank finite branch in13/18. The probabilistic
claims of3..12 describe the clean reference core;18 proves the adaptive
iterated classical-record comparison. Per-root and controller guards apply to every state.

RLOG and all arithmetic use the finite rational algorithms in8; no real
oracle is supplied. Notation:dn=floor(log2N),N=2^a2 M withM odd,s1=s modM,
s2 in[0,2^a2) withs=s1+M*s2 moduloN,omega=exp(2pi i/N). Logs are base2.
Labels are known nonnegative integers; data basis states|u> have0<=u<N.

## 1. Actual sources and the new non-power robust composition

Immediate complete adaptive framework is frozen QUDIT-L16-LARGE64,
registered b9f17935-d58b-41c4-a321-621a0f7e9ce0 after its first genuine
all-five-claim review386.52s/finalization1. Hosted publication is pending
at construction; before this derivative's upload verify its actual
canonical published files and relevant graph and declare its actual ID.
It supplies the full low-label-only physical verifier, adaptive classical
record comparison, bounded backtracking/chains, one wide coarse batch,
large output blocks, all-N fraction log2n/(2^18n17), finite-bank proof,
charged synthesis and exact64-term reciprocal envelope. All arguments
are reproduced, not imported verdicts. No clean-only success statement
replaces its adaptive adversary model or all-N2/3 guarantee.

New explicitly measured non-power merge comes from the frozen private
NONPOWER-CUBE artifact, first genuine all-five-claim accepted244.21s,
finalized2/3. Its actual canonical files/graph must likewise be verified
and declared if registered before this upload. Its exact interval maps,
binary-incidence bucket moments and fresh-trial renewal are reproduced
in nonpower_merge.md, and applied below both to ordinary roots and the
low-only verifier. Corrections must propagate; no publication is assumed.
This composition checks the actual W64 caps Cc64dl2m/Cf16dl2m,
missing3/32 and3/8, not a stronger imagined root law. The final root is
still full2^d, so every physical verifier/vector decoder interface is
proved unchanged. The complete full time improves by one log factor.

W64's earlier change w32u->w64u and fraction doubling are retained
unchanged here, including its exact margin231/320000. Its complete
immediate source was published Large16
316d16c3-e6c7-4284-ab8d-05eff620cb4a at
5e378e99f91a59e6588b69a143b17db4938b0477, all three source files
fetched/cmp verified and five provisional incoming declarations read.
Historical directly used WIDE16,CHAIN16,SPLIT16,ROBUST,BANK credits
are retained precisely through that complete source; no graph-wide
redundancy or independence is asserted. The PGM/frequency-bin credit is
Bacon,Childs,vanDam quant-ph/0501044v2 Sections4,5,8; constructive
balanced commutator credit is Dawson,Nielsen quant-ph/0505030v2
Sections2..4, which omits numerical arithmetic costs. The additional
certified bitprecision/explicit-generation proof is reproduced from
Large16. Pending references are not accepted ancestry.

The actual cap upper bound476526n17 permits the strengthened fraction
log2n/(238263n17): epsilon*Qcap<=2log2n<=w/32, since476526=2*238263.
This improves W64's dyadic denominator262144, keeping its error-model
specification unchanged. The finite branch below uses the ACTUAL new
fraction and the sufficient epsilon*k<2^-30; no stale smaller finite
fraction or unsupported2^-32 remainder is used. All-N success remains2/3.

The exact new base/lengths and capacity/memory/charged-work proofs below
replace every tapered nonroot construction. Prior verdicts and diagnostic
checks are never mathematical premises. No optimality, physical-runtime,
primitive-priority or source-independence claim is made.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger/T/T^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on indexed qubits are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.          (2.1)

Main source wrapper MICROTAKE. Keep a countera of active/padding
microbanks,initially0. A reference acquisition in3..12 means:
(1) ifa=Qcap,ABORT before requesting any raw copy;
(2) pause every core gate/measurement and acquire exactly1024 raw copies
into distinct(n+1)-qubit registers,without ANY algorithm operation,private
draw or measurement between these deliveries;
(3) only after the last delivery,measure10 freshH|0> coins,forming uniform
J in0..1023; SWAP raw registerJ into an empty source working register
with3(n+1) CNOTs on classically known addresses;
(4) reset/release all unchosen registers,and incrementa. Return the chosen
copy to the core. All selection/cleanup outcomes are ignored by the core;
its own decoder coins remain fresh independent coins. The adversary may
see these outcomes before later deliveries,as its model permits.

The local per-root guards in9 count SELECTED MICROTAKE
deliveries,not the1024 raw acquisitions inside one call. Every raw copy
counts in actualQ. After core success orABORT,record its output,release
the core quantum state,and acquire/reset dummy microbanks untila=Qcap.
Dummy banks return no copy and their measurements never alter the output.
Thus actualQ=1024Qcap on every branch; all padding work/storage are charged.
At mostone microbank is allocated at a time,beside the reused core wires.
LE confidence usesQcap,because at mostQcap selected copies are extracted.

## 3. Source identities, the latent-label model and data transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into rho_s = (1/N) sum_x |psi_x><psi_x|,
with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,          (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is a convex mixture, with uniform weights, of the
product states phi_k(s) (x) chi_k. The whole algorithm is a linear adaptive quantum instrument
on independent copies. So the joint law of all classical outcomes equals the law obtained by
first drawing, per copy, an independent uniform latent label k and then running on
phi_k(s) (x) chi_k. All probabilities below use this model. Applying X to the control maps
phi_k(s) to, up to a global phase, the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each is a permutation
of all 2^n data encodings, extended by the identity on encodings >= N, and maps the copy
exactly to rho_s' for a known s'. The latent label of a copy is the Fourier label of its
TRANSFORMED data register.

(T1) Mult_alpha: u -> alpha u mod N, for known alpha coprime to N. Since x -> alpha x is a
bijection of Z/NZ, the copy becomes exactly rho_(alpha s). It uses n controlled modular
additions of the constants alpha 2^v mod N into a clean register, a swap, and the inverse
computation with alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for known c. Since |1,x+s>
becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N, an addition, a
comparison and a selector. It is the identity on encodings >= N, uses O(n) Boolean gates, and
is computed cleanly: compute, swap or XOR out, uncompute.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20 of
cos(2 pi v/4096) and sin(2 pi v/4096): bound pi within 2^-90 with Machin's formula
pi = 16 atan(1/5) - 4 atan(1/239), summing 40 terms of each alternating series (tails below
2^-91); at the angle 2 v p_mid/4096 < 7, with p_mid the midpoint of the pi bounds, sum 80 Taylor
terms (remainder <= 7^81/81! < 2^-160; angle error < 2^-89; sin and cos are 1-Lipschitz); round
to denominator 2^24. This is a fixed finite computation, an absolute constant, not advice.

For x in [0,1) put tab_0(x) = Cos[floor(4096x)], tab_1(x) = Sin[floor(4096x)], and let
cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                        (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k for latent k, beside arbitrary spectators. Let Qcap be the
source cap of Section 13. Parameters: J_e = n + 4, h_e = ceil(log2(Qcap (n+5))) + 12,
F = 2^21 h_e.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k. A TEST AT LEVEL j
prepares an ancilla in |+>, applies Tr_((N - 2^j) mod N) controlled by it, so that the |1> branch
gets eigenvalue omega^(k 2^j), and measures the ancilla in X (H then Z) or Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi 2^j k/N) or sin(2 pi 2^j k/N). Conditioned on k, chi_k and every
spectator are unchanged and outcomes are independent. Each test costs O(n) core steps.

For each j = 0..J_e take F tests per basis, giving empirical means x_j and y_j.

Decoding a level. Pick the least dr in [0,64) maximizing x_j Cos[64 dr] + y_j Sin[64 dr]. If both
means are within 1/1024 of their expectations, each computed dot product differs from
cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256. The nearest direction has true dot
>= cos(pi/64) >= 511/512. Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
The gap 15/512 exceeds 2/256, so alpha_j = dr/64 is within circular distance 1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be whichever of g_(j+1)/2
and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j (ties: the first). If g_(j+1) is within
e < 1/16 of 2^(j+1) k/N, the correct preimage is within e/2 of 2^j k/N, hence within
1/16 + e/2 < 3/32 of alpha_j, while the other is more than 13/32 from alpha_j. So the choice is
correct and the error halves. Finally g_0 is within 2^-(n+8) < 1/(2N) of k/N, and LE outputs
floor(N g_0 + 1/2) mod N = k. On any input LE returns a value in [0,N) after its fixed number of
tests, and then resets the data register. It uses no Fourier transform, no lookup, and no rotation
other than H and S.

Concentration. For F independent +-1 variables the centered log-moment generating function has
second derivative at most 1 and vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and F = 2^21 h_e this is
2 exp(-h_e). So LE errs with probability at most 4(n+5) e^(-h_e), uniformly in k and in the adaptive
schedule. Over at most Qcap calls, the probability that ANY call returns a wrong label is at most

    4 (n+5) Qcap 2^(-h_e) <= 2^-10.                                                (5.1)

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(log2n) (Section 14),
this is O(n^2 log2n) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. Execute this same NONPOWER-ROBUST16 algorithm but replace each LE
output by its latent labelk. Actual and ideal runs can be coupled until
the first incorrect label, whose probability is at most2^-10 by(5.1).
There are no additional ancilla-preparation trials. Every resource bound
is for actual branches, using fixed caps and allocations.

## 6. Phase vectors and the explicitly charged non-power merge

A nonroot vector at level i has lambda_i qubits and EXACTLY M_i
supported basis indices, with equal ideal magnitudes1/sqrt(M_i). Its
known logical label table is stored as one common low prefix and
ABSOLUTE high parts, not as a materialized full-label array or a gauge
subtracting entry0. Entries retain distinct0/1 source-incidence vectors.
The complete leaf-range instrument, two-pass radix selected-residue join,
rank and arbitrary-integer division maps, measured complete-block rule,
linear selected inverse interval, full padded-address behavior and charge
ledger are nonpower_merge.md A..C. They are part of this SAME algorithm.
They explicitly specify Toffoli/XOR lookup circuits, reversible arithmetic,
all measurements and resets. There is no A*B pair array, q-residue array,
quantum-addressed memory or free non-power uniform-state preparation.
The exact fixed-table failure formula is its B.1. Its D..F prove the
conditional bucket moments, dyadic margins, root retention and renewal
bound including within-trial cost/success correlations. No prior verdict
is used as a substitute for any of those reproduced proofs.

## 7. Direct phase-qubit supplier and quantum allocation

NEXT(0) simply requests the next accepted phase qubit from the batch
supplier. There are no other NEXT levels, slots, READY or PENDING queues.
The source and Section5 establish that, conditional on latent labels and
past outcomes, every delivered qubit is the two-entry phase vector(0,k)
in tensor product with all other live registers, on a fresh source-leaf set.
The supplier's acquisition counter includes rejected labels and failed tests.
All source/data scratch is reused. Each supplied control qubit is transferred
into a free location in the current leaf index register by counted SWAPs.

Use a fixed array of O(n) quantum working wires: two stacked tree-index
registers per level, global O(n) modular/LE scratch, O(n) merge lookup
scratch, and K=O((log n)²) root qubits. Section14 gives its uniform size bound.
A classically addressed free-handle stack or equivalent known recursive
wire layout permits reuse with O(n)-bit bookkeeping per allocation, within
the charged ledger. No exponential register bank is allocated. Classical
tables are looked up by the explicit Section6 scan circuits, not QRAM.

## 8. Exact logarithmic depth and tapered capacity

### 8.0 RLOG(n): an explicit rational lower approximation

Put j=floor(log2n),u=ceil(log2n),t=2u+10, and
z=(n-2^j)/(n+2^j), so0<=z<1/3. Define exact rationals

    A(x)=2 sum_(v=0)^(t-1) x^(2v+1)/(2v+1),
    delta=3^(-2t),
    RLOG(n)=j+A(z)/(A(1/3)+delta).

For0<=x<=1/3, the power-series identity
ln((1+x)/(1-x))=2sum_(v>=0)x^(2v+1)/(2v+1)
follows by integrating the uniformly convergent geometric series on
[0,1/3]. The omitted tail is at most
2x^(2t+1)/((2t+1)(1-x²))<=3^(-2t)=delta.
Thus Az<=ln(n/2^j)<=Az+delta and A2<=ln2<=A2+delta,
where Az=A(z),A2=A(1/3)>=2/3. Also Az<=ln2<1. Consequently

    j+Az/(A2+delta)<=log2n<=j+(Az+delta)/A2,
    0<=log2n-RLOG(n)<=4delta<=1/n².                  (8.0)

The last inequality uses delta<=2^(-2t)<=2^(-4u-20)<=2^-20/n^4.
All powers, sums and quotients here are rational and computed exactly.
There are O(log n) terms with O((log n)²)-bit common denominators;
ordinary schoolbook rational arithmetic costs poly(log n) core steps
and poly(log n) classical bits. That memory is O(n) and the work is
polynomial in n, with absolute constants. No real-number or logarithm
oracle is supplied. In the main range1<=ell=RLOG(n)<=log2n.

For n>=2^128 let l=log2n in analysis,ell=RLOG(n),m=ceil(16ell),
u=ceil(log2n),base=ceil(n/(m+1)-m/2)+2,dl=base,H=base+m-1.
Set lambda_i=base+i,delta_i=2^(i-m-2),
M_i=2^lambda_i-2^(lambda_i+i-m-2) for0<=i<m,lambda_m=d,M_m=2^d.
Exact RLOG arithmetic gives16l-1<m<=16l+1,m+1>16l,m>=10u+100.
With t=n/(16l), endpoint/exponential comparisons at128 give
 base>=t/(1+2/(16l))-(16l+1)/2+2>=t/2,
 base<=t-(16l-1)/2+3<=t,H<=2t,(m+1)H<=4n,m<=n/4,
 base>=16m+64u,base>=3m+100u,gw+1<=base.
Indeed2^l/l² grows and is enormous at128; u<=l+1. All dyadic
length exponents are nonnegative integers. Each nonroot register has
lambda_i qubits with exact supportM_i, at least7/8 its padded dimension.
Also lambda_i=H-k,k=m-1-i. No nonroot kappa or plateau is run.

Choose nonroot windows b_i<=base+i-2=2lambda_(i-1)-lambda_i
and final window b_m<=2H-d-2. Their total maximum is
 (m+1)base+m(m-1)/2-d-2>=n+m-d.                  (8.2)
Every maximum is positive. Greedily allocate exactly requiredB root-down
within these maxima, so every residue read ends belowB. The complete
nonroot probability proof is nonpower_mergeD..F, conditional on exposed
LOW bits rather than full high tables; only the final root uses a2-bit
margin with a fixed-table failure bound. No old pointwise2^-kappa law
or independent ghost-retry domination is asserted.

For coarse roots use output width d=1. For each ACTUAL data block b,
put noise=ceil(log2(n^5)), r=b+noise, d=r. The total capacity in8.2 is at leastn+m-r; requiredB<=n-b,
so the large b cancels and slackm-noise>=0 remains. Root maximum
2H-r-2 stays positive because r<=H and H>2. All nonroot/root
moments, retention and renewal statements apply to these exact dimensions.
Coarse and low-only verification final roots use d1. The low-only kernel
uses stored source labels Lmod2^B; these have independent uniform bits
withinB in the clean reference, so the new current-window moment proof
applies to them. It need not store physical labels aboveB.

Put Cc=64dl2^m,Cf=16dl2^m,Y=ceil(log2Cc),E=8u,
htop=Y+E+12,P=htop+Y+8,Kc=36864u,w=64u,
b0=floor(H/2)-1024u,Lblk=ceil(n/b0),noise=ceil(log2(n^5)).
All these integers are computed before acquisitions; each data block's
r=b+noise is computed from its known block length. Integer bit_length
computes noise, so no real logarithm is used operationally.
robust_decoder.md I proves b0>=n/(35u)>0, Lblk<=36u,
noise<=5u, r<=H, m+gw+b0<=H, and htop<=27u with
m+gw+htop<=H. Thus all ordinary high fields satisfy the same tapered
memory lemma. The odd actual block b is at most Jtarget<floor(log2M),
so B=dn-b>=a2+1 even if b0 itself exceeds log2M. No supplier with
an invalid precision is requested. Y need not exceed b0; no proof uses
that old logarithmic-block inequality. LARGE coarse and fine suppliers
still use their separate physical transforms and error bounds.

## 9. BATCH(supplier, B, R, h=1)

This section specifies ordinary coarse/data roots; the low-only
verification variant with capCf is fully specified in robust_decoder.md A.
Input: a supplier of leaf qubits with known labels,whose ideal accepted
values are independent uniform[0,2^(B+h)),1<=h,1<=B,B+h<=n.
Wide coarse roots useh<=htop; data roots useh<=b0. The new wide-field
lemma robust_decoder.md I provesm+gw+h<=H forcoarse roots.
VROOT(supplier,B,h,d) builds ONE root of outputwidthd in{1,r}.
SetCroot=Cc for coarse andCroot=Cf for data.
For data use r=b+noise determined by this actual block, never a global r. Allocate
nonroot lambda_i as8,lambda_m=d,and budgets under the changed root
capacity. Start with all quantum workzero. Count selected source calls;
if callCroot+1 would be needed,stop,reset all work and returnmissing.
Rejected suppliers and failed merges count. Completion returns the
root index and its high-part table; it is immediately decoded/measured,
then ALL work is reset before any new root call. No earlier source or
quantum root persists between calls. Source parameters are fixed within
a root. The controller makes one proposal attempt at a time; missing
produces a hold,as robust_decoder.md D specifies.

The ONE COARSE batch F callsVROOT with its computedh,d=1,R=Kc.
A completed root is immediately measured in a fresh fairX/Y basis,
recording(W,beta,Z); a missing root contributes scorezero. Reset all
quantum work between roots. Stage parameters stay fixed until allR
classical records exist,then scores and the centre are updated.
For cost bounds only putD_R=C_R=R*Cc; there is no separate demand guard.
Fine vector attempts and direct final blocks are specified in11/12/13.

Each nonroot frame has actual M_i rows (or a constant-factor2^lambda_i
padded allocation) and lambda_i qubits. The root has2^d rows. The
canonical footprint at level i is still <=dl2^i fresh delivered source
coordinates. Failed and discarded construction copies are counted in
Croot but do not enlarge a successful entry's0/1 incidence vector.

VEC(0) is nonpower_mergeA's REAL measured leaf projection: acquire dl
accepted phase qubits, measure index<M0, retry fresh on false, respecting
the selected-source cap at every call. Its known absolute labels are the
tensor subset sums on surviving indices. VEC(i),1<=i<=m, repeatedly
builds TWO fresh VEC(i-1) inputs and runs nonpower_mergeB at precision
tp_(i-1), window b_i, output length M_i (nonroot) or2^d (final root).
FAIL resets BOTH inputs and scratch before fresh retries. Root completion
returns exactly d qubits and a2^d-row high table. All retries stop before
callCroot+1, and the whole root is measured/reset before the next call.
There is no retained quantum source pool or unbounded actual execution.

Field widths. Put D_src=B+h and g_w=ceil(log2dl). A level-i logical
label is a sum of at most dl2^i source labels below2^D_src, by disjoint
canonical footprints. It is below2^(D_src+i+g_w). Thus store its high parts
in exactly

    w_i=D_src+i+g_w-tp_i >=1

bits per row, and one tp_i-bit common prefix. These dimensions are fixed
before acquisitions. At a merge w_(i+1)=w_i+1-b_i, so the w_i+1-bit
sum sv fits and its right shift fits the output field without truncation.
The same integer bound holds on actual wrong-label branches: accepted
stored source values still lie in[0,2^D_src), and the logical sum invariant
is maintained exactly. No high-value overflow check or abort is needed.

Root. At p=B store common prefixc and highpartshi[a] for0<=a<2^d.
PutW_a=hi[a]-hi[0],soW_0=0. The ideal state,up to global phase,is

    2^(-d/2) sum_a exp(2pi i 2^B W_a th)|a>.       (9.1)

For d=1 coarse notationW meansW_1. Each label sums at mostdl2^m accepted values below2^(B+h). Each actual
root uses at mostCroot<=Cc source calls. Consequently

    |W_a|<=2^h Croot<=2^h Cc<=2^(Y+h).                        (9.2)

Since2^(m+g_w)<2dl2^m<=Cc,m+g_w<=Y. All high fields obey
w_i<=D_src+m+g_w<=n+Y<=3n; wrong-label branches obey these dimensions
because accepted stored labels still belong to the same finite ranges.
The common prefix cancels in every W_a. No full logical label table is
reconstructed. For a fine root its EXACT2^r rows are explicitly stored,
2^r<2^(b+1)n^5; no polynomial-size-root claim is made.

Ordinary coarse decoding useswideh<=htop; data decoding usesh=b<=b0.
Verification h=j may be larger and uses the distinct low-only kernel
of robust_decoder.md A; its width proof replaces the known-label bound.

Lemma9.1 (new clean-reference capped-root law). Nonpower_mergeD..F
proves expected uncapped selected cost<6dl2^m, with actual leaf-range
failures, all nonroot retries and the final full-power root charged.
Its fresh-trial renewal permits within-trial cost/success correlation.
Markov under ACTUAL caps Cc64dl2^m,Cf16dl2^m gives coarse missing
<=3/32 and fine/verification missing<=3/8, uniformly given any fixed
clean ideal preceding history. Structural decisions/caps read only
exposed low labels, hence completion preserves proof10's unused-top law.
This is a clean reference-root theorem, not conditioning actual roots
on adaptive corruption flags. Actual branches terminate at their caps.
For the low-only verifier, apply exactly the same theorem to uniform
stored source Lmod2^B, with window endpoints<=B and final output2.
All index-range, rank/division and FAIL maps depend only on stored L,
so physicalK/storedL induction in robustA is preserved. No full physical
high labels or fictitious positive-robustness theorem is required.

## 10. Unused-top-block independence and score discrimination

ForBATCH(B,R,h),write each accepted labelk_v=low_v+2^B tau_v,
0<=low_v<2^B,tau_v uniform inZ/2^h. LetG include all low_v,all merge
outcomes(e,bl),FAIL/retry/root-cap/qubit assignments and controller selection
history,but exclude root measurements,their fresh basis coins,unusedtau_v,
and LE internal coins/outcomes,which feed no ideal selection decision.
It is a coarse sigma-field,not the full computer record. Rejected source
history is independent of the subsequent uniform accepted value; every
fixed preceding rejected sequence has equal probability before each value
in its accepted interval. Direct modular suppliers are already uniform.

Every residue,sort,rank and block partition inspects only logical positions
belowB. Bits belowB of a sum depend only onlow_v. Stored prefixes and
exposed residue windows end belowB. Lemma6.1 makes the conditional law
of merge outcomes a function of these low bits and earlier outcomes only.
Induction factorizes the joint law as

    law(tau) law(low) law(outcomes,controller | low).

Thus within a clean reference root,conditional on its G,thetau_v remain
independent uniformZ/2^h. A table entry is the sum of leaves with a0/1
incidence vector. Distinct indices have distinct vectors: it holds for a
leaf(0,k_v),LEAF concatenates disjoint coordinates,and MERGE injectively
reindexes pairs on disjoint coordinates. The two root entries therefore
have different incidence vectors,so

    W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,       (10.1)

with disjointG-measurable sets,nonempty union,and integralG-measurablecst.
Every nonzero coefficient is+1 or-1. Holding all but one suchtau fixed
proves W mod2^h is uniform. Clean reference roots use disjoint fresh sources and have identical marginal laws for fixed stage parameters. Completion reads onlyG and preserves these unused-top-bit identities. Forh=1 this also gives

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd<=|cos(pi phi)|,
    Pr(W odd |G)=1/2,                              (10.2),(10.3)

wherehd=|Sp|+|Sm|>=1,as used by the unchanged coarse bootstrap.

Fine-vector lemma. For a completed root with d=r,putq=2^b,h=b.
For any distinct output indicesa,c,their incidence-vector difference is
nonzero and has a coefficient+1 or-1 on some unused top labeltau_v.
ThereforeW_a-W_c is uniform moduloq conditional on the complete
structural transcriptG. No independence of the full frequency vector is
asserted. qudit_decoder.md constructs a finite Clifford+T measurement
for the known vector(W_a),oddJ and phasevector

    2^(-r/2) sum_a exp(2pi i J W_a v/q+i eta_a)|a>,
    |eta_a|<=1/(16n^4).

It outputs the truev with error at most2/n^4 averaged over the conditional
unused top bits,for EVERYv andG,including all gate-synthesis error. This
law holds conditional completion because caps/retry read onlyG.

For the final two-adic B=0 proposal use the explicit r-direct-qubit
product-vector measurement in robust_decoder.md C. Prefix verification
uses its low-only one-qubit kernel or direct final X record. No Kp-score
final block is used by this candidate.

## 11. Odd coarse recovery and fine physical identity

Run robust_decoder.md F's ONE wide-top coarse batch,with its fixed
parameters htop=Y+E+12,P=htop+Y+8,Kc=36864u.
M=1 skips; SMALL odd components return exacts1; LARGE components
producechat,R0 and proceed to the explicit signed-prefix controller B/D.
All supplier/gate/characteristic/grid/missing/edit/concentration details
are in F and are part of this proof. The legacy staged bootstrap is not
run. Both branches count all source acquisitions and reset roots.

Fine data identity. For a current prefixlow of j bits and a next block
of b bits put B=dn-b,gamma=2^(B-a2) modM,K0=(-2^b)^(-1) modM,
J=(2^b K0+1)/M. Compute the CRT unit alpha=1 mod2^a2 and
gamma*alpha=K0*2^(-j) modM. On each selected copy apply
Shift_(chat+low modM),Mult_alpha,LE,accept iff k<2^dn,then X.
An ordinary known-label r-qubit root has relative phase

 exp(2pi i K0 W_a t_j/M)
 =exp(2pi i J W_a t_j/2^b) exp(-2pi i W_a t_j/(2^b M)), (11.2)

where t_j=(t0-low)/2^j is integral on correct past. The physical
2-adic component cancels becauseB>=a2. On correct past |t_j|<=R0
by signed quotient induction. With |W_a|<=2^b Cf the error phase is
below2^-E<1/(16n^4). Thus the explicit qudit decoder is wrong with
probability<=2/n^4 conditional completion. This is ONE data proposal;
it is not retried until completion. The target bit count,verification,
backtracking,missing decisions,guards and final signed recovery are
EXACTLY robust_decoder.md B,D. In particular arbitrary prefixes are
verified by its distinct low-only kernel and uniform phase estimate.

## 12. Two-adic physical data identity and controller

After correct s1,write s=s1+M*s2 moduloN. For candidate prefixlow of
j bits,Shift_(s1+M*low) and LE produce uniform k moduloN and phase
exp(2pi i k(s2-low)/2^a2) after the standard X convention. For a
correct prefix let wd=a2-j,kk=k mod2^wd. This is uniform,with phase
exp(2pi i kk*remaining/2^wd). Withb=min(b0,wd),B=wd-b>=1,
the ordinary r-qubit root has phase2pi W*remaining/2^b,so the known
qudit decoder has error<=2/n^4 conditional completion. WhenB=0
robust_decoder.md C instead acquires r DIRECT qubits and their explicit
product vector. Its pairwise-uniform subset labels give the same decoder
bound. Verification for every prefix,including j=a2,uses the distinct
low-only X kernel or direct X record in C. The actual guarded controller
is D. It also fixes all wrong-prefix branches and their resource caps.

## 13. Actual complete algorithm and reference-core error budget

Finite branch(n<2^128). Putk=n+10,Qcap=N*k,Qbank=1024*Qcap. Prefetch and
shuffle as18. For EVERY candidatec=0..N-1,use its predetermined block ofk
consecutive bank slots,applyShift_c,measure the control inX,and record
whether all outcomes wereplus. Test every block in full; no early stop,
skipped candidate or adaptively shifted block boundary is used. Output the
first candidate whose block was allplus,or0 ifnone. Unused bank slots are
reset/released without conditioning the output on their measurements.
Section18 proves robustness of this branch uniformly,not a clean-only premise.

Main branch(n>=2^128). Compute all exact parameters fromN first,
includingw=64u,htop=Y+E+12,P=htop+Y+8,
Kc=36864u,I=16Lblk+128(w+u),Hchain=8w+64u,
 Qcap=Cc*Kc+Cf*10I,Qbank=1024Qcap.
Size LE confidence byQcap. Run the ONE wide coarse batch of
robust_decoder.md F,then its exact D controller: four checks+one data
proposal on ordinary fixed-prefix batches,four checks per full-candidate
chain link,accept atHchain and at mostI iterations per component.
SMALL odd components return exacts1 and skip that controller. There is
no staged bootstrap or unbounded retry. Every record resets ALL quantum
work. All source rejects,failed/missing roots,guard aborts and padding
count. Its E..I prove unconditional adaptive success,full resource caps
and the new wide-field storage lemma. Actual code sees no truth or flags.

## 14. Resource bounds on every branch

Every root and enumeration loop is capped. Letl=log2n. Parameters
m,Y,E,P,htop=Theta(l),Kc=Theta(w),dl,H=Theta(n/l),Cc,Cf=Theta((n/l)2^m).
ONE coarse batchO(u),ordinary/chain rootsO(u) and all guards jointly
fitO(u) by robust_decoder.md I. Therefore

    consumed_slots<=Qcap=O(n2^m).             (14.0)

This includes rejected copies and every capped/failed/retried construction.

Quantum workspace. At mosttwo retained core indices per level,each<=H,
useO(n) qubits by8.4. Leaf,source/data,modular/LE,lookup/controller scratch
andone active root addO(n),with wires reset/reused. Each MICROTAKE holds only
1024 raw(n+1)-qubit copies and10 coin qubits(also reusable). Hence the main
total peak isO(n),including EVERY microbank register and core wire.
The finite whole-bank branch is explicitly handled by uniform outer
constants in15/18; no main-only space bound is asserted there.

Classical space. Put k=m-1-i. Remaining precision satisfies
R_i=B-tp_i<= (m-i+1)H=(k+2)H since each nonroot capacity is belowH
and the root below2H. Thus actual high fields obey
w_i=R_i+h+i+g_w<=(k+3)H, usingm+g_w+h<=H forwidecoarse byrobust_decoder.md I,
andm+g_w+b0<=H fordata. For low-only verification use instead
w_i=R_i+i+g_w<=(k+3)H by robust_decoder.md A,independent of h=j.
No full physical high-label table is retained for those roots. Radix buckets, records,
ranks/orders and inverse maps need O(H) bits per row. Output length
is at most2E_i with field at mostw_i+1. The exact linear index schedule gives

    E_i=M_i<=2^lambda_i=2^H*2^(-k).

Every retained sibling, field, output and scratch frame is bounded by a
constant times

    H2^H sum_(k>=0)(k+4)2^(-k)=10H2^H.

The sum uses sum_(k>=0)2^-k=2 and sum_(k>=0)k2^-k=2. No n-dependent plateau is hidden in a constant.
Prefixes, small roots, source/LE, controller, decoder and parameter records
add O(2^(2b)n^128) decoder space and polynomial controller space,
absorbed by H2^H since2b<=H-2048u. Hence S_C=O(H2^H), without
any storage or lookup oracle.

Work. A leaf TRIAL costs O(n2^dl) core steps and consumesdl delivered qubits; a failed range projection resets and retries
with fresh counted qubits.
At heighti a merge attempt consumes2^(i+1)dl canonical delivered qubits
not reused by another attempt there and costs O(n2^(dl+i+1)). A partial
leaf at abort is charged fully. Each root costs O(nCroot2^dl(m+1)/dl); coarseRroots sum their
root caps. Here(m+1)/dl=O(l²/n). Summing14.0 gives
O(n*l²*2^(m+dl)) core tree steps; address width O(H+logn)=O(n/l)
gives the complete tree bound

    T_tree=O(n²*l*2^(m+dl)).                          (14.1)

Confidence has logQcap=O(l). Source/extraction costs O(n²l) core per
acquisition,and all charged source/extraction work is O(n^5 2^m).
The wide coarse grid is streamed over at most2^P<=2^45n^45 candidates,
withKc=O(n) records ofO(logn) bits. Its addressed fixed polynomial work,
including exact integer score arithmetic,is explicitly bounded and
absorbed byT_tree in robust_decoder.md I. Fine vector measurements,verification,backtracking,CRT/signed updates,gates,resets,
parameter computation and source charges(n+1)Q count as well. All
polynomial terms with exponentm are absorbed by14.1 since dl=Theta(n/l)
grows faster than log n. Initializing all compressed frames overO(u) root calls
costs O(u*H²2^H), bounded by14.1 usingH<=2n/(16l),H=m+dl-1.
Thus14.1 counts every branch, even after earlier errors.

The explicit large-vector tables and circuits in qudit_decoder.md cost
O(2^(2b)n^128) work/bits and O(b+r)=O(n) qubits per data attempt.
There are O(u) such attempts. Since2b<=H-2048u, their total is
O(2^H/n^1900), absorbed by14.1 and H2^H. This includes the
new explicit finite-precision compiler analysis, table preprocessing,
all actual lookups and execution, on arbitrary input states. It is not
an uncharged polynomial decoder or a subset-sum/rotation oracle.

Wrapper overhead. Actual fresh acquisitions equal1024Qcap=O(n^17).
Acquisition,selection,routing,reset and padding useO(nQcap) additional core
steps up to fixed factors,and polynomial classical bookkeeping. Address
width isO(H+logQcap)=O(n/l),so all this charged polynomial work is absorbed
by n^10*l*2^F64(n); classical wrapper records are absorbed by the declared
exponential classical envelope. Idle core wires are counted throughout
prefetch. Uniform selection uses exactly10 bits,no rejection loop.
All branch bounds hold even after bad states or incorrect labels destroy
the probabilistic reference-core statements. No source/bank operation is free.

## 15. Exact reciprocal-series envelopes

Letl=log2n,x=16l,x0=2048,r0=2048/2049. Define the EXACT exponent

 F64(n)=n[sum_(j=1)^63 (-1)^(j-1)/(16^j l^j)
                 -(2048/2049)/(16^64 l^64)].        (15.0)

These64 monomials,not merely the leading one,are the two structured
exponent lists. No real-valued parameter oracle is used;F64 is an analysis
expression,the actual protocol still uses RLOG's finite rational arithmetic.
RLOG>=l-1/n² andm=ceil(16RLOG) imply m>=16l-16/n². Putdelta=16/n²<1.
Since m+1>=x+1-delta andboth denominators below are at leastx,

 n/(m+1)<=n/(x+1)+n*delta/[(x+1-delta)(x+1)]
           <=n/(x+1)+16/(n*x²)<=n/(x+1)+1.        (15.1)

The finite geometric identity is

 1/(x+1)=sum_(j=1)^63(-1)^(j-1)/x^j
                    -1/[x^63(x+1)].

Forx>=x0, x/(x+1)>=r0. HenceF64>=n/(x+1),so15.1 gives
n/(m+1)<=F64+1. This is a uniform inequality,including all rounding;
no asymptotic truncation or fitted coefficient is used. Moreover
F64>=n/(x+1)>=n/(2x),andF64<n/x forx>=x0: pair the alternating terms
starting with -1/x²,leaving negative pairs and the negative final term.
Thus remaining polynomial costs in14 are still absorbed by its tree bound.

Use H<=n/(m+1)+m/2+2,m<=16l+1. We obtain

 H<=F64+8l+4,
 m+dl=H+1<=F64+8l+5.                (15.2)

Insert into T_tree=O(n²*l*2^(m+dl)) and S_C=O(H2^H),withH=O(n/l).
The additional constants only change absolute outer factors. All64 exact
terms therefore occur in the complete uniform envelopes

 T=O(n^10 l 2^F64(n)),S_C=O((n^9/l)2^F64(n)),
 S_Q=O(n),Q=O(n^17).

The leading monomialF64 is n/(16log2n)>0 and the others are successively
smaller powers of1/log2n. Therefore time/classical indices remain1;
copy andquantum indices0. The negative n/(256l²) correction is retained,
along with every later coefficient displayed in15.0. Finite n<2^128
changes only absolute outside resource constants; its success is separate.
At n=1 resource logarithms usepositive n=2 values,not a division byzero.

For clarity,the finite branch quantum allocation is at most
1024N(n+10)(n+1)+O(n) circuit scratch. With fixedC0=2^128 andn<C0,
this is bounded by a fixed absolute constant timesn,for example by
C_f*n with C_f=2^20*2^C0*(C0+100)^2. The same finite-range argument
covers its work,copies and classical storage. This constant can be enormous;
the theorem is an asymptotic uniform bound,not a practical-space claim.
The finite SUCCESS guarantee still requires and receives its separate
positive-fraction proof in18; it is not absorbed into an outer constant.

## 16. Guaranteed malformed fraction

The exact supported fraction islog2n/(238263n^17),with natural value0
atn1. All-N unconditional full-secret success>=2/3 and all four bounds
are proved jointly by robust_decoder.md E..I and18. On the MAIN branch
n>=2^128 ONLY,the raw allowance is at least144log2n,unbounded (integer allowance >=floor(144log2n)).
This auxiliary count is not a replacement fractional score.

## 17. Scope

This is a joint upper-bound construction with explicit parameters,
charged circuits/tables,and an adaptive fractional robustness proof.
It makes no lower-bound,optimality or impossibility assertion. The
low-only verification and backtracking lemmas are fully reproduced in
robust_decoder.md; no inherited acceptance is used as proof.

## 18. Adaptive record comparison and finite-bank proof

Finite-bank lemma. In the finite branch,before the last delivery the algorithm makes no
measurement,private draw,source transform or abort decision. Record each
adversary clean/malformed decision in an analytical hidden classical
register. Inductively,conditional on the decision trajectory,the delivered
operator factors as a tensor product ofrho_s on its clean slots with a
positive operator on all malformed slots and the adversary system.
A private adversary instrument acts only on the latter; a malformed
delivery transfers part of that operator,and a clean delivery appends a
fresh productrho_s by the model. Countably many private outcomes preserve
this form upon summation. After acquisition,trace out the adversary and
condition on the flags: the input is a mixture over fixedBad sets with
|Bad|<=floor(epsilon Qbank),independent ideal factors on all other slots,
and an arbitrary joint malformed state. Prove bounds for each such component
and integrate. This reproduces the cited bank-first argument; it assumes
no independence among malformed copies. Later local processing of the
adversary cannot signal into the algorithm or change its marginal output.

Finite shuffle. Setz=ceil(log2Qbank),ell_s=2z+u+100. Fori=Qbank-1 down1,
generate exactlyell_s fresh fairH-measurement bits after acquisition,
form integerR,putj=R mod(i+1),and swap whole bank registersi,j.
Modulo uses finite ordinary bit arithmetic. Each swap costs3(n+1) CNOTs;
all addressed gates,coin gates/measurements,resets and integer operations
are charged. No rejection loop or quantum memory oracle is supplied.
For anm-element range,the modulo distribution of a uniformell_s-bit
integer is within TV m/2^ell_s of uniform. Couple each step to an ideal
uniform Fisher-Yates step; the total permutation TV is at most

    delta<=Qbank²/2^ell_s<=2^(-u-100).

The ideal order is uniform independent of the bank. Every subsequent
quantum/classical computation contracts this classical TV distance,so
delta is added ONCE to any total failure event. The new coins are drawn
only after all copies arrive; they cannot affect any adversarial source
decision. No later fresh acquisition occurs. Only the finite branch uses this whole-bank shuffle; all its dimensions
are finite with charged outside constants. The main branch instead uses
exact10-bit microbank selection. Every loop has a fixed finite bound.

Main adaptive argument. robust_decoder.md E gives the post-delivery
bank expectation and iterated positive-classical-submeasure coupling
including AFTER prior malformed selections. F gives a new Dirichlet
wide-grid coarse proof; G/H prove the bounded chain progress/wrongaccept
potentials. Its I proves
 Qcap<=476526n^17,epsilon=l/(238263n^17),E C<=w/32,
 Pr(C>w)<=1/32,totalfailure<=1/32+2^-10+3*2^-20<1/3.
All expectations use the unconditional all-flag taint count; final edit
implications restrict to NOLEerror andC<=w without conditioning virtual
laws. Its wide-field/low-only lemmas prove the unchanged full classical
envelope. Main raw allowance is at least144log2n (integer allowance >=floor(144log2n)). No prior verdict is
a mathematical premise.

Finite branch. Putk=n+10. A fixed candidate block under the ideal shuffle
is a sizek sample without replacement from the fixedBad set. LetI_j mark
bad positions andB_c=sum I_j. For every chosenh positions,
Pr(allh bad)=(|Bad|)_h/(Qbank)_h<=(|Bad|/Qbank)^h<=epsilon^h.
Expanding product(1+I_j) gives

    E2^B_c<=sum_h binom(k,h)epsilon^h=(1+epsilon)^k.

Forc!=s,a clean shifted copy has unbiased X control because its two data
branches are orthogonal. Conditional on the bad pattern,clean copies
factor independently and arbitrary entangled malformed-copy measurement
effects are bounded by the identity. The probability allk outcomes are
plus is therefore at most2^(-(k-B_c)),without assuming independent bad
outcomes. Union overN candidates givesfalse acceptance probability
<=N2^-k(1+epsilon)^k<=2^-10 exp(epsilon k)<=2^-9.
Forc=s every clean test isplus,so rejection of the true candidate requires
at leastone bad copy in its fixed block,with probability<=epsilon k.
Atn>=2,uselog2n<=n,k<=6n to getepsilon k<=6/(238263 n^15)<2^-30.
Atn=1 the logarithmic fraction is0. Thus uniformly exp(epsilon k)<2. Adddelta once: finite total
failure<=2^-9+2^-30+2^-100<1/100. Testing EVERY fixed block in full
is essential to this argument; no adaptive early-stop layout is used.
All finite bank/copy/workspace costs are bounded by absolute outer
constants over the fixed finite integer range,as stated in0 and15.

The two branches prove the uniform positive fraction and all resource
claims for everyN and secret and every adversary of0.
