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

## Global counted ledger

perm_fw.md Sections7-8 preserve the exact FW instrument while preparing
keys only after kind=matching. Every request still increments M_K's
counter. Completed matching/Ev outcomes number O(C_0), by sum rho and
w-1 removals, plus at most one incomplete matching request on abort.
Successful key attempts are thus O(C_0+1); failed attempts are EXECUTED
at most F_K=O(r C_0). Full bitonic private work costs
O(n^(3/2)(log n)^3) each, hence O(n^2(log n)^3 C_0) globally.
The O(w)-gate pair realization costs O(n^(3/2)log n) each; all requests
give O(n^(5/2)log n C_0), including complete physical arguments.
The joint coarse-plus-cell macro has the same arbitrary-input Kraus law;
no extra cell refinement or leaked count remains.

The key cutoff proof above still applies: fresh failed-key indicators
have the same conditional probability even after current kind, and the
old M_K request allowance is an upper bound on the fewer actual seeds.
On cutoff after kind the entire window is decoded and cleaned normally.
No ideal law is conditioned on successful key survival. All source,
fallback, pool/decoder couplings and actual acquisition caps are unchanged.

With the retained dictionary, tree and source terms the complete bound is
 T<=c[n^(5/2)(log n)^(3/2) C_0+n^2(log n)^3 C_0
       +n^3(log n)^(3/2)2^(H+dl)+n^2(log n)^2 Qcap
       +n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(43/4)(log2 n)^2 2^((7/6)sqrt n)).
The four other complete structured objects and success >=1-2^-8 are
unchanged. All initialization, retries, actual gates/addresses and final
or abort cleanup remain counted; finite deterministic layout fallback
selects the original exact implementation without a new failure event.
