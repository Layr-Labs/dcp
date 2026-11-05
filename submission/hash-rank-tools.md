# Counted hash sparsification and coherent ranks for PSR4

This helper changes the physical rank implementation. quantum-count-tools.md
supplies the ACTUAL counted circuits; exact counts below are reference
functions with the stated small implementation error, never free oracles.
All decisions here use low labels, original indices and private randomness,
not unused top source-label bits or the unknown secret phase.

## Sparsifying a measured key bucket

After a low-key measurement the t-bit product index is a uniform-magnitude
superposition on S⊂[0,2^t), M=|S|>=1. Its phases can be arbitrary. Set
lambda0=2^30 n^2 L, Kcap=2^10lambda0=2^40 n^2 L.
Obtain a private factor estimate Mtilde∈[M/2,8M] using the supplied circuit.
If Mtilde<lambda0, set h=0. Otherwise choose
h=max(0,min(t,floor(log2(Mtilde/lambda0)))).
This uses exact integer comparisons and shifts, not a real logarithm oracle.
The factor estimate is at most8M<=8*2^t and lambda0>=8, so clipping does
not affect an accurate estimate. All bad outputs still give a finite h.

For h>0 draw an h-by-t uniform binary matrix H using counted private bits,
compute Hx by CNOTs and measure it, retaining the observed hash value. For
h=0 this is the empty hash. Its Boolean predicate is appended to the low-key
predicate. No phase or original incidence vector is inspected by this hash.
Measure no full index. The resulting state is uniform in magnitude on the
selected bucket and retains its original phases.

