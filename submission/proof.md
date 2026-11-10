# CS1-GCAP: a growing terminal plateau

## 1. The algorithm and the scope of the included source

For every N >= 2 and s in Z/NZ let n = ceil(log2 N). CS1-GCAP is the
following single uniform algorithm. Its primitive circuits, measurements,
source transformations, label extraction, odd-part decoder, 2-adic decoder,
and finite branch are specified in the included cs1_base.md. That file is
an unmodified copy of the CS1 proof from Yukon submission
f1481815-9577-4990-abe3-7b79fa5d9284, candidate commit
200ef0387acb280adcd272f4fbcdb805d1786bbe. It is included as technical source,
not as an appeal to its verdict. Its original theorem concerns its original
parameters; the theorem for GCAP is the one proved here. The parameter and
resource changes below supersede Sections 0, 7 and 11--14 of that source
where applicable. All other instructions are retained literally. In particular,
we use its original verified Kitaev label extraction, not later Fourier-circuit
variants. The proof snapshot contains every circuit and probability argument
needed here; fetching a reference is unnecessary for review.

GCAP outputs s with unconditional probability at least 1 - 2^-8, with all
resource bounds below holding on every branch, including caps, failures,
restarts and wrong-label branches. All constants are absolute. Put

    H(n) = sqrt(2n) + (2n)^(1/4),
    E(n) = a sqrt(n) + (6/5) n^(1/4),
    F(n) = a sqrt(n) - (5/4) n^(3/8) + (6/5) n^(1/4).

Here a is EXACTLY u_333/v_333 defined and written in cs1_base.md Section 0;
the displayed Pell recurrence proves a > sqrt(2), without a numerical fit.
The joint bounds are

    T = O(n^4 (log2 n)^2 2^E(n)),
    S_C = O(n^2 2^F(n)) bits,
    S_Q = O(n) qubits,
    Q = O(n^(3/2) (log2 n) 2^E(n)).

The main branch is n >= 64. The original exhaustive finite branch is used
unchanged for n < 64, including its n+10 tests per candidate. Since only
finitely many N occur there, its costs are absorbed in absolute constants.

## 2. Exact parameter computation and schedule

For a TREE_D call let B=D-1 >= 1. Define using integer arithmetic

    mu = ceil(sqrt(2B)) + 1,
    r = ceil(sqrt(mu)),
    U = mu + r,
    s = min(mu-1, floor(mu^(3/4))),
    kappa = ceil(log2 U) + 1,
    m = min{z >= s+1: z(z+1)/2 - s(s-1)/2 + kappa >= B}.

Here floor(mu^(3/4)) means the largest integer v with v^4 <= mu^3;
ceil square roots and ceil logarithms are integer comparisons, not real
arithmetic or advice. Binary search computes them with polynomial work.
Use the original Section 7 formulas, with THESE mu,s,kappa,m:

    lam_i = kappa+1+min(i,m-s),  0 <= i < m; lam_m=1,
    bmax_i = i,                         0 <= i < m-s,
    bmax_i = m-s+1,                     m-s <= i < m-1,
    bmax_(m-1) = kappa+2(m-s)+1.

Allocate b_i from the root down greedily as in that source, summing to B.
The leaf takes kappa+1 qubits, as in the source; no leaf boost is used.
Depth-first evaluation, failed-input disposal and VEC retries are unchanged.

Lemma 1. The schedule exists, s+1 <= m <= U, all b_i >= 0, and every merge
fails with conditional probability at most 2^-kappa <= 1/(2U) <= 1/(2m).

Proof. mu >= 3, 1 <= s <= mu-1, and s^2 <= mu^(3/2). Since r >= sqrt(mu),

    U(U+1) - s(s-1)
    >= mu^2 + 2mu r + r^2 + mu + r - mu^(3/2)
    >= mu^2 >= 2B.

Thus U meets the capacity inequality and U >= s+1. The original exact sum
identity remains valid:

    sum_i bmax_i = m(m+1)/2 - s(s-1)/2 + kappa >= B.

The greedy allocation therefore exists. Substitution, separately for growing,
capped and root levels, gives b_i+lam_(i+1)-2lam_i <= -kappa, exactly as in
(7.1) of the included source. Its distribution-free counting proof Lemma 6.1
then gives the failure bound for every pair of input tables, without a
random-label assumption. Finally 2U <= 2^kappa < 4U. QED.

