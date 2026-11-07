# Required appendix: PSG2-DENSE-E complete dense construction

This appendix and grover_dense.md, grover_dense_caps.md,
grover_dense_oracle.md, grover_dense_compiler.md and grover_dense_bound.md
define one complete selected algorithm. Sections 2--12 of the complete
source proof below are the actual dense substitution. H=2048 there is
the main's Hcap, not an odd-decoder scale. The whole instrument, probability,
nominal ratio, old q0/C/Wcap, source guard, pool and all-branch proofs
are included. Mathematical target references mean the package-local
profile/source/decoder proofs. Historical source identities remain credits.
The old .71 and polynomial resource displays are valid auxiliary bounds;
main (9.5)/(9.9), the cap and rational appendices give the selected final
.708 envelopes with kappa=5/32 and zero outer prefactors.

The source reproduced verbatim below is dense_cyclic_source_transfer.md,
29,686 bytes, SHA256
b9404e273739276a67c5d48d699a2dd0a0d1c7abf7323714a3fb438857c209d9.
Its original bounded-note status records provenance; no external proof or
verdict is required because every argument is in this package.

## Complete verbatim dense proof

# Dense cyclic extraction with k=b+5

## 1. Scope and exact sources

This is a bounded transfer proof. It changes no existing proof package,
cyclic note, declaration, stage or upload. The proposed substitution below
has complete local circuit, probability, guard and resource proofs. A full
candidate still needs its own integrated proof and joint review.

The target is the fixed PSG2-GBGR package:

- `grover_grouped.md`, SHA256
  `079b9fcd68c7d0e0a116efd8dda21586fa723f6eff8a89aa6e8e8e9e98283744`;
- `grover_grouped_caps.md`, SHA256
  `5b66577a50211a3fac45beb0efcfda0cf94ba387c7d3e2748fb6ea81c16b875c`;
- `grover_grouped_oracle.md`, SHA256
  `d34f10863ec822ea9e1153f501eae1e7c1a9337a8d4ac4847f75a060aa2c0414`;
- `grover_grouped_compiler.md`, SHA256
  `cf4b575204c25ef8a0911fd4ebefca5ce465267acd91931d14569584d9cf551d`.

Its declaration is SHA256
`115919ddb0fe5a7e44a26b09a6de7cb56b10de6a7b468e503bf7015e3af6f8be`.
The immediately preceding bounded cyclic transfer is fixed at
`cyclic_source_transfer.md`, SHA256
`7d50d62868a6b442d5caa5a6f1792902ee74e143097e7152412d76d7992b80ac`.

The cyclic instrument is inherited from CYG1 and its CYC1 source. The exact
CYG1 archive was read before this task: submission
`70564803-3637-426f-9587-e1333aa07b39`, commit
`ed8984b1d82c7fb891d1ba200c13743589abd34d`, proof SHA256
`c7903f95a1165d6587f1e09a10cee11d7df74590aefd8efc92f18cf89bcf8aa1`.
CYG1 credits CYC1, submission `7a4cecdc-7941-4027-8c95-8520de9fbcf3`,
commit `cd8f16692833b52dd0fd3a8dd335667eec5a6e61`, proof SHA256
`e75607fc05101e99cac8480cfbffc23729c64f6f5a03643ee02de917274b4a17`,
and PSG1's separate-query bounded discovery and fresh-label induction.
The preceding note contains their complete source identities and read
chronology. This task did not directly inspect a CYC1 archive.

The exact two-row determinant argument was also used in the earlier
PSG14C transfer note, SHA256
`42ef49d4387927b1c9c6cf2eeaa7889c7e9fa61c3cff1a849993d39adec8e318`.
It preserves PSG14C's credits to CYG1 and CYC1. The present note uses
pairwise moments with mean near 32. It does not require the seven-moment
bound. No acceptance, previous review or finite census is a premise.

## 2. One specified dense substitution

Put n=ceil(log2 N), L=log2 n. Keep the target's finite n<256 algorithm.
On its main branch keep exactly its truncated profile

    delta(v)=ceil(log2(3(2v+1)))+1,
    u=floor(sqrt R), u<=v_1<...<v_m=R,

