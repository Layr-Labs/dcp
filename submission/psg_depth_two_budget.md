# Complete profile, record and budget proof for PSG-D2

This required proof is used jointly with psg_depth_two.md,
psg_depth_two_base.md and psg_depth_two_compiler.md. Every one of the
five claims cites all four files. Sections 2--10 below reproduce the
complete positive theorem from the exact bounded depth-two source with
package-local interfaces. The ancillary literal time-prefactor barrier
is not a formal claim and is not needed here.

## 1. Exact construction sources and proof closure

Immediate source: psg_depth_two_transfer.md, SHA256
`2fb8ec6ce3d8d3d38e4c111908e392b7478b7e865db926b7858a196aa9533a07`.
Its independent bounded audit is SHA256
`3cfd4283ce8e8c288823b1eaa79241fb0c0e5f3ba50e953f6e38da0258695635`.
The older exact count/virtual-record template is psg14c_streamed_budget.md,
SHA256 `2668b8f2c135c52a4911db4766a458f312b24a485e12d06d7cd7b5663b2ab854`,
which reproduces psg14c_record_budget.md, SHA256
`41021054aeed39ebeb552fc13dfce9717245f3c3cedbb9761ee2236c835cdca3`.
The present package was built after those notes. All new profile, exact
source count, local guards and resource arguments are given below; all
unchanged semantic, helper and literal controller arguments are in the
other required files. Source/review hashes record reuse, not correctness
premises. No external proof is required to execute or review this package.

## 2. Exact mathematical sources and one parameter point

The direct semantic source is public PSG14C, submission
`30304a9e-15d5-4b58-9998-d5a4ccc1a67e`, commit
`398d8457f6c25e29a941403e4e75eccb290dda79`,
[proof](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/submission.json),
SHA-256 respectively
`2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6` and
`626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6`.
Its source/transform/EXTRACT, disjoint-pair instrument, unused-bit proof,
odd geometry, multi-bit 2-adic decoder and virtual-record model are used.
The proof steps needing a change of depth are closed below; correctness
is not inferred from the public entry's status.

The actual online compiler construction is in
`psg14c_compiler_transfer.md`, SHA-256
`0524ec65f682efc625237ad074d71430cfdfdf60d6e80cc1ecb6167b82e61224`.
Its full G.2--G.4 fixed-field/tape-head/marked-strip stream is retained.
The K=2^17n concentration choice and old finite-precision split come from
`psg14c_record_budget.md`, SHA-256
`41021054aeed39ebeb552fc13dfce9717245f3c3cedbb9761ee2236c835cdca3`.
The required base and compiler appendices reproduce those actual constructions
in full. No source or generator oracle is assumed.

PSG14C credits CYG1 note `70564803-3637-426f-9587-e1333aa07b39` for its
parity-support disjoint-pair mass and two-row factorial-moment bound, with
CYC1 credited upstream. The earlier bounded-transfer author read their arguments as reproduced in
PSG14C Section 4.3, without the originals. That historical read chronology
is preserved. The current package uses the same reproduced disjoint-pair
proof; its author separately read CYG1 for later cyclic research.
All inherited source credits and private-alias distinctions remain required.
No private local alias is equated to a public archive, and no review verdict
is a proof premise. The source's corrected positive K in the M=1 case is
preserved.

For n=ceil(log2 N)>=256 use the exact TWO-level profile in Section 3 and

    q0=(2R+1)^2,
    K=2^17n,
    Qroot=4096q0,
    Wroot=4096*2^R,
    Proot=4096n^2,
    Hmax=2048K=2^28n,
    Qtot=Hmax*Proot=2^40n^3,
    epsilon(n)=1/(2^33n^2).                             (D1)

Every odd and 2-adic stage uses exactly this positive K, including M=1.
Root-local counters start at zero. The source guard is checked before
acquisition; the weight is checked/charged before the positive combiner
attempt, after child construction. A local abort yields a neutral record
and stops that root only. Each actual or dummy record consumes exactly Proot.
Only the odd stage count is zero when M=1.

