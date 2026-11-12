# R3: three-level DCP recovery with a explicit phase-class ranking

## 0. Selected algorithm, exact resource representatives and scope

For every integer N>=2 and every secret s in Z/NZ, let n=ceil(log2 N).
The ONE R3 program specified below recovers the entire s with unconditional
probability at least 1-2^-8. Jointly on EVERY execution branch,

 T=O(2^(n/9) n^24), S_C=O(n^2),
 S_Q=O(2^(n/9) n^5), Q=O(n^4).        (0.1)

All outside constants are absolute, independent of N,s,outcomes. Costs
include original source acquisition, every discarded copy, failed search,
initialization, full dense allocation and metadata, all classical and
quantum gates, address fees, circuit generation, output and cleanup.
The four exact representative growth indices are 1,0,1,0. The guaranteed
malformed fraction is zero under the canonical ideal-copy model in
Section 7; it has no numeric score. No positive tolerance or robustness
impossibility is asserted.

This is a time/query/quantum-memory tradeoff, not a cube-root exponential
algorithm or a claim to improve the known square-root time-growth index.
The high-width helper uses full dyadic canonical tables and explicit linear
coherent scans. The low-width helper uses deterministic streamed exhaustive
enumeration. Their threshold makes the latter polynomial in n. These are
upper bounds, not tight costs or practical hardware promises.

## 1. Complete material sources and selected changes

The directly used three-level schedule, logarithmic odd-decoder leftover,
literal acquisition cap, conservation accounting and CQ basis-record method
are adapted from own published BJ3-C submission
84757087-63d6-4712-94f1-26a53b8fcc36, evaluated commit
5b5418b163d7ab5635c29c77dea93e473bf0e73d, proof SHA-256
91eb9794ab5e3cb6f47d8630ae604f0c9dd963dc659d9b86db50f1714098d67c.
The exact file was fetched and matched to official metric evidence.
Its batched finder, prime sampler, numerical resource theorem and fixed
arity are replaced; no prior validity verdict is a mathematical premise.

The complete source instrument and all-modulus decoder remain reproduced
unmodified in family-source.md, SHA-256
11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7.
The direct source is own QLOG submission
8870de8c-e8dd-4d03-82c7-57842e846e4f, evaluated commit
4f7e2b4f8dbcf19aa8dce588a8771a21297f42be. Historical credits remain.
We use its Sections 1-3 for exact transforms/extraction, Section 4.1 for
verified-pair compression, Section 4.3 for the size-biased fiber moment,
Section 5 for unused-block/frequency laws, Sections 6-7 for the full
arbitrary-modulus decoder, and Section 8 for the finite exhaustive tester.
Its old height profile, Grover discovery and numerical theorem are unused.

The measured-basis-record method originated in own QLOG-BANK
f949830e-3dd9-4a7e-af4e-4aabedbfb672, evaluated commit
59100526ce3dc11de2289a0a5d3f1b2c1c59463b, proof SHA-256
cd1f8f1af807ce35a8f2994666627eb63aca4dd03c2db645dee3dac7a60cbb8b.
It is restated fully in class-ranking.md; old polynomial-bank layout is
unused. Only large helper records occupy basis qubits; ordinary labels
remain classical.

Four-block filtering and canonical dictionaries have conceptual precedent
in Chukhin, Kulikov, Levitskii and Mihajlin, arXiv:2608.07309v1,
Sections 3.1-3.3, https://arxiv.org/html/2608.07309v1 . We do not import
QRAQM, quantum walks, a subset-sum oracle or its runtime theorem. The new
high-width helper projects the ORIGINAL phase register and ranks every
member of its measured class using Cartesian metadata. Its success proof
uses fresh uniform LOW labels, not worst-case subset-sum discovery. The
complete construction, collision/class counting, circuits and resources
are supplied in class-ranking.md. No literature-first claim is made.

## 2. Actual three-level phase generator and literal source cap

For n<256 run the complete source Section 8 exhaustive tester with n+10
fresh tests per candidate. The true candidate always passes; each wrong
candidate passes all tests with probability 2^(-n-10), so error <2^-10.
Its exact modular-permutation Clifford+T circuit and resource accounting
are supplied. This is a FIXED finite prefix, with no advice about s.

For n>=256 put ell=ceil(log2(n+2)),
rmax=ceil(4*ceil(n/3)/3)+16ell+128 and q0=rmax^3. A PS3(D,B) call has
1<=D<=n and 0<=B<D. Split B deterministically into three nonnegative
widths b_1,b_2,b_3 differing by at most one, each <=ceil(n/3).
For example write B=3v+r, give v+1 to the first r positions and v to
the rest. Let p_i=sum_(j<i)b_j.

