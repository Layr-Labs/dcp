# GPS-STRICT-RETRY-BANK: geometric retry weights and revised literal cutoffs

For every N>=2 and s modulo N, n=ceil(log2N), ONE uniform physical algorithm
recovers the ENTIRE secret with unconditional success at least1-2^-8.
On EVERY execution branch, including all failed/discarded work and aborts,
its simultaneous envelopes for n>=2 are

 T=O(n^2 (log2n)^2 2^(a sqrt(n log2n))),
 SC=O(n), ENTIRE SQ=O(n^2), Q=O(2^(a sqrt(n log2n))),
 a=176777/250000, epsilon(n)=0.                            (0.1)

The four growth indices are1/2,0,0,1/2. The finite n=1 program has bounded
absolute costs. The full dense bank, inactive cells, matrix, genuine work
and raw source wires count in SQ. This is a NEW cutoff/extraction-parameter
program with a new success and resource proof, not a different envelope
for the unchanged predecessor or an assertion that their output laws agree.

## 0. Complete immediate source and the actual mathematical change

The immediate program, mathematical and physical source is GPS-BLOCK-NATIVE,
fc8f2316-5191-4cf0-8ede-85b55e721fb2. Its complete main is copied unchanged as
native-source.md, full SHA-256
5d25a109a4dd68e36d0312c06dcdae8db638871af48ae69a46c83385177c14d1.
ALL FIVE complete helpers from that selected archive are copied unchanged:
controller-source.md, previous-bank-source.md, gps-source.md,
bank-interpreter-source.md and stream-source.md, respectively with hashes
0e11424104cd7fd4371f9a05676099a7b7133ecf4952c40c6ce2a9de17343950,
b8a58ced5432baa998432d96450301265d17e83f0998e358895b409b881837f6,
3016a821fcc6ae313f0156326e1ca1f7de2f240c18d07bba70eb0db7859519f7,
26b64d6eb0471b0e73a66164c39c03d9a5954d9cad120a52729fdd50a2467298,
5ad693a64b57913c580fbec4798bf021fe9d505f3c2fa2421f4fcf080fd8affd.
Every active algorithmic/math helper is present. Historical archive paths
inside old method files describe their own algorithms, not missing premises.

The original GPS-BLOCK quantitative conditional-return proof is fully
reproduced in gps-source.md5.3, with its carried GPS-HALF/GPS-VLE/GPS-C3/
CS1/GPS3 and upstream credits. Its fixed-schedule search, signed high-part
laws, occupancy inequality and return bound are not claimed newly invented.
The native/typed/measured-bank methods retain their supplied credits too.
No additional ancestor feature outside this complete immediate archive was
separately imported. No previous review, simulation, source score or pending
graph reference is a mathematical premise or certified ancestry.

The source used only the weaker return bound>=1/2 in its retry accounting.
We exploit the supplied STRICT quantitative margin p>=67/128. Its inverse
is kappa=128/67 and its weighted decay is lambda=64/67<1. Summing actual
weighted retry costs geometrically removes the old growing factor m from
the required weighted cap. We CHANGE both literal global caps, recompute
ALL Q-dependent extraction/confidence/fallback fields and give a NEW
uncapped/capped success proof. The native ATTEMPT templates remain exact,
but the complete capped/extraction program is different from the parent.

## 1. Exact source promise and complete new public parameter rule

The fifth structured object uses EXACTLY

"Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies."

There is no positive malformed guarantee, purification, source control or
preparation inverse. Unread passive source-held copies are excluded from
accessible allocation only under the challenge convention. An arbitrary
inaccessible reference can be included in the implementation channel; no
interactive reacting supplier or reference access is used.

For n<256 run the COMPLETE original clean exhaustive shift-testing program
of gps-source.md8, with its actual tests, rejection rule, source count and
unconditional guarantee. For every n>=256 the new logical program is the
complete original GPS-BLOCK word/array program with ONLY the parameter
replacements below. All tree/Grover/decoder/2-adic instruments and tie rules
are unchanged. The physical controller is specified in Section7.