Root EXTRACT uses its exact general formula with P_label=Qroot:
h_extract=ceil(log2(2^16Qroot(n+5))), F=2^21h_extract. For n<256 retain
the original mF=2^20(n+16) one-copy finite shadow algorithm and its old
literal EXTRACT precision P_label_old=2^40n^4. Its final actual padding
uses Qtot=2^40n^3. No main profile is evaluated on the finite branch.

## 3. Exact two-level profile and all root widths

For a positive trial R put delta(R)=ceil(log2(3(2R+1))). Retain R and
R-delta(R) if the latter is positive, then stop. Reverse their order to
obtain v_1,...,v_m=R, with m<=2. Choose the least positive integer R for
which twice their sum is at least n. Scan trials sequentially; no capacity
monotonicity is assumed. Put u=max(1,floor(R/4)).

Let l=ceil(log2 n) and

    Rtest=ceil((n+2l+4)/4).

For n>=256, Rtest<=n/2 and 3(2Rtest+1)<=4n. Its decrement is therefore
at most l+2. Its second value is positive because Rtest>=n/4>l+2.
The trial capacity is at least 4Rtest-2(l+2)>=n. Minimality and the
at-most-two-values bound prove

    n/4<=R<=Rtest<=n/4+(1/2)L+5/2,
    2^R<8sqrt(n)2^(n/4),                               (D2)

where L=log2 n. At n=256 and thereafter L+5<=n/4, so Rtest<=3n/8.
Also delta(R)<=l+2<=L+3<=n/8<=R/2. Thus both selected values are
positive, m=2, v_1>=R/2, v_i>=u, n=O(R) and

    R<=3n/8, 2R+1<=n, q0<=n^2.                        (D3)

The scalar inequalities hold at 256; their real differences increase
thereafter. The ceilings are included in the displayed slack. All choices
are exact integer operations on public n.

For PS_TREE(D,B), 1<=D<=n and 0<=B<D, assign b_2=min(2v_2,B) and
b_1=B-b_2, omitting absent/zero-width levels. Capacity at least n ensures
0<=b_1<=2v_1. Put r_i=b_i+1 and p_i=sum_(j<i)b_j. The tree is exactly
the source's depth-first verified-pair recursion with these widths. B=0
returns a leaf without a combiner. A zero-width level returns its child.
Every returned tree has at most product_active r_i<=q0 nominal leaves.
This includes partial rows, partial lower levels and all D requested by
the odd and multi-bit decoders.

The numeric output label is a full signed sum of those nominal leaves.
It is divisible by 2^B and has |W|<2^(D-B)q0 after dividing by 2^B.
Its sign and word width are O(n+log q0)=O(n), even on incorrect numerical
label branches. No zero/high label is rejected by a new selection rule.
The nonzero incidence vector uses disjoint leaf sets and coefficients
in{-1,0,1}, exactly as in the original pair projection.

## 4. Fresh root law, two local cutoffs and exact precision

The source's disjoint-pair calculation applies to each positive width b:
k=b+1 fresh uniform low weights, complete adjacent disjoint pairing,
size-biased fiber tail and bounded discovery give fresh success at least
37/50. It is an average BEFORE fresh child generation, not a bound for
an arbitrary fixed child-label list. Query registers are separate from
the held phase register. All selection kernels depend only on numeric
low residues, independently of the held phase.

The unused-block induction is independent of a maximum depth of three.
At a leaf, the numeric Fourier label is uniform. At a fresh node, child
calls use disjoint fresh sources, and its selection kernel reads only
bits below p+b. On any finite successful low transcript, at least one
uninspected high leaf block has coefficient +1 or -1 in the output.
Averaging that uniform block gives a uniform output quotient modulo
2^(D-p-b). Fresh disjoint calls retain conditional independence. Failures
release all children and restart, so the conditional positive success
bound gives almost-sure termination. The same induction closes at depth
two, including a skipped zero width. It does not condition on EXTRACT
success or later cap survival.

Each accepted leaf costs at most two raw copies in expectation; odd-part
label rejection accepts with probability 2^d/N>1/2, and a direct 2-adic
leaf costs one. Let a=50/37. Conditional geometric sums at every reached
fresh attempt give E_i<=a r_i E_(i-1), with E_0<=2. Attempt cost and
success need not be independent. The event of reaching attempt j depends
only on its earlier failed attempts; its new children have the same
uniform conditional expected cost. Consequently every requested root has

    E acquisitions<=2a^2 product_active r_i
                   <=(5000/1369)q0<4q0.                (D4)

