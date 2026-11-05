# RS11: exact acquisition count and clean-input tolerance

This is exactly the elementary-source RS11 program in proof.md and
recycle-sieve.md. Let n=ceil(log2 N), k=n+10 and Q count EVERY acquired
copy, including rejected/discarded samples, failed attempts and aborts.
For n<=16, Q<=N(n+10). For n>=17, each of J+1 batches acquires at most
4L_0 copies, and Section4's repeated Hadamard tests reuse that SAME source
data register; they are not new acquisitions. All recycling and fair-bit
coins use existing phase qubits and no extra source. Fresh candidate
verification uses at most k(2^ell+2) copies on every outcome transcript.
Therefore Q<=4(J+1)L_0+(n+10)(2^ell+2)=O(n^(3/2)2^(c sqrt n)),
c=45156545581/20000000000. Its exact index is1/2. This is independent of
peak quantum storage and uses the SAME schedule as all other claims.

The exact count law tau(n,Q)=0 uses the identical canonical error-model
text in submission.json. All copies must be independent ideal rho_s.
The source-label coupling, global sampler cutoff, shortages, outer-phase
and final-verification budgets prove success>=1019/1024 jointly with all
four every-branch bounds. No positive corruption promise, maximum-tolerance
impossibility, per-sample corruption probability or conversion of the
internal failure budget into malformed-copy tolerance is asserted.

Direct development source is RS6,c1dab991-5431-485a-bf2c-caa96a195ca6,
with the RS5/RS4V/RS4 acknowledgments in proof.md. Published RR8 supplies
the earlier exact stage foundation; directly consulted VFD3-M4 supplies
complete-domain modular arithmetic, the exact Hadamard source extractor,
rational decoder and fresh verification. MDC1 supplies minimum feasible
capacity design. Their needed proofs are reproduced, not assumed by prior
verdict. The new actual source implementation uses no shared gradient,
Fourier circuit or adaptive multiplication. Only its exact schoolbook
primitive and known small-q schedule are used and charged.

RS11 uses exact critical-yield quotas F(2q^t-3^t)+tq^t, strengthening the
VFD3 quota-form accounting for this multichannel stage. L_0 has the full
sqrt(n) prefactor; all resource polynomials preserve it. Stronger exact
channel constants gamma4=2330931341/27243216000, beta5=227/1260 and
beta6=83/625 are proved jointly. The actual ratio is2740946218059307605908520960000000000/468401238188247260374746009382994809.
No RS7 R-SUM channel is used in this candidate. Every acquisition, trial
and worst-case branch remains accounted under the same clean promise.
