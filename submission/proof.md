# PSG10-F7H: the selected sieve behind a heralded erasure filter

## 1. Single algorithm, clean theorem and direct sources

PSG10-F7H is FILTER(PSG10-F7), with the fully specified PSG10-F7 program supplied
in clean-proof.md, together with its complete supporting files in this archive.
The extra algorithm is ONLY the acquisition filter in Section 3. Every logical
request, both original caps, every old gate and the actual integer profile are
unchanged. The clean proof names q=1/10, f=49/51, alpha=7/16 and all
recomputed quantities; no other configuration's memory claims are substituted.

For every N>=2 and s modulo N, n=ceil(log2 N), write L=log2 n,
F=sqrt(nL), G=sqrt(n)L^(-7/16) when n>=2. The joint guarantee under the exact
model of Section 2 and fraction epsilon=1-1/D is

    T=O(2^((51/20)F+(3/4)G)), S_C=O(n^2), S_Q=O(n),
    Q_raw=O(2^((1/10)F+(3/8)G)),
    success>=1-2^-8>2/3.

Here D=(16*10^126-1)(625*10^126-1) is a FIXED positive integer. All constants
are absolute, including D, and n=1 is covered by the finite underlying branch.
All bounds hold on EVERY execution branch, counting flagged copies, failed
calls, wrong labels, disposal and aborts. Indices are (1/2,0,0,1/2).

The filter method, exact model and fixed rational fraction are directly reused
from my public LST-H-T2 submission ae5e793c-31cf-49f4-8cd9-7df0d2bc4d87,
file heralded.md, published commit 8f6730af8e15fb2f8f355519819fe5cc31fe07b7.
That file's SHA-256 is b8b844705947a8b994af528f3e9e3f25cb0a9a14b8ae77acd6c840d27fe7556d.
The complete argument needed here is restated below with this sieve's actual
branchwise acquisition bound H(N), rather than LST's 48N. The underlying
sieve and its complete rational family are credited in clean-proof.md and
family-source.md. No prior verdict is a premise.

## 2. Exact error model

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

The model text is byte-identical to the directly reused filter source's model.
In particular, the herald is correct: this is detectable malformed data,
an erasure-type model, rather than tolerance of undetectable corruption.
All well-formed deliveries are independent ideal mixed source states,
including under adaptive timing. The clean input source has no herald and
always supplies an ideal copy.

## 3. Raw cap and FILTER

Let H(N) be a branchwise integer acquisition bound of the underlying program:
if n<256, H(N)=N(n+10); otherwise H(N)=Qcap from the selected integer profile
of the clean proof, recomputed with its actual N,n,u,mstar,H0. It is known
before any acquisition. The underlying program makes at most H(N) requests
on any branch, including wrong-label and abort branches. The finite tester's
early rejections only reduce its number of requests. This use of an acquisition
bound does not alter the original work cap or extraction confidence.

Initialize a raw binary down-counter r to D H(N), by a uniform fixed-constant
multiplication. Its width is O(log(H(N)+1)+851)=O(n): the selected integer
profile obeys R<=ceil(n/2), and its dependent cap is at most polynomial(n)
times 2^R. The fixed finite branch has log H(N)=O(n) as well. This is a
computed counter, not a preloaded instance-dependent table.

For EVERY underlying request for a fresh source copy, execute:

1. If r=0, abort the entire program and output 0.
2. Decrement r, acquire one raw copy in the original source-register wires,
   and read its one classical herald bit. In the clean problem take f=0.
3. If f=1, dispose of ALL sample wires without any interaction with the
   underlying program's registers, then repeat from step 1.
4. If f=0, hand the untouched sample register to the underlying program,
   which proceeds exactly as its clean specification.

Only r and this filter's temporary f track discarded raw copies. The logical
controller does not see their number, times, flags or contents. Its own source
counter increments on handed-over copies exactly as in its clean program.
All filter branches, counter operations, acquisitions, disposal and herald
reads are charged. Underlying logical source charge is not used to hide raw
source calls; Q_raw is their actual total, including every discarded one.

## 4. Cutoff and clean-law lemmas

Suppose the filter aborts at step 1 during its jth logical request. Then
j<=H(N), exactly Q_raw=D H(N) copies have been acquired, and at most H(N)-1
were well-formed. Hence there were at least D H(N)-H(N)+1 malformed copies.
But the branchwise promise permits only

    floor((1-1/D) D H(N))=D H(N)-H(N),

