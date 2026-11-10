# PCT25: phase-compressed threshold search under a joint clean marginal

One uniform physical algorithm for every N>=2 and s in Z/NZ, n=ceil(log2N),
has unconditional full-secret success at least95/128 and simultaneous bounds
on EVERY branch:

    T=O(2^((1/2)n)n^2(log2n)^2), SC=O(n^2), SQ=O(n), Q=2^16(n+16).

Logarithmic envelopes concern n>=2; N=2 has its explicit finite branch. The
malformed fraction is epsilon(n)=1/4 under Section1's exact fixed-set joint
marginal promise, including clean inputs. Exact resource growth indices are
1,0,0,0. The coefficient1/2 multiplies n, not sqrt(n). This is a compressed
robust threshold construction, not a polynomial-time or cube-root DCP claim.

## 0. Material sources and selected algorithm

This proof is self-contained. The actual design/proof uses four contributions:

* RWT25-STREAM, 405da11f-af21-4670-a65a-8a97d84c1f05: threshold-projector search,
  mixed-witness telescoping, integer iteration rule, and persistent public gate
  descriptors. Its complete RWT25 source credits kaankolcu's
  3f48c893-2d1b-4e9b-ac9e-e9d318149910. Here the source count/threshold change,
  the raw bank is NOT retained, and BOTH true and false overlaps need bounds.
* LLV-GRF320-DENSE, 48524b61-1c0c-4821-99f2-b46e732c285a: its complete virtual
  proof Sections3-5 supplies Fourier-mixture identities, exact modular
  translations, fixed trigonometric directions and label unwrapping. Here
  extraction parameters are newly chosen and independently bounded per copy.
  No GRF tree, source budget or strict sieve margin is executed.
* f0bfcbc9-ef55-4754-b61e-061100ace74f: phase appendix Sections3 and6 supplies
  the exact prefix/window map and its uniform circular error through wraparound.
  That source credits 493303b5-06f6-4ee0-9596-d8cae89c8bb4 for the prefix/cache
  idea. Here prefixes are ordinary CLASSICAL data; the phase map is used to
  rotate a retained row, not a cubic score/tournament or saved pivot cache.
* f3de6f8e-db2d-4c45-b8dc-16f6ed7bd972: model appendix Sections1-3 supplies
  passive sequential delivery under the same joint marginal and the full local
  compression-channel argument with arbitrary reference. Its actual selected
  filter, gradient, one-third score and endpoint are not imported.

These are actual material sources, including earlier work by this account
where applicable; no independence is inferred from restatement or an indirect
path. No separately used ancestor feature outside those selected sources is
omitted. Historical credits are retained. Prior review is not a proof premise.

## 1. Input promise, passive delivery and complete fixed schedule

Let k=2^16(n+16), h=k/4 and a=11k/16, all integers. Exactly Q=k original
copies are delivered and counted. The structured error-model text is:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

The entire joint input is fixed before delivery. For each fixed B, write
b_bad=|B|<=h, G its complement, and R an inaccessible reference. Its sole
clean condition is Tr_(BR) sigma=rho_s^(tensor |G|). Arbitrary extensions and
convex mixtures over such fixed B are allowed. The algorithm does not know B.
The inaccessible source holds unread registers passively and releases them in
fixed order, with no measurement, replacement, feedback or later action.
This is an implementation of the fixed joint-state promise, not an assumption
that conditional unread good registers remain ideal after earlier outcomes.
The rules exclude state held by the inaccessible source. Every acquired row,
current data register, classical record, probe, scratch and address is counted.
Each delivery still costs n+1 source work units.

At N=2: acquire all k copies in order; on each perform the baseline t=0
controlled shift test and measure its first qubit in X. Discard/reset its
register after recording its plus bit into a running counter. Output0 iff
at least a plus results occurred, otherwise1. No early source stopping.