where R is the least feasible profile for capacity n. Allocate B=D-1
canceled bits greedily from the root down for each tree width 1<=D<=n,
with 0<=b_i<=2v_i and sum b_i=B. At a positive width use

    k_i=b_i+5

fresh children. At zero width use the existing one-child shortcut; it has
no attempt and does not add four children. Keep the same frequency bound
q0, root constant C, root count F, precision budget and weighted cap:

    q0=(2u+1)2^(R-u),
    C=6(2u+1)2^(R-u-(m-1)), H0=F+2n,
    Qcap_old=1024(C H0+2n),
    Wstar=6*2^R H0, Wcap=1024 Wstar.                  (D1)

Sections 6--7 below prove that these old q0 and C bounds still hold.
Thus the same strided decoder and pool parameters are used exactly.

Set the verified-list cap H=2048. If k<13, enumerate all 2^k<=4096
indices and retain the first H solutions. Otherwise use at most H blocks
of at most 128 trials. Each trial uses uniform j in [0,J0),
J0=2^ceil(k/2), a new uniform k-bit query, exact Grover membership in the
measured fiber excluding the found list, measurement and classical
verification. Stop a block on a new solution and discovery at an empty
block or H solutions. Every solution is verified and distinct.

Use the exact grouped G1 and physical stored-tape implementation, with
k=b+5 in their explicit loops and allocation. Retain the original phase
index during the separate query discovery. Use the cyclic instrument
below on the verified list. After any failure release all inputs and
start with fresh children. The new source guard is

    alpha=25/72, beta_m=min(1,32 alpha^m),
    Qstar_dense=beta_m C H0+2n,
    Qcap_dense=ceil(1024 Qstar_dense).                (D2)

Keep the before-action weighted check at nominal weight 2^v. Compute
D2 before acquiring copies. Check it before every raw acquisition.
If either guard would fail, abort before its action, reset/release the
current state and output zero. No cap interrupts an uncounted subroutine.

## 3. Complete cyclic instrument with eleven rank bits

The k=b+5 child phase qubits have full signed labels a_j divisible by
2^p and joint state proportional to

    sum_x exp(2pi i theta A(x)) |x>,
    A(x)=sum_j a_j x_j.

Set c_j=(a_j/2^p) mod2^b. Compute f(x)=sum_j c_j x_j mod2^b by the
target's fixed-query wrapper: k CNOTs copy x to a zero query z, stored G1
adds f(z) into a zero accumulator, and the same k CNOTs clear z. Measure
and reset the accumulator to obtain e. G1 preserves z and clears all
its helpers, so this is the exact coherent f(x) map, also with references.

Let F_e be the true fiber, f=|F_e|>=1. The original register has equal
magnitudes on F_e and its original phases. Keep it untouched during the
separate-query discovery. Sort its verified list by original binary index:
x_0<...<x_(h-1), h<=H. If h<2 fail and release the inputs. Otherwise:

1. Compute and measure [x in H_list] by at most H clean equality scans.
   On zero fail. On one reset the known flag. This projects onto the
   verified list with probability h/f.
2. Into eleven zero rank bits XOR q when x=x_q. Uncompute each equality
   helper before the next scan. No unchanged rank copy is saved.
3. Prepare output c in |+>. On the rank and c apply in place

       (q,c)->((q-c) mod h,c) for q<h,
       (q,c)->(q,c) for q>=h.                        (D3)

   Measure the changed rank, obtaining t. Its conditional probability is
   1/h. The remaining two branches are |x_t,0> and |x_next,1>, where
   next=(t+1) mod h, with their original phases and equal magnitudes.
4. For each original index bit, apply X if that bit of x_t is one,
   then CNOT from c if x_t and x_next differ there. This clears all x.
   Reset the measured rank and every helper. Return c with full signed

       a'=A(x_next)-A(x_t).                          (D4)