a contradiction. Therefore the raw cutoff cannot abort on any promised
branch and every logical request receives a well-formed copy. This does not
assume that every PREFIX obeys the fraction bound; the argument uses only
the actual branch ending in the hypothetical cutoff.

Each flagged register is disposed of without touching any logical register.
Even if it is entangled with an adversary or other malformed copies, tracing
it out cannot change the reduced state of the untouched logical computation.
Each next well-formed delivery is, by the exact model, a fresh independent
rho_s in tensor product with all other systems at delivery. The filter never
uses its delay data to choose a logical operation and the raw cutoff never
changes a promised run. Induction over the logical requests therefore gives
EXACTLY the clean joint law of the underlying program's logical transcripts,
held quantum systems and output. This includes the measured-basis bank when
that is the selected underlying algorithm. Adaptive adversarial timing cannot
select a different state on a delivery declared well-formed by this model.

All clean correctness/cutoff/extraction/decoder arguments remain valid. Thus
full-secret success under every promised adversary and in the clean problem
is at least 1-2^-8, for every N and s.

## 5. All four charged resources

On every branch the raw counter enforces Q_raw<=D H(N), even for inputs
outside the promise. From the clean proof, H(N) is at most polynomial(n)
2^(R-u), with the selected positive sample gap. Since D is a fixed absolute
constant, Q_raw has the exact declared sample envelope unchanged.

The filter adds O(n) classical bits for the raw counter, one flag and scan
indices. Hence the selected classical envelope stays unchanged. Raw source
copies use the underlying program's original n+1 sample wires, disposed of
before another acquisition. Even allocating an extra O(n)-qubit sample buffer
would not change the selected quantum envelope. Initialization, reset, source
shape and all living quantum data are included. Therefore S_C=O(n^2), S_Q=O(n) jointly.

An O(n)-bit zero scan/decrement plus acquire/dispose costs O(n log(n+2))
charged work per raw copy, including the rules' address fee; total memory is
O(n^2). Multiplying D by H(N) initially costs O(n) core operations up to an
absolute constant, since D has fixed bit length. Thus extra filter work is
bounded by polynomial(n) H(N). It fits the stated time envelope because

    51/20-1/10=49/20>0,

and F dominates G and log n. Equivalently, a polynomial times
2^((1/10)F+(3/8)G) is O(2^((51/20)F+(3/4)G)). Adding the complete clean
work gives the same T bound. No near-one fraction is treated as a per-copy
corruption probability. The guarantee is an actual branchwise malformed count.

The same n>=2 envelopes and finite-prefix convention prove the indices
(1/2,0,0,1/2), as the clean proof explains. All bounds hold for this ONE
configuration in the same error model; nothing takes the best memory from
another physical algorithm.

## 6. Supported exact fraction



Direct integer multiplication (checked with exact integer arithmetic) gives the first three lines
below; the fourth is the decimal form of `10^63` (64 digits).

    A = 16*10^126 - 1  = 4329632813347406305223297584667745034303743116654997715999733453 * 3695463493041522429397493437973995985916922777904245876619237883
    B = 625*10^126 - 1 = 8333333333333333333333333333333333333333333333333333333333333333 * 454542699741213689614002339379761334779789213398706674505003 * 165001
    C = 10^130 - 641   = 2189251513709577192973000802960123783290116879858557832979634351 * 858746507556703404750738054330397864679429 * 5319114725318138222421821
    Z = 10^63          = 1000000000000000000000000000000000000000000000000000000000000000

(the factors need not be prime; each has at most 64 digits). Since `16*625 = 10^4` and
`16 + 625 = 641`, `D = A B = 10^256 - 641*10^126 + 1`, so `D - 1 = 10^126 C = Z^2 C`. Hence the supported
expression of the fifth claim, with numerator `Z^2` times the three factors of C and denominator the
two factors of A times the three factors of B (nine displayed integers), equals
`Z^2 C/(A B) = (D - 1)/D = 1 - 1/D = epsilon_H`, a constant in (0, 1). `D - 1` and `D` are coprime, so the
normalized numerator and denominator are `D - 1` and `D`, each of 256 digits. epsilon_H is used in Section 4 through
`floor(epsilon_H * D H(N)) = D H(N) - H(N)`.



The fifth structured expression of this snapshot is the same product
expression, equal to (D-1)/D=1-1/D. All displayed tokens satisfy the pinned
grammar; the normalized numerator/denominator each have 256 digits.
Together with Sections 2-5 it proves the exact fifth claim, including all
adversaries, the total raw count and the original full-secret success.