At N>=3, the complete schedule is:
1. Acquire each of k copies, apply Section2's local label instrument, retain
   only its row qubit and classical prefix record, and reset/release position
   and probe work BEFORE the next acquisition. Ignore all unused probe/reset
   outcomes after their charged processing. No new source call follows step1.
2. Set L=2^n, r=largest integer with16r^2<=9L. Prepare n candidate qubits in
   |u>=L^-1/2 sum_(t<L)|t>. Execute exactly r iterations D R from Sections4-5.
3. Measure candidate t; output t if t<N, otherwise0. Reset/release all quantum
   work and clear every classical record. No verification, restart or postselection.

## 2. Exact local Fourier-label channel with counted extraction

Let omega=exp(2pi i/N), chi_k=N^-1/2 sum_(y<N)omega^(ky)|y>, and
phi_k^-=(|0>+omega^(-ks)|1>)/sqrt2. Direct expansion of the coset mixture
and orthogonality of characters gives

    rho_s=(1/N) sum_(k<N) |phi_k^-><phi_k^-| tensor |chi_k><chi_k|.       (2.1)

First measure data validity y<N by a reversible comparison, measurement of
its flag and uncomputation, so valid/padding cross blocks are removed. On
padding set the classical decoded label ell=0, reset/release data, and apply
X to the retained row. No claim is needed about its arbitrary state.

On valid data, translation Tr_c:y->y+c modN has eigenvalue omega^(-kc) on
chi_k. Extend every translation by identity on padding. It is an exact
O(n)-gate reversible modular permutation: constant ripple comparisons,
addition/selection, compute to clean output, swap, inverse compute to clear
old input; O(n) scratch. Controlled versions use constant extra controls and
exact Toffoli decompositions. No Fourier transform or source inverse is used.

Choose J_e=n+4, h_e=ceil(log2(8192(n+5))) and F=2^21 h_e. At EACH j=0..J_e
perform F X and F Y fresh-ancilla tests: prepare |+>, apply Tr_((N-2^j)modN)
under that ancilla, then measure X (H,Z) or Y (Sdag,H,Z). Conditional on k,
means are cos(2pi2^j k/N), sin(2pi2^j k/N); chi_k and the row are unchanged.
Tests are independent conditional on k. Their full Kraus operators are
spectral functions of the valid data label and identity on the row.

Generate a fixed rational table Cos[dr],Sin[dr], dr=0..63, within2^-20 of
cos(2pi dr/64),sin(2pi dr/64). A finite uniform construction bounds pi within
2^-90 by Machin's16 atan(1/5)-4 atan(1/239), using40 terms of each alternating
series; Taylor through degree80 at angles<7 has remainder<=7^81/81!<2^-170.
Use exact rational arithmetic and round to denominator2^20. All table work
and storage are counted absolute constants, not external advice.

At each j let x_j,y_j be the empirical means. Choose the least dr maximizing
x_j Cos[dr]+y_j Sin[dr], and set alpha_j=dr/64. If both empirical errors are
<=1/1024, each score differs from its exact cosine by less than1/256.
The nearest direction has cosine>=511/512; directions circularly farther
than1/16 have cosine<=31/32. The gap15/512 exceeds twice1/256, so alpha_j
is within circular distance1/16 of2^j k/N. Put g_J=alpha_J. Descend j=J-1..0,
choosing the circularly nearer to alpha_j of g_(j+1)/2 and (g_(j+1)+1)/2,
with fixed first-preimage tie breaking. The correct preimage is within
3/32 of alpha_j; the other farther than13/32. Error halves at each step.
Thus g_0 is within2^(-n-8)<1/(2N) of k/N, and ell=floor(Ng_0+1/2)modN=k.
On failure this decoder STILL returns some ell in [0,N), in fixed time.
All unwrapping and comparisons use exact O(n)-bit fractions.