Let nq_D=2^m(kappa+1). Field widths remain B+1+i+ceil(log2(kappa+1))-p_i.
The quantum stack is O(m(kappa+m))=O(n) because U=O(sqrt n). All label
widths are O(n), and lam,b=O(sqrt n), uniformly for B<=n. These asymptotic
bounds also hold for small B; constants cover any finite exceptions to the
source's convenient numerical inequalities such as '8n' and '3n'.

## 3. Revised acquisition cap and correctness

For B=n compute mu*,r*,U*,kappa* by the definitions above. All these quantities
are nondecreasing in B, so m(B)<=U* and kappa(B)<=kappa*. Replace Q* by

    nq* = 2^U* (kappa*+1),
    K* = 2^13 (ceil(log2 nq*) + ceil(log2 n) + 30),
    Q* = 6*2^U* (kappa*+1) (n K*+2a2) + 2a2,
    Qcap = 1024 Q*.

The actual decoder uses J,K,a2 from the included source's Sections 9--11;
its odd-part acquisition contribution is at most n K*. When M=1 that
decoder is skipped entirely, and no J or K is required. All LE parameters, the acquisition down-counter,
and fallback cap are computed from this revised Qcap. On an acquisition
or fallback overflow, release everything and output 0, as before.

The correctness proof is unchanged in substance but its parameter checks
are supplied here. An accepted leaf has the same uniform label law. Lemma 1
makes the retry multiplier rt=2^kappa/(2^kappa-1) satisfy

    rt^m <= exp(m/(2^kappa-1)) <= exp(m/(2m-1)) <= e < 3.

Thus the expected acquisitions for a root are at most
6*2^U*(kappa*+1), and the complete ideal uncapped run uses at most Q*
acquisitions in expectation. Markov bounds acquisition-cap failure by 2^-10.

No residue operation reads the top label bit: all measured windows still
lie below B and all reindexing uses only those windows and index order.
The induction of cs1_base.md Section 8 therefore applies to the new schedule
verbatim. In particular |E exp(2 pi i phi W)| <= |cos(pi phi)| and W is odd
with probability 1/2, conditional on the low-bit tree history. Distinct
root indices still have distinct incidence vectors. Its odd-part decoder
Lemma 9.1 and exact 2-adic recovery therefore retain their original error
bounds, now using the actual nq_D in K and the candidate grid.

The LE error argument is uniform in the adaptive history. Since
log2 Qcap=O(sqrt n), h_e=O(sqrt n) remains true. Moreover Qcap is at least
the original lower bound used in Lemma 5.2, because U*>=mu*. Its cap
Cf=ceil(Qcap/ceil(sqrt n)) and the same cheap-estimate and verification
bounds still give fallback overflow probability <=2^-20. The per-label
union bound is <2^-11, using h_e=ceil(log2(Qcap(n+5)))+14. The actual
and ideal capped runs couple except on those events. Consequently

    Pr[output=s] >= 1-2^-20-2^-10-2^-11-2^-20 >= 1-2^-8.

All statements are unconditional and for every N and s, with clean,
independent ideal copies. Epsilon(n)=0 is the tolerance guarantee; no
claim of a maximum possible tolerance is made.

## 4. Every-branch resource analysis

Write x=sqrt(2n). Since mu*<=x+2 and ceil(sqrt(mu*))<=sqrt(mu*)+1,

    U* <= x+sqrt(x)+4 = H(n)+4.

The elementary estimate sqrt(x+2)<=sqrt(x)+1 holds for x>=1.
Thus 2^U*=O(2^H(n)), kappa*=O(log n), 2^kappa*=O(sqrt n).
The decoder uses K=O(log nq+log n)=O(sqrt n) roots per stage and at most
n stages. Its nq <=2^U*(kappa*+1). Hence

    Q <= Qcap = O(n^(3/2) (log2 n) 2^H(n)).

The original every-branch charging argument (Lemma 11.2) uses only
m=O(sqrt n), 2^kappa=O(sqrt n), lam,b=O(sqrt n), and fixed caps. Each
acquisition is charged at most one merge per level, even on wrong-label
branches, because failed inputs are discarded. It yields

    core work = O(n^2 log n)Qcap + O(n^(5/2)nq) + poly(n)
              = O(n^(7/2)(log2 n)^2 2^H(n)).