D3 is a permutation of all 4096 encodings of eleven rank bits and c.
Generate it from the classical h by bounded loops. Compile its cycles
into transpositions. A transposition of two twelve-bit words uses a path
of at most twelve bit changes: apply its adjacent transpositions forward,
then all but the last forward edge in reverse order. Each edge is a
controlled bit flip with eleven known positive/negative controls. Exact
fixed Clifford+T words and a fixed number of clean helpers implement it.
Every table entry, instruction bit, address, gate and reset is generated
and counted. The bound is an absolute constant independent of n. No rank
oracle, preloaded advice, quantum lookup or old-rank copy is used.

On the verified subspace the Kraus maps are

    K_t=(|0><x_t|+|1><x_next|)/sqrt(2),
    sum_t K_t^*K_t=P_H_list.

Each list element occurs twice in orthogonal output positions. The
complementary projector is membership failure. Before membership
conditioning each t has probability 1/f, so total success is h/f.
These identities hold with arbitrary reference systems. They are
independent of theta for every equal-magnitude phase input. The eleven-bit
rank covers h=2048, and the permutation covers every smaller h and the
wrap edge. All old index bits are cleared before c is returned.

Both edge endpoints are distinct members of the same fiber, so D4 is
divisible by 2^(p+b). Its coefficients on children are in {-1,0,1},
not all zero. Distinct child leaf sets and nonzero child incidence vectors
give a nonzero signed leaf vector with coefficients in {-1,0,1}. The full
signed sum is computed only after t is selected. Neither sorting nor any
success decision uses high labels or A(x_q). A numerical zero label is
returned without a filter.

## 4. Pairwise moments give complete survival at least 63/65

Put P=2^b, k=b+5 and K=2^k=32P. Before fresh child generation the next
c_j are independent uniform residues modulo P, by the induction below.
The measured residue has the planted law f(X), for uniform independent X.
Writing another subset as X xor z signs the uniform c_j but preserves
their joint law. Hence the size-biased measured fiber has

    |F_e|-1 =_law Z,
    Z=#{nonzero z in {0,1}^k:sum_j c_j z_j=0 mod P}.

Every nonzero row has a unit coefficient, so its zero probability is
1/P. Any two distinct nonzero binary rows have a determinant +1 or -1
minor: choose coordinates from disjoint supports, or a common coordinate
and one from their symmetric difference. The two zero events are
independent because that minor is invertible modulo P. Thus

    mu=E Z=(32P-1)/P=32-1/P>=63/2,
    Var Z=mu(1-1/P)<=mu,
    E binom(Z,2)=binom(32P-1,2)/P^2<512.              (D5)

No mutual independence of three or more rows is assumed. By
Cauchy--Schwarz, mu^2=(E[Z 1_(Z>0)])^2<=E[Z^2] Pr[Z>0]. Therefore

    Pr[Z>0]>=mu^2/(mu^2+Var Z)>=mu/(mu+1)>=63/65.

Complete cyclic extraction fails exactly on singleton fibers, so this
is its complete success bound for every b>=1. It is an exact second-moment
bound, not a fitted distribution or a seven-moment approximation.

## 5. Bounded discovery succeeds with probability above 24/25

If |F_e|>H=2048 then Z>=2048. Markov applied to D5 gives

    Pr[|F_e|>H]<512/binom(2048,2)
      =1024/(2048*2047)=1/4094.                      (D6)

For k>=13, 1<=s<=H remaining members imply s<=2^k/2. With
sin^2(gamma)=s/2^k the exact random-iteration formula is

    mean success=1/2-sin(4J0 gamma)/(4J0 sin(2gamma))>1/4.

This follows from sin(2gamma)>=sqrt(2/2^k) and J0>=sqrt(2^k).
For every fixed true fiber of size at most H, H blocks of 128 trials
therefore have total premature-stop probability at most

    H(3/4)^128<2^-37.                               (D7)

Indeed (4/3)^8>8 gives (3/4)^128<2^-48 and H=2^11. If k<13,
enumeration uses at most 4096 indices and has no miss on a fiber of size
at most H. When the fiber is larger, D6 applies to both branches.