For F independent +-1 variables, their centered log-mgf has second derivative
at most1, hence Pr[|mean-Emean|>delta]<=2exp(-F delta^2/2). At delta=1/1024,
F=2^21 h_e gives2exp(-h_e). Union over2(n+5) means gives

    Pr[ell!=k | k]<=4(n+5)exp(-h_e)<=4(n+5)2^-h_e<=1/2048.             (2.2)

This is uniform for every true k, not conditioned on successful decoding.
Reset/release the data and probes and apply X to the retained row. A good
row now has positive phase phi_k=(|0>+omega^(ks)|1>)/sqrt2. Store only ell
and the prefix defined in Section3, plus validity if desired.

The arbitrary-reference channel argument is essential. For a complete valid
probe transcript z its position Kraus operator is K_z=sum_k c_z(k)|chi_k><chi_k|.
Let p(ell|k)=sum_(z:decode(z)=ell)|c_z(k)|^2. After tracing/resetting position,
the retained row/reference output for ell on ANY input tau is exactly

    A_ell(tau)=sum_(k<N) p(ell|k) X_row
       [(I_rowR tensor <chi_k|) tau (I_rowR tensor |chi_k>)] X_row.      (2.3)

Partial trace kills all k!=k' terms. The invalid branch is its measured
padding block traced over position, with ell=0. Formula (2.3) tensored with
identity on any other slots is a complete local CPTP channel. It never assigns
an ideal latent phase to a bad register. Applied independently to the original
product GOOD MARGINAL, these channels leave a PRODUCT GOOD OUTPUT MARGINAL.
An arbitrary extension to bad systems and R remains arbitrary. This follows
from locality and partial trace even though conditional unread good states
may be steered during physical delivery. There is no favorable-outcome or
all-labels-correct conditioning. Hidden k is a proof refinement, not data
read by the algorithm.

## 3. Uniform phase windows and a fixed finite Clifford+T circuit

Let ell_n=ceil(log2n), b=ell_n+16, P=n+b, R0=16, and H_b=2^b. For each
classical decoded ell compute and store the classical P-bit word

    E=floor(2^P ell/N), 0<=E<2^P.

Ordinary restoring long division uses O(n+b) classical scratch and a fixed
polynomial number of bit steps; no quantum divider is needed. Keep no
expanded array of windows. For j=0..n-1, read the consecutive b-bit slice

    W_j=floor(E/2^(n-j))mod2^b.

For any candidate word t=sum_j t_j2^j, compute into a b-qubit accumulator

    A_E(t)=sum_j t_j W_j mod2^b,
    C_E(t)=floor(A_E(t)/2^(b-R0)).                              (3.1)

Each term is a controlled addition of a KNOWN classical b-bit window,
with its quantum control t_j retained, O(b) exact Clifford+T gates and
O(b) reused scratch. Reverse additions clear the accumulator after use.
Everything is defined also for invalid t>=N and ell=0.

Nested integer division gives floor(E/2^(n-j))=floor(2^(b+j)ell/N).
Thus W_j/2^b approximates frac(2^j ell/N) downward with error<2^-b.
The total downward lift error before modulus is<n2^-b<=2^-16; truncating
to R0 bits adds<2^-16. Uniformly over ALL labels/candidates there is a real
0<=e_t<2^-15 with

    C_E(t)/2^16=t ell/N-integer-e_t.                          (3.2)

The lift identity proves the circular bound through wraparound. There is
no distributional assumption, stochastic rounding or average-case precision.

For the row implement the correction diag(1,exp(-2pi i C_E(t)/2^16)), then H.
For each of its16 fixed binary angles theta_v, compile a single-qubit word
W_v in H,T,Tdag approximating P(theta_v)=diag(1,exp(i theta_v)) to norm2^-30
UP TO AN OVERALL SCALAR. These16 targets and tolerances are independent of
n,ell,t and outcomes. Use the same actual words on every iteration.

