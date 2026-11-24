# Pair buckets with programmed threshold search

## 1. Theorem

For all $N\ge2$ and $s$ modulo $N$, put $n=\lceil\log_2 N\rceil$.
The algorithm recovers all of $s$ with unconditional probability
at least $7/8$ in the independent ideal problem and in the fixed-position
model of the fifth claim, with malformed fraction $2^{-20}$. The model
fixes the full joint input and malformed positions before private
randomness, with independent ideal reduced state on the good positions.
The joint every-branch bounds are
$$
T=O(2^{n/3}n^2(\log_2n)^2),\quad S_C=O(n),\quad S_Q=O(n^2),\quad
Q=O(2^{n/3}n).
$$
We use the native collective probe and dyadic lift from the attached
base13.md and short-readout.md, and the reciprocal quotient identity
from fast-score-arithmetic.md. The arithmetic used on each reported
copy is implemented by the measured basis tape of Section 3. The other
source handling, candidate stages, tests and cutoffs below are the
complete program.

## 2. Public stage parameters

For $n\ge1024$ set $B_*=\lfloor n/3\rfloor$, $h=n-B_*$,
$d_0=\lfloor\log_2N\rfloor$ and $B=d_0-h$. Thus $1\le B\le B_*$.
Write $N=2^a M$ with $M$ odd.

If $a<B$, recover $s\bmod M$ by odd stages $j=0,\ldots,J$, where
$\lambda_j=j(h-6)$ and $J$ is the least $j$ with $2^{\lambda_j+h}>4M$.
Here $M\ge3$ and $J\le1$. For the $j$th odd stage define the public unit $\alpha_j$ by
$$
\alpha_j=1\bmod 2^a,\qquad
\alpha_j=2^{\lambda_j}(2^{B-a})^{-1}\bmod M.
$$
After native readout, replace a reported residue $k$ by
$\alpha_j^{-1} k\bmod N$ in ordinary arithmetic. Keep its
row unchanged. Interpreted with the new label its clean phase
is precisely the phase for a multiplier by $\alpha_j$ and
effective secret $\alpha_j s$. Accept the relabeled reports in the centered signed interval
$[-2^{d_0-1},2^{d_0-1})$ represented modulo $N$. Use
the pair cells with width $b=B$ below. A useful paired response has
difference $2^BW$ and ideal positive phase $\exp(2\pi i 2^{\lambda_j}
W\theta)$, where $\theta=(s\bmod M)/M$. This is the phase
$\exp(2\pi i 2^BW\alpha_js/N)$ by the unit congruences.
Construct the odd grids as in Section 6. Round the last
accepted angle to recover $c=s\bmod M$, and put $M_0=M$, $D=a$.

If $a\ge B$, use one direct stage with $b=B$, no multiplier, and
truncation to $[0,2^{d_0})$. A useful response of difference $2^BW$
has phase $\exp(2\pi i W s/M_0)$ for $M_0=N/2^B\in[2^h,2^{h+1})$.
Search all candidates modulo $M_0$, giving the prefix $c$, and set $D=B$.

In either case $N=2^D M_0$ with $D\le B_*<h$. For $D>0$, use
one residual direct stage with $b=0$, full cyclic labels and no
multiplier. A record of label $k$ has its row rotated by the known
phase $\exp(-2\pi i k c/N)$ before searching candidates $t$ modulo
$2^D$. Its effective ideal phase for a correct prefix is
$\exp(2\pi i k t_*/2^D)$ for $t_*=(s-c)/M_0\bmod 2^D$. Output
$(c+M_0t)\bmod N$. If $D=0$ the prefix is enough.
This row rotation occurs after native label extraction, which never
depends on a previously decoded prefix.

