# Bounded private enumeration of a measured chunk

This changes metadata generation only. Coherent rank and inverse-rank erasure
on the source phase index remain the supplied approximately clean circuits.
All search below acts on NEW known private registers, not a source copy.

## Exact reference output and interval endpoints

After high rank bits c have been measured and the partial-chunk test passed,
the retained ranks are cK,...,cK+K-1, where K=L for a regular node and K=2
at the root. Compute a=g(cK), b=g(cK+K-1) on two private known ranks.
The counter/g hybrid already covers these calls. For the exact reference
the accepted low-key/hash predicate together with a<=z<=b has EXACTLY K
solutions. We must reproduce their increasing numerical order, since that
is the order of the retained quantum rank index. Merely finding any K masks
and leaving them unsorted would not implement the claimed phase vector.

Keep a classical list of masks already found, initially empty. At row i
the remaining count k=K-i is known. Mark z iff it satisfies the original
low-key/hash predicate, lies in[a,b], and differs from every found mask.
Literal scans of at most L t-bit masks implement the exclusion test. Compute
each equality into one flag, conditionally increment a (R+2)-bit match
counter, erase that equality flag, and finally test matchcount zero.
Reverse all scratch after the marking phase. No array of L coherent flags
or quantum-addressed lookup is allocated. The original predicate, interval
comparison, exclusion scan, phase Z and inverse fit2^202 n^12 L core steps
per Grover iteration, including bit-serial gate/address generation.
Everything receives the additional main-proof clock/access charge.

## Explicit randomized search and bounded failures

Set U=2^t, S=ceil(sqrt(U/k)) by rational integer-square comparison and
J=the least power of two at least8S. These are counted classical integer
algorithms on O(n)-bit buffers. J<16S<=32sqrt(U/k). Choose a uniform
classical j in[0,J) by its exact number of private random bits. Prepare
H^t|0>, perform j Grover iterations, measure z, and verify the entire
predicate exactly by classical bit operations. A failed verification resets
only private registers and retries. Cap attempts per row at A=1024n;
exhausting them aborts globally with output zero. All attempts are charged.

The private diffusion is2|unif><unif|-I, implemented as the literal
-H^t Z0_neg H^t circuit from the count helper. Marking is compute-predicate,
Z, uncompute. This uses only Hadamard, Clifford and Toffoli networks; no
angle, arbitrary rotation, real oracle, source purification or source inverse.
Its t-bit index and O(n)-bit arithmetic scratch use O(n) qubits.

For completeness the two-dimensional span of the uniform marked and
unmarked states gives, by direct multiplication of the marking/reflection
matrices, marked probability sin^2((2j+1)theta), where
sin^2(theta)=k/U. This theta is ANALYSIS only. Here k<=K<=L and t>=512R,
so k/U<1/2 and sin(2theta)>=sqrt(k/U). Summing the finite geometric series
of cos((4j+2)theta) yields exactly
 (1/J)sum_(j=0)^(J-1) sin^2((2j+1)theta)
 =1/2-sin(4Jtheta)/(4J sin(2theta))
 >=1/2-1/32>1/4.
Thus each fresh trial succeeds with probability>1/4 uniformly in all
previous found masks, without any source phase assumption. The probability
any row exhausts its cap is at most
 K*(3/4)^(1024n)<=2^n*2^(-256n)<delta=2^(-100n),
because (4/3)^4>2 and K<=L<=2^n. Rejection or false classically verified
solutions have no hidden success promise: every encoded predicate is a total
Boolean function, and all loops are bounded even after erroneous endpoints.

The randomized Grover technique is standard; see Boyer, Brassard, Hoyer
and Tapp, [Tight bounds on quantum searching, v1 Section4](https://arxiv.org/html/quant-ph/9605034v1).
The matrix/geometric-series proof and explicit bounds needed here are given
above, rather than using a unit-cost search oracle or its complexity theorem.

## Reproduce the exact metadata and charge every output

After collecting K distinct valid masks, sort the classical list by increasing
numeric index, with counted bit-serial compare/swaps. Read the child rows and
compute the normal raw/phase/common-weight records in this order. This gives
EXACTLY the same table as individually evaluating g on each retained rank.
The source phase register is untouched by private search, sorting or record
generation. Only low-key/hash/interval/mask information selects masks; full
phase labels are read for the same final metadata computation as before.
Thus the unused-top-bit law and aggregate invariants are preserved.

The found masks use O(Lt)<=O(Ln) classical bits, reusable as output-table
scratch. This fits the SAME full classical envelope. Even a quadratic sort
takes at most polynomial(n)*L^2 core work and O(Ln) bits. Its quantum
workspace is only the private search/arithmetic registers; it does not retain
search-attempt histories. All clearing/resetting and endpoint reversal count.

On every branch, including failed trials,
 sum_(k=1)^K J_k <=32sqrt(U)sum_(k=1)^K k^(-1/2)<=64sqrt(UK).
With A=1024n the total iterations are at most2^16 n sqrt(UL). Expanded
queries cost at most2^218 n^13 2^(ceil((t+3R)/2)).
Classical roots/J generation, all A*K resets/verifications, sorting, row
arithmetic and their generated indices have conservative total core cost
at most2^900 n^25 2^(ceil((t+3R)/2)): their explicit schoolbook loops are
polynomial of degree at most25 times L^2, and t>=R gives
L^2<=2^(ceil((t+3R)/2)). No emitted gate list is stored.
Consequently reserve the WHOLE metadata block
 gmeta=2^1000 n^25 2^(ceil((t+3R)/2))
BEFORE private enumeration begins, pad completed blocks to this cost, and
abort if that reservation fails. Endpoints use their separately reserved
count blocks. No guard interrupts a promised metadata instrument.

At most64t count blocks now cover a node's rank, inverse, private factors,
total count, and two endpoint searches; there is no additional L factor
in this number. Adding gmeta, the fixed-node and expected-leaf core work
to these blocks fits ACTUAL G=2^10000 n^26 2^(ceil((t+3R)/2)).
Every actual recurrence, guard and padded runtime uses this smaller G.

## Unconditional replacement and totality

In the ideal-count reference, every successful complete list yields the
same sorted deterministic table; the only possible error is the bounded
metadata abort. Conditionally on every classical input, its channel is
within delta in trace distance of the exact metadata instrument with the
same paid block cost. The bound also holds with outside entanglement:
private search never controls or changes the retained source index.
Discard/reset private random registers before continuing.

For the full capped computation use ideal prefixes, actual suffixes and
channel contraction, including metadata aborts and guards. Existing count
and factor replacements handle erroneous endpoints; no correctness of an
actual noisy endpoint is assumed. With at most B metadata blocks, the whole
kernel bound is now B*(4delta+2sqrt(delta))<1/1024, since log2B<n/8.
This remains within the same single kernel allowance in the main proof.
The exact reference used for source/work Markov estimates pays the same
gmeta and replaces rare metadata aborts by the deterministic correct output.
No actual noise-independence, postselection on labels/caps, or new free
resource is introduced. Classical mask/quotient/field-range checks still
abort on failure, with their existing total fixed-width behavior.