On the complement of D6 and D7 the list is complete. The actual cyclic
instrument then has the complete rule's success. Subtracting both bad
event bounds, with no independence assumption, gives

    p_dense>=63/65-1/4094-2^-37>24/25.                (D8)

The strict rational margin is

    63/65-1/4094-2^-37-24/25
      =821678782667077/91434699771084800>0.

Use sigma=24/25 at every positive width. This is a guarantee before a fresh attempt's
children are generated, conditional on earlier external history. It is
not a guarantee for each fixed list of child labels.

## 6. Uniform nominal product ratio is below 32

Let d=log2(6u)>0. Consecutive retained values have gaps
v_i-v_(i-1)=delta(v_i)>=d. Using natural logarithm ln, for i>=2,

    1/v_i<=d^-1 integral_(v_(i-1))^(v_i) dx/x.

This holds because the interval length is at least d and 1/x>=1/v_i
throughout. Include the first value separately and telescope:

    sum_i 1/v_i<=1/u+ln(R/u)/d.

Since R<(u+1)^2 and (u+1)^2/u<=6u for u>=1,
ln(R/u)/log2(6u)<=ln 2. Hence

    ln product_i[(2v_i+5)/(2v_i+1)]
      =sum_i ln(1+4/(2v_i+1))
      <=2 sum_i 1/v_i<=2+2ln 2.

Exponentiating proves a product bound at most 4e^2<32. To check this
last absolute constant without numerical approximation, the series
for e has tail from 1/3! at most (1/6)/(1-1/4)=2/9. Thus
e<=49/18<11/4 and 4e^2<121/4<32. Consequently, for every nominal
truncated profile,

    product_i (2v_i+5)<=32 product_i (2v_i+1).         (D9)

This proof includes u=1, m=1 and every retained base. Its constant does
not depend on R, n, D or sampled outcomes. No large-threshold asymptotic
is used in D9.

## 7. Old full signed frequency bound q0 still holds

Let r_i=b_i+5 at an active level and r_i=1 at a shortcut. Insert all dense
nominal factors to bound its returned tree's leaf count. For v>=1,
2v+5<=3(2v+1). Thus for ancestors i>=2,

    r_i<=3(2v_i+1)<=2^(delta(v_i)-1).

The base has r_1<=2v_1+5. The function (2x+5)2^-x decreases on positive
integers, so

    q_D_dense=product_i r_i
      <=(2u+5)2^(R-u-(m-1)).                         (D10)

If m>=2 and u>=2, 2u+5<=2(2u+1), and D10 is at most the old q0.
If m=1, q_D_dense<=2R+5. The decreasing function (2R+5)2^-R and
R>=u^2 give

    (2R+5)2^(-R+u)
      <=(2u^2+5)2^(-u^2+u)<=2u+1

for u>=2. For the last inequality use u^2-u>=u, 2^u>=u+1 and
(2u+1)(u+1)>=2u^2+5. A shortcut-only tree has one leaf. The target main
branch n>=256 has R>=sqrt(n/2)>11 and therefore u>=3. These cases prove

    q_D_dense<=q0                                   (D11)

for every requested tree width on the main branch. The n<256 algorithm
is retained unchanged. Thus |W|<2q0 for the returned signed root
label 2^B W. The existing signed field n+ceil(log2 q0)+4 bits suffices.
Compute D4 in one pass with coefficients x_next,j-x_t,j; each partial
sum is bounded by the sum of absolute leaf labels in that returned tree.
No new frequency scale, q0 enlargement, guard bit or decoder grid is
needed. Failed attempts do not enter a returned label's incidence; their
source copies remain counted separately.

## 8. Source and weighted recurrences with the old constants

The joint fresh-label induction is the same for k=b+5. Conditional on
the prior history, fresh children have independent uniform unused-block
quotients. D8 gives success at least sigma=24/25 before their generation.
Reaching an attempt depends on previous attempts only. Hence its uniform
expected child-cost bound gives

    E_i<=(25/24)(b_i+5)E_(i-1)