For $n<1024$ set $B_*=0$, $h=n$ and use one direct stage with $b=0$,
full labels and no transform to search all $t<N$. This includes $n=1$.
Let $S\le16$ be the public number of stages. Every stage uses $R=2^{18}$
trials, one search packet and a distinct validation packet per trial.
There are $P=2RS\le2^{23}$ packets. Take $K=2^{38}(n+16)$ and
$M_{\rm raw}=K2^{B_*}$. Each packet acquires exactly $M_{\rm raw}$
copies. All trials run, even after a candidate has validated. Local
failure uses the fallback value zero and continues, hence exactly
$Q=P M_{\rm raw}$ copies are acquired on every branch.

## 3. Selected-cell packets

A packet consists of $K$ consecutive groups of $2^{B_*}$ positions.
For $b>0$ each group has $2^{B_*-b}$ rounds of $2^b$ raw positions
each. A round has $2^b$ cells indexed by low $b$ bits after the
prescribed truncation. Draw a single uniform $B_*$-bit word per
group. Its high part selects a round and its low part selects a cell.
Only the chosen round is read out. Acquire and release all other
copies without reading them. In the chosen round keep at most the
first two rows and labels in the chosen cell. On the third hit
release both and saturate its count at three. If exactly two hit,
apply CNOT from the first row to the second and measure the latter
in Z. On odd parity keep the first positive-phase row and signed
difference label. On even parity and all other occupancies the
record is inert and all rows are released. For $b=0$ choose one
raw position uniformly with the same $B_*$ bits, and retain its
label and positive row. Other copies count and are discarded.
All choices are independent of the fixed source.

### Balanced private acquisition order

Physically pack every group index $i=0,\ldots,K-1$ across all
$P$ packets at the same time. For each local raw offset
$r=0,\ldots,2^{B_*}-1$ within that group, acquire $P$ consecutive
copies, one for each packet. Draw an independent uniform
cyclic shift modulo $P$ for this set, and assign these $P$
acquisition positions bijectively to the packets in that
shifted order. Thus all packets have exactly one copy at
each offset and actual assignment is private. A packet's
selected round and cell for this group are chosen by the
independent private bits above. Keep the first two row
and label hits separately per packet. At the end of the
group carry out the prescribed pair instruments and save
their measured labels, output rows and inert flags, then
reuse the occupancy workspace for the next group. One
classical label word of each saved record is stored in
counted basis qubits. All $P$ packets coexist during
this acquisition phase. The number $P$ is an absolute
constant. Subsequent search reads the packets in their
original logical order and prepares its phase program
registers using one saved frequency word at a time. No
search affects the native readouts, pair operations or
acquisition schedule.

Implement each cyclic shift using $d=\lceil\log_2P\rceil+
\lceil\log_2M_{\rm raw}\rceil+80$ fair bits reduced modulo $P$.
The residue bias is at most $P/2^d$ in total variation.
There are $M_{\rm raw}$ shifts. Hence replacing them by
exact uniform choices in the analysis costs total
variation at most $2^{-80}$. The fixed modulus $P$ is an
absolute constant, so streaming the reduction costs
$O(n)$ bit work and $O(n)$ bits, including reading each
bit from fresh measurements with address fee $O(\log(n+2))$.

Use the collective Clifford+T extraction of base13.md and
the exact linear-pass lift of short-readout.md. The newly specified
ordinary integer products replace the helper’s quantum products,
and the stage-unit relabeling replaces its position permutation.
Set the constant precision parameter of short-readout.md to
$2^{90}$; otherwise use its formulas, giving a uniform unconditional
error probability at most $2^{-104}$ per clean readout, including
after each specified unit relabeling, which is a bijection on
the reported alphabet. Native report extraction always works on
the untransformed position wires. Conditional on true Fourier
label $k$, the row phase relation satisfies
$k s = (\alpha_j^{-1}k)(\alpha_j s)\pmod N$. Hence the classical
relabeling implements the same logical phase input on ideal
records. Arbitrary measured reports are still well-defined
residues. No coherent position multiplication is performed.

### Charged per-copy readout

The constant precision factor gives $F=\Theta(\log(n+2))$
rounds per basis, each with $O(n)$ addressed Clifford+T gates
and measurements by the collective register-translation
construction in base13.md. It uses a constant number of
ripple additions and comparisons, so a linear pass of raw
register addressing suffices. Gates and code generation
cost $O(n\log(n+2))$ per round inclusive of the address
fee.

