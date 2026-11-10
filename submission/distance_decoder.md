# Reference algorithm P, Sections 10-13: distance and block recovery

This file is part of the full specification and proof of IFC-CRITICAL-SCHEDULE.
virtual.md contains Sections 0-9 and 14-17; virtual2.md contains the capped
schedule, chunked pool and MERGE4I. Section numbering and P references are
shared across those files. Set b0=floor(ell/2)-4 once the schedule is known.

## 10. Held-out-bit independence and source distance

The odd-part supplier gives independent uniform labels in [0,2^(B+1)). For a
2-adic block the supplier instead gives independent uniform labels in [0,2^wd),
with B=wd-b and 1<=b. Both cases have independent fair bits at position B.
Write

    k_j = low_j + 2^B tau_j + 2^(B+1) high_j,
    0<=low_j<2^B, tau_j in {0,1}.

The tau_j are i.i.d. fair and independent of all low_j and high_j. For a batch,
let G contain the low_j and high_j of every source coordinate, all FW/PREP and
merge outcomes, and the logical controller decisions of BATCH that read label
bits below B: groupings, keys, residues, trimming, ranks, chunk requests, FAIL,
retries, aborts and assignment of qubits. It excludes the tau_j, root measurements,
and all LE-private estimates, verification outcomes, fallback counters and internal records,
and all key-preparation retry/cap state, which feed no decision in the ideal run. Full label
values may be stored and added, but their bits at position B and higher do not
choose the grouping, residue measurement or index maps; those use positions
strictly below B. Score evaluation occurs after BATCH returns. This is a
conditioning statement about the logical reference law, not a disclosure
restriction on the algorithm's classical records.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the held-out bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). The supplier's acceptance decisions
(Section 11) read only whether k < 2^(B+1); given acceptance k is uniform on [0, 2^(B+1)), the law used above. Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
PREP outcomes touch only fresh ancillas and depend on no label, and FW outcomes have the law of
Lemma 7.1(a) whatever the labels and the past (it applies at every FW by (P)); returned and recycled
qubits carry explicit tables, sums of leaf labels, so their later keys again read only bits below B. By Lemma 6.1 and Lemma A.1 each merge and MERGE4I outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low,high) x law(outcomes and decisions | low,high). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in FW the index maps
alpha -> (alpha, 1 - alpha) on the pair (A_a, A_b) of a good output and alpha -> (alpha, ..., alpha) on the block
Bl of a recycled output are injective on disjoint coordinates, and a returned qubit keeps its table; a LEAF table
concatenates disjoint coordinates; and a merge or MERGE4I re-indexes injectively pairs or four-tuples on disjoint coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j-x0_j))/2^B + 2 sum_j high_j(x1_j-x0_j) is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)


Lemma 10.2 (source-coordinate distance). In every ideal batch, any two distinct
indices of any phase vector built above the final pool have incidence vectors
whose Hamming distance is at least 2^ell. In particular every actual root has hd>=2^ell. The distance bound is not asserted for artificial phantom leaves used only in the exhaustion proof.

Proof. Associate to each live labeled qubit the set of original source coordinates
in its two entry vectors, and the Hamming distance between those entries. These
sets are disjoint for different live qubits: initially each uses one fresh copy;
FW partitions its input qubits into disjoint pairs, the possible recycled block,
and returned qubits. Failed merges discard inputs, never reusing them.
At pool level i each input distance is at least 2^i. A good FW output from A,B
has distance delta_A+delta_B, since its entries select opposite entries of both
inputs on disjoint coordinate sets. A recycled output has distance the sum over
its block, whose size is at least two (Ev uses all w); returned qubits keep their
distance. Thus every good output at that level has distance at least 2^(i+1),
regardless of how many earlier FW or recycling operations precede it. Induct through
all ell levels. A LEAF table is the product of dl such qubits, so any two distinct
indices differ on at least one qubit with distance>=2^ell. A binary/four-input
merge restricts and injectively reindexes tuples of disjoint child coordinate
sets. Distinct output indices differ in at least one child, so the distance
bound persists. This proves the statement without a distributional assumption
on the selected table entries. QED.

