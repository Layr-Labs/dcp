# Coherent terminal-block search with exact score arithmetic

In the terminal-block construction increase h from R to 2R and
choose first feasible R with 2 sum_i v_i + 2R >= n. Its asymptotic
leading coefficient becomes n/10 at fixed depth four, provided the
terminal scores can be searched in square-root work. The score data
are already classical and measured before the search. This removes
any need to reflect about unknown source samples during the search.

For the odd stage, the BASE13 bounds in Section 6 give a true-near
grid witness with score at least K times
(1/2)cos(pi/128) - 1/64 - 1/625, and every far candidate has score
at most K times (1/2)cos(pi/8)+1/64+1/625. Choose any verified fixed
rational strictly between these two constants and mark every valid
grid candidate whose actual rational score exceeds the threshold.
There is at least one mark and all marks lie in the radius certified
for the next stage; finding the maximizer is unnecessary. For a
direct terminal score use its existing 7/16 threshold. On its
concentration event it marks exactly the correct residue.

Implement the marking predicate reversibly. The candidate register
holds a padded grid index, which can be mapped into its one or two
classically fixed intervals using exact comparisons and addition.
The loop over K records is classical. For one record, compute the
known-multiplier modular product into one O(n)-bit accumulator by
repeated controlled modular adds. All arithmetic registers keep
O(n) qubits, including temporary carry, comparison and uncomputation
scratch. Apply the fixed table by comparing the argument to its
fixed-rational interval endpoints. Add the signed rational value
to the score counter with common fixed denominator and uncompute
the per-record arithmetic. Then perform the phase mark and undo
the computed sum. No data is quantum indexed through a bank:
each record address is a classical emitter choice. The addition
and carry subroutines must be explicitly charged for invalid
candidate padding as well, with invalid indices never marked.

Pad candidate count to its least larger power of two and prepare
the uniform state with Hadamards. Take a fixed sequence of doubling
trial cutoffs through O(sqrt(candidate count)), testing uniform
random numbers of Grover iterations at successive cutoffs, with
fresh restart and exact postmeasurement mark checks. Standard
two-dimensional averaging gives constant success at a valid scale;
an explicit iteration cap and repetition enough to union over all
terminal stages is required. Cases with many marked positions are
covered via testing a direct uniform candidate before trials. The
size of the odd grid is O(q0 2^(2R)), hence search costs
poly(n) 2^R work once the marking circuit and caps are fully proved.
This preserves the O(n) qubit bound per clean solver.

## Rational threshold and bounded Grover trials

Use 12/25 as the normalized odd-score threshold. The elementary
bounds cos(pi/128)>999/1000 and cos(pi/8)<37/40 suffice:
the first follows from cos x>=1-x^2/2 and pi<4, the second
from cos^2(pi/8)=(2+sqrt(2))/4 and sqrt(2)<99/70.
The near lower bound is >999/2000-1/64-1/625>12/25,
and far upper bound <37/80+1/64+1/625<12/25.
These comparisons are between exact rationals at runtime.

Let A be the padded search count, a power of two. For each
scale M=1,2,4,... through the first power of two with M^2>=16A,
perform S=128 ceil(log2(n+2)) fresh trials. Each trial starts
in the exact padded uniform state and uses a uniform number
j in [0,M) of Grover iterations (exact fair bits). Measure
and check the classical predicate, stopping on the first
valid mark. If no trial succeeds, output the fixed default.
The work sum over the scale cutoffs is O(S sqrt A).
All budgets are computed by integer bit lengths.

If p is the marked fraction, p>=1/2 gives success >=1/2 per
scale-1 trial. If 0<p<1/2, write sin^2(theta)=p. Averaging
sin^2((2j+1)theta) over j gives
1/2 - sin(4M theta)/(4M sin(2theta)). Thus the first
M>=2/sin(2theta) gives success >=3/8, and such a scale
is included because p>=1/A and sin(2theta)>=sqrt(2/A).
The failure at that scale is at most (5/8)^S < (n+2)^-32.
Conditioning on earlier failed attempts does not change
fresh uniform trials on unchanged classical records.
This proof is valid for every conditioned record set
containing a mark. It does not charge a successful sample
as necessary to continue the finite work loop. A union
bound over at most n stages gives probability below 2^-24
for n>=1024. For p=0 the same deterministic work cap applies.