Compute the ORIGINAL profile by the same first-qualifying integer scan:

 Delta(R)=2ceil(log2(4R)), m(R)=floor((2R-2)/Delta(R))+1,
 S(R)=sum_(j=0,...,m(R)-1)(2R-1-j Delta(R)),
 R=least integer>=2 with S(R)>=n-1,
 v_i=2R-1-(m-i)Delta, q0=product_i(v_i+1), G=2^m q0.

Use the same PS_TREE(D,B), p_i,b_i,r_i=b_i+1 and their pass-through levels.
The original letter d=floor(log2N) is unchanged; kappa below is unrelated
to that bit length. Let K,Smax and H0=Smax K+2n be EXACT source6,8 formulas.
All signed/unsigned mode choices, CRT transformations, h,step,pdec, candidate
grids, root-frequency guard Fmax=nq0 and final output remain those formulas.

Set the fixed rationals and NEW literal caps

 p0=67/128, kappa=128/67, lambda=kappa/2=64/67,
 J_retry=(128^m q0)/(67^m),
 Qstar=ceil(2 J_retry H0)+2n, Qcap=1024 Qstar,
 Wstar=64*2^R H0,             Wcap=1024 Wstar.             (1.1)

These are actual public finite integers. Compute the ceiling by dividing
2*128^m*q0*H0 by67^m with upward integer rounding, then add2n. Numerator,
denominator and caps have O(R+m+log n)=O(n) bits. Iterated constant products
and schoolbook division compute them in polynomial bit work, not a real
arithmetic primitive or instance advice. Nothing uses measured labels or s.

For each actual node use its SAME weight w_i=2^ceil(r_i/2), checked AFTER
building its children and BEFORE admitting the ATTEMPT. Source acquisition
checks Qcap before the next original. The root-frequency guard is unchanged.
All refusals, private erasure and final output/cleanup are actual operations.

Recompute ALL Q-dependent EXTRACT values from the NEW Qcap:

 h_e=ceil(log2(Qcap(n+5)))+18, t_V=64h_e, F(h)=2^21h,
 sn=ceil(sqrt n), Cf=ceil(Qcap/sn).                        (1.2)

The cheap h_A=2ceil(log2(n+5))+14, J_e=n+4, T_V and P_V retain the source
formulas; the verifier's round count and high-confidence RUN use the new h_e.
All counters, rational words, integer cap widths, template bounds and static
pool dimensions are recomputed. No old h_e,Cf,Qcap,Wcap or display-only
resource column is substituted into the new program.

Because kappa<2 and2G H0 is an integer,

 Qcap<=1024(2G H0+2n)=old_Qcap, Qcap>=2048n.               (1.3)

Also Wcap/old_Wcap=32/m<=32, so even when a small m makes the new weighted
cap larger, its word width increases by at most a fixed constant. All
semantic numeric field widths remain O(n); extraction h_e remains O(R).

## 2. Exact quantitative margin and the right conditional history

The included source5.3 proves, for a fresh level-i batch with b_i>=1,

 Pr[return]>=alpha^2*(19/36), alpha=1-(3/4)^20>299/300.

It derives the conditional residue/high-part laws and deterministic
occupancy inequality rather than assuming Poisson or independent buckets.
Using EXACT integers,

 299^2*19*128-67*90000*36=343232>0,
 so alpha^2*(19/36)>67/128=p0.                            (2.1)

This does NOT lower-bound success conditional on already-known FULL input
labels/residues: fixed pathological residues can have small return chance.
The useful history is BEFORE STARTING A FRESH BATCH of r_i child calls.
It may contain all earlier failed batches, outside copies and previous
source/decoder information. In the uncapped ideal process of Section3,
fresh child copies and the supplied untouched-high-part laws allow source5.3
to be averaged by the tower property, giving (2.1) at this pre-batch history.
The bound is uniform over the effective secret, widths and that past.

Each child call's expected cost bound is likewise used at its START, even
after earlier siblings return full records. No child cost is conditioned
on the later success/failure of its parent batch. These costs and the
parent outcome may be correlated. This conditioning distinction is required
for the following geometric argument, not an independence shortcut.

## 3. New uncapped acquisition and weighted-cost expectations

