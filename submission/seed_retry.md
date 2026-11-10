# Global short-key preparation budget

This is the normative key-preparation control for perm_fw.md Section2.
It changes the fresh key width and actually retries collisions, with an
executed global cutoff. All accepted permutation states and subsequent
FW gates/channel are unchanged. Its error event is separate from the
conditional pool-yield argument; no proof conditions on future cutoff
survival. Put b_w=log2 w, Lg=ceil(log2 n) and

 b_K=2b_w+Lg+10,
 M_K=10r(ell+1)(C_0+1), F_K=10(ell+1)(C_0+1)=M_K/r.

Both counters below start at zero and are basis-state bank records.
Before a new FW seed request, increment its request counter and ABORT
if it exceeds M_K. To serve that request, prepare fresh keys, sort/clear
as in perm_fw.md and measure distinctness. On collision reset/release
ALL attempt ancillas, increment the global failed-key counter, and
ABORT if it exceeds F_K; otherwise try fresh keys again. On success
keep the pure uniform permutation and return it. Neither a collision
nor a retry touches the input pool qubits. A global ABORT resets/releases
every remaining register with the existing cleanup and outputs0.
The counters are global over all batches, levels and requests, not reset
at each FW or chunk. They acquire no source copies.

## Deterministic requests and every-branch work

Each completed FW cell reduces LIVE by rho>=2. A chunk with Cin inputs
therefore makes at most Cin/2 completed requests; an incomplete global
abort contributes at most one more request in the whole algorithm.
For a batch, sum_i Rc_i D_i<=ell C_0, and there are at most5r batches.
Thus fewer than(5r ell C_0)/2+1 requests occur on every capped branch,
including erroneous labels and wrong decoder prefixes. This is below
M_K. Hence the request guard is executed but cannot fire within the
other specified caps. The count uses only valid FW cell sizes, not a
yield probability or correctness of recorded phase labels.

At most F_K failed attempts are followed by another attempt; an aborting
failure may be the(F_K+1)-st. The total number of actual key attempts is
at most M_K+F_K+1<=2M_K+2. This deterministic bound applies even if all
rejections occur inside one FW call. No per-chunk bound on private retry
work is asserted. Failed attempt registers are released before fresh
allocation, so the peak gate/register capacities of a single attempt
are unchanged, with a smaller key width than the preceding construction.
The two counters and their thresholds occupy at most four extra fixed n-bit rows; they fit the existing bank
owner/row/scratch margins and do not enlarge its physical prefix.

## Exact accepted seed and global cutoff probability

One attempt's collision probability is at most

 p<=w(w-1)/2^(b_K+1)<=2^(-Lg-11)<=1/(2048n).

Its keys are fresh zeros in tensor product with everything else before
Hadamards. Thus this probability is independent of the data, labels,
previous quantum state, past failed keys and adaptive request schedule.
Each successful attempt has exactly the same positive uniform |S_w>
factorization proved in perm_fw.md. Conditional on any earlier failure
history, the returned seed is that same pure state. Repeated attempts
without a cutoff terminate almost surely, since p<1.

Expose an infinite independent stream of such collision indicators,
padding unused attempts. If the global failure cap fires within M_K
requests, the first M_K+F_K+1<=2M_K+2 indicators contain more than F_K
failures. Let X be their binomial sum. Its mean satisfies
mu<=(2M_K+2)/(2048n)<=M_K/(512n). Exponential Markov gives

 Pr[X>=F_K]<=(exp(1)mu/F_K)^F_K
             <=(exp(1)r/(512n))^F_K<2^(-F_K)<=2^-80.

Use exp(1)<11/4, r<=sqrt n+1, n>=2^40 for the strict half bound.
Also ell>=r/2 and C_0>=1 imply F_K>=80 directly. The proof permits
adaptive request counts because the padded indicators are fresh and
independent and the request bound is deterministic. It is not a product
of conditional per-FW nonabort probabilities.

The IDEAL OUTER run omits both key counters/guards and all private key
attempt states from its conditioning histories, and serves each request
with the exact uniform permutation. It also has the independently
specified ideal verified-extraction convention. The actual and ideal
outer laws couple until the global key cutoff or an already counted
error. Request overflow cannot occur by the deterministic count.
Consequently the new preparation cutoff contributes at most2^-80 to
the complete success union. The retained pool-stage yield probability
is applied to this ideal outer run, not conditioned on actual survival.
Near the cutoff an actual call need not have the former tiny per-call
abort probability; no such assertion is made or used.

## Global structural ledger

Now b_K=O(log n). One key attempt and the fixed post-preparation cell,
canonical-map and ticket networks each have O(w(log w)^3)=O(n(log n)^3)
elementary gates/actual scratch. The incremental generator of perm_fw.md
Section7 costs O(log n) aggregate per gate, giving O(n(log n)^4) per
attempt/body. The counters' full bit work and resets fit this allowance.
Since M_K=O(n C_0), all key attempts and FW Boolean bodies over the whole
algorithm cost O(n^2(log n)^4 C_0).

The current cursor-role stream generator of typed_dispatch.md gives
borrowed GROUP, FIFO/dictionary and consumed-label work O(n^(3/2)Cin)
per chunk, separate from private attempts. Summing levels and batches
costs O(n^(5/2)C_0). Key/body generation keeps the O(n^2(log n)^4 C_0)
global bound above. Since (log2 n)^4<=3sqrt n for n>=2^40, this fits
the same global allowance without a per-chunk retry-work claim.

The smaller width cannot violate c_F=2^20n^3: the preceding explicit
sorting/decomposition bound remains a larger upper bound. Array counts,
slots, full field widths, OWN and all physical fees are unchanged.
Every acquired source remains charged; preparation uses no source and
makes no change to Qcap. New gate/owner event counts still have logarithm
(7/6)sqrt n+O(log n), so exact epoch handling and eventual no-wrap remain
valid. Ordinary staging is constant many O(n)-bit words; counters/arrays
and every recursive context remain counted bank data.

approx_estimate.md and verified_extract.md give aggregate LE work
O(n^2 Qcap)+poly(n), with the same verifier/high-confidence cap
and the guarded cheap-estimator modes, both satisfying its error bound.
Since Qcap=O(rC_0), that fits the same global FW allowance. The retained
tree sum is O(n^(7/2)2^(H+dl)); decoder work is O(n^(5/2)C_0).
Therefore the total structural count is

 C_S=O(n^(5/2)C_0+n^(7/2)2^(H+dl))+poly(n)
    =O(n^(7/2+alpha)2^(e sqrt n)), alpha=29/4,e=7/6.

The typed bank gives T=O(n^(51/4)2^((7/6)sqrt n)). All storage,
source and exact error-model objects are unchanged. The previous success
sum receives just the additional2^-80 term, still strictly below2^-8.
All these bounds concern every actual branch; the unbounded private
retry process is used only as the a.s.-terminating ideal coupling.