Inserted missing factors only increase this bound. It includes B=0,
partial/zero widths, odd M absent and earlier wrong scalar histories.
For such wrong histories, equal held basis magnitudes and separate-query
selection preserve the numeric low-label and resource law; correct phase
identities are needed only after correct earlier decoder estimates.

For level i, expected attempts in one root are at most
a product_(j>i)(a r_j)<=2 product_(j>i)(3r_j).
Our decrement gives 3r_2<=3(2R+1)<=2^(R-v_1). Thus multiplying by
2^v_i and summing at most two active levels yields expected weight at most
4*2^R. Partial/zero levels only reduce this bound. Qroot=1024*4q0 and
Wroot=1024*4*2^R therefore each have clean cutoff probability at most
1/1024 by Markov on the uncapped reference process.

Both are actual before-action guards. Children already built before a
failed parent check remain charged. An abort propagates only to that root,
then its record pads and the whole fixed schedule continues. These expected
bounds prove cutoff probabilities; hard guards enforce all-state resource
limits on every branch, including arbitrary malformed states.

Each EXTRACT call with P_label=Qroot has uniform true-label error at most
1/(2^14Qroot); at most Qroot calls give local total 2^-14. The formula is
valid for this positive integer budget as in the source's proof, and its
actual test rounds and label decoding are paid. Couple clean capped and
ideal uncapped roots until a cutoff or numerical-label error. Their local
record laws disagree with probability at most

    p0=2/1024+2^-14=33/16384.                            (D5)

This is unconditional before the fresh record, not conditioned on it
remaining clean or on all records succeeding. Neutral score 0 and bounded
clamping in[-1,1] give the same uniform clean mean allowance 2p0+1/625.

## 5. Odd and 2-adic decoders are fully specified

Keep N=2^a2 M with M odd and d=floor(log2 N). If M=1 put s1=0 and
Sodd=0, but keep K positive. Otherwise set

    hmax=1+floor(u/8)=1+floor(R/32),
    h=min(d-a2,hmax), B=d-h>=a2,
    stride=max(1,h-4), nq=2^(h-1)q0.

Use the original CRT unit alpha_j, which is 1 modulo2^a2 and equals
2^(j*stride)(2^(B-a2))^-1 modulo M. A fresh source transformed by this
unit has uniform Fourier label; accept it if k<2^d, apply X to its row,
and use it as the PS_TREE(d,B) leaf. A root has phase frequency
f=2^(j*stride)W for theta=s1/M by the same exact integer identity.
No odd factorization or source inverse is used.

For each odd stage take K isolated ROOT RECORDS. Each successful root is
measured once in a fresh fair X/Y basis, storing frequency, basis and sign;
an abort stores the neutral flag. Then pad that record to Proot and reset.
The candidate grid is P_j=j*stride+ceil(log2 nq)+8 bits. Stage zero scans
the full grid; later stages scan the one or two exact integer intervals
within circular radius 2^-(j*stride+2) of the previous center. Score each
candidate with the exact stored sign times the clamped source table,
using zero for neutral records. Keep its least maximizer. All loops,
fixed denominators, streamed residues and exact final rounding are retained.
The stage count is least Sodd with 2^(Sodd*stride+2)>2M.

The exact ideal signed-frequency characteristic bound uses only the
uniform uninspected h-bit blocks and q0 nominal-leaf count. Both were
proved in Section 4. Thus the source's near mean at the nearest grid point
is at least (1/2)cos(pi/128), while every far point has mean at most
(1/2)cos(pi/8), with gap >0.0379. Its circular arc induction, endpoint
coverage and final floor(Mz+1/2) mod M therefore apply with this new q0.
No high-label or success-conditioned substitute distribution is introduced.

