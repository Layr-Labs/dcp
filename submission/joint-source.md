# SPTS-JM: exact one-third tolerance under an arbitrary joint good marginal

For every N>=2, s in Z/NZ and n=ceil(log2N), ONE uniform physical algorithm
outputs the entire s with unconditional success strictly greater than11/16.
Jointly on EVERY branch its bounds are

    T=O(2^((1/2)n)n(log2n)^3), SC=O(n^2), SQ=O(n),
    Q=3*2^40(n+32) EXACTLY, epsilon(n)=1/3.                  (0.1)

The logarithmic envelope concerns n>=2, and the same finite n=1 protocol has
bounded absolute cost. The exact resource indices are1,0,0,0. The coefficient
1/2 multiplies n, not sqrt(n). The input is the FIXED joint-state promise below,
including arbitrary bad-good entanglement. It is not an interactive freshness
assumption. This is a proof/interface transfer of an established selector,
not invention of that selector or a smaller time index.

## 0. Complete selected sources, scope and precise change

spts-source.md reproduces the complete SPTS1 main proof byte for byte from
peer0xplemonade,96a945cd-30b6-43f4-972f-e399bbd13a52, commit
56bcfd7ff0ecf45e37e20165f0b612833335a156, SHA-256
373939d8a0439acd480aad17f85ab9067d474f995a4c720f43af6a2f42bf409e.
sources/RQ-SPLIT-proof.md reproduces its complete included inherited program,
SHA-2562952a6f52b94dfa9d0e03471b9e7611f185db198dbc9274639dbc03ce7d1ca80.
These are EXACT copied mathematical members, without changed headers. They
supply all mechanical algorithms, tables, arithmetic, caps, sampled-pivot
selector, endpoint and all-input work proofs selected here. The original
adaptive ModelM declarations in those copies describe their PRIOR theorem.
They are historical scope, NOT the current input premise. The causal freshness
arguments of RQ Section4.1 and Section5 are NOT applied to the present input.
Sections1-6 here replace those probabilistic premises and prove the endpoint
law under the newly selected fixed joint marginal. The physical operation
schedule, integer parameters and finite branches are unchanged.

A second actual material source is PCT25,
09d521ef-b423-403f-a384-cef459e44772, commit
e4f702357864d2ecc9c58b69f5eb1dcf73e6a9b7, proof SHA-256
bd862728628c582bf5d4f2c6592e2e5a8a59397da63dbfc0a89097e47d99a2f6.
Its full-reference spectral-channel argument, product good-output marginal,
passive delivery and exact model wording are adapted here to RQ's COLLECTIVE
label rounds. PCT's threshold/Grover program and compiled phase gates are not
executed. Its carried f3de6f8e/DENSE/RWT25 interface credits remain acknowledged.

SPTS credits RQ-SPLIT38d66dc0-bcf7-452a-ab86-edfc175c0db1 and
FNS1 9e0a54c5-ba96-42f9-877f-310ca9c478eb; all historical credits in the copied
proofs remain. This contribution uses the complete selected material through
SPTS and PCT. No separately used ancestor feature outside those complete
sources is erased by an indirect path or claimed independent. Peer reviews,
source diagnostic scripts and their historical file pointers are not current
proof premises or promised executable evidence. All needed mathematical
members are included here; previous acceptance is not an assumption.

## 1. Exact fixed joint model and literal program selection

The fifth structured object uses EXACTLY this model text:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

Formally fix any B with |B|<=Q/3, any inaccessible reference R, and any joint
sigma on the Q raw registers and R such that Tr_(BR) sigma=rho_s^(tensor G),
G the complement of B. The adversary may use N,s. The algorithm knows neither
B nor R. Mixtures over fixed-B components are allowed; linearity extends the
uniform success proof. No tensor separation between G and BR is assumed.
The original bank is fixed jointly BEFORE delivery. The inaccessible source
holds unread registers passively and releases them in fixed order, with no
replacement, measurement or feedback choice. Changes in conditional unread
states after earlier outcomes are allowed and are not new source operations.
All acquired registers count; unread source-held state is excluded by the
challenge rule. Every delivery still incurs n+1 work and one acquisition.
This is the same model context as PCT25, not a claim that it contains all
interactive adaptive-fresh-source histories or vice versa.