The exact sign oracle, checked postmeasurement mark, and
diffusion require only reversible fixed-point integer
logic and Clifford+T. The address length O(log n) is
already charged to every classical and gate index. With K=O(n),
a schoolbook reversible predicate costs O(n^3 L), including
the inverse and recurrence over records. The trial count
adds O(L), and sqrt(A)=O(sqrt(q0) 2^R) in the odd stage.

## Numerical profile and joint envelope

For n>=1024 set D0=ceil(log2 n)+3. Test
R'=ceil((n+12D0)/10), which is <=n and has four positive
backward values. Its capacity plus 2R' is at least
10R'-12D0>=n. The least feasible R has n/10<=R<=R';
all four values are positive and at least R/4 since
3D0<=3n/40<=3R/4. Also 2R+1<=n and 2R<floor(log2 N).
This gives 2^R=O(n^(6/5)2^(n/10)). Use h=2R everywhere
the classical terminal variant uses h=R. The exact same
two-branch modulus proof applies: cancellation B=d0-h
is at most the current capacity and any direct residual
stage cancels at most B. Its concentration run uses
Kdir=8192(h+ceil(log2 n)+32), with candidate range
<=2^(h+1), while the odd decoder continues its original K
with nq=2^(h-1)q0. With stride=h-4>=h/2 the stage count
is at most 11 odd and 5 subsequent direct stages, or up
to six direct stages when starting from high valuation.
Both K bounds are still <=2^15 n, so H0=2^20 n and the
same caps and padding remain valid. Add search failure
to the existing coupled analysis well within 1/8 total
error (in fact within the original clean per-bank 1/3).

The full decoder work is O(n^5 L^2 2^R): use the O(n^3 L)
predicate, O(L) repetitions and sqrt(q0)<=n^2. The number
of stages is bounded by an absolute constant. The
current combiner, extraction and preprocessing terms
fit that allowance. Multiplying by the tenth-root bank
count yields the single envelope 2^(n/10) n^(63/10) L^2.
The extra coherent score and search registers are O(n)
qubits and all classical record storage remains O(n^2)
per bank. No changes are required in the wrapper's
sample fraction, total acquisition or memory claims.

## Exact implementation details for the coherent predicate

At each stage allocate a candidate index i and an O(n)-bit candidate
value c, initialized to zero. Compute c by converting a valid index
to the corresponding interval offset, using comparisons with the
two fixed lengths and additions with their lower endpoints. On
padding set c=0 and carry an explicit validity bit. Both registers
are retained until the full predicate is uncomputed. This is a
reversible evaluation of a function into a fresh register, so
padding values need not have a distinct c value.

For one stored signed coefficient f and modulus D, precompute the
successive constants (2^b f) mod D by modular doubling. An O(n)
current constant and an O(n)-entry list give O(n^2) classical
space. Alternatively the controlled additions can be emitted in
reverse from a retained list when uncomputing. The coherent
accumulator starts at zero. For each bit of c add the constant
modulo D controlled by that bit. The adder is the bijection
x->x+a mod D on 0<=x<D and identity outside, with an extra
identity branch when the control is clear. Evaluate the O(n)-gate
ripple-carry Boolean function into a fresh word using retained
scratch, clear scratch, exchange words, and clear the old input
by evaluating the inverse x->x-a mod D into it. This gives O(n)
gates and O(n) simultaneous scratch per addition. At D=2^P use
ordinary fixed-width wraparound. All controls and inverse loops
remain exact on the padded candidate branch.

Compute the finite score table integer from the residue using
a fixed number of exact threshold comparisons to O(n)-bit constants.
For a rational endpoint e, r/D<=e is an integer comparison to
floor(D e), and strict comparisons use ceil(D e)-1. Record
the X/Y choice selects the proper constant threshold list,
and the measured sign controls the sign of the resulting integer.
Accumulate the signed table integer by a reversible addition
into a sufficiently wide score register (O(log(n+2)) bits),
then reverse the per-record table arithmetic and modular product.
All signed sums are bounded by K times the fixed table scale.
Compare the finished sum to the specified exact rational multiple
of K, flip sign on a passing valid index, then reverse the entire
score calculation and clear c and the validity flag. There are
O(n^2) gates per record, O(n^3) per predicate before addresses,
and only O(n) simultaneous qubits because the loop reuses scratch.
A classical checked mark uses the very same integer comparisons.