For the 2-adic part use the source's MULTI-BIT procedure, not the earlier
parity-repeat decoder. With g known low bits and integer t0, set
wd=a2-g, h=min(wd,hmax), sh=(s1+M*t0) mod N. Obtain K ROOT RECORDS
from PS_TREE(wd,wd-h), using shifted source copies and numeric kk=k mod2^wd.
Scan r=0,...,2^h-1 with exact clamped-table score based on W*r mod2^h.
Keep the least maximizer, update t0<-t0+2^g*r and g<-g+h, and repeat.
A wd-h=0 tree is a leaf. There is no odd-W filtering or root reuse.

When earlier estimates are correct, the row phase is exactly
exp(2pi i W*rem/2^h). The quotient W mod2^h is uniform by Section 4,
so the ideal true score mean is 1/2 and every wrong residue has mean 0.
If earlier estimates were wrong, this phase identity is not assumed;
all loop lengths, scalar ranges and local caps still enforce resource
safety. The actual block count is deterministic and bounded above in Section 6.
The final residue is (s1+M*t0) mod N on every branch.

## 6. Finite record counts, exact Q and inverse-quadratic fraction

The odd schedule has Sodd<=1536. For h<hmax the bound is at most 8.
For h=hmax,R>=256, stride>=R/64 and n/R<=4 give at most 257 stages.
For R<256, n<=4R<1024 and Sodd<=n. These also cover an absent odd part.
The 2-adic block count is ceil(a2/hmax)<=128 because hmax>R/32 and
n<=4R; we may retain the common conservative 192 bound. All actual
stages use exactly K records even after wrong earlier estimates.

Thus there are at most 1728K actual records. Each root's count is at
most Qroot<=4096n^2=Proot by (D3), independent of its state or outcome.
Use a separate padding counter after return/neutral abort to reach Proot.
After computing the saved candidate, consume dummy records of Proot
acquired/discarded copies until the total record count is exactly
Hmax=2048K. Dummy corruption cannot change the saved classical result.
There is no whole-run abort or retry after padding begins. Every actual
record is reset; scratch is reused and old private entanglement cannot
remain in fresh zero work.

Main-branch total acquisitions are exactly

    Hmax*Proot=(2^28n)(2^12n^2)=2^40n^3.

For n<256 keep mF=2^20(n+16) one-copy shadow records, EXTRACT with
old precision P_label_old=2^40n^4, and the full exact scan t in[0,N).
Compute and store the least maximizing residue, pad directly to Qtot=2^40n^3,
then return the stored residue.
Since mF<=17*2^20n<=2^25n<=Qtot for every n>=1, the count is nonnegative
and exact in this branch, including n=1,N=2. The main profile is never
used there. Both branches have the same fixed count rule.

With the expression in (D1),

    floor(epsilon(n)Qtot)=floor((2^40n^3)/(2^33n^2))
                         =128n.                        (D6)

This budget is among all actual acquired copies, including rejected leaves,
local aborts, record padding, dummy records and final finite padding. It
is not a per-copy noise probability or a big-O substitution for actual Q.

## 7. Adaptive virtual records and full-secret success

The exact model is reproduced in main Section 1 and base Section 10. It requires fresh ideal clean
copies in tensor product with every other system. A reset record starts
from pure zero work, independently of an arbitrary conditional private
reference state. Condition on the complete earlier real/virtual classical
history and the current stage's actual parameters. Share the virtual clean
record with the real one until its first malformed acquisition; afterward
continue only the virtual record by its ideal conditional kernel and fresh
analysis randomness. Flags are decided before delivery. This adaptive
prefix coupling preserves the full clean capped-record marginal without
conditioning on the actual record staying clean. It includes neutral
aborts, the one measurement and all padding. It is a coupling of outcome
laws, not physical cloning or an extra actual source.

Each bad copy contaminates at most one isolated record. Every score is
bounded in[-1,1]. The pathwise budget (D6) therefore gives, simultaneously
for all candidate scores at any stage, actual/virtual average difference
at most 2(128n)/K=1/512. Dummy/ignored-padding faults may be counted
conservatively. No independence of corruption events or actual records
is used. Clean phase identities apply on correct earlier arcs/prefixes;
resource laws hold also on the remaining histories.

For each fixed stage candidate, virtual centered score increments have
conditional interval width two. Conditional Hoeffding gives

    Pr[|sum(X_i-E[X_i|past])|>=Kt]<=2exp(-Kt^2/2).

