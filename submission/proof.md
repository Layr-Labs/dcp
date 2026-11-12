# CYCLIC-FIXED128: larger fixed fourth-root boost and counted high-part storage

## 1. Complete algorithm and joint claims

This construction doubles the actual boost of this session's complete
fixed64 configuration. Its material public source IDs and immutable file
identities are supplied in the dependency declaration and public note.
The full cyclic_base.md is copied byte for byte; it originates in
cyclic source e9fc2eca-9d1c-469b-a629-a43e0f7ce928, commit
45d9985c85813b2f3d30c62c717faba3621eb57a, via the complete fixed32
source d4e19ee1-d817-4281-ac3a-13d5aa2965d3. The fixed128 configuration
below replaces every older fixed16/32/64 schedule and resource conclusion.
All source identities, circuits, collective extraction, collision and
freshness proof, top-bit law, all-modulus backward decoder, literal parity
caps and finite n<64 branch are retained in full. No validity verdict is
a mathematical premise.

For each collimation width B compute exactly, before source acquisition,

    mu=ceil(sqrt(2B))+1, kappa=2,
    x=s=min(mu-1,128 floor(sqrt(mu))), q=x+3,
    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+2,
    m=min{z>=s+1:C(z)>=B}.

The integer roots use counted integer arithmetic. Retain the generic
boosted vector lengths, residue capacities, root-first greedy allocation,
leaf tables, cyclic-window instrument and failed-input disposal of the
source at these actual x,s. Recompute every actual decoder and collective
extractor size, mode, precision and confidence parameter. Compute literally

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), this ONE configuration
recovers the entire s with unconditional probability at least 1-2^-8 from
independent ideal copies. On every execution branch jointly,

    T=O(n^3 2^(a sqrt n)),
    S_C=O(2^(a sqrt n-152 n^(1/4))), S_Q=O(n),
    Q=O(2^(a sqrt n-152 n^(1/4))).

The exact rational a=u_333/v_333, and its proof a>sqrt2, are supplied in
cyclic_base.md Section 0. All constants are absolute, independent of N,s
and outcomes. The representative envelopes are positive for every n>=1;
all success and resource guarantees cover every N. Their exact growth
indices are 1/2,1/2,0,1/2. Fractional malformed-copy tolerance is zero,
under independent ideal copies; no maximum possible tolerance is asserted.
All failed, rejected, discarded and cutoff-abandoned acquisitions count.

## 2. Uniform capacity, retries and unconditional full recovery

Always 2<=x=s<=mu-1. Capacity holds at z=mu since x=s and
x mu-x^2/2>=0. Thus m exists, s+1<=m<=mu. Explicitly use
lambda_i=3+x+min(i,m-s) below the root and lambda_m=1;
bmax_i=x+i on growing levels, x+m-s+1 on capped levels, and
2+2x+2(m-s)+1 at the root. Summing gives C(m), while every merge
satisfies bmax_i+lambda_(i+1)-2lambda_i=-2. All selected windows
remain below the retained top bit. Injective cyclic rank maps and the
source's low-prefix conditioning preserve independent untouched high
source bits. The supplied collision argument gives fresh non-root failure
<2^-q under whole-child averaging; root failure is <=1/4. This is not
a bound for every fixed full non-root high-label table.

We have m2^-q<=1/2. If mu<16 use m<=15,q>=5. If mu>=16 and
x=mu-1, then q=mu+2>=log2(mu)+1. Otherwise x=128 floor(sqrt(mu));
floor(sqrt(mu))>=sqrt(mu)/2, so q>=64sqrt(mu)+3>=log2(mu)+1,
using log2(mu)<=sqrt(mu). Since -ln(1-p)<=2p for p<=1/32,
the retry product is <=(4/3)e<4. Fresh-whole-attempt reach-probability
accounting gives expected tree acquisitions <=8 A_star; no independence
of attempt cost and success is required.