This includes label extraction and its capped high-confidence runs,
transforms, table construction, generation, initialization, disposal,
measurements and classical arithmetic. Source cost is (n+1)Q.

The quantum stack remains O(n), including data, labels, merge scratch,
and transform arithmetic. The classical stack has O(m) tables, at most
2^(kappa+1+m-s) rows each, and O(n)-bit fields. Merge scratch is smaller.
Decoder records and LE scratch are polynomial. Thus uniformly over the
actual TREE_D calls,

    S_C <= O(n^2 max_(1<=B<=n) 2^(m(B)-s(B))) + poly(n).

For every integer mu>=3, floor(mu^(3/4))<=mu-1 (because mu^(3/4)<mu),
so s=floor(mu^(3/4)) >=mu^(3/4)-1. Consequently

    m-s <= mu+sqrt(mu)-mu^(3/4)+2.

The function f(z)=z+sqrt(z)-z^(3/4) is increasing for z>=1, since
f'(z)=1+1/(2sqrt z)-3/(4z^(1/4)) >=1/4. Also mu<=x+2. Therefore

    m(B)-s(B) <= f(x+2)+2
                <= x+sqrt(x)-x^(3/4)+5
                 = sqrt(2n)+(2n)^(1/4)-(2n)^(3/8)+5.

We used sqrt(x+2)<=sqrt(x)+1 and (x+2)^(3/4)>=x^(3/4).
This establishes the stronger real-radical space bound

    S_C=O(n^2 2^(sqrt(2n)-(2n)^(3/8)+(2n)^(1/4))).

Polynomial ancillary storage is absorbed because the exponent is eventually
positive and of order sqrt n; the finite initial range only changes the
absolute constant. Address cost log2(S_C+S_Q+2)=O(sqrt n). Multiplying the
core-work bound by that charge, and adding source costs, gives

    T=O(n^4 (log2 n)^2 2^H(n)).

These allocations and caps are deterministic bounds, not expectations.

## 5. Exact structured envelopes and comparison

a>sqrt2 is proved by the Pell recurrence in the included source. Further,
(6/5)^4=1296/625>2, so 6/5>2^(1/4), and
(5/4)^8=390625/65536<8, so 5/4<2^(3/8). Termwise comparison therefore gives
H(n)<=E(n), and

    sqrt(2n)-(2n)^(3/8)+(2n)^(1/4) <= F(n).

No unspecified coefficient inside an exponential is substituted in a
structured object. The retained polynomial factors are precisely those
proved above. The envelopes are 2^E n^4(log2 n)^2, 2^F n^2, n, and
2^E n^(3/2)log2 n, respectively. The three exponential envelopes have
log2 B=a sqrt n+o(sqrt n), so log2 log2 B=(1/2)log2 n+O(1)+o(1).
Their exact growth indices are 1/2. The envelope n has index 0. Constants
and the finite branch do not change these limits.

This is a time/space tradeoff, not a claim that GCAP dominates CS1 in all
resources. It has a larger explicitly retained n^(1/4) term in time and
samples, but a classical-space saving of order n^(3/8) in the exponent.
Its classical envelope is eventually smaller than
2^(a sqrt n - c n^(1/4)) times any fixed polynomial for every fixed c.
It preserves O(n) quantum space and time growth index 1/2. It does not
achieve the challenge's 1/3 goal. Other submissions can have different
tradeoffs; no global frontier membership is asserted without comparison.

## 6. Provenance

The complete CS1 source and its proofs are reused from submission
f1481815-9577-4990-abe3-7b79fa5d9284. In particular, source-label extraction,
linear merge/reindexing, the top-bit characteristic function, general-N
CRT decoding, finite branch and cutoff accounting are inherited. Their
prior published sources are identified in cs1_base.md Section 1, including
Kuperberg arXiv:1112.3333v1 and the earlier COL3 submission. The growing
mu^(3/4) terminal plateau, its U=mu+ceil(sqrt mu) depth certificate, and
the resulting explicit mixed-power resource analysis are the change here.
CS1-LBQ's public note was read as a comparison with constant-multiple
sqrt(mu) caps; none of its later leaf-boost or Fourier-circuit changes is
used. Earlier verdicts are not a premise of this proof.