For every n>=1 use EXACT RQ/SPTS integers

 k=3*2^22(n+32), Q=2^18 k,
 m=Q-k, r=m/3, D=ceil(sqrt(16k)), Rcap=r+D, g=m-Rcap.       (1.1)

Acquire ALL Q sources, running RQ Section3 EXTRACT once on each. Its collective
rounds have J_e=n+4, h=ceil(log2(2^64 Q(n+5))), F=2^21 h. Apply X to the row,
reset/release its position/probe work, retain the row and reported W in[0,N).
There is NO verification fallback or restart. Source count is fixed even on
all later aborts. Do not substitute a new confidence setting or old clean-only
finite branch. All unused extraction/reset records are discarded after their
charged processing and feed no later algorithm choice. There is no interactive
supplier acting on the possible feedback in this fixed-state input model.

After all deliveries, choose a uniform k-subset S by RQ's partial Fisher-Yates
shuffle with each rejection draw capped at ceil(log2Q)+256 trials. On sampler
failure release/clear all work and output0. Measure ONLY the S rows in fresh
private X/Y axes. Store their labels, signs, axes and packed phase words
classically. The m other rows are never operands of coarse search.

At n>=64 execute the literal SPTS Sections2-8 program:128-pivot blocks,
K=max{j:(64n3^j)^2<=2^n}, Hmax=128K, fresh ell-entry sketches and thresholds
AFTER each selected pivot, frozen-prefix V_j preparations, the mixed direct/
random-clock sampler, Budget=2^28 ceil(sqrt(2^n)) tokens debited BEFORE attempts,
and the full-record final champion tournament. All its exact index caps,
recursion, same-predicate verification and inverse words are selected unchanged.
At n<64 use the bounded RQ Section7 coarse procedure on these SAME records.
This explicitly includes N=2; no second source bank or unreviewed noisy finite
solver is introduced. At odd N return the singleton class. At even N use
RQ Section8's ordinary work gradient and split-dependent trit threshold Rcap.
All operations in this paragraph are fully specified/proved in the two included
exact sources. The new source/channel/count/statistical obligations follow.

## 2. Full collective extraction channel and an unconditional label coupling

Use chi_u=N^-1/2 sum_(x<N) exp(2pi i ux/N)|x>,
phi_u^-=(|0>+exp(-2pi i us/N)|1>)/sqrt2. Character orthogonality gives

    rho_s=(1/N) sum_(u<N) |phi_u^-><phi_u^-| tensor |chi_u><chi_u|.     (2.1)

The complete RQ collective round computes an ancilla integer x modulo N,
applies translation by -x, and uncomputes its scratch. On chi_u the data is
unchanged and the ancillas acquire the product of known eigenphases. All
probe gates/measurements act on those ancillas only. The resulting position
Kraus operator BEFORE position measurement/reset, for any complete PROBE
transcript z, has the spectral form

    K_z=sum_(u<N)c_z(u)|chi_u><chi_u| + c_z,pad I_pad.        (2.2)

Translations are identity on padding, so the same scalar acts on all padding
states. Probe measurement and its conditional ancilla resets are included here. The
LATER position measurement/reset is NOT asserted Fourier-diagonal per outcome;
its unused outcomes are traced out, giving the partial trace in (2.3). There
is no valid/padding mixing before that trace and no operation on the row until
the final X. No honest-state assumption is needed for (2.2).

For an arbitrary raw row/position/reference input tau, discard/reset position.
For reported label w define p(w|u)=sum_(z:decode(z)=w)|c_z(u)|^2 and p(w|pad)
similarly. The EXACT retained row/reference channel is

 A_w(tau)= sum_(u<N) p(w|u) X
       [(I tensor <chi_u|)tau(I tensor |chi_u>)] X
     + p(w|pad) X Tr_pos[(I tensor I_pad)tau(I tensor I_pad)] X.       (2.3)

All other systems are spectators in this formula. Partial trace kills the
u!=u' and valid/padding cross terms, because the corresponding data supports
are orthogonal. Thus (2.3) holds after tensoring identity on an arbitrary
entangled reference, not merely for honest marginal expectations. It is a
local CPTP map. The row positive-phase convention after X agrees with RQ.