at positive widths; shortcuts multiply by one. The cost of the current
attempt need not be independent of its success. An accepted raw leaf
costs at most two original copies in expectation.

Set a_i=(25/24)(b_i+5) at active levels, and a_i=1 otherwise. Insert
nominal factors greater than one at all m levels. With
rbar_i=2v_i+1, D9 gives

    E_root<=2 product_i a_i
      <=32 (25/72)^m [2 product_i(3rbar_i)]
      <=32 (25/72)^m C.                             (D12)

There is also the bound E_root<=C without the factor 32. For every
integer v>=1,

    (25/24)(2v+5)<=3(2v+1),

since this reduces to 53<=94v. Shortcuts also obey 1<=3rbar_i.
The same nominal product and profile telescoping therefore give

    E_root<=C min(1,32(25/72)^m)=beta_m C.            (D13)

For completeness, the target's exact nominal telescoping is

    3rbar_i<=2^(v_i-v_(i-1)-1) for i>=2,
    2 product_i(3rbar_i)
      <=6(2v_1+1)2^(R-v_1-(m-1))<=C.

Every retained gap is at least five, so R-u>=5(m-1) and C's exponent
is nonnegative. These bounds include every partial width, all leading
shortcuts and D=1 under the same full nominal m.

For weighted work use sigma itself, rather than changing the children
and then retaining an old weaker retry multiplier. The expected root
weight expands into active-level contributions

    (25/24)2^v_i product_(active j>i) a_j.

Since a_j<=3rbar_j, inserting all nominal ancestors bounds this by
(25/24)2^R 2^(-(m-i)). Summing the geometric series gives

    E root weight<(25/12)2^R<6*2^R.                  (D14)

The old Wstar in D1 is therefore valid. This includes child attempts in
failed ancestors and those constructed before a failed parent check.
Zero-width shortcuts add no weight.

## 9. Exact source guard and the unchanged decoder laws

Use the exact D2 guard. Compute powers 25^m and 72^m, compare 32*25^m
with 72^m for the rational minimum, then compute its final integer ceiling.
All operands have O(R+m+log n)=O(n) bits. Long multiplication/division,
comparisons, every stored bit, counter and address debit are charged.
The setup is polynomial work with O(n^2) peak classical bits.

D13 applies conditionally before each odd root and each wider 2-adic
root. The odd schedule has exactly the old F calls. A returned edge has
a nonzero signed incidence vector. Conditional on its low transcript,
untouched accepted top leaf bits tau_l are independent fair bits, and

    W=c_low+sum_(l in S+)tau_l-sum_(l in S-)tau_l,
    |S+|+|S-|>=1.

Therefore |E exp(2pi i yW)|<=|cos(pi y)| for every real y and
Pr[W odd]=1/2. Repeating wider 2-adic roots costs at most two calls in
expectation, even if source cost and parity correlate. Condition on
reaching each fresh call to use D13. Truncation at the old K2 only
reduces that expectation. The direct width-one case uses the safe extra
2n raw-copy allowance. Thus the ideal process without global caps has

    E Q_ideal<=beta_m C(F+2n)+2n=Qstar_dense,
    E W_ideal<=6*2^R(F+2n)=Wstar.                    (D15)

The source bound and D14 also apply after incorrect earlier scalar
decoder outputs. Membership, rank and list probabilities depend only
on equal basis magnitudes and known low residues, not their actual
phases. Full signed labels are computed only after selection. In the
ideal source model, known physical transforms preserve independent
uniform latent Fourier labels. Numerical EXTRACT errors are treated by
first-error coupling, not by assuming the recorded labels were correct.

Since beta_m<=1 and Qcap_old is an integer,

    Qcap_dense<=Qcap_old.                            (D16)

The actual-call union bound in RUN(F) uses Qcap_dense<=Qcap_old; its
precision continues to use Qcap_old. These are the source-count roles
throughout this substitution.