For t=1/512, K=2^17n this is 2exp(-n/4)<2^(1-n/4).
All mean/tolerance allowances are the same constants:

    eta=2p0+1/625+1/512+1/512
       =48817/5120000<0.009535.

Twice eta is below the odd gap 0.0379 and the 2-adic gap 1/2.
The odd nearest candidate remains better than all far candidates; the
2-adic correct residue remains the unique maximizer on these good events.

Here h-1<=R/32<=n/64 and log2q0<=2L. Thus the odd grid's log2nq is
at most n/64+2L<=n/8 for n>=256; for example, the stronger scalar
2L+2<=7n/64 holds at 256 and increases thereafter. The same ceiling/count
slack gives at most 2^(n/8+12) candidates per stage, including stage zero.
The 2-adic grid 2^h<=2^(1+n/64) is smaller. A union bound over at most
2048 actual stages and their fixed-at-stage-start candidates gives

    failure <2^11*2^(n/8+12)*2^(1-n/4)
             =2^(24-n/8)<=2^-8                         (D7)

for every n>=256, strictly at the endpoint as well because e>2.
Conditional stage-start bounds and induction on the correct prior arc
or prefix justify random stage parameters. Independence of stage successes
is not assumed. Exact circular rounding and CRT then return the entire s.

In the finite branch, old precision and the unchanged table leave virtual
conditional means above 3/8 for s and below 1/8 for every other residue.
The old mF martingale tail and union over N<=2^n give failure below 2^-20.
At most 128n one-copy records can be contaminated, with
2Bbad/mF=n/[4096(n+16)]<1/4096. Thus the virtual 5/16 versus 3/16 gap
keeps the true least maximizer unique. Final padding cannot change it.
This covers all N=2 cases and keeps success at least 1-2^-8 on the whole
domain. Uniform local label errors enter virtual means; no event claiming
that all O(n) roots succeed is used.

## 8. Literal online controller and complete root work

Select the full G.2--G.4 online implementation reproduced in the required
psg_depth_two_compiler.md. It uses power-of-two DATA rows, a fixed number of ready operand
words, physical tape heads for carry/return walks, and marked bit-loop
strips. A complete m-bit pass costs O(m+A) raw bit/head actions including
address setup, known-bit reads, all carries, endpoint tests, rewind,
short/empty setup and reverse passes. A=ceil(log2(M_alloc+2))=O(L) is
charged to every raw indexed action, gate and fixed-arity ready-address use.
There is no stored O(R^2)-gate instruction tape or free address emission.

The two-level profile gives n=O(R), u>=R/8, n<=32u for large R, and
A=O(u)<=O(v_i). Thus even b_i<u partial rows pay O(A) setup once per row.
Low labels are copied by indexed bit windows; no full n-bit walk is made
for each residue bit. Known weights and found-list bits are read on every
full row scan, including identity slots. In a positive attempt, k=b+1,
and all oracle/inverse rows cost O(k(b+A))=O(R^2) raw actions per iteration.
At most 64 exclusions, diffusion and their inverse scans add O(k+A).
A Grover trial's O(v_i)-bit draw/decrement/limit tests are covered. There
are at most 4096 trials with O(2^v_i) iterations each.

Initial f(y) on the retained original index, residue measurement/reset,
fresh query preparation/measurement, classical verification, sorting,
list insertion, adjacent-pair projection, sign/flag measurements, affine
clearing and failure cleanup all use these same complete scans. Full signed
output sums cost O(nk)=O(R^2) raw work once per attempt. The fixed b/k
strips are prepared after the weighted guard in O((b+k+1)A)=O(R^2) raw
work; global label strips are initialized at charged polynomial setup.
All finite Clifford+T expansions and literal inverse words are included.
Thus every complete paid attempt, on every branch, costs

    O(R^2 L2^v_i).                                     (D8)

Reuse in-place O(b) carry scratch after each row. No O(kb)-node quantum
Boolean history is retained. A parent creates its query/strip buffers only
after all children and its weighted guard; no parent query stays allocated
while replacement children are built.

Each root's actual weights sum to at most Wroot=4096*2^R, including child
attempts in failed ancestors. Therefore all its combiner work is
O(R^2 L2^R). There are O(n) actual records; dummies only pad. Using (D2),

    T_comb=O(nR^2 L2^R)
          =O(n^3 L sqrt(n)2^(n/4))
          =O(n^(7/2)L2^(n/4)).                          (D9)