Analyze the SAME ideal outer GPS process as the full source: EXTRACT reports
its latent correct label, all private extraction records are ignored by outer
routing, and acquisition, weight, fallback and root-frequency caps are omitted.
This ideal process is for proof ONLY, not a supplied Fourier-label oracle.
Actual sources still use the real translation tests in (1.2).

A fresh accepted leaf costs at most two originals in expectation (exactly
one per try in the 2-adic supplier). Suppose a level-i call repeats fresh
batches until return. Let A_t mean its t-th batch is STARTED, before any of
that batch's children. By (2.1) and sequential conditioning
Pr(A_t|initial past)<=(1-p0)^(t-1). Each started batch has r_i fresh child
calls followed by one local attempt. Uniform expected child bounds apply
before each such call. Summing E[1_(A_t)*batch_cost] therefore gives, for
acquisitions E_i and weighted-attempt work F_i,

 E_0<=2, F_0=0,
 E_i<=kappa r_i E_(i-1),
 F_i<=kappa(r_i F_(i-1)+w_i).                             (3.1)

No expected cost given a later failure is multiplied by a geometric trial
count. In particular the proof does not assume cost/outcome independence.
Pass-through levels have r_i=1 and local w_i=0: their actual factor1 is
bounded by kappa r_i, so (3.1) also bounds them. This induction proves finite
expectations and almost-sure ideal return, uniformly at call starts.

Thus a root uses at most2 kappa^m product r_i<=2 J_retry originals in
conditional expectation. Expanding the weighted recurrence instead of
charging every level equally gives

 F_m<=sum_(i=1,...,m) kappa w_i product_(j>i)(kappa r_j).

For the ORIGINAL unchanged profile,

 r_j<=v_j+1<=2R, kappa r_j<=lambda*(4R)<=lambda*2^(Delta/2),
 w_i<=2^((v_i+1)/2)=2^(R-(m-i)Delta/2).

The weight inequality follows because v_i is odd and r_i<=v_i+1 has an
even upper endpoint; inactive levels contribute zero. Therefore

 F_m<=kappa*2^R sum_(t=0,...,m-1)lambda^t
     <=[kappa/(1-lambda)]2^R=(128/3)2^R<64*2^R.           (3.2)

This is where the OLD growing factor m disappears. The profile, search,
arity and instruments have NOT changed. The quantitative strict success
margin makes the weighted contributions of lower levels decay geometrically.

The odd decoder uses at most Smax K roots. Each of at most n 2-adic bits
uses an expected two roots/copies by the source's fair-parity law, including
when the odd answer was wrong; each new root has the same uniform bounds.
The indicator that a root is called is decided BEFORE its fresh work, so
the tower property applies without conditioning on a later decoder result.
Using H0=Smax K+2n exactly as the source, the entire uncapped ideal process
has expected acquisitions <=2 J_retry H0+2n<=Qstar and expected total weight
<64*2^R H0=Wstar. The +2n covers direct one-bit cases as in the source.

## 4. New actual cutoff and extraction correctness proof

Couple the actual protocol and uncapped ideal process until a label error,
fallback refusal or any of the other cutoffs. A refused next acquisition
implies the ideal total originals would exceed Qcap. A refused weighted
attempt implies its already-built children plus the original attempted
weight lie in the ideal run whose total weight exceeds Wcap. All that child
work/source cost remains counted. Markov with the NEW expectations gives

 Pr[ideal acquisition exceeds Qcap]<=2^-10,
 Pr[ideal weight exceeds Wcap]<=2^-10.                    (4.1)

This is unconditional ideal-process analysis, not conditioning a supplied
high-part law on cap survival. Statistical expectations establish cutoff
failure only; Section6 proves actual work using the hard caps on ALL branches.

All needed extraction arguments hold with the actual NEW parameters (1.2).
The cheap estimate remains wrong with probability<=1/(2n). Conditional on
k,k_A, the randomized verification rejects a correct k_A or accepts a wrong
one with probability<=e^-h_e, and a high-confidence RUN errs with probability
<=4(n+5)e^-h_e. All tests are the exact source nondestructive translations.
Thus at at most Qcap actual calls the wrong-report union bound is

 (4n+21)Qcap e^-h_e<=5*2^-18<2^-14.                       (4.2)