A constructive finite compiler enumerates words in length/lexicographic order,
and scalar phases on finite dyadic angle grids of mesh decreasing with length.
Approximate word/target matrices by rational intervals to certificate uncertainty
less than one hundredth of the fixed tolerance. Accept only if a certified
Frobenius-norm upper bound for W_v-z_v P(theta_v), |z_v|=1, is below2^-30.
Otherwise move on, without infinitely refining one uncertain word. Clifford+T
is dense projectively in single-qubit unitaries; Dawson and Nielsen,
The Solovay-Kitaev algorithm, quant-ph/0505030v2, Theorem1 and Sections2-3,
https://arxiv.org/pdf/quant-ph/0505030 , gives constructive finite approximation.
A word within half tolerance exists. Padding it with HH permits arbitrarily
fine scalar grids without changing its matrix, so a strict certificate is
eventually found. Target trig and Clifford+T entries have computable rational
intervals (Machin/Taylor or exact algebraic arithmetic). All targets are fixed,
so termination time, word length and workspace have ABSOLUTE finite bounds,
counted in initialization, memory and every subsequent word emission.
No advice or n-dependent rotation oracle is supplied.

The EXACT controlled version of each ACTUAL compiled word is implemented gate
by gate, with the accumulator bit as control. This preserves that bit EXACTLY.
Controlled T or Tdag: compute control AND row into a clean bit by Toffoli,
apply T or Tdag to that bit, then uncompute the AND. The bit is zero again
on every input, and the two logical wires are unchanged in computational value.
For controlled H let V=S H T H Sdag, which is Ry(pi/4) up to scalar, so
V Z Vdag=(X+Z)/sqrt2=H. Thus controlled H is Vdag on the row, CZ, V on the
row in chronological order. This is exact Clifford+T and preserves its
control. CZ is exact H,CNOT,H. Each controlled elementary gate has a fixed
finite exact word and a constant number of clean scratch bits. No controlled
source or inverse preparation is involved.

Apply the exact controlled W_v for each top accumulator bit v, then reverse
all additions in (3.1). Because these controlled words never change any
accumulator bit, that reversal returns accumulator and its arithmetic helpers
to zero EXACTLY, even with candidate/row entanglement. Reuse them for the next
row. No separate logarithmic workspace is retained per source copy.

There is a subtle relative phase, which is accounted for rather than ignored.
For a FIXED candidate t, C_E(t) is a definite binary word, and the retained-row
unitary is a product of the W_v whose controls equal1. It approximates the
ideal row correction up to the product of their scalars z_v, with norm error
<=16*2^-30. The scalar can depend on ell and t. Thus the entire controlled
row test is NOT asserted close to the ideal controlled phase modulo one
common scalar on all candidates. Instead Section4 uses the EXACT implemented
block V_t and projector V_tdag |0><0| V_t. Its scalar cancels from this
projector. The full reflection applies the actual V and its literal inverse
BEFORE diffusion, so no extra candidate phase survives. Correctness only
needs the fixed-t test probabilities and this exact cancellation.

For ell=k, combine (3.2) with the product error. Up to the harmless fixed-t
scalar, the row test differs from ideal phase correction followed by H by

    xi=2pi*2^-15+16*2^-30<1/1024.                             (3.3)

For any row state, a measurement probability changes by at most2xi. Under
a good copy's uniform hidden k and decoded-label law, (2.2) adds at most
1/2048. The total error is <5/2048<1/100. Therefore the actual local test
on the GOOD OUTPUT MARGINAL has pass probabilities

    p_s>=99/100,       p_t<=51/100 for every wrong t<N.        (3.4)

The ideal correct pass is1. The ideal wrong mean is1/2, since
(1/N) sum_k cos(2pi k(s-t)/N)=0. Misdecoded outcomes are bounded in total
probability without conditioning on successful extraction. Equations(3.3-4)
are used only on good inputs; arbitrary bad local outputs need no phase law.

## 4. Exact threshold reflection and both overlap tails