The actual logarithmic root size is O(sqrt n), so the source-aligned
backward decoder retains its O(n) expected-root budget. Its actual size
controls every grid, mode and precision choice. Q_star is an uncapped
ideal expectation bound, and Markov adds <=2^-10 cutoff error. The
unchanged collective-label coupling, seed/backward/parity error ledger,
literal parity caps and finite exhaustive branch keep total failure below
2^-8. These are unconditional first-error and cutoff comparisons.
Incorrect extracted labels or previous decoding mistakes still obey every
fixed width and literal resource cap. Neither the resource guarantees
nor recovery probability condition on perfect extraction or avoiding cutoff.

## 3. Fixed128 depth bounds and maxima over actual widths

For analysis put R=sqrt(2B), Y_B=sqrt R. We have R+1<=mu<=R+2.
For R>=65536 the min with mu-1 is inactive: 128sqrt(mu)<=mu-1
for mu>=65536. Thus

    128Y_B-128 < x <=128Y_B+128, q<=256Y_B.       (1)

The upper bound on x holds below this threshold too. Completion of the
square bounds m by the maximum of s+1 and
ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2), dropping a negative constant.
With s=x, concavity bounds the square-root candidate plus x by

    R+x^2/R+x/(2R)+1/(8R)+1.

For R>=65536, x<=128sqrt(R+2), so the excess is less than16400:
x^2/R<=16384+32768/R<=16384.5, x/(2R)<1, and1/(8R)+1<2.
The lower constraint plus x is bounded by
2x+1<=256sqrt(R+2)+1<=R+4. At65536 its excess is below3;
thereafter its derivative minus1 is128/sqrt(R+2)-1<0.
Thus m+x<=R+16400 there. For R<65536 use
m+x<=2mu-1<131075 and m<=mu<65538. The common explicit
C0=1048576 yields, uniformly for every B>=1,

    m+x<=R+C0,
    m<=R-128sqrt R+C0+128.                         (2)

For the second inequality below the threshold,
R-128sqrt R=(sqrt R-64)^2-4096>=-4096 and m<65538;
above it use (1) and the first bound. The finite prefix is explicit.

Let R*=sqrt(2n), Y=sqrt R*. The function f(R)=R-128sqrt R
increases on R>=4096 and is bounded on the finite smaller interval.
Combining the uniform bounds with the EXACT maximum over all B<=n,
absorbing finite smaller widths into one absolute constant, gives

    A_star=O(Y 2^(R*-128Y)),
    Qcap=O(n^(5/4)2^(R*-128Y)).                    (3)

No monotonicity of a rounded integer schedule is assumed. The exact
maximum and fixed-width cap are computed with counted polynomial setup.

## 4. Deterministic every-branch charge

Each acquisition pays at most one merge per level because failed inputs
are discarded. The deterministic source charge is
O(n(m+1)2^kappa 2^x/q), including aborted partial trees. The function
2^v/(v+3) increases for v>=2. Using the uniform upper bound
x<=128Y+128 and m=O(sqrt n), all widths have common per-copy charge

    O(n^(5/4)2^(128Y)).

Multiply by the ACTUAL cutoff (3) for the SAME fixed128 configuration:
tree core work is O(n^(5/2)2^R*). Source transforms and collective
extraction cost O(n^2) per copy, hence O(n^(13/4)2^(R*-128Y)),
which is smaller. Seed scoring O(n^2 A_star), feedback and polynomial
setup are also smaller. All source cost, initialization, circuit
generation, explicit lookups, measurements, resets/disposal, failed
attempts, wrong-label work and cutoff-abandoned work are counted.
Address length is O(sqrt n), so charged sequential work is

    O(n^3 2^R*)=O(n^3 2^(a sqrt n)).                 (4)

The physical quantum stack and active scratch use O(n) qubits because
m and all index lengths are O(sqrt n), as in the full source.

## 5. Classical high-part storage, including all plateau levels

A level-i label has fixed stored high-part width
w_i=B+1+i+ceil(log2 q)-p_i, where p_i is the sum of previously used
windows. Greedy allocation only reduces remaining windows. Each
remaining bmax is O(sqrt n), while m and log q are O(sqrt n).
Consequently w_i=O(sqrt n(m-i+1)). This also covers the row-index,
rank, ordering, residue and lookup scratch fields when allocated;
small fixed widths are harmless. There are only constantly many
resident tables and merge scratch blocks per level in a depth-first
execution, including failed attempts.