Keep the target's exact Qcap_old precision, q0, C, ell, U,
A_pool=2^40(C+1)U^3, g_pool, h_pool, Delta, F and H0. D11 and D13 prove
their defining frequency and root-cost premises. D16 and the old exact
Qcap_old<=2^27(C+1)U^2<=A_pool prove pool inclusion. This array is only
a probability variable, not allocated storage.

Here is the needed phase and unused-label argument in full. For a finite
successful low transcript, condition on source leaf parts only modulo
2^(p+b), separate-query records, residue, membership and changed-rank
outcomes, canonical index choices and retries. All their probability
kernels use only low data; every K_t^*K_t is diagonal. The selected leaf
incidence z_l in {-1,0,1} is nonzero and fixed by that transcript. Write
k_l=u_l+2^(p+b)H_l, with independent uniform high blocks H_l. Then

    a'/2^(p+b)=c_low+sum_l z_l H_l mod2^(D-p-b)

is uniform because some coefficient is a unit. Marginalize over all
finite successful low transcripts. Fresh retries have geometric tail at
most (1/25)^(t-1), so they terminate almost surely and the marginal covers
all returned outputs. This jointly proves termination, unused-block
uniformity and independent fresh child calls, closing D5's premise.
Do not condition on stored high labels, irrelevant extractor records,
correct extraction, decoder outcomes or future cap survival.

For accepted source labels, their value is independent of the exact
waiting/rejection record; its joint mass with specified rejected labels
and waiting time t is N^-t. Each fixed odd schedule therefore uses fresh
low-dependent prefixes of independent latent-label arrays. Conditional
on all low pool coordinates, waiting/rejection records and construction,
search, membership, changed-rank and retry outcomes, accepted top bits
are independent fair bits. The cyclic selections do not use high labels.

Use one global pool and one low signed-sum distance event for the complete
fixed odd schedule, across all its stages and physical scales. That event
has failure below 2^-190. On it
and Fitodd, every root uses at least h_pool signed leaf coordinates:
its nonzero low signed sum vanishes modulo 2^B, so a smaller support
would contradict the event. Its coordinates lie in the pool by D16.
Distinct roots use disjoint supports. The product of at least h_pool
fair-bit characteristic factors, D11 and the phase-independent kernels
give exactly the target stride/backward decoder premises. Their total
odd error remains 2^-20, with the same h_pool<16 fallback and pure
2-power case. No new high-bit condition is imposed by the new guard.
Fitodd concerns only the fixed odd schedule; it excludes the later full
adaptive 2-adic cap event from top-bit conditioning.

Markov applied separately to D15 bounds each guard loss by 2^-10.
The weighted check occurs after children are built, so their previous
sources and weights are included in the reference process. With the
old exact EXTRACT precision and at most Qcap_dense<=Qcap_old calls,
the first-label error is at most 2^-14. Couple actual and ideal runs
until the first error or guard. Add the unchanged distance, decoder and
2-adic attempt-limit bounds. The strided failure total is

    2^-190+2^-20+2*2^-10+2^-14+2^-30<2^-8.

The fallback bound is 2*2^-10+2^-14+2^-20+2*2^-30<2^-8. M=1 has no
odd loss, and the retained finite n<256 branch fails below 2^-10.
Thus entire-secret success remains at least 1-2^-8 for every N and s.
Every raw acquisition, including rejections and partial/failed children,
is counted. Correctness uses only independent ideal coset copies.

## 10. Grouped G1, literal tape and the factor eight

At positive widths b<=2v and k=b+5, so k<=2R+5 and k<=n+4.
The exact G1 construction is unchanged as a function of its explicit
k query wires and b output bits. Its table recurrence, selected-count
CNOTs, retained-input/history sum, top modular truncation and clean
reverse all apply to any k. Use direct rows when k<max(16,u); otherwise
set

    w=floor(log2(k)/2), d_count=ceil(log2(w+1)),
    g_count=ceil(k/w),
    h_count=min(b,max(1,floor(n/(g_count*d_count)))).

Now g_count*d_count<=k+w=O(n). The batches have at most
max(n,g_count*d_count)=O(n) record bits. Each table has
2^w*d_count<=k<=n+4 bits. The sum keeps its at most three times the
record count of original/intermediate bits and clears all of them by
reverse computation. It also has O(b) dense rows/adder scratch.
Thus the whole G1 pool remains O(n) qubits.