Let C denote ALL retained classical prefixes and decoded records, held read-only.
For fixed C and fixed t, V_(C,t) is the product over rows of their actual tests
from Section3. Let A_a be the projector for at least a zero outcomes on the k
row wires. Define Pi_(C,t)=V_(C,t)dag A_a V_(C,t) for t<N, and zero otherwise.
It is an EXACT projector on the k retained row qubits. Reusable accumulator,
AND and arithmetic scratch are exactly clean after each local V and its inverse.

The physical reflection R computes candidate validity, applies every actual
local V to the rows, reversibly counts row zeros with an O(log k)-bit counter,
flips phase iff valid and count>=a, reverses counting, applies all literal
local inverses, and clears the valid flag. This implements

    R= sum_C |C><C| tensor [I-2 sum_(t<L)|t><t| tensor Pi_(C,t)].       (4.1)

The classical direct-sum notation is analysis of ordinary classical control,
not a physical quantum encoding of C or quantum-addressed classical storage.
No intermediate row outcome is measured. The same fixed record-dependent
reflection is used every iteration. All uncontrolled scalar phases introduced
by compilation cancel in Vdag A_a V within each candidate block, exactly.

Let omega_CQ be the ACTUAL compressed joint classical/quantum state, including
arbitrary extension to bad systems. For a fixed t, the local row-test projectors
controlled by their OWN classical records act on disjoint output slots. Their
good output marginal is a product by (2.3). Thus the hypothetical commuting
test outcomes on good slots are independent Bernoulli variables with the
means in (3.4). One never conditions all classical prefixes on favorable values.

At the true s, if the good-pass count Z>=a, threshold acceptance is certain
regardless of bad outcomes. Its mean is at least .99(k-b_bad). Uniformly for
b_bad<=k/4,

    E Z-a >= (99/100)(3k/4)-11k/16 =11k/200 >k/20.

For a wrong t, threshold acceptance requires good passes Z>=a-b_bad; its mean
is at most (51/100)(k-b_bad). The gap is minimized at b_bad=k/4 and equals

    a-b_bad-E Z >=11k/16-k/4-(51/100)(3k/4)=11k/200>k/20.

These are event inclusions for commuting projectors, so they hold on arbitrary
bad-good extensions, not just states with independent bad systems. For independent
Bernoulli variables with arbitrary means, each centered log-mgf has second
derivative<=1/4. Summing gives E exp(z(Z-EZ))<=exp(g z^2/8), hence the
one-sided deviation bound exp(-2u^2/g) by Markov and optimization. With
g<=k and u>=k/20, both tails are bounded by

    delta=exp(-k/200)<=2^(-n-20),                              (4.2)

because k/200>=n+20 and e>2. In the CQ direct-sum notation this states

    Tr[(I-Pi_s)omega_CQ]<=delta,
    Tr[Pi_t omega_CQ]<=delta, wrong t,                         (4.3)

where Pi_t includes its classical-record control. True acceptance is NOT
asserted certain for this algorithm. Its small rejection probability is
included in (4.3). B empty includes all clean inputs; mixtures over fixed B
inherit the bounds by linearity.

For N=2 the streamed ORIGINAL t=0 shift test has good true0 passes certainly,
and good s=1 passes mean1/2. Threshold a=11k/16 is below3k/4; a wrong0 needs
at least7k/16 good passes at b_bad=k/4, versus mean3k/8, a gap k/16.
The same concentration argument gives failure<=exp(-k/128)<1/128. This
branch needs no phase compiler or label extraction.

## 5. Mixed-state search, candidate phases and uniform success

For mathematical analysis only, purify omega_CQ into |Omega> with an inaccessible
reference. Classical record blocks may be represented by orthogonal basis states
in this analysis; their physical cost remains the counted CLASSICAL bits.
Let R_s^* mark only s on the candidate and act identically on the bank.
For any normalized candidate state |v>=sum_t v_t|t>, orthogonal candidate
supports and (4.3) imply

    ||(R-R_s^*)|v,Omega>||^2
     =4|v_s|^2 Tr[(I-Pi_s)omega_CQ]
       +4 sum_(t!=s)|v_t|^2 Tr[Pi_t omega_CQ] <=4delta.         (5.1)