On the last s levels, lambda_i=lambda_max=3+m because x=s.
Their total high-part storage is
O(sqrt n s^2 2^lambda_max). On growing levels, put d=m-s-i>=1;
the row count is 2^(lambda_max-d) and remaining-height factor is
O(s+d+1). Summing the geometric tail gives
O(sqrt n(s+1)2^lambda_max), which is smaller since s>=2.
Common residues, extractor records, seed scores, feedback and rational
setup use polynomial scratch, separately included. Since
s<=128sqrt(R*+2)=O(n^(1/4)), (2) proves

    S_C=O(n 2^(R*-128Y))+poly(n).                     (5)

The positive exponential absorbs polynomial scratch. Field widths and
allocations are fixed even on wrong-label branches, and allocation,
reset and release were counted in (4). No table or advice is preloaded.

## 6. Exact coefficient conversion and improvement

The exact integer inequality 128^4*2>152^4 proves
128*2^(1/4)>152. Put gamma=128*2^(1/4)-152>0. Equations(3)--(5)
first give Q=O(n^(5/4)2^(sqrt(2n)-128(2n)^(1/4))) and
S_C=O(n2^(sqrt(2n)-128(2n)^(1/4))). Divide these by
2^(a sqrt n-152n^(1/4)), with the SAME exact Pell rational a.
Their ratios are at most n^p2^(-gamma n^(1/4)), p=5/4 or1.
This tends to zero without using any positive Pell slack.

For an explicit finite bound, let u=n^(1/4). Since ln u<=sqrt u
for u>=1 (its maximum ratio is2/e<1) and ln2>2/3,
4p log2u<=6p sqrt u. For u>=(12p/gamma)^2 this is at most
gamma u/2, so the ratio is <=2^(-gamma u/2)<=1. If a rational
threshold is desired, use the POSITIVE lower bound
 g=(2*128^4-152^4)/(32*128^3)=3076096/(32*128^3)<gamma,
from difference of fourth powers and both bases less than256.
Then n>=(12p/g)^8 suffices; the remaining finite prefix contributes
an absolute constant. Polynomial auxiliary memory is absorbed as well
by the positive leading exponential. No finite-size advantage is asserted.

Therefore the exact joint structured envelopes are
 T=O(n^3 2^(a sqrt n)), S_C=O(2^(a sqrt n-152n^(1/4))),
 S_Q=O(n), Q=O(2^(a sqrt n-152n^(1/4))).
The three exponential logarithms are a sqrt n+o(sqrt n), so their
exact indices are1/2; the linear quantum index is0. T is first proved
with sqrt(2n), including ALL work; only sqrt2<=a converts its coefficient.

Compared with the complete fixed64 configuration, the actual boost and
plateau multiplier doubles64 to128. Time and linear quantum space remain
the same, while the negative classical/sample coefficient increases76
to152 and both displayed polynomial prefactors are removed by the
explicit fourth-root margin above. This is a stronger proved guarantee,
not tight complexity, practical speed, smaller time index or global
frontier leadership. The clean independent-copy model is unchanged.

## 7. Material provenance

This uses the complete fixed64 configuration developed immediately before
it, including its deterministic charge, maxima, cutoff and high-part
plateau/geometric storage proof. That construction builds on the complete
fixed32 source d4e19ee1-d817-4281-ac3a-13d5aa2965d3. The unchanged
cyclic base and its direct background credits remain supplied. Fixed32's
high-part framework credits CYCLIC-LOG1f1debc0-0a4b-409c-bcc4-1eb8c5c9d470;
its graph links to that source and the cyclic base are pending proposals,
not certified ancestry. Current dependencies and public notes identify
all actual material submissions and publication statuses. New quantitative
constants, doubled ACTUAL boost and prefactor absorption are proved here.
Prior verdicts and finite diagnostics are not theorem premises.