On grouped rows k>=u, log k=Theta(L), 2^w=O(sqrt R), and the same
J<=1+2b*g_count*d_count/n=O(d_count) bound holds. Consequently its
complete exact elementary slot bound remains

    O(J*g_count*2^w*d_count+g_count*b*d_count+J*b+k+b)
      =O(n log2(L+2)).                              (D17)

Direct rows have k=O(u+1) and cost O(kb+k)=O(R+1), also covered.
The explicit constructor/allocator loops over the new k and actual b,
uses O((G1_slots+kb+n)L^3)=O(nL^4) charged work and O(n^2) bits,
and counts every mask, word, wire map and gate description. The literal
physical-tape controller still reads O(L) actual bits per slot and pays
every indexed gate's full address debit. Table addresses are classical,
with counted construction; there is no QRAM or free program read.

The list now has at most 2048 strings. A full comparison, exclusion,
verification or rank pass is at most 2048 complete k-bit scans. This is
O((k+L)L) charged work with a larger absolute constant. Equality scratch
is reused; distinct known strings permit one XOR membership accumulator.
Diffusion and control still cost O((k+L)L). Hence a whole iteration,
including forward/backward G1 and list tests, costs
O(nL log2(L+2)) charged work. The initial original-to-query wrapper
costs its full 2k indexed CNOTs, using that same query pool.

The iteration word has ceil(k/2)<=v+3 bits. In particular

    J0<=2^(v+3)=8*2^v.                              (D18)

There are at most 2048*128=2^18 trials. Their total number of iteration
words is less than 2^(v+21). The factors eight and 2^18 are fixed
constants, independent of n and all sampled outcomes. No depth, free
parallelism or query-count replacement is made. Trial coins, full
counter updates, every measured candidate, verification and reset are
also counted. The small-k enumeration is a constant-length loop of at
most 4096 indices. Every failed or partial search obeys these bounds.

The eleven-bit rank permutation has at most 4096 encodings, generated
and implemented exactly as in Section 3. All list sorts, rank/membership
scans, CNOT clearing and full signed D4 arithmetic are paid one-off
polynomial work. Signed output takes O(nk) core bit actions with the
existing guard bits, or O(nkL^2) under the conservative address generator.
Program clear, measurement and all reset/release work is included.
Every such polynomial P(n) fits an absolute constant times 2^u, since
n<2(u+1)^4 and polynomial(u)2^-u is bounded. Thus a full paid attempt
still costs

    O(nL log2(L+2)2^v)                              (D19)

on every branch, after the one-off work has been counted. A weighted
failure builds no program, and a source failure during child construction
retains the complete partial-stack charge.

## 11. Peak space and full time

Depth-first retained siblings and outputs number at most

    1+sum_(active i)(r_i-1)
      =1+B+4*(number of active levels)<=n+4m=O(n).

The main profile has m<=n. The original and separate query now have
k<=n+4 wires. The grouped tables, record/history pool and carry scratch
are O(n) by D17. The cyclic rank, output and permutation helpers add
O(1). Every returned output replaces its k children. Source extraction
and physical transforms keep O(n) qubits. Thus S_Q=O(n) jointly on
every execution branch, including release during an abort.

Each retained full label still has O(n+log q0)=O(n) bits by D11. There
are O(n) such labels. The O(nL log2(L+2)) stored G1 word, explicit
constructor/wire maps, source/decoder records, counters and exact rational
cap setup fit O(n^2) classical bits. The 2048 strings take O(n) bits;
the finite permutation table and its gate word take a fixed constant
number of O(L)-bit addresses. Only one attempt/program is active.
Every instruction, marker, head location, helper and saved frame is
included. Thus S_C=O(n^2), with actual address width O(L).

