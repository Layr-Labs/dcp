# Filtered search with a fixed amplification schedule

Status: a parent mathematical draft responding to Opus's Track A recommendation.
The new search lemma below is self-contained. The DCP application uses the
copied, hash-verified ROB-G2 record construction. This packet is not submitted,
has not had an independent review, and does not claim a production circuit replay.

## 1. Interface and deterministic parameters

Let D=2^n. A fixed classical record string contains Q records and defines exact
rational scores z_i(t) in [-1,1] for 0<=t<N<=D. Let theta be rational. Suppose,
on an event E of probability at least 7/8, there is the true secret s with

    mean_i z_i(s) >= theta+gamma,
    mean_i z_i(t) <= theta-gamma for every valid t != s,          (1)

where gamma>0 is an absolute constant. Invalid t>=N are rejected by every
predicate. The full predicate v tests mean_i z_i(t)>theta and t<N. It therefore
marks exactly s on E. The records may otherwise have any joint law. In
particular they need not be independent after conditioning on E.

For n>=20, set

    d = ceil(log2(n+2)), a = 4d+8,
    L = ceil(2/gamma^2) a,
    b = max(12,n-a+12), G=2^b,
    k = floor((isqrt(2^(n-b))-1)/2),
    j = floor(3 isqrt(G)/4).                                    (2)

Here isqrt is the integer floor square root. No real arithmetic is required to
choose these schedules. For all n>=20, G>=4096 and D/G>=256: indeed
n-b=min(n-12,4d-4)>=8. For smaller n use the inherited full-search fallback
described in Section 5. These are finitely many input lengths.

The filter sample is a list of L independently sampled record indices WITH
replacement. This deliberately changes the review's subset into a multiset.
Duplicates count in its mean and in all work and storage. It avoids any need
for sampling-without-replacement algorithms or an uncharged uniqueness test.

Generate each index with capped rejection sampling from ceil(log2 Q) fair bits.
Allow r=ceil(log2(128L)) trials per index. Each trial succeeds with probability
at least 1/2. If any index fails all its trials, output 0 and stop. The probability
of any such failure is at most L*2^(-r)<=1/128. Conditional on no failure, all
indices are independent and uniform, since each finite geometric sum gives
the same probability for every accepted index. This conditioning is independent
of the fixed records; no source is acquired after the records have been made.

The filter f(t) tests t<N and whether the mean over this indexed list exceeds
theta. It is a deterministic Boolean function once the list is fixed.

## 2. Filter retention and cardinality

Condition on any record string in E and successful index generation. Independent
bounded draws from that fixed string obey Hoeffding's inequality. Its standard
moment-generating-function proof applies directly to the newly drawn indices;
it makes no assumption about independence of the original records. Because
scores are in [-1,1],

    Pr[f(s)=0] <= exp(-L gamma^2/2) <= exp(-a) <= 2^(-a),
    Pr[f(t)=1] <= 2^(-a) for every valid t != s.                 (3)

Let H be the number of marked candidates of f, including s if it passes. By
linearity of expectation, not independence between candidates,

    E H <= 1+D*2^(-a) <= 1+G/4096 <= G/2048.

Markov and a union bound give the event

    F={f(s)=1 and 1<=H<=G/64}

probability at least 31/32-2^(-a). In particular it is at least
31/32-2^(-16). The last weaker uniform bound simplifies the final certificate.

This repairs the review's insufficient Markov slack. Its proposed
G=64(1+ceil(D epsilon)) does not by itself make H<=G/64 likely: that cutoff is
only an upper bound on the mean. For example H=t+1 with probability 1-1/t and
H=1 otherwise has E H=t but Pr[H>t]=1-1/t. The changed G above supplies the
required factor between expectation and cardinality cutoff.

## 3. Nested amplification, including integer rounding

Let O_f and O_v be the exact phase oracles of the filter and full predicate.
Let R_0=2|0^n><0^n|-I and R_u=H^n R_0 H^n. Define

    V=(R_u O_f)^k H^n,
    output state = (V R_0 V^dagger O_v)^j V|0^n>.               (4)

All scratch in both oracles is returned to zero. V^dagger is the actual reverse
gate word, not a source inverse or reflection about an unknown supplied state.
The routine holds no raw quantum source state at this stage. Global signs in
implementing R_0 or R_u only change an overall phase and cancel between V and
its adjoint.

On F, put h=H and theta_h=arcsin(sqrt(h/D)). Standard two-reflection algebra
gives the amplitude of each filter-passing basis vector after V as

    alpha = sin((2k+1)theta_h)/sqrt(h).                         (5)