Level zero obtains one fresh accepted phase leaf with an independent
uniform label in [0,2^D), through the exact transforms in Sections 3-4.
At level i:

* If b_i=0, return the output of one lower-level call directly.
* Otherwise set k_i=b_i+6 when b_i<12ell+96, and
  k_i=ceil(4b_i/3)+16ell+128 otherwise. Build that many fresh
  lower-level outputs depth first. With full signed labels a_j divisible
  by 2^p_i, form c_j=(a_j/2^p_i) mod2^b_i. Execute exactly the LOW or
  HIGH phase-class instrument in class-ranking.md, respectively. LOW
  measures the low residue and streams a complete capped fiber list;
  HIGH projects canonical block membership then measures full low-label
  integer sum T and dyadic residue q. Both return one exact pair phase.
* On FAIL discard ALL these inputs and scratch and make fresh children
  for a new attempt. On success return the exact known full signed label
  difference and its one phase qubit. Never reject a successful output
  just because its high label or full value is zero.

There are at most three positive levels. No coherent source control,
preparation inverse, purification, QRAM or additional input oracle is used.
All helper coins and measurements have finite fixed bounds. The global
source counter aborts the WHOLE algorithm before the next acquisition
would exceed Qcap; it releases all registers and outputs 0. The abort
propagates through partial children, so there is no unguarded retry.

Define all odd-decoder parameters in Section 3 first, from n,N,q0 only.
With Sodd,K there, put

 H0=Sodd K+2n,
 Qstar=6q0 H0+2n, Qcap=1024 Qstar.                    (2.1)

These are finite explicitly computed integers. Every original acquisition
increments this counter, including rejected Fourier labels, every failed
or restarted tree, and all parity repeats. Helper zeroes and random-bit
ancillas are not source copies, but their full cost and space are counted.
The cap is never merely an expected-resource convention.

Use the exact extraction circuit in family-source.md Section 3 with
h_e=ceil(log2(2^16 Qcap(n+5))) and F_e=2^21 h_e collective rounds in
each basis. This is a new recomputed confidence, not a value inherited
from another profile. All labels and cap/precision records are explicit
bit strings. The actual finite extraction returns some label on every
branch, even a bad estimate; resources below do not condition on correctness.

## 3. Exact odd-part decoder with a logarithmic leftover block

Write N=2^a2 M with M odd, d=floor(log2 N). The full source identity is
rho_s=(1/N)sum_k |phi_k(s)><phi_k(s)| tensor|chi_k><chi_k|,
with uniform latent k, as derived in the included source. Exact data
multiplication by a known unit and controlled known subtraction preserve
this mixed-coset law with transformed secret. Exact translations read the
latent label nondestructively; no QFT or approximate rotation is needed.

If M=1 set s1=0, K=Sodd=0 and skip the odd decoder. Otherwise choose

 h=min(d-a2, max(1,ceil(log2(n+2)))), B=d-h,
 stride=max(1,h-4), nq=2^(h-1)q0,
 K=2^13(ceil(log2 nq)+ceil(log2 n)+30).

Here d-a2=floor(log2 M)>=1, so h>=1 and B>=a2. For stages j=0,...,J,
let J be the least nonnegative integer with 2^((J+1)stride+2)>2M,
and Sodd=J+1. These are fixed before sampling.

For stage j compute the unit alpha_j by CRT and extended Euclid with
alpha_j=1 (mod2^a2) and
alpha_j=2^(j stride)(2^(B-a2))^(-1) (mod M). Acquire a fresh original
copy, multiply its data by alpha_j, extract its label k and accept only
when k<2^d (otherwise discard and acquire again). Apply X to its control.
In the ideal-label process each accepted leaf has uniform label in
[0,2^d), with acceptance probability 2^d/N>1/2 and positive phase.
Run PS3(d,B) to obtain root label 2^B W. Exactly as in the included
source Section 6,

 2^B W alpha_j s/N = 2^(j stride)W s1/M (mod1).

Measure K such roots in independent fair X/Y bases, recording their full
signed W, basis and +/-1 outcome. Use EXACTLY the finite dyadic candidate
arcs, scores, table approximations and tie-breaking of the included
source Section 6, with this nq, stride, K and stage count. Its proof only
requires the root's unused h-bit block characteristic bound and signed
magnitude bound, established in Section 5 below. It does not require the
old height rule or old hmax.

For clarity, the candidate-grid exponent is P_j=j stride+ceil(log2 nq)+8.
Stage 0 enumerates the whole grid; later stages enumerate the arc of
radius 2^(-j stride-2) around the previous center. For each candidate
compute the K signed trigonometric table scores by exact integer arithmetic,
keep the least maximizer and continue. This entire grid is COUNTED work,
not an optimization or decoding oracle. The source proof shows stage
failure <=2^-20/n and final s1=round(M z_J) mod M equals s mod M except
with total probability <=2^-20.