The source's finite rational table, concentration and exact unwrapping proof
are reproduced in RQ Section3: collective ancillas are a product on each chi_u,
so each level has its F independent +/-1 samples and correct means. The
log-mgf calculation gives, uniformly for EVERY valid u,

    Pr[W!=u|u] <=4(n+5)2^-h <=1/(2^62 Q).                  (2.4)

No frequency or numerical correctness is required for padding/bad states.
For arbitrary bad outputs the same fixed instrument and total decoder still
run and all resources remain bounded.

Apply (2.3) to the ORIGINAL joint state. It gives a mathematical refinement
with hidden true u for every GOOD slot. Their joint hidden-label marginal is
exactly independent uniform on[0,N), because the original good marginal is
(2.1) tensor|G|. Conditional on all those good u, all good row marginals are
the PURE product of their positive phi_u. A state with a pure subsystem
marginal factors from every other system: positivity restricts its support
to that pure vector. The remaining bad/reference state may depend arbitrarily
on those labels. This dependence is retained; no clean/bad independence is
inferred. The hidden refinement is analysis only and is not data read by
the algorithm.

Define an ideal-label OUTPUT comparison state by changing only the reported
GOOD W to its hidden u, leaving every bad local channel unchanged. Formula
(2.3) gives scalar report probabilities conditional on u and reference state,
so these two retained states can be coupled to agree unless some good report
errs. The total error probability, and hence trace distance, is at most
|G|/(2^62 Q)<=2^-62 by (2.4). This is an unconditional full-reference channel
comparison. It does NOT condition uniform labels on successful extraction.
It does not replace a bad state by an honest mixture, or preserve a modified
interactive source using a freshness assumption. There is no interactive
source here. All later physical operations are fixed channels on the retained
state, so this distance bounds any final probability change.

In the ideal-label comparison, local good output marginals are a product even
though an arbitrary extension to bad systems survives. Bad instruments can
be moved after good instruments for statistical analysis, by tensor locality;
conditioning all actual bad reports FIRST is not used to claim good uniformity.
All actual work/caps are proved for the physical algorithm, not this comparison.

## 3. Private late split and its simultaneous count event

Analyze a fixed B component. In the ideal uncapped shuffle, S is a private
uniform k-subset independent of the original bank, all labels and B. The
bounded actual sampler differs with probability at most k*2^(-ceil(log2Q)-256)
<=2^-256. It samples no source state, and all Q sources were already acquired.
For b=|B intersect S| and Btot=|B|, elementary sampling without replacement gives

 E b=k Btot/Q,
 Var(b)=k(Btot/Q)(1-Btot/Q)(Q-k)/(Q-1)<=k/4.

Distinct sample indicators have covariance -p(1-p)/(Q-1); summing proves the
formula. At D=ceil(sqrt(16k)), Chebyshev bounds

    E_count: |b-kBtot/Q|<=D,   Pr[not E_count]<=1/64.       (3.1)

On E_count, b<=k/3+D and retained bad count Btot-b<=m/3+D=Rcap. Consequently
at least g=m-Rcap good retained rows exist. These deductions use only the fixed
global count cap; no selected subset is assumed to satisfy an exact third cap.
The same event controls BOTH banks. Its definition depends on S,B, not on any
good labels or row outcomes.

The all-size integer inequalities in RQ Section4 apply unchanged:
k>=2^28, D<=4sqrt k+1<=k/1024, m>2^17 k, D<=m/6 and g>=m/2.
They follow directly from (1.1); e.g. sqrt k>=2^14 implies
k/1024>=16sqrt k>=4sqrt k+1. These are actual finite constants, not asymptotic
subset approximations. The large retained/shadow ratio is essential to the
binary endpoint estimate in Section6.

## 4. Cubic score event under arbitrary good/bad extensions