Invalid candidates contribute0. Unlike a noiseless witness proof, (5.1)
explicitly includes the nonzero TRUE rejection term. No operator-norm
approximation to a full controlled phase is substituted for this estimate.
Record-dependent candidate scalars have already canceled exactly in (4.1).

D=(2|u><u|-I) tensor I_bank is exact diffusion on n candidate qubits, built
from Hadamards and a Toffoli zero-string chain with O(n) scratch. Its fixed
global sign is immaterial. In the ideal iterate D R_s^*, the initial bank
and reference stay unchanged. A telescoping expansion of r unitaries against
that ideal trajectory, unitarity and (5.1) give final vector distance at most

    2r sqrt(delta)<=2*2^(n/2)*2^(-(n+20)/2)=1/512.             (5.2)

No independence/factorization of REAL disturbed intermediate states is assumed.
The physical algorithm neither accesses a purification nor inverts a source.
Trace distance and any output-probability change are bounded by (5.2).

For sin(theta)=1/sqrt L, ideal success after r=floor(3sqrt L/4) iterations
is sin^2((2r+1)theta). At L=4 it is1; L=8 it is121/128. At L>=16,
1/sqrt L<=theta<=16/(15sqrt L), so 5/4<=(2r+1)theta<=28/15. The interval
lies in [pi/3,2pi/3], using3<pi<22/7; ideal success>=3/4. Thus actual
full-secret success is at least3/4-1/512=383/512>95/128, uniformly for
all N>=3, s and allowed joint inputs. N=2 has the stronger bound above.
No abort, hidden favorable conditioning or extra source acquisition occurs.

## 6. Complete simultaneous resources and controller

All gate operations are exact Clifford+T words; approximations enter only
the probabilities in (3.4). The actual words and inverses are known circuits.
One local phase calculation uses n additions of b=O(log(n+2)) known bits,
its16 fixed compiled controlled words and the inverse additions. An in-place
controlled known addition is O(b) exact Boolean/Toffoli gates and O(b) reused
scratch by ripple compute/swap/inverse. Its candidate control is not measured.
The threshold count uses k full controlled O(log k)-gate increments and their
inverses. No amortization over unknown quantum carries is used. Diffusion,
validity and comparisons are O(n) gates. Total raw gates per R,D iteration are

    O(knb+k log k+n)=O(n^2 log(n+2)).                          (6.1)

The classical controller actually emits these gates, including all unsimplified
constant templates and inactive quantum controls. Use regular per-position
Boolean layouts and persistent microstep descriptors as follows. For a length-m
ripple sweep, each role pointer is a base plus a fixed signed stride times the
position. Retain a fixed descriptor per microstep; use its existing full address
fields for emission rather than copying address words at every gate. Over m
consecutive increments/decrements of any w-bit index, bit j is visited at most
O(m/2^j+1) times, so total bit reads/writes and pointer carry walks are O(m+w).
A fixed stride is a constant number of unit updates. A decrementing public
sentinel exits on underflow, avoiding a full equality test per emitted gate.
Initial descriptor fields and first/last addresses cost O(log(n+2)) per sweep.
These deterministic bounds include reverse passes and arbitrary start indices.

Each window adder has m=b, with O(b+log(n+2)) controller bit work, including
all consecutive CLASSICAL prefix-bit reads, candidate/accumulator role pointers
and its complete gate word. Window start n-j and row bases can be recomputed
by ordinary O(log(n+2))-bit arithmetic ONCE per adder, not per emitted gate.
There are kn=O(n^2) adders, giving O(n^2 log(n+2)) actual core bit/gate-generation
operations. The16 constant controlled words per row use constant gates, plus
O(log(n+2)) public descriptor setup per row. Threshold generation, inverse,
validity and diffusion fit the same bound. An O(n)-bit outer iteration counter
may cost O(n) bit operations per iteration; that too is included. Classical
record contents affect only known gate bits; reading each bit is charged.
No instruction oracle or free word-RAM is assumed.