No successful-report or future-cap conditioning is used. The new high-
confidence fallback count has conditional trigger probability<=1/n. Its
Cf=ceil(Qcap/sn) and Qcap>=2048n satisfy the source Chernoff calculation:
for n>=256, a Bin(Qcap,1/n) dominating count exceeds Cf with probability
<=2^-20. This domination is sequential, not an independence claim about
adaptive fallback indicators. The source's calculation needs only (1.2),
(1.3), not its old Qstar formula. The new actual h_e is O(R), so all original
every-branch extraction work/width estimates still apply with the NEW Qcap.

The ideal signed-high-part/tree laws, odd multibit decoder, root tail and
2-adic parity are unchanged because the uncapped outer instrument is the
same. The frequency guard is still analyzed on UNGUARDED ideal roots and
added separately, not used to postselect a favorable characteristic law.
Its union bound is <=2^-20; odd-decoder error<=2^-19. Combine these with
(4.1), (4.2), fallback coupling and the original source proof:

 total failure<=2^-10+2^-10+2^-14+2^-19+2^-20+2^-20<2^-8. (4.3)

This proves full-secret recovery for the NEW cap/extraction program for
every n>=256 and modulus/secret. The original exhaustive n<256 branch has
failure<2^-10 and hence qualifies too. The actual output law need not equal
the old capped predecessor's; it is this NEW unconditional proof that gives
the stated guarantee. No positive malformed behavior is claimed.

## 5. Actual physical implementation and complete allocation

Instantiate the complete dyadic/typed measured-bank controller and shared
native ATTEMPT method of native-source.md with the NEW public cap/extraction
fields. All exact finite Boolean/Clifford+T word templates are supplied in
its complete helpers. Compute integer powers/ceilings/counters in the real
bit model and assign actual public word widths/offsets/padding afresh.
New rational-preprocessing fields have O(n) bits and polynomial scratch.
All original arrays, private erasure, source/decoder fields and generator
frames remain in a fixed O(n^2) classical pool; added arithmetic fits it.
No list of subsets or exponentially many original-source records is stored.

Let B be the next-power-of-two padded basis-bit capacity and H the complete
compact genuine pool. B=O(n^2),H=O(n). Map classical i to even wire2i,
genuine j to odd wire2j+1 and reserve the ENTIRE paired prefix through
2max(B,H)+3, including inactive/unused cells. Add n+1 raw temporary source
wires, the ONE reusable current-node residue matrix and compact input area
exactly as the full native source proves. All meaningful matrix R^2 bits,
row padding, cached handles and every genuine helper are counted. Full
address length stays O(log(n+2)). Unread passive originals are excluded
only under the challenge convention.

The physical classical input/output plus bounded O(w^2) generic staging and
a fixed number of native O(n) or O(R)-bit words occupy O(n) bits, including
all inactive reservations. Matrix/label lists/long frames stay banked, not
an R^2 physical classical array. Current matrix rows are read at CLASSICAL
outer-loop indices; genuine query controls stay coherent on odd wires.
All original source calls are one physical raw original followed by paid
SWAP to its designated genuine slots, never an inverse/control/source oracle.

For n>=2^4096 use the COMPLETE native pair ATTEMPT: residue measurement,
BOTH fixed-schedule searches with all trial/coin/clock/decrement work,
classical SAME-predicate verification, diffusion, pair projection,
compression and every failure reset. Precompute rho_j ONCE per admitted
node from its banked signed labels; no full-label scan or generic callback
occurs per Grover iteration. Row reads, pointer carries, controls and actual
inverse words pay their full address/generation charges. Its all-state
per-attempt bound remains C R^2 L w_i, L=max(1,ceil(log2n)), since changing
global cutoffs does not change this fixed local instrument.

For n<2^4096 use the generic dyadic bit interpreter for the ENTIRE NEW
logical program specified in Sections1-4. For n>=256 this means the new
caps, h_e,t_V,Cf and real extraction tests, NOT an unchanged old-caps program.
For n<256 it means the original exhaustive semantic branch. Each finite
program has explicit finite guards; polynomial/generic overhead on this
FIXED finite input-length prefix contributes an absolute outside constant.
This never absorbs an unbounded factor on the large native branch. Both
modes have the same O(n) physical classical and O(n^2) full quantum bound.