This statement is obtained by multiplying the two real 2x2 reflection matrices
on the uniform-marked/uniform-unmarked plane. Since O_v marks exactly s, the
outer two reflections give success sin^2((2j+1)arcsin(alpha)). Other components
of V|0> form one normalized vector orthogonal to |s>; they need not be uniform.

Here are rational bounds valid for the entire parameter range, not just the
sampled grid in the earlier review. Write q=2k+1 and x=sqrt(D/G). Integer
rounding gives x-2<=q<=x. Since x>=16,

    (7/8)/sqrt(G) <= q/sqrt(D) <= 1/sqrt(G).

Also h/D<=1/16384, and arcsin(y) is between y and y/sqrt(1-y^2). Therefore
z=q theta_h satisfies z^2<=256/16383<1/63. Using sin(z)/z>=1-z^2/6,

    (377/378)(7/8)/sqrt(G) <= alpha <= (129/128)/sqrt(G).

The upper estimate uses 1/sqrt(1-1/16384)<129/128. As sqrt(G)>=64,
alpha<=129/8192<1/63; consequently arcsin(alpha)<=64 alpha/63. The outer
integer count satisfies

    (3/2)sqrt(G)-5/2 <= 2j+1 <= (3/2)sqrt(G)+1.

Combining these bounds puts the outer angle strictly between

    (3/2-5/128)(7/8)(377/378) = 70499/55296 > 5/4,
    (3/2+1/64)(64/63)(129/128) = 4171/2688 < 25/16 < pi/2.

The elementary bound pi>25/8 suffices here. On this interval sine is positive
and increasing. Its alternating Taylor series gives

    sin(5/4) >= 5/4-(5/4)^3/6+(5/4)^5/120-(5/4)^7/5040,

whose square is 245618323006225/272747603165184 >7/8. Thus (4) succeeds with
probability greater than 7/8 on every record/list pair in E and F. There is no
amplitude estimation, unknown stopping time, postselection or random iteration
count in this argument.

The resulting unconditional main-branch success is greater than

    (7/8)(127/128)(31/32-2^(-16))(7/8)
      =395079601/536870912 >2/3.                               (6)

The first factor pays for bad records, the second for index-generation failure,
the third for losing s or retaining too many candidates, and the fourth for the
quantum readout. All failures are part of the output distribution. On success
of neither condition the algorithm still terminates and outputs a residue,
reducing a measured invalid candidate modulo N if necessary.

## 4. Fully charged search resources

Let C_f,C_v be the complete costs of the two exact phase oracles, including
arithmetic, cleanup, circuit generation and addressing. The number of filter
calls is exactly k(2j+1), and the number of full-oracle calls is j. Uniform or
zero-state reflections and H layers add O((k(2j+1)+j+1)n) gates. Therefore

    T_search=O(sqrt(D) C_f + sqrt(G) C_v + sqrt(D)n log(n+2)).  (7)

No exponential gate list is retained. Forward and reverse streams use a fixed
number of binary loop counters of O(n) bits. Increment/decrement across each
full loop has amortized constant bit work; resets and bound computation have
O(n)-bit cost per invocation and fit (7). A fixed-depth nesting does not create
a stack of quantum states. Inverting a gate reverses its emitted word and uses
the exact adjoints.

Because

    sqrt(G)=max(64,4 sqrt(D)/2^(2d))
           <=64+4 sqrt(D)/(n+2)^2,                            (8)

an O(n^2 log^2(n+2)) full predicate contributes only
O(n^2 log^2(n+2)+sqrt(D)log^2(n+2)).

For the ROB-G2 score circuit, processing each record costs O(n log(n+2))
Boolean/Clifford+T gates, including reversals, and another O(log(n+2)) address
factor. Its n+p-bit stored expansion supplies all p-bit shifted windows with
p=O(log(n+2)); no n-by-p table per record is stored. A filter processes the L
explicit indices, so

    C_f=O(L n log^2(n+2))=O(n log^3(n+2)),
    C_v=O(Q n log^2(n+2))=O(n^2 log^2(n+2)).                  (9)

For either list, the accumulator width is bitlength(list length)+29. The
same explicit signed-score comparator and both its reversals apply, including
the t<N guard. The controller classically reads an index, then the selected
stored record; this is counted classical addressing, not QRAM. A reverse pass
uses the list in reverse, so all score scratch clears.

Index generation costs O(L log Q log(L+2)) fair bits, measurements and ordinary
binary operations before addressing. This is polylogarithmic in n with fixed
gamma. The L stored indices use O(L log Q)=O(log^2(n+2)) bits. The records occupy
O(n^2) bits and dominate that asymptotically. Filter/full accumulators use
O(log(n+2)) qubits and can share the original O(n) arithmetic pool.