The fixed R profile is shared across every requested D,B. Wrong prefixes,
arbitrary labels, neutral roots and failed projections cannot enlarge
the guarded weight/call counts or literal work in (D8).

## 9. All other charged work and simultaneous storage

Depth-first recursion, zero-width returns, metadata, source/weight guards,
partial-stack release, dirty resets and final failed parent checks retain
polynomial cost per source/attempt event. Sources are capped by Qtot=O(n^3).
Every paid attempt has nominal weight at least 2^u, so across all roots
their number is O(n2^(R-u)). A fixed polynomial multiplying that count
is absorbed by (D9), since u=floor(R/4)>=floor(n/16). Already executed
child attempts stay charged. Each root has at most one failed weighted
check and a bounded-depth cap propagation. All last partial calls count.

Main EXTRACT has h_extract=O(log(n+2)) with its new P_label=Qroot=O(n^2).
Keep the conservative O(n^2 L^2) charged source/transform/reset bound per
call. Across Qtot=O(n^3) it is O(n^5 L^2), polynomial. Padding and counters
cost at most O(n^4 log(n+2)). Old finite precision has the same polynomial
space/work form. Every allocated zero, source n+1 cost, private coin,
measurement and reset is charged; none is free preprocessing.

Odd grids have O(q0 2^h) candidates and K=O(n) records; 2-adic grids have
2^h candidates. All numerical words and stored frequencies use O(n) bits.
Products, exact remainders, streamed residue updates, table access, clamp,
sums and least-tie comparisons cost polynomial(n) per grid point with
all address/control work counted. Since h<=1+R/32, their total is at
most polynomial(n)2^(R/32). The positive 31R/32 gap absorbs every fixed
polynomial relative to (D9). Exact profile search, CRT, finite table,
source parameters, counter constants and layout setup are polynomial too.
The explicit n<256 exhaustive procedure has a finite maximum and fits
by one absolute outside constant; it is an actual program, not advice.

The sibling/current phase count is sum_i(r_i-1)+1=B+1<=n. Original-index,
separate query, per-row reused carry, source/extraction and reset scratch
add O(n) qubits. There is no extra quantum table or state-copy access.
O(n) signed labels and K=O(n) classical records of O(n) bits, one active
O(R^2) residue DATA array, bounded found list, two frames, streamed grid
residues and arithmetic use O(n^2) classical bits. Fixed O(n) loop strips,
O(L) ready addresses/head fields and all local/global counters fit there.
Records are reused between stages; no exponential candidate or gate list
is retained. Thus S_C=O(n^2), S_Q=O(n) simultaneously on every branch.

## 10. Total output and the proved joint result

A source/work abort only supplies a neutral record. Successful roots are
measured exactly once. Numeric record encodings remain bounded on every
source state. Odd estimates are reduced modulo M or set to 0, and 2-adic
maximizers are h-bit residues. The last update has g<=a2 and t0<2^a2.
The final output is (s1+M*t0) mod N. The finite branch selects t in[0,N).
Wrong earlier scalar outcomes affect correctness only; they cannot enlarge
later loop bounds, numeric widths, root guards or total copy count.

The preceding source/selection/decoder, virtual-record and controller
arguments give the one selected all-N point in the exact model in main Section 1 and base Section 10:

    T=O(n^(7/2)L2^(n/4)), S_C=O(n^2), S_Q=O(n),
    Q=2^40n^3=1099511627776n^3 exactly,
    epsilon(n)=1/(2^33n^2)=1/(8589934592n^2),
    Pr[entire output=s]>=1-2^-8>2/3.                   (D10)

All constants are absolute and independent of N,s,the adversary and
outcomes. L=log2 n for n>=2; the exact n=1 branch is finite, or use
log2(n+2) for a positive whole-domain envelope. The time envelope has
coefficient 1/4 on n, nPower 7/2, logPower 1 and growth index 1.
Classical/quantum/source powers are 2,1,3 with growth index 0.
No lower time prefactor, maximal tolerance or invention claim is made.