Allocate exactly k retained row wires and only ONE current source position
register, one current extraction probe set, n candidate wires, the reused
b-bit phase accumulator/carries and constant compiled-control helpers, threshold
counter and O(n) diffusion/arithmetic scratch. Every inactive wire, flag and
unused fixed-field padding is counted. Old source position/probe work is
reset/released before the next delivery. The exact controlled-word construction
makes phase accumulator/carries zero between rows. Thus the ENTIRE quantum
peak is O(n) on every branch, including malformed inputs and failed extraction.
No hidden k-by-log(n) retained quantum helpers are allocated.

Classical records retain k words of P=n+b=O(n) prefix bits and decoded labels,
flags and any unused fixed-field padding, totaling O(n^2). Current N, extraction
counts/means, exact rational unwrapping, division scratch, public loop constants,
outer iteration counter and all persistent descriptors fit O(n) additional bits.
The finite compiler and trigonometric table have absolute finite counted size.
Hence SC=O(n^2), and M=SC+SQ=O(n^2) including ALL actual allocations. Every
quantum gate, classical bit action, gate-generation operation, measurement,
reset and operand use receives the stipulated FULL ceil(log2(M+2)) charge
O(log(n+2)), never just an offset charge. From (6.1) and the controller count,

    charged work per iteration=O(n^2(log(n+2))^2).             (6.2)

Source fees are (n+1)k=O(n^2). LE on one source has O(n) levels, O(log(n+2))
tests per level and O(n) gates per test; its arithmetic decoding is a fixed
polynomial. For k=O(n) sources, all extraction, classical prefix division,
validity, record initialization and discards are additive fixed polynomials
in n with the same space bounds. The trigonometric/phase compiler is a finite
absolute-cost algorithm, not supplied advice. Integer computation of r is
polynomial-time and O(n)-space. Cleanup resets all retained rows and clears
ALL prefix records with O(n^2 log(n+2)) charged work, within the final bound.

Every fixed polynomial and absolute constant is eventually dominated by
2^(n/2)n^2(log(n+2))^2; finite small exceptions change only an absolute outer
constant. For n>=2, log(n+2)=Theta(log2n). With r<=2^(n/2), (6.2) proves
T=O(2^(n/2)n^2(log2n)^2), simultaneously with SCn^2,SQn and Q=k on every
branch. N=2 has its fixed finite cost and the same Q formula. No source
reacquisition, parallel discount, preparation inverse, purification access,
quantum-addressed classical lookup or adaptive source choice is available.

## 7. Scope and attribution limits

The intended result is a few-qubit robust threshold point at time index1.
The unchanged RWT25-STREAM point has smaller time n^2 log n and smaller
classical space n, but quadratic quantum storage; this point trades those
for linear qubits. One-third-tolerance rows have a stronger malformed fraction
and are not claimed dominated when that metric is worse. Comparisons require
all four exact bounds and identical error context. No universal optimality,
frontier certification, new source model, physical timing or cube-root result
is claimed. The proof's local finite checks are development evidence only.

The four source uses in Section0 remain separately declared, even where a
provisional indirect path exists: threshold/control, label/trig extraction,
fixed uniform window map, and passive-delivery/reference-channel interface
are distinct actual material uses. The new construction combines them with
an exponentially reliable approximate threshold, exact controlled compiled
words whose candidate scalar cancels, and a counted clean O(n)-qubit layout.
It does not import the source filters, cubic witnesses, one-third endpoint
or GRF sieve into this algorithm. Native and hosted reviews, when available,
are separate from this mathematical argument and are not proof premises.