The physical implementation executes exactly the NEW semantic instruments.
The full-reference hybrid CQ invariant is the supplied native-source.md6
argument instantiated with these current fields: decode native active words
and banked inactive records, relabel genuine slots and forget deterministic
copies. READs copy already-classical records; WRITE/erase/source moves and
native words preserve the decoded state, including arbitrary references.
Private unsigned/sign/EXTRACT copies are forgotten at their logical release.
No readout/cache transcript becomes new routing, randomness or source feedback.
This transfers the NEW proof (4.3) to the physical machine with ZERO added
loss, rather than transferring a parent output law after changing its caps.
Output the entire result FIRST, then pay trace-and-zero release of every
bank/genuine/raw/padding/staging field. No hidden unbounded transcript remains.

## 6. Deterministic actual work and supported joint envelopes

On every actual large-branch path the ORIGINAL per-node weight is debited
against the NEW literal Wcap, so the supplied native cost gives

 T_native<=C R^2 L Wcap
          =O(n R^2 L 2^R)
          =O(n^2 L^2 2^R),                               (6.1)

using H0=O(n), R^2=O(n log n). No expectation is used for this resource
bound. Failed searches, late failures and refused-attempt children are
counted; native clock work and source actual adjoints are not free.

All remaining generic work, source/extraction/signing, full labels, frame/
mode/matrix/handle work and full decoder costs retain the explicit bound

 T_gen<=C n^20(Qcap+q0+1).                                (6.2)

The complete native source supplies the termwise operational ledger:
O(nQcap)+poly(n) node events from disjoint nonempty input acquisition sets,
polynomial word/matrix/mode work per event, O(n^2 log n Qcap) extraction,
O(n^3 K q0+n^3 K) streamed decoder and polynomial public setup, with the
whole generic field/generation/address cost included. The new public integer
power/division and recomputed metadata add only polynomial bit work; their
widths are O(n). Both new caps have at most the old widths plus a fixed
constant, and Qcap<=old_Qcap. The same generous degree20 therefore covers
all these real actions. No repeated Grover action is left in (6.2).

Source9.4 proves q0,old_Qcap=O(n^-A 2^R) for EVERY fixed A. Since Qcap is
smaller, the statement holds for the NEW Qcap. Choose A=64: (6.2) is
O(n^-44 2^R+n^20), absorbed in n^2 L^2 2^R, because R/log n tends to
infinity. This is an explicit superpolynomial cap gap, not hiding generic
polynomial work in a tight loop or changing a cap only in a display.
The fixed finite generic prefix in Section5 is separately bounded.

Finally the original ACTUAL profile has
2^R=O(2^(a sqrt(n log2n))) with the exact a in (0.1), including its explicit
threshold and finite-prefix proof in gps-source.md9. This profile is
unchanged. Combining (6.1)-(6.2), public computation, initialization and
output-first cleanup proves the stated EVERY-BRANCH time. Entire physical
space is SCn,SQn^2 from Section5, not a virtual classical/coherent pair.

Every acquired/discarded/failed original is in the NEW hard Qcap, so
Q=O(2^(a sqrt(n log2n))). Zeros, extra bank reads, integer preprocessing,
source SWAPs and native known words create no original samples. The fifth
expression is EXACTLY0 under its literal independent-ideal-copy model.
All N,s, including the finite cases, have success at least1-2^-8 jointly
with these four actual bounds. No robustness/impossibility is inferred.

For time and samples log2 of the representative is a sqrt(n log2n)+O(log n),
giving exact growth index1/2. The two polynomial space indices are0. All
five supported structures concern THIS one modified physical configuration;
only the time index is the numeric objective. The saving from the former
n^(5/2)(log n)^(3/2) to n^2(log n)^2 is the unbounded removed retry-level
factor m=Theta(sqrt(n/log n)), not a change of the inner coefficient or an
arbitrarily strengthened slack-envelope display.