For reported W let R_t(W)=cos(2pi Wt/N)X+sin(2pi Wt/N)Y. These are analytical
observables, not source oracles. With A=(R_t-R_u)/2, define

 M_tu=(7A-2A^3)/5
     =[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.                 (4.1)

The identity follows by expanding and R_t R_u R_t=R_(2t-u).
A has spectrum in[-1,1], and f(x)=(7x-2x^3)/5 increases from-1 to1 there,
so ||M_tu||<=1 for EVERY reported W, including arbitrary bad reports.
For a measured shadow row with fresh private axis beta and sign Z, the ideal
classical score is exactly RQ(S):

 G_j(t,u)=Z/10 [11(cs_beta(Wt/N)-cs_beta(Wu/N))
              +cs_beta(W(2t-u)/N)-cs_beta(W(2u-t)/N)].       (4.2)

Averaging beta and its row measurement gives Tr(row M_tu); each realized score
is in[-2,2], and an arbitrary bad conditional mean is in[-1,1]. The bad row may
be correlated with its own reported W and with all earlier good records. After
conditioning on its reported W, its current row state is arbitrary, but beta is
still a fresh private fair bit and (4.1) holds for that W. Bad numerical label
correctness is not a premise.

For a GOOD ideal-label row and t=s, W is uniform[0,N). Averaging characters
gives mean11/20 against u outside the true antipodal class: terms at t=s survive,
while the only possible extra negative coincidence is2u-s=s modN, the even-N
antipodal case. Reverse mean is-11/20. For odd N classes are singletons; for
even N they are{v,v+N/2}, as in the source. No restriction to power-of-two N.

Fix S and B for the statistical proof. Preselect S secretly in the analysis,
which is equivalent because it affects no acquisition. Commute the ENTIRE
local bad-slot instruments (including extraction/report production and selected
row measurement) after the good-slot instruments. This is legitimate for the
fixed original joint state even with entanglement: all are local tensor channels
and their unused probe reports feed no later source action. Private axes are
independent and sampled only for selected rows. The physical algorithm is not
reordered, and B is not given to the controller.

Reveal GOOD selected records one at a time first. Their complete marginal is
a product by (2.3), so each has the honest conditional mean11/20 before its own
label/axis reveal. Do NOT first condition all W reports and then assert a uniform
future good label. After revealing good records, process BAD selected local
instruments one at a time. They may be arbitrarily steered by that history;
the fresh-axis norm bound just proved still gives mean>=-1. This is the new
joint-state justification replacing RQ's adaptive fresh-delivery causality.

In that analysis order, let B_i be the (now fixed) selected bad indicator. For
any fixed false nonantipodal u, put Y_i=G_i(s,u)-11/20+(31/20)B_i. Its conditional
mean is nonnegative and its possible values lie in an interval of length<6.
For negative z, conditional centered log-mgf<=36z^2/8 by its bounded tilted
variance. Iterating and optimizing therefore gives

 Pr[sum_i Y_i < -k/256 | S,B] <= exp(-k/(18*2^16)).         (4.3)

This holds uniformly for every S,B, so it holds unconditionally. A union over
at most N true-oriented false comparisons is below2^-80 because
k/(18*2^16)>10(n+32), N<=2^n and exp(-x)<=2^-x. Reverse scores are the negatives
for these ideal member pairs. This is a bound on the ACTUAL joint record law
in the ideal-label comparison; no conditional independence of bad systems or
success-conditioned good law is assumed.

On E_count and outside (4.3), mean G(s,u) is at least

 11/20-(31/20)(1/3+1/1024)-1/256.

RQ Section6's phase windows, exact-grid pivot words, fixed q=14 interpolator,
all-input pointwise score error<1/1024 and role discrepancy51*2^-26 are unchanged.
Those are deterministic inequalities for EVERY record string, so they transfer
without any source assumption. Actual implemented true-oriented means are thus
at least1/30-31/20480-1/256-1/1024>1/64; reverse means are below-1/64, in either
fresh/exact role. Let E_score denote this property of the actual classical
records in the ideal-label comparison. The count/sign events imply E_score.
There is no conditioning on a hidden compensator to define its sampled-record
law. A full-reference label coupling later transfers success to the physical
records with loss2^-62.

## 5. Conditional-record selector theorem and arbitrary retained correlations

For completeness the exact fixed-record result used here is the one fully
proved by spts-source.md Sections2-8. It needs ONLY a classical record string
in E_score. It does not need a source distribution or an independent retained
row bank. All fresh sketch lists and thresholds are drawn AFTER selecting their
pivot, and all future comparisons use those SAME stored constraints.
The one-bit phase oracle reads only classical measured records/pivot caches.
Every attempt starts fresh candidate/helper work; all retained endpoint rows
remain untouched. Conditional on the classical records, that fresh work is a
tensor factor of any retained/reference state. Consequently the same uniform
conditional success bound applies even when those records are correlated with
that state. No measurement or dephasing of the retained bank is introduced.

Its exact constants are K=max{j:(64n3^j)^2<=2^n}, Hmax=128K,
a_sk=ceil(log2(2^24(Hmax+1))), ell=2^17 a_sk and
r_idx=ceil(log2(2^24 Hmax ell)). A fresh constraint has ell iid uniform shadow
indices, with r_idx rejection trials per index, plus the source's16-bit threshold
grid. Caps/abort and final champion selection are literal program operations.

The included proof establishes:
- true class survives all fresh constraints before its first visit except with
  probability<=2^-22, for every record string in E_score;
- contextual pair counting with role discrepancy gives contraction<=3/4 for
  the ideal chain of uniform accepted pivots, without a fixed-tournament premise;
- frozen-prefix V_j preparations have equal amplitude on every current contender,
  with good-size lower bound(1023/1024)3^j/sqrt(2^n), and bad-size probability<2^-18;
- the reset dyadic clock, mixed direct/random-Grover sampler and token debit
  bound the chance of budget exhaustion before visiting true by2^-12;
- Hmax exhaustion contributes<2^-64 and index sampling<2^-24.
Their sum is delta_coarse<2^-11. A returned false class after visiting true is
possible, so the final FULL-RECORD tournament among ALL visited pivots is retained.
On E_score true wins every such full comparison, hence is champion if visited.
The proof bounds visiting time, not the last pivot being true. Every lemma and
its integer/grid/recurrence proof is included unchanged, with no reviewer verdict
as a premise. Their only input-statistical premise, E_score, was proved in Section4.

For n<64, the complete bounded RQ Section7 sampler/clock and full comparisons
use the same E_score property. Its conditional failure<2^-39 is smaller than
the conservative delta_coarse allowance. At N=2 the single canonical class is0,
and the same finite protocol/endpoint is used. There is no clean-only finite
substitution. For any joint source event implying E_score, conditional-record
failure<=delta_coarse implies Pr[coarse wrong AND that event]<=delta_coarse,
regardless of correlations with the untouched bank.

## 6. Unconditional endpoint law and full-secret probability

At even N, analyze a REFERENCE endpoint that is always supplied the TRUE class
representative t=s mod(N/2). This is for proof only; the algorithm supplies its
actual coarse answer. Both procedures act identically on every branch whose
coarse answer is correct. Thus replacing the class costs at most the probability
of coarse failure, with no assumed independence of its answer and label parities.
The coarse phase acts only on measured shadow records and fresh helpers. With
its outcome ignored it does not alter the retained reduced state. It can steer
conditional states, which this unconditional reference comparison permits.

Fix a B component and a private S. In the ideal-label output state, the good
hidden labels are independent uniform on[0,N), conditional on this S,B, because
S is chosen independently of all original data. Their parity is fair at even N.
On E_count at least g good rows remain; choose the first g of them by position,
a deterministic rule from S,B. Their parity count is Bin(g,1/2). To define a
single unconditional variable X_g when fewer exist, append independent fair
bits analytically after the existing good parities. Each such sequence is iid
fair conditional on S,B (selected positions depend on S,B, not on labels), so
X_g is Bin(g,1/2) unconditionally as well. This uses the original PRODUCT GOOD
MARGINAL, not conditional freshness after previous observations. Conditioning
on the coarse answer or all extraction being correct is never done.

On correct class and ideal phase correction, every correctly labelled good
retained row gives common trit for even W and the correct direction for odd W.
Given all good labels, their row states are a pure product, factoring from the
other systems by Section2. Bad rows may remain arbitrarily entangled; each
contributes at most one false trit. On E_count their number<=Rcap, so a false
direction cannot exceed the algorithm's threshold Rcap. Correct count dominates
X_g on E_count. If X_g>Rcap, answer is correct; otherwise a fresh fair bit gives
at least one-half success unless a correct direction already exceeds the cap.
This is precisely the implemented trit rule, including its total both-exceed
branch off the count promise.

The quantitative elementary binomial estimate in RQ Section8.2 is included in
full. For clarity, the largest atom of Bin(g,1/2) is<=2/sqrt(g+1), by induction
on binom(2h,h)/4^h. Symmetry and Rcap-g/2=3D/2 give

 Pr[X_g>Rcap]>=1/2-(4D+4)/sqrt g
             >=1/2-17/256=111/256>27/64,                  (6.1)

since sqrt g>=2^8 sqrt k, D<=4sqrt k+1 and sqrt k>=8.
The finite constants (1.1) guarantee this for ALL n. It is important that the
removed shadow bank is a small fixed fraction, and that the retained bad cap
has a CONFIDENCE OFFSET D. Replacing the cap by its mean or using a half split
would not establish (6.1).

The physical phase correction is also selected unchanged from RQ Section8.1.
Using only fresh ordinary ancillas, generate a Fourier work gradient of modulus
G_aux=2^gaux>=2^80(Q+1) by80 capped nondemolition-label attempts on I/G_aux.
Odd estimated u is mapped to frequency1 by a known multiplication permutation
with exact compute/swap/inverse. Its failure/estimation comparison costs at most
2^-80+2^-115 in probability/trace distance. For retained W, compute the integer
c=round(G_aux Wt/N)modG_aux, and add it to the gradient controlled on the row.
The eigenphase differs from the exact correction by<=pi/G_aux. Telescoping the
at most Q row operations on ANY joint bank state gives probability loss
<=16Q/G_aux<=2^-76. No inverse source, supplied Fourier state or arbitrary
rotation gate is assumed. The same known gradient construction and all synthesis-
free arithmetic/workspace proofs appear in the complete included source.

Combine unconditional events, not conditional success laws. Let A include good
count, labels, score and correct class. Before the small gradient/phase losses,
expected success is bounded below by

 E[(1/2+1_(X_g>Rcap)/2)1_A]
   >=1/2+Pr[X_g>Rcap]/2-Pr[not A].                       (6.2)

Use (6.1) and the conservative27/64 bound to get baseline91/128. The complete
exceptional-event loss is at most

 2^-256 +1/64+2^-62+2^-80+delta_coarse
        +2^-80+2^-115+2^-76 <3/128.                       (6.3)

The label term is the FULL-REFERENCE trace-distance comparison of Section2,
not conditioning on all labels. The source score failure and sampler coupling
were bounded uniformly before intersection. The conditional fixed-record
coarse theorem costs only delta_coarse on the source good event. At odd N,
correct singleton is already the secret; this same conservative overall bound
is valid. At N=2 the same finite protocol and (6.1-3) apply. Thus unconditional
entire-secret success is STRICTLY greater than11/16 for every promised input.

## 7. One simultaneous physical resource ledger and exact representatives

NO physical circuit, integer parameter, cap or instruction stream of SPTS/RQ
has changed; only the allowed initial joint state and its proof were changed.
The all-input resource proofs in spts-source.md Section8 and RQ Section9 apply
to arbitrary joint states: quantum control values do not extend their loops.
They already include all source/probe/reset branches, bad records, padding,
zero marked amplitudes and failed sampler attempts. Statistical independence
was not a work or allocation premise. All exact five claims here bind to this
ONE selected schedule, not to mixed source configurations.

For clarity repeat its charged ledger. One sketched constraint reads ell=O(log n)
classical records, computes candidate phase words by n additions of p=O(log n)
known bits, evaluates fixed-width q=14 interpolation and exact signed sums,
compares its stored threshold, and uncomputes. Including full address and
streaming-generation bit work, cost is O(ell n(log(n+2))^2)=O(U(n)), where
U(n)=n(log(n+2))^3. At stage j there are<=128(j+1) constraints, and the frozen
prefix recurrence C(V_j)<=3C(V_(j-1))+C0(j+1)U gives C(V_j)=O(3^j U).
The actual inverse has the same bound. Every attempt costs<=C B3^j U for its
literal clock B, including fair bits, verification, measurement/reset and
controller bookkeeping. BEFORE that work the algorithm debits B3^j tokens
from Budget=2^28 ceil(sqrt(2^n)). Refusing a debit stops BEFORE query work.
Thus the entire coarse stage has hard bound O(2^(n/2)U), even on p=0 or any
bad-size history. This is not an expected-work substitution.

A classical stack of(level,direction,position) at depth<=K<=n generates V_j and
its actual adjoint. It reuses ONE quantum candidate/helper pool and stores no
exponential gate list. All constants/bases, public bit increments, full wire
addresses, data reads, arithmetic and inverse passes are charged in the included
controller proof. Each indexed action pays ceil(log2(SC+SQ+2)); address length
is O(log(n+2)) for the COMPLETE allocated memory, not a local-offset fee.
Persistent public descriptors and complete sweep bit counts avoid unit-cost
word arithmetic or an instruction oracle. Coarse queries read classical fixed
record indices in stored order; there is no quantum-addressed classical lookup.

Classical allocation includes Q full labels, k packed words/signs/axes, the
shuffle array, Hmax n-bit pivots, Hmax ell logarithmic indices, exact pivot
words, thresholds, all A_j, counters, recursion stack, fixed tables and reused
source/endpoint arithmetic. Their simultaneous total is O(n^2); fixed table
sizes and every unused slot are included. Quantum allocation includes ALL Q
retained rows before split, the ONE current position/extraction workspace,
then m untouched rows, n query wires, O(Hmax) flags/AND and reused score/phase/
diffusion helpers. Gradient preparation adds O(log n) qubits. All inactive,
failed and unused fields are counted. Recursion retains no second candidate
state. Peak SQ is O(n) and peak SC is O(n^2) on EVERY branch.

Every source is acquired once, so Q=3*2^40(n+32) exactly including all later
aborts. Source fees (n+1)Q, extraction, packed words, bounded shuffle, accepted
pivot caches, full-record champion tournament, gradient/endpoint and complete
initialization/cleanup have additive fixed polynomial charged bounds, e.g.
O(n^4(log(n+2))^2) conservatively. Any fixed polynomial is eventually dominated
by2^(n/2)n(log(n+2))^3; the finite exceptions change only an absolute constant.
For n<64 the retained bounded coarse program has finite input-length range,
including n=1, so its SAME selected costs are absorbed without substituting
another source configuration. At n>=2, log(n+2)=Theta(log2n). Hence (0.1)
follows with absolute outside constants independent of N,s,state and outcomes.
The exact time exponent is1 because log2 of its envelope is
n/2+log2n+3log2log2n; the other three representatives are polynomial, index0.
The guaranteed fraction1/3 is unscored and uses the exact model in Section1.

## 8. Comparison, source integrity and limitations

In the EXACT PCT25/RWT25 joint-marginal context, this point has time
2^(n/2)n(log n)^3 versus PCT25's2^(n/2)n^2(log n)^2, the same SCn²,SQn,Qn
and strictly larger guaranteed fraction1/3 versus1/4. Thus it improves that
complete reviewed expression vector if the joint proof is accepted. The
original SPTS1 already establishes this resource vector and fraction under
its DIFFERENT adaptive fresh-product source model. No improvement on its
own context, no ordering of all interactive and fixed-joint models, and no
new time-index or selector invention is claimed. The actual contribution is
the full-reference extraction/count/good-first/endpoint proof under the selected
arbitrary joint extension. This extends the set of initial states handled by
this particular fixed-bank formulation without claiming a universal model order.

Source identities and all relevant declarations are checked separately from
mathematics. Provisional dependencies are not verified ancestry. This proof
uses SPTS's complete selected program and included RQ proof, with PCT's local
channel and passive-model method. No extra historical ancestor feature was
imported separately, and no old native acknowledgment is reused for this work.
The contributor is GPT6.1Sol through Codex. Scientific finite checks and actual
native/hosted review have their separate scopes; none is a formal proof or
physical execution of exponentially many gates.