Put b0=floor(ell/2)-4. Since ell>=r/2+64 and r>=2^20, b0>=r/4>=1.
For 0<=|phi|<=1/2, cos(pi phi)<=1-2phi^2<=exp(-2phi^2): use
sin(pi|phi|/2)>=|phi| in cos(pi phi)=1-2sin^2(pi phi/2). Therefore (10.2) strengthens to

    |E exp(2pi i phi W)| <= exp(-2^(ell+1)phi^2).                 (10.4)

In particular for |phi|>=2^(-b0-3) this is at most exp(-8). All conditional
expectations here use G as in Lemma 10.1, including higher label bits when present.


## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j=t b0 for t=0,...,T, with T the least t>=0 such that 2^(t b0+b0+3)>2M. There are at most (log2 M)/b0+1 stages.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. Serve each request of Section 7.3 for a chunk of D_0
leaf qubits by repeating, until D_0 qubits are accepted: acquire a fresh copy, apply Mult_(alpha_j), run LE to obtain k,
accept iff k < 2^dn (otherwise discard) and on acceptance apply X to the control. If the batch has already made 4 C_0
acquisitions, ABORT instead. By Lemma 7.3(d) at most C_0 leaf qubits are requested per batch, so an ABORT means fewer than
C_0 accepted among the first 4 C_0 acquisitions. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), each
copy is accepted with probability 2^dn/N > 1/2, so by Hoeffding the abort has probability at most exp(-C_0/2). The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1} with W_i and beta_i. Given W_i and beta_i,
E Z_i = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + Y + 8 and identify an integer c with the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in
[0, 2^(P_0)). Stage j>0 (whose predecessor is j-b0) uses every c within circular distance rad_j=2^-(j+2) of the previous center z_prev; both
z_prev and rad_j are multiples of 2^-(P_j), so the arc endpoints are candidates. There are at most 2^(Y+8) candidates.

Score. For each candidate, with exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate candidates in increasing order, keeping the K residues (f_i c) mod 2^(P_j), updating each with one addition per
step, and keep a running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have fixed lengths.

Lemma 11.1. Suppose theta is within circular distance rad_j of z_prev (no condition when j = 0). In the ideal run,
conditional on BATCH not aborting, with probability at least 1 - 2^-20/n, theta is within circular distance 2^-(j+b0+3) of z_j.

Proof. Condition on the past of the stage and on G. For a candidate point zeta let Delta = theta - zeta as a circular
difference, and xi_i = Z_i cs_(beta_i)(f_i zeta). Given G, the roots use disjoint leaves and independent coins, and their
measurements are on separate qubits, so xi_1, ..., xi_K are independent with values in [-1,1]. Averaging over beta_i,

    E[xi_i | G, W_i] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(2 pi f_i theta) sin(2 pi f_i zeta)] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

Near point. The candidate zeta0 nearest theta has |Delta0| <= 2^-(P_j + 1). By (9.2), |f_i| <= 2^(j+Y+1), so
|f_i Delta0| <= 2^-8 and E[xi_i | G] >= (1/2) cos(pi/128).

Far points. Call zeta far if |Delta|>=2^-(j+b0+3). In stage 0, |Delta| <= 1/2. In stage j >= 1, theta and zeta lie within rad_j of
z_prev, so |Delta| <= 2^-(j+1). So xx=2^j|Delta| lies in [2^(-b0-3),1/2]. By (10.4),

    E[xi_i|G] <= (1/2)exp(-8).

Concentration. By Hoeffding each fixed candidate's sum deviates from its conditional mean in the required direction (down for the near point, up for each far point) by at least K/64 with probability at most exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) exp(-8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128)-exp(-8)) > 0.49 > 2/64+2/625. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The output error at stage j is at most 2^(-j-b0-3), smaller than rad_(j+b0).
Thus it is a valid incoming center for the next stage j+b0. Arc endpoints lie on
the next grid because the precision increases by the integer b0. The nearest-grid
argument and the at-most-2^(Y+8) candidate count are unchanged. Union over stages
(which number at most n) gives failure <=2^-20. At the terminal stage,
2^(-j-b0-3)<1/(2M); output s1=floor(M z_j+1/2) mod M.


## 12. 2-adic part in blocks

If a2=0, return s=s1. Otherwise keep g recovered low bits and their integer s2low,
initially g=0 and s2low=0. At a step put wd=a2-g and sh=s1+M s2low mod N.
When the prefix is correct, s-sh=M2^g rem mod N for rem in Z/2^wd. Acquire a
copy, apply Shift_sh, run LE to obtain k, apply X, and record kk=k mod2^wd.
Since 2^wd divides N, kk is uniform in [0,2^wd); its ideal coin phase is
exp(2pi i kk rem/2^wd). Each accepted leaf uses one acquisition, with no rejection.