## 4. Exact 2-adic recovery and the full output

If a2=0 set s2=0. Otherwise, once s1 is obtained, maintain the known low
g bits s2low of s2 in s=s1+M s2 (mod N). Put wd=a2-g and
sh_g=s1+M s2low (mod N). On a fresh original copy apply the exact
controlled data subtraction sh_g, extract k and apply X to its control.
Use kk=k mod2^wd as label. Since 2^wd divides N, this metadata label
is uniform on [0,2^wd), independently for fresh copies.

For wd=1 discard kk=0; at kk=1 measure X to obtain the next bit.
For wd>=2 run PS3(wd,wd-1). If its full signed root W is even discard
and repeat. If W is odd, X measurement gives the next bit exactly when
s1 and the earlier bits are correct. Set that bit and continue, finally
outputting (s1+M s2) mod N. This is precisely the exact phase identity
proved in family-source.md Section 7, with PS3 replacing its tree.
The root metadata parity remains fair even after an earlier incorrect
odd-decoder output, because selection kernels are phase independent.
This fact is used only for the unconditional resource expectation below;
bit correctness is asserted when the preceding recovery was correct.

## 5. Unused labels, success and the exact all-branch acquisition bound

The helper proves fresh-attempt success >20/21 for BOTH branches,
and low-only selection, in class-ranking.md Sections 3 and 7. Thus the full
unused-block induction in family-source.md Section 5 applies to the
THREE fixed levels as follows. A level-zero label is uniform modulo 2^D.
Fresh disjoint child calls have independent uniform remaining quotients.
A successful pair uses only residues through its newly cancelled b_i
bits; every returned signed incidence on its distinct original leaves
is nonzero with a coefficient +/-1. Conditional on the finite successful
LOW transcript, an untouched leaf block on that unit coefficient makes
the output quotient uniform. Retry transcripts also use only these low
parts; their geometric sum preserves the law. Unrelated high-valued
records are marginalized, not conditioned on, and successful outputs
are not filtered by high labels inside PS3.

In particular a root label is exactly 2^B W, with |W|<2^(D-B)q0:
a successful tree contains at most q0 original leaves in its signed
incidence, each label <2^D. Its held-out h=D-B bit blocks are independent
uniform. Conditional on the low transcript,

 W=c+sum_(S+)tau_l-sum_(S-)tau_l,
 tau_l uniform on [0,2^h), |S+|+|S-|>=1.

Hence its characteristic modulus is at most that of one uniform h-bit
block, bounded by both |cos(pi y)| and 1/(2*2^h*||y||) when ||y||>0.
Its parity is fair. These are exactly the source decoder's Lemmas 5.1
and 6.1 hypotheses. They prove full odd recovery except with probability
<=2^-20, followed by exact 2-adic recovery whenever it was correct.
No assumption of uniform FULL integer W or heuristic subset sums is used.

Let beta=21/20. In the ideal uncapped process, an accepted leaf needs
at most two original copies in expectation. Before each fresh positive
node attempt its success probability is >=1/beta. If E_i is a uniform
conditional expected acquisition bound for a level-i output, fresh-child
reach-event accounting gives E_i<=beta k_i E_(i-1). This does not assume
attempt cost is independent of success; costs of a reached attempt's
fresh children have the same uniform conditional bound. Zero-width
levels simply return their child. With at most three positive levels,

 E_root<=2 beta^3 product(k_i)<=3q0<6q0.

Calls terminate almost surely with finite expectations by the same
finite-level geometric induction. Odd recovery uses exactly Sodd K roots;
each of at most n parity bits needs two roots or direct copies in
expectation. These expectations remain valid following a wrong earlier
decoder result, since the metadata law and fresh-attempt success do not
depend on the unknown phase. Thus total ideal expected acquisitions
are <=Qstar in (2.1).

Couple the actual capped computation to this ideal uncapped process until
a cap or extraction error. Markov bounds acquisition-cap loss by <=2^-10.
The exact extraction construction, with the recomputed Qcap, has per-call
label-error probability <=1/(2^14 Qcap) uniformly in the true latent label;
the union bound for at most Qcap adaptive calls costs <=2^-14. This is
an additive coupling error, not conditioning on estimates succeeding.
Together with the decoder loss, failure is at most

 2^-10+2^-14+2^-20 <2^-8.

The finite exhaustive branch already has smaller error. This proves the
unconditional full-secret theorem for every N and s.