D14 validates the same Wcap=O(n2^R). Sum D19 over its charged nominal
weights to get O(n^2L log2(L+2)2^R). The retained separate whole-stack,
source/extraction and seed charges are still

    O(n^3L^2[Qcap_old+Wcap/2^u+1]),
    O(n^2L^2 Qcap_old), O(n^2L^2 q0)+poly(n).

Their deterministic proofs use only O(n) retained labels, O(n)-bit
fields, the number of source/attempt events, and their fixed caps. The
extra four children per active level preserve those bounds up to fixed
constants. D11 keeps all signed fields and decoder loops exact. D16
keeps the Qcap_old source bound. Dividing these terms by
n^2L log2(L+2)2^R again gives bounded polynomial factors times 2^-u
or 2^-R. The target has n<2(u+1)^4 and R>=sqrt(n/2). Backward decoding
and setup are polynomial. Hence

    T=O(n^2L log2(L+2)2^((71/100)sqrt(nL)))
     =O(n^2L^(3/2)2^((71/100)sqrt(nL))).              (D20)

The second is the supported time envelope. The first retains the tighter
nested logarithm without claiming its exact structured representation.

## 12. Supported source correction minus 5/32

The unchanged profile gives

    2^R=O(2^((71/100)sqrt(nL))),
    u>=(1/2)(nL)^(1/4)-1,
    2u+1=O((nL)^(1/4)),
    m>(1/16)sqrt(n/L), H0=O(n).

Since 72^2=5184>5000=8*25^2, log2(72/25)>3/2. Therefore

    2^(-(m-1))(25/72)^m
      =2*2^(-(1+log2(72/25))m)
      <=2*2^(-(5/32)sqrt(n/L)).                     (D21)

Use beta_m<=32(25/72)^m in the actual D2 guard. It follows, including
the ceiling and direct-copy summand, that on every branch

    Q<=Qcap_dense
      =O(n(2u+1)2^(R-u-(m-1))*32(25/72)^m+n+1)
      =O(n^(5/4)L^(1/4)
          *2^((71/100)sqrt(nL)-(5/32)sqrt(n/L)
              -(1/2)(nL)^(1/4))).                   (D22)

The factor 32 is an absolute outside constant. The positive leading
exponent dominates both negative lower-order terms, so n+1 is absorbed
eventually. The actual D2 minimum covers all smaller m without a new
asymptotic exception. The target's n<256 and h_pool<16 finite branches
have uniform finite maxima included in the same outside constants.

D22 is supported exactly with outer nPower=5/4, logPower=1/4 and
exponent terms

    (71/100,1/2,1/2), (-5/32,1/2,-1/2),
    (-1/2,1/4,1/4),

in (coefficient,nPower,logPower) order. The other envelopes are the
supported D20 time and n^2,n spaces. The exact four growth indices
remain [1/2,0,0,1/2]. All bounds hold jointly for this one substitution,
with unconditional entire-secret success at least 1-2^-8. The malformed
fraction is zero under the exact same model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

A future full package must include the eleven-bit instrument, dense
children, new finite discovery limits, extended G1 allocator, D2 guard
and all complete source/decoder proofs before release. No full package
is created by this note. Independent review of this bounded proof is
required before that integration.

## 13. Scoped exact checks

`check_dense_cyclic_source_transfer.py`, SHA256
`95addc184d20536876b37f61f63dd65c4d82e744d5800b8aff118082efa803dd`,
passed the finite checks below. They are supporting evidence, not the
uniform proof or a simulation of the full capped solver.

- All 2047 list sizes from 2 through 2048: 8384512 rank encodings and
  4196350 exact original-index clearing branches.
- Pairwise moment formulas at 32 positive widths, both rational success
  margins and the exact logarithm guard 5184>5000.
- 515 nominal profiles, including 512 old-q0 leaf bounds.
- 2433 all-D source/weighted products and 21 exact rational-ceiling guards.
- 1663 dense G1 parameter rows over five input lengths, including short
  rows, batch counts, table sizes, query lengths and record-space bounds.

The all-domain instrument, product, q0, source/weight and memory proofs
are Sections 3--12. No empirical fiber distribution or fitted exponent
is used. No full package or stage changed during these checks.