Keep one unsigned count of plus outcomes for each of the
$O(n)$ probes in measured basis qubits. Use binary increment
only on positive outcomes. One monotone count after $F$
trials incurs at most $2F+O(\log(F+1))$ visits and flips in
its carry chains over all rounds: bit position $j$ is
visited at most $1+F/2^j$ times. Reading or toggling one
basis bit costs $O(\log(n+2))$ including the address and
index progression. Traverse all counters in each round
with ordinary serial indices. All resets and $O(nF)$
outcome tests are charged. The work is therefore
$O(n(\log(n+2))^2)$ even on an arbitrary sequence of
outcomes. After the probes, the fixed rational direction
table comparisons use only fixed-polynomial work in the
$O(\log(F+1))$-bit counter width, hence $O(n(\log(n+2))^2)$
addressed work over all directions. The precise dyadic
lift needs $O(n)$ elementary bit steps beyond the final
multiplication by $N$ to round the phase estimate.

For this multiplication and the modular unit relabeling,
use the deterministic multitape Turing-machine integer
multiplication of Harvey and van der Hoeven,
[Integer multiplication in time O(n log n)](https://annals.math.princeton.edu/2021/193-2/p04).
Use the usual binary encoding on its fixed number of linear
tapes. For operands of width $O(n)$ the number of steps and
visited tape cells are $O(n\log(n+2))$. Simulate the fixed
finite transition table with a constant number of ordinary
head positions and state fields. Store its tapes in measured
basis registers (constant bits per symbol). Read a symbol's
bits with Z measurements, write with X toggles based on
the old bits, and move each classical head by one position.
A newly visited cell is a fresh basis zero. Give each tape
disjoint indexed addresses by interleaving the fixed number
of tapes. At most $O(n\log(n+2))$ cells can be allocated on
any copy. Their address width and the ordinary cost of
head movement and address generation are $O(\log(n+2))$,
including when the packet bank is allocated. Counting
all input loading, output copying, head moves and clearing
the visited cells, a product costs $O(n(\log(n+2))^2)$
charged work and $O(n\log(n+2))$ measured basis qubits.
The classical controller uses a constant number of words
and head counters, altogether $O(n)$ ordinary bits.
Tape simulation uses only ordinary addressed basis data.

The final estimated dyadic numerator and $N$ have $O(n)$
bits. Multiply by this routine, copy its needed upper bits
and round exactly; guard a reported endpoint $N$ by mapping
it to zero. For relabeling let $w_0=n+1$ and precompute
$u=\lfloor2^{2w_0}/N\rfloor$ once using ordinary long
division in $O(n)$ bits. For product $p$ of the reported
residue and the public inverse unit, $0\le p<2^{2w_0}$.
Then $\lfloor pu/2^{2w_0}\rfloor$ is the exact quotient
$\lfloor p/N\rfloor$ or one smaller. Recover the remainder
by multiplication and subtraction and one conditional
subtraction of $N$. These are a constant number of
$O(n)$-width products and linear passes at the same
addressed work bound. No long division occurs per copy.
The once-per-stage inverses and all parameter computation
use ordinary polynomial-time, linear-space integer
arithmetic. Together, all operations per processed copy
cost $O(n(\log(n+2))^2)$ charged work. Acquisition,
fixed cell checks, release on skipped positions, and
record arithmetic satisfy the same cap. These counts
hold on every padded transcript.

In a clean round the probability of a given cell hit is between
$1/(2\cdot2^b)$ and $1/2^b$. The probability of two hits is
at least $1/64$ by the binomial formula: for $L=2^b\ge2$ use
$\binom{L}{2}\ge L^2/4$ and $(1-1/L)^{L-2}\ge e^{-1}>1/4$.
The fair odd parity makes a record useful with probability
at least $1/128$. Conditional on usefulness, its signed $W$
is a difference of independent uniform high blocks of
width $A=2^h$. The two low values are equal. The centered
interval begins at a multiple of $2^B$, so this statement
covers both truncations. Thus $\mathbb E W^2\le A^2/6$ and
$$
|\mathbb E \exp(2\pi i \gamma W)|\le
\left|A^{-1}\sum_{k=0}^{A-1}e^{2\pi i \gamma k}\right|
\le \min(1,(2A\|\gamma\|)^{-1}).
$$
The difference characteristic is the squared magnitude of
that sum. In clean $b=0$ packets the frequency is exactly
uniform modulo the searched modulus. Records in distinct
groups are independent in the ideal marginal.

## 4. Coupling the selected records

For analysis run the native label instruments on all raw positions.
Native choices do not depend on the recovered prefixes or selected
cells. Unobserved results on unused positions can be marginalized,
since operations are local and the source is fixed before randomness.
For a good position the Fourier index can be measured latently before
these probes. The translations are diagonal in that basis, and the
position trace eliminates the off-diagonal terms. The good-position
marginal supplies independent uniform true latent labels. Given these
labels the retained good rows are pure product phase states. Conditioning
on other position reports cannot change these pure rows. Malformed
reports can still depend on good labels through source correlations.

Make a virtual clean pool from those same latent good labels and
independent ideal replacements for all malformed positions. Its
marginal is the independent ideal experiment. Count as replaced
every malformed position and every erroneous good report.
Each replacement affects at most two cells in its round, its
actual and virtual cell, possibly one or zero after truncation.
For $b=0$ it affects one choice. The resulting comparison geometry
is independent of the private cell selections. On unchanged
selected cells, actual and virtual pair instruments receive the
same pure product input rows and can use identical parity results.
The remaining actual and virtual instruments have their own
conditional joint laws. This constructs a coupling with the correct
marginals even when actual malformed rows are entangled with each
other and with other raw systems. On unchanged active records the two
output rows and their labels are exactly identical and pure.

In the ideal uniform-shift comparison each packet receives
one copy out of each chronological set of $P$ acquisitions,
uniformly and independently across sets. Let $m$ denote the
number of malformed copies assigned to one fixed packet.
It is a sum of independent Bernoulli variables with total
mean at most $\epsilon M_{\rm raw}$, where $\epsilon=2^{-20}$.
The fixed global corruption set has size at most
$\epsilon P M_{\rm raw}$. Using the exponential moment at
$t=\ln2$ gives
$\Pr[m>2\epsilon M_{\rm raw}]\le
\exp[-(2\ln2-1)\epsilon M_{\rm raw}]
\le\exp(-\epsilon M_{\rm raw}/3)$.
This holds for every packet; no independence across packets
is required. Conditional on all allocations, the native
wrong-report count $E$ on good positions of a packet has
expectation at most $2^{-104}M_{\rm raw}$. By Markov,
$E>2^{-40}M_{\rm raw}$ has probability at most $2^{-64}$.
Both probability statements persist after averaging over
the assignment.

Given full geometry, including the reported labels in all
virtual rounds, the selected-cell draws in a packet are
independent across groups. The number $H$ of affected
selected cells is a sum of Bernoulli variables with
conditional mean at most $2(m+E)2^{-B_*}$. On the bounds
above this is at most
$(4\epsilon+2^{-39})K<2^{-17}K$. The same moment argument
bounds the conditional chance $H>2^{-16}K$ by
$\exp(-2^{-17}K/3)$. The geometry distribution is independent
of the choices of selected cells after conditioning on the
allocations: apply all raw label instruments first in the
analysis, then act on the records selected from the
resulting local states. As argued above, outcomes of
unused probes can be marginalized.

Union over $P\le2^{23}$ packets of these three bounds,
using $M_{\rm raw}\ge K=2^{38}(n+16)$, gives failure below
$2^{-39}$ (excluding the separate shuffle approximation).
Denote the joint event with at most $2^{-16}K$ changed
records in every packet by $\mathcal E$. All threshold
estimates on this event are subnormalized and the ideal
clean tails use their unconditional law. Conditional on
allocations, the virtual pool is still exactly the
independent ideal experiment because the allocations
are independent of the source and use disjoint positions.

## 5. A counted phase program per live row

For a frequency $f$ and modulus $D_0$ prepare a program register
in the Fourier state
$$
|\chi_f^{(D_0)}\rangle=D_0^{-1/2}
\sum_{x=0}^{D_0-1} e^{2\pi i f x/D_0}|x\rangle .
$$
For an odd stage with points $t/2^{p_j}$ defined in Section 6,
take $D_0=2^{p_j}$ and $f=2^{\lambda_j}W\bmod D_0$. For the initial
high-valuation direct stage use $D_0=M_0$ and $f=W\bmod M_0$.
For the residual stage use $D_0=2^D$, $f=k\bmod D_0$, with the
one-time row phase offset in Section 2. For the finite direct case
use $D_0=N$, $f=k$. Store inert flags in basis qubits. After
preparing a program, free the ordinary frequency word, keeping
only program, row and inert flag for that record. All moduli,
products and phases at preparation use $O(n)$-bit words.

Translation of this program by $t$ modulo $D_0$ has eigenvalue
$\exp(-2\pi i f t/D_0)$. Apply the exact ripple translation,
controlled on the row being one, and then H on the row. The row
test sign $Z=\pm1$ is exactly the target comparison X measurement
on the ideal program. Valid residues undergo a permutation and
padding is fixed. Compute the new residue with ripple arithmetic,
swap, and erase the old residue using the inverse permutation.
For every useful record the score is $4Z-3$, either $1$ or $-7$.
An inert record has zero. Let $\Pi_t$ be the conjugated projector
onto strictly positive total integer score. For a fixed candidate
the row test projectors act on disjoint registers. For a coherent
candidate compute its value and validity, transform the rows,
add weights reversibly into a signed $O(\log(n+2))$-bit counter,
flip sign for a positive total and valid index, and uncompute.
An invalid candidate gives identity. Use a classical-candidate
projector measurement with a separate packet for validation.
Every controlled modular translation is $O(n)$ gates on
$O(n)$ reused scratch, and each score update is $O(\log(n+2))$
gates. If the index is invalid skip the translation using
the exact validity flag. The processor touches every live
record by ordinary control, at cost $O(Kn\log(n+2))$ including
all address and generation fees. There is no quantum-indexed
table.

Use approximate program initialization followed by exact
query and validation gates. To prepare the uniform state
on $[0,D_0)$, follow its binary prefix tree. At each level
there is at most one partially filled prefix. Full active
prefixes split equally, and the partial prefix splits with
amplitudes proportional to the square roots of the two child
counts. Compute the corresponding controls with reversible
prefix comparisons and clear them. A controlled Y-rotation
can use two CNOTs and two unconditional half-angle rotations
with opposite signs. Per-bit phase rotations with angles
$2\pi f2^\ell/D_0$ then create the desired phases.
One current ratio of integer subtree counts fits an $O(n)$-bit
staging area. Compute probabilities and rotation amplitudes
to $O(\log(n+2))$ fractional precision using integer division,
square-root bisection and fixed-precision trigonometric
arithmetic, taking a fixed constant times the needed accuracy
bits for the square-root step. Work is polynomial. Use uniform
single-qubit Clifford+T synthesis by Dawson and Nielsen,
[The Solovay–Kitaev algorithm](https://arxiv.org/abs/quant-ph/0505030).
Each classical gate word and compilation scratch take a
polynomial of the logarithm of the required accuracy in bits.
Compile and apply one single-qubit rotation at a time.
The fixed base gate net is input-independent, and every
synthesized gate is charged.

The needed operator-norm precision for every approximate
rotation (including a residual row offset) is at most
$2^{-80}/(100 P K(n+2))$, rounded down dyadically.
There are at most $100K(n+2)$ preparation rotations per
packet. The total trace-distance cost of replacing all
preparations by exact ones is at most $2^{-79}$ by summing
their norm errors, including rounding the input matrices.
This hybrid is over the actual bounded initialization gates,
uniform over all preceding histories. It introduces no
additional cost per coherent query. Both versions have the
same allocated register layout. The controlled translation
and reflection themselves are exact, including on arbitrary
states in the program register.

## 6. Candidate sets and score margins

For odd stage $j$ set $p_j=\lambda_j+h+12$. In each trial
choose a uniform $u\in[0,2^{16})$. The candidates are circle
points $x=t/2^{p_j}$ with $t\equiv u\bmod 2^{16}$.
Their spacing is $16\,2^{-\lambda_j-h}$. Use the whole
circle at $j=0$, and later the arc about the preceding
center $x_0$ of radius $r_{j-1}+16\,2^{-\lambda_j-h}$,
with $r_j=2^{1-\lambda_j-h}$. At most two integer intervals
of coarse grid indices specify this set, with at most
$2^{h+1}$ entries even after extension. Compute their
integer endpoints by fixed-width rounding, and map a
padded index to the corresponding numerator by adding
its position to the appropriate lower endpoint and
combining it with the fixed $16$-bit offset. This uses
$O(n)$ exact reversible work per query with a validity
bit, and no candidate list.

A point is near if $2^{\lambda_j}\|\theta-x\|\le 2^{-8}/A$
for $A=2^h$, and far if $2^{\lambda_j}\|\theta-x\|\ge2/A$.
If the previous center is within $r_{j-1}$, the extended arc
contains any near candidate. There are at least 31 possible
integer numerators within radius 16 of the true real
numerator in units of $2^{-p_j}$, with different residues
modulo $2^{16}$. Hence an offset contains a near
point with probability greater than $2^{-12}$. On such an
offset every other point is far by the spacing. In later
odd stages on a correct-prefix history the relevant scaled
distances are bounded by
$2^{\lambda_j}(2r_{j-1}+16\,2^{-\lambda_j-h})
=4/64+16/A<1/4$.
For stage zero use ordinary circle differences and
$\lambda_0=0$. Thus the scaling introduces no alias in
the separation argument.

For ideal useful records the cosine mean at a near point
is at least $999/1000$ by the second moment in Section 3
and $1-\cos v\le v^2/2$. The mean at a far point is at
most $1/4$ by the geometric characteristic bound.
In high-valuation direct decoding, the true candidate
has cosine mean one. If $t$ is wrong, then
$\gamma=\|(s-t)/M_0\|\in(1/(2A),1/2]$.
The smallest nonnegative $j$ with $2^j\gamma\ge1/4$
has $j<h$ and $2^j\gamma\le1/2$. In the character product
of the independent bits of a uniform length-$A$ block this
bit bounds the magnitude by $1/\sqrt2<23/32$. The
difference-record character obeys the same bound.
For the exact residual or finite case, the true cosine
mean is one and the wrong mean zero by uniform labels.

Each clean record's integer weight lies in $[-7,1]$,
has mean at least $2^{-11}$ at a near or true candidate,
and at most $-2^{-11}$ at a far or wrong candidate.
Indeed the mean given usefulness is four times the cosine
mean minus three, and usefulness has probability at least
$1/128$. The least margin on the wrong side uses
$4(23/32)-3=-1/8$. At a fixed candidate and correct fixed
prefix, the ideal clean packet scores are independent.
This is unconditional over cell choices, or conditional
on all such choices because all clean rounds give the
same one-record distribution.

For each fixed candidate compare the hypothetical
threshold measurement on the actual packet and its
coupled virtual one. On unchanged records the actual and
virtual rows and exact eigenphase programs agree, so
the measurement signs can be coupled identically.
Conditional on their classical geometry they are pure
factors, even if the changed records remain entangled.
The at most $2^{-16}K$ altered outcomes on $\mathcal E$
change the score by at most $2^{-13}K$.
Thus the intersection of $\mathcal E$ with a wrong-side
threshold outcome implies a deviation of at least
$2^{-12}$ in the mean of the ideal packet. Dropping
$\mathcal E$ on that side, Hoeffding gives
$$
 \Pr[\text{wrong-side outcome and }\mathcal E]
 \le e^{-K 2^{-22}/128}<2^{-100(n+16)}=:p_* .
$$
These inequalities bound $\Pi_t$ for far or wrong
candidates and $I-\Pi_t$ for near or true candidates
on the subnormalized packet state on $\mathcal E$.
Use the fixed physical label report and program frequency
for a record on all branches, so these are estimates for
the defended circuits rather than a decoded-label oracle.

## 7. Reused reflection and independent-packet validation

For each trial prepare the uniform state on dimension
$D_{\rm search}=2^{h+1}$. Embed its direct candidates or
the selected odd grid by the map of Section 6, with invalid
padding. Choose a uniform $g\in[0,L)$, where
$L=2^{\lceil(h+1)/2\rceil+1}$. Apply $g$ Grover steps using
the exact reflection from Section 5 and diffusion about
the uniform candidate state. Measure the candidate.
Validate this one classical candidate on the trial's second
packet using its threshold measurement. Run every trial with
fresh private grid and iteration choices. Keep the first
validating result and ignore later results after their
scheduled work. When none validates return the local fallback
as prescribed. If the branch is direct, any validated
correct result gives its entire next residue. For an odd
stage every non-far answer suffices for the invariant
$\|\theta-x\|<r_j$ and the final rounding.

An odd trial is favorable when the grid contains a near
candidate. Every direct trial is favorable. For a favorable
trial with a fixed admissible preceding center, idealize
the search by replacing its oracle by the exact mark on the
unique intended candidate. In such an ideal prefix the
candidate register factors from the entire packet and its
purifying reference. At a coherent query, expand the
candidate in its basis, with squared amplitudes summing
to one. The wrong-candidate projector bounds and the
true-candidate complement bound from Section 6 show that
the squared norm of the single-query error on the
subnormalized state on $\mathcal E$ is at most $4p_*$.
The different candidates lie in orthogonal subspaces.
For a padded candidate the oracle is exactly identity.
Use skipped identity positions to compare the fixed
query cap. By a hybrid with the actual suffix after
each replaced query, the trace-distance cost of replacing
a favorable trial's entire search is at most
$2L\sqrt{p_*}$ on $\mathcal E$. This proof does not
use source independence in any actual prefix of a
trial. For a grid with no near witness keep its search
actual, even when its mark structure is ambiguous.

We justify this replacement and validation on correlated
packets and random preceding centers. The native extraction
and selected-cell pairing procedures use public transforms
and data-local measurements. They do not depend on earlier
logical outputs. For the analysis they can be applied to
their disjoint raw packets before the logical computation,
with a classical reference storing the analytical geometry.
The actual schedule prepares and counts all packet record banks before logical search. The
virtual reordering is only for analysis. The residual phase
offset and candidate arc can depend on a preceding answer,
and are applied only at their fixed logical stage.

For each possible preceding center, restrict to that value
of the earlier stage output. Before the current trial its
favorable-search packet is untouched by all logical
operations except its own fixed preparation. Earlier
operations may be entangled via the supplied input but act
on disjoint packets. In the state on $\mathcal E$, selecting a
branch of the earlier outcomes yields a reduced substate
dominated by the marginal without selecting those outcomes.
Consequently the bound on the squared norm in the hybrid
holds for the subnormalized branch with this fixed center.
This can be shown by including as reference the measurement
dilation of all earlier operations. The common later
channels, including validation and adaptive later stages,
do not increase trace distance. An oracle replacement leaves the native geometry that defines $\mathcal E$ unchanged.
Within a stage the trials have no outcome-dependent routing
and operate on disjoint packets. Hybrid trial replacements
therefore also obey the same bounds with their preceding
operations as reference. Sum the bounds over all relevant
previous centers, trial offsets and stage choices.

For validation, fix a candidate and preceding center.
The measured candidate is obtained by an instrument on its
search packet, disjoint from its validation packet.
The joint probability of proposing that value and an
undesired validation outcome is at most the probability
of that undesired outcome in the corresponding fixed
validator measurement on its packet alone. This is
the positive-operator inequality obtained by dropping
an effect bounded by identity on the other systems.
It also applies in the subnormalized state on $\mathcal E$
and after favorable search has been replaced by its ideal
mark. Sum over all fixed tested candidates and correct
preceding centers. There are at most
$P2^{4n+20}$ index, offset and preceding center descriptions
in all these sums, since each relevant numerator has
width below $2n$ in the main branch and the offset is
16 bits. The finite branch has only the direct
candidate family. With $L\le4\,2^{(h+1)/2}$ and the given
$p_*$, the total replacement and validation error is below
$2^{-20}$. The error of one-time synthesis is also charged.

For the ideal unique mark on a favorable trial,
$\sin\alpha=D_{\rm search}^{-1/2}$ gives success
$\sin^2((2g+1)\alpha)$. Its uniform average over $g$
is at least $1/2-1/(2L|\sin(2\alpha)|)\ge1/4$ by a
geometric sum. The new trial's offset and random
Grover schedule are independent of all earlier
decisions, including earlier stage centers. On a
correct preceding center, each odd comparison trial
finds a near mark with probability at least $2^{-14}$.
In the comparison the trial outcomes do not affect
the schedules or witnesses of other trials. With
$R=2^{18}$ trials the probability of no success is
less than $e^{-16}$, also valid for direct stages.
For this last bound sum over stages conditional on
their correct prior outputs, rather than unioning
over their possible values. Except for the charged
errors, a near or true mark when found validates,
and a far or wrong answer never validates. Thus
the first validating value keeps the needed invariant
even if other searches used arbitrary ambiguous grids.
Total failure is below
$2^{-39}+2^{-80}+2^{-20}+2^{-79}+16e^{-16}<1/8$.

## 8. Resource ledger and source credit

Each packet acquires $K2^{B_*}$ raw copies, costing
at most $O(n(\log(n+2))^2)$ work per position including source,
probes, assigned offsets, cell checks, label arithmetic and fees.
Even on skipped positions all acquisitions and
release costs count. Preparing the finite program
bank costs polynomial work per packet. The total
number of packets is an absolute constant. Each
search uses $O(2^{h/2})$ steps of
$O(n^2\log(n+2))$ charged work by Section 5, also
covering exact diffusion and candidate maps. Guard
checks, validation, every failed attempt and cleanup
have the same bounded schedule. As $h=n-\lfloor
n/3\rfloor$ and $B_*=\lfloor n/3\rfloor$ on the
main branch, the total work is
$O(2^{n/3}n^2(\log_2n)^2)$ and samples $O(2^{n/3}n)$.
Each finite-case cost is bounded separately by the
literal finite schedule, which changes only the
absolute outside constants.

The controller keeps the modulus, stage counters,
the current selected-cell labels, one program's
preparation staging, and a fixed number of candidate
words in $O(n)$ ordinary bits. Phase programs,
row qubits and inert flags for all $P$ live packets
occupy $O(n^2)$ allocated qubits because $P$ is an absolute constant. The measured
basis probe counters, current raw position, addresses,
modular arithmetic and synthesis temporaries are
included. The time and sample envelopes have double
logarithm $\log_2n+O(1)$ eventually and index one.
Both polynomial space representatives have index zero.
The fraction $2^{-20}$ applies jointly to the same
program and exact deterministic count $Q$.

Subsampled pair buckets, cb387962-e1b9-4d23-8400-e54e615d4a24,
supplies the valid-padding native Fourier instrument,
fast charged arithmetic, fixed-position geometry
coupling pattern and unit-transform decomposition.
Its complete used arithmetic helpers are reproduced
in the archive. The new method distributes raw slots in private cyclic shifts,
chooses one round-cell per equally large source group, retains its row with
a counted comparison eigenstate, and controls
coherent reuse by a query hybrid and independent
validator packets. The one-copy reflection mechanism
uses the earlier retained-source working proof's
ideal-prefix argument. The proof above establishes
all guarantees directly.