The Born distribution is exactly described by first choosing a uniform z0
in S, independently of H, and returning the bucket containing Hz0. Conditional
on S,z0, the number M' in that bucket is
1+sum_(z≠z0) 1[H(z-z0)=0]. Each indicator has mean2^-h. Distinct nonzero
differences over F2 are linearly independent, so pairs of these indicators
are independent. Thus mu=1+(M-1)2^-h and Var(M')<=mu.
If h>=1, accuracy of Mtilde gives M2^-h∈[lambda0/8,4lambda0]. Consequently
mu∈[lambda0/8,4lambda0+1]. Chebyshev gives
Pr(M'<lambda0/16 or M'>16lambda0)<=40/lambda0:
the lower event lies below mu/2 and the upper above2mu, costing at most
4/mu+1/mu<=40/lambda0. This is over the private matrix and the Born-selected
bucket, not a claim for every individual bucket. For h=0, M<=4lambda0.

Obtain a second private factor estimate Mtilde' of M'. Discard the whole
attempt and all children if Mtilde'>256lambda0. Every accepted bucket then
has M'<=512lambda0<Kcap in the reference. A bucket in[lambda0/16,16lambda0]
always passes since Mtilde'<=128lambda0; an unhashed bucket also passes.
The physical factor routines' rare failures are transferred by the global
hybrid in quantum-count-tools.md, not assumed impossible.

## Rank and inverse on the accepted bucket

Use the supplied coherent integer counter for
rank(x)=#{z<x : z∈S and Hz=observed hash}.
The total accepted bucket is below Kcap, so EVERY prefix count is under
that cap, including on arbitrary comparison inputs x. Compute rank into
a zero register by the actual approximate-clean XOR routine. Its ideal
reference is the exact Boolean rank function with the same paid block cost.

Define g(u) as the u-th valid product index, in increasing numerical order,
and0 outside[0,M'). It is computed by t-step coherent binary search. At a
prefix, count valid indices in its lower half. Compare the residual rank,
choose the half and subtract the lower count when appropriate. Retain the
t decisions and t small count values to reverse these operations after copying
out the selected index. Guard the whole search with u<M'. Exact counts and
ordinary add/compare make it a total Boolean function. All calls have the
same uniform cap because they count subsets of the accepted bucket.
A compute-XOR-uncompute implementation of g uses O(t) counter calls and
O(t*(R+log n)+t) history qubits. The actual count routine is a unitary
involution, so it supplies the required reversed calls. No source operation
is inverted. Exact integer arithmetic is implemented by clean Toffoli/ripple
circuits, with defined modular behavior on all encoded inputs.

For a valid x, g(rank(x))=x. Therefore clean XOR evaluation of rank followed
by XOR g erases the old product index and leaves its rank with the same phase.
Only high rank bits are measured, retaining a full L chunk at a regular merge
or a pair at the root. An exact private count of the entire accepted set gives
M' to test the partial last chunk; this predicate has no source-index control,
so reading its deterministic reference count measures no source phase.
All approximate-function errors, including this readout, are included in the
uniform count hybrid. Their rare failures are not excluded by conditioning.

Here L=2: run g on the two known ranks, measure the private deterministic
reference masks x,y, and compute the signed-difference output a/rawLow/weight
from the main proof. The equal measured weight key gives new weight0.
All endpoint source supports remain disjoint and their signed coefficients
stay in{-1,0,1}; no binary-incidence/common-weight-leaf premise is used.
The two inverse searches are fully charged and no2^t list is stored.

## Uniform attempt success and unused top bits

On an unhashed regular bucket, the partial L-chunk probability is exactly
(M mod L)/M. Summing over just these low keys is at most the old global
bound(m+1)2^b/2^t<=1/(32n)<=1/(16n), regardless of which keys use h=0.
On a hashed bucket in the concentration interval, partial mass is at most
16L/lambda0. The probability outside it is at most40/lambda0. Cap rejection
occurs only in that exceptional event. Thus all extra failure is at most
(40+16L)/lambda0<1/(16n). Total regular failure is at most1/(8n), uniformly
for every input table list. Fresh groups of children are charged on retries.
This justifies f0=8n/(8n-1) and A0=m f0 in the reference recurrence.

At the final root, the original global unpaired bound is at most1/4.
The same hashing adds less than1/12, so root pair probability stays at least
2/3. Its selected pair is still ordered by original numerical index inside
a bucket that uses only low information. The equal signed weight and exact raw-low
matching keys give the centered-binomial known frequency W proved for
signed disjoint source coefficients in the main proof. For two-adic parity, W is odd with probability1/2 for each
nonzero even support, giving success at least1/3 per root trial. Arbitrary
odd W is not a literal-frequency substitute for odd moduli.

All count estimates used to choose/check the hash depend only on the low-key
predicate. The reference's accuracy clipping changes only these low-data
outputs. The coherent rank/reference permutation also uses only that predicate
and index order. Hence this entire new selection history leaves unused top
label bits independent in the exact-reference argument. This does not claim
independence after observing the full high-label transcript, errors or caps.

## Full query, generation and storage accounting

One predicate query expands into m literal L-row equality/XOR scans, O(n)-bit
sum/comparison arithmetic, the h-by-t matrix parity circuit, and its reversed
scratch. No quantum-addressed table access is assumed. Its primitive gate
and Boolean work is at most a fixed polynomial in n times L; a conservative
2^200 n^12 L CORE allowance includes classical gate/address generation.
The allocated-memory address and monitor charges are additionally applied by
the main proof to every primitive operation, including this generator.

One count/factor block has the literal paid cost gcount from its helper.
Rank, inverse, exact M' readout, factor estimates and all L metadata rows use
O(tL+1) such blocks. Since gcount=2^1000 n^30 2^(ceil(t/2)+2R),
all nonrecursive merge/root work fits
G=2^10000 n^100 2^(ceil(t/2)+3R).
Leaves and initial gradient generation fit this allowance as well. Every
block reserves its whole cost before starting, and all padding/resets count.
The extra classical hash matrices and integer work fit O(n^2): even D matrices
would use at most D t^2<=2nt<=O(n^2), by tD<=2n and t<=n. No failed history
accumulates. The counted private phase window and counting scratch use O(n) qubits.
Search history is O(t(R+log n))=O(n), as proved in window-tools.md. No
coherent median arrays are allocated.
All loops, including invalid-estimate branches, have fixed word widths and
syntactic source/work guards. Rare approximate errors do not remove a branch
from the resource theorem. Every gate, query, discarded child, private coin,
measurement, state preparation and initialization is charged.