Original acquisition and record preparation cost O(n^3 log^2(n+2)). This is
absorbed by 2^(n/2)n log^3(n+2); for example n^2=O(2^(n/2)log(n+2)). The constant
cosine-table generation, initialization and memory addresses remain charged as
in the copied construction. There are no approximate quantum rotations in this
algorithm. Its only precision is finite rational score discretization, already
included in (1) and in the inherited record proof.

## 5. DCP specialization and the exact inherited gap

The primary source is ROB-G2 submission 55a6ce76-34af-468f-b735-a1197f3d3459,
evaluated commit 77b383ed0ea3c8b9765c332de88add12c3d2b52d. Its complete proof is
copied unchanged as sources/ROB-G2-proof.md; SHA-256
64a87926620815ae4030997207eedff9f4507b5fb825c3c07d88c5794f566228 matches the official
evidence in the saved 2026-11-09 snapshot. Hosted validity is not a premise.

Use precisely its Sections 1-4.5 acquisition, rational table, and score circuit,
and its Section 4.7 exact phase-oracle construction for both list lengths. The
source count remains

    Q=2^33(n+4), epsilon=3333/10000.

Use the verbatim adaptive model in sources/error-model.txt, with SHA-256
fd67d2af7a9a9733f2422981afd4a6ce00bb9ceac8c29d345f29535cc0156475. Every delivery is
completed, measured and discarded before the private filter indices are drawn.
The adversary sees the same acquisition-phase outcomes as in the inherited
construction. Its future-free record concentration applies to every allowed
adaptive strategy, including one that knows our changed search algorithm.

The event G_0 in its Theorem 1 has probability >7/8 and supplies more than a
unique marked candidate: it gives all the mean gaps needed in (1). Put

    tau=2^(-24), R=1+tau, p_F=10^(-8), delta=1/50000,
    eta=(3pi+1)2^(-24), kappa=2R p_F+eta,
    Lo=(1-epsilon)(1/2-kappa)-epsilon(1/2+eta)-delta,
    Hi=kappa+epsilon(1/2+eta)+delta,
    theta=6667/40000.

Substituting pi<22/7 gives exact lower bounds

    Lo-theta >256318304059827/58720256000000000000,
    theta-Hi >24376142481/5872025600000000.

Both exceed gamma=1/250000. The table range in its Lemma T ensures the EXACT
scores z_i(t) are in [-1,1]. Thus all hypotheses of Sections 1-4 hold. This gap
is roughly four millionths on either side, not the review's roughly 0.0006
overall gap, which came from the less tolerant ROB-G configuration.

Run the filtered search for n>=20 and the original ROB-G2 output procedure for
n<20, reusing the identical records. The finite fallback has success at least
49/64 and never acquires additional copies. Its constant range does not affect
the bounds. Every branch, including bad records and index-generation failure,
has the fixed stated source count and bounded search schedule.

The resulting DRAFT all-modulus joint theorem is

    T=O(2^(n/2)n log^3(n+2)), S_C=O(n^2), S_Q=O(n), Q=2^33(n+4),
    epsilon=3333/10000 in the exact inherited adaptive model,
    success >=min(49/64,395079601/536870912)>2/3.

The indices remain (1,0,0,0). Compared with ROB-G2's full envelope, the proposed
time ratio is log(n)/n with the same other three envelopes and tolerance.
This is a candidate full-envelope improvement, not a lower time index or an
established new hosted frontier row. Our snapshot comparison does not establish
novelty against all submissions or all literature.

Constants are large. Here L=125000000000(4 ceil(log2(n+2))+8) records, counting
repetitions, and the inherited Q coefficient is 2^33. The theorem is asymptotic;
it is not a practical crossover claim. The source cap is NOT the n+1 cap of
PFD-N1. Only the O(n) sample envelope agrees.

## 6. Attribution, diagnostics and remaining work

The random-record filtering/nested-amplification proposal is from Opus 5.5's
2026-11-09 review. The parent repairs the cardinality slack, replaces subset
sampling by capped independent index sampling, supplies integer schedules and
the uniform sine bounds, and checks the exact ROB-G2 gap. ROB-G2 supplies the
entire robust measurement/score front end, arithmetic, error model and record
separation. These are material dependencies, not just comparators.

The standard-library checker verifies the rational certificates, the schedule
range over finite input lengths, and exact small H/phase-oracle circuits with
uncomputation. Finite checks are diagnostics; the inequalities above establish
the uniform conclusions. They do not compile ROB-G2's full table or simulate its
production source count. Independent proof review, complete candidate packaging,
admission checks and a fresh comparator audit remain required before submission.