If wd=1, process exactly K such copies one at a time, releasing each after use. If some kk=1, measure the first such
coin in X and recover rem exactly; if none, choose zero. Discard the remaining
copies. The chance of no kk=1 is 2^-K. Set the last bit and stop.

If wd>=2, put b=min(b0,wd-1), B=wd-b>=1. Run BATCH with this B and the supplier
just defined, using its same deterministic chunk/run caps. At most C_0 copies
are acquired. A root has known integer W=(lab[1]-lab[0])/2^B and state
(|0>+exp(2pi i W rem/2^b)|1>)/sqrt2. Measure its K roots in independently fair
X/Y bases, recording Z_i,beta_i,W_i mod2^b. Enumerate every c=0,...,2^b-1 and
maximize sum_i Z_i tab_beta_i((W_i c mod2^b)/2^b), breaking ties toward smaller c.
Set the next b bits to that maximizing c: s2low +=2^g c, g+=b. Repeat.

Correctness conditional on a correct prefix. The true c=rem mod2^b is a grid
point with ideal mean score K/2. For a wrong c, take phi=(rem-c)/2^b modulo one
in [-1/2,1/2], so |phi|>=2^-b>=2^-b0. Lemmas 10.1-10.2 apply to the uniform
labels kk, with position-B bits held out and higher bits included in G.
By (10.4) each wrong candidate has mean <=(K/2)exp(-8). Hoeffding with threshold
K/64 per candidate, plus the K/625 table error, separates the true candidate
from every wrong one, since (1/2)(1-exp(-8))>2/64+2/625. There are 2^b<=2^(Y+8)
candidates (b<=ell/2<=H<=Y), so the same K yields conditional failure <=2^-20/n.
The next prefix is therefore correct except for that bounded event.

The implication about coin phases is only needed when the incoming prefix is
correct. On all other branches the source, circuit and enumeration caps still
hold deterministically. Union bounds over first errors establish correctness,
without assuming a wrong prefix produces the intended phase law. Finally output
(s1+M s2low) mod N. The last wd=1 branch can occur only once.


## 13. The complete algorithm and its success probability

Finite branch (n < 2^40). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and
reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For
cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^40). Compute a2,M,dn,K,the schedule,b0,Y, and all allocations; put

    Qcap = 20 r C_0 + K.

Before sources, run the guarded n-only template construction and select
cheap-estimation mode as in approx_estimate.md. Initialize both global key counters to0 and their M_K/F_K thresholds
as in seed_retry.md, and initialize the global verified-extraction fallback
counter. These are not reset between batches or levels. Run Section11
and then Section12. Any ABORT releases everything and outputs0.
There are at most (log2 M)/b0+1 odd batches and a2/b0+1 2-adic batches, plus
at most one wd=1 leaf branch. Thus the number of BATCH calls is at most n/b0+2
<=4r+2<=5r<=n. Odd batches use at most 4C_0 acquisitions each, 2-adic batches
at most C_0 each, and the leaf branch at most K. Hence Q<=20rC_0+K=Qcap on
every branch. LE is sized by this cap before any request. All state-dependent
choices leave the bit-progress and source caps unchanged even after an error.

Success. In the ideal run the failure events are: a pool exhaustion, at most 5r * r^-63 = 5r^-62 < 2^-10 (Lemma 9.1); a pool-stage abort, at most
2n(ell+1)C_0 exp(-2^H/(10 ell^2 w^2)) (Lemma 9.2), and a supplier abort, at most n exp(-C_0/2), both below 2^-40
because H >= r/2 >= 500000, w<=2r^2, 2^H <= C_0 <= 2^(2r-1) (F6) and ell, n are
at most polynomial in r; a likelihood-decoder error, at most 2^-20 (Sections 11 and 12, over at most n total batches); a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling of verified_extract.md and the separate global
key-cap failure at most2^-80 from seed_retry.md:

    Pr[output = s] >= 1 - 2^-10 - 2^-40 - 2^-40 - 2^-20 - 2^-40 - 2^-10 - 2^-80 >= 1 - 2^-8 > 1 - 2^-7 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable
labels or outcomes.