Finally Qcap=O(n^4), with NO missing logarithmic factor. Indeed
q0=O(n^3), 2^h<=2(n+2), nq=O(n^4), and K=O(log(n+2)). If h is the
chosen ceil(log2(n+2)), then stride=Theta(log n) for large n, giving
Sodd=O(1+n/log n). If h is smaller it equals floor(log2 M); then the
source stage rule gives Sodd=O(1), including h<=4. Hence Sodd K+2n=O(n)
in all cases. Consequently Qstar and the LITERAL Qcap are O(n^4).
Every original acquired copy, rejected label, failed attempt and abort
is included. Q is not peak stored states or a count of successful roots.

## 6. Deterministic complete work, physical spaces and exact indices

The source cap also gives a deterministic bound on ALL internal attempts,
without a missing expected-time assumption. Count logical live phase
outputs. Each accepted leaf creates one. A positive-width combiner consumes
k_i>=7 child outputs and returns at most one, decreasing this count by at
least six. Root measurements, parity discards and abort cleanup only
consume further outputs. Zero-width levels create none and just return
one owned child. Therefore on EVERY branch, if L leaves were accepted
and I positive combiner attempts started/completed,

 6I<=L<=Qcap.

An interrupted child call cannot invalidate this conservation count;
children discarded on abort still came from counted acquisitions. Helper
query qubits carry no new DCP source phase and are not counted as logical
outputs. Their full gates and allocation are counted separately below.
Every helper has fixed bounded loops on every input, so no other retry
can run without a guarded source call or a counted internal attempt.

For a HIGH width b<=ceil(n/3), put k=ceil(4b/3)+16ell+128,
L=2^ceil(k/4). Then L<=C 2^(n/9)(n+2)^4 for an absolute C. Its
explicit work is O(L(n+1)^12) and physical qubits O(L(n+1)), including
all reserved cells and scratch, by class-ranking.md Sections 8-9.
Each LOW helper costs O((n+2)^20) work and polynomial space, because
b<12ell+96 and its exhaustive loop has 2^(b+6) iterations. Its fixed
C=4096 retained strings occupy O(n) ordinary classical bits.

Only one helper runs at a time in depth-first generation. Allocate its
complete dense prefix lazily on entry and release it before returning.
Charge all initialization, unused cells, staging and cleanup. The full
physical address length is O(n), included in all word/gate costs; the
source's old O(log n) address fee is NOT substituted. No exponential
circuit description or uncharged classical duplicate exists.

Source transforms/extraction and decoder arithmetic have polynomial
work: nq=O(n^4), K=O(log n) and each finite grid is polynomially long.
The source proof's explicit exact-integer score tables and streamed
loops give the conservative bound (n+1)^16 per acquisition/root/stage,
including the larger O(n) address fee. Thus I<=Qcap/6 and Qcap=O(n^4)
give on EVERY branch

 T<=C'[2^(n/9)(n+2)^20+(n+2)^24]
   =O(2^(n/9)n^24).

This includes every failed helper and interrupted recursion. No expectation
is substituted for a branchwise gate count. Total physical qubits are
O(2^(n/9)n^5): the full HIGH prefix is O(Ln), and LOW scratch plus
source/pending phase wires are polynomial and absorbed by this envelope.
For n with no HIGH call the same bound remains an upper bound.

For ordinary classical memory, the depth-first pending phase count is
at most 1+sum_i(k_i-1). The uniform overestimate
k_i<=4b_i/3+16ell+130 (also for LOW) gives at most
4B/3+48ell+388<=64(n+1) for n>=256. Each full signed label has
O(n+log q0)=O(n) bits, including on bad extraction branches where the
returned estimate still has bounded word length. Coefficients, depth-three
frames, fixed-C LOW lists, extraction/control counters and K decoder
records fit O(n^2) ordinary bits jointly. All LARGE tables, sorting data,
counts and rank metadata occupy counted basis qubits with only a fixed
number of O(n)-bit staging words. Thus S_C=O(n^2).

All smaller n use finite literal caps and finite arithmetic. The fixed
n<256 branch and any finite inequality exceptions enlarge only absolute
outside constants, independent of N and s. The program and source promise
are defined for every N; there is no instance-dependent advice.

For B_T=2^(n/9)n^24, log2 B_T=n/9+24log2n, so the defined growth index
is exactly 1. Likewise B_Q=2^(n/9)n^5 has index 1. The classical n^2
and original-copy n^4 representatives each have index zero. All four
structured records concern this ONE three-level algorithm/configuration.
No resources from a different height choice or physical implementation
are combined. The projection/ranking helper and variable arity are substantive
algorithm changes, not just a relabeling of a prior numerical envelope.

## 7. Fractional error tolerance

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For every N,s, malformed fraction zero gives unconditional full-secret
success at least1-2^-8 jointly with all four resource bounds above. No
positive corruption tolerance or impossibility of robustness is asserted.
The fifth expression has no numeric score. No sample upper bound is
substituted into a count to manufacture a fractional guarantee.
