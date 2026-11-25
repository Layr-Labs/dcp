# Exact target phases by interval-matched differencing

Fix an integer modulus N>=2 and secret s in Z/NZ. Write n=ceil(log2 N), and let phi(k) denote the balanced qubit (|0>+exp(2 pi i k s/N)|1>)/sqrt(2), with k reduced modulo N whenever convenient. We use only fresh independent clean copies. Set t=ceil((21/40)sqrt(n)), b=4t and r_0=n-1. Compute t by comparing 1600t^2 with 441n. Choose the smallest D>=0 such that
```
sum_{j=1}^D [1+min(b,4(D-j))] >= r_0.
```
For j=0,...,D, set b_j=min(b,4(D-j)), B_j=2^b_j and U_j=262144(n+1)B_j. For j>=1 set r_j=max(0,r_{j-1}-b_j-1); then r_D=0. Define
```
F = max(0,D-t),    R = 8 U_0 * 13^F * (n+16).
```
The raw acquisition cap is R. Each bank at level j has U_j rows and residual width 2^r_j. We give a branchwise implementation with success greater than 0.98. The main proof uses ideal spectral readout first, then transfers its guarantees to the actual counted circuit.

## Raw phase interface

With eigenangle convention exp(2 pi i k/N) for modular increment, ideal residue spectral measurement yields uniform k in [0,N) and leaves phi(k). The eigenvector coefficients are proportional to exp(-2 pi i kx/N), so the two source coordinates separated by s differ in the measured branch qubit's amplitude by exp(2 pi i k s/N), with the unknown x contributing a common phase. This holds for mixed source states and factors across independent copies.

For a fixed target a in Z/NZ, a bank of offset a at width 2^r consists of U_j labeled qubits at level j. Each row has an independent uniform residual label x in [0,2^r) and state phi(sigma a+x), with a recorded sign sigma in {-1,+1}. An ordinary bank means offset zero. A level-zero call obtains one ordinary bank and one bank at offset a, using two disjoint blocks of 4U_0 raw copies. For the requested offset c in {0,a}, retain input k if (k-c) mod N is less than 2^(n-1), and use that remainder for the residual label. The recorded sign starts at +1. The chance is at least 1/2, independent across inputs, and the retained residual labels are uniform conditional on the flags. Use the first U_0 retained rows for each bank. Abort if either block is short. Hoeffding or a binomial Chernoff bound gives probability at most 2 exp(-U_0/4) of base failure.

## One interval transition

For the transition to level j, put r=r_{j-1}, U=U_j and B=B_j. For r<=b_j set W=1, H=2^r and next width 1. Otherwise let W=2^(r-b_j), H=B and next width W/2. Thus all r-labels split into H equal buckets of width W, H<=B, and the next width matches r_j.

The transition to create one output bank at offset c uses 17U/4 rows at offset c and 17U/4 ordinary rows from independent input streams. Select the first K=33U/(8H) rows of each stream in each bucket. These integers exist because U is a multiple of 8B and H divides B. Abort if any bucket has insufficient rows. This selection uses only residual bucket indices, not the signs or within-bucket labels.

Pair the K rows from each stream in order within each bucket. For each pair apply a CNOT from the first phase qubit to the second and measure the second. Outcome one has probability 1/2 independent of all labels and signs. In this case the remaining row has physical phase label sigma c+x-y, where x,y are the residual labels and sigma is the recorded sign of the first row. The second row has offset zero. Discard the even outcomes. If x<y, apply X to the remaining qubit, which reverses its phase label up to global phase, and negate sigma. The residual label is now d=|x-y|, and the physical label is still of the form sigma c+d with the updated sign. Never use the sign in selecting or accepting a pair.

For W>=2, keep only d<W/2. Accept d=0 with certainty after an odd outcome. For each d>0 below W/2, accept it with independent probability W/[2(W-d)]. To see why, conditional on the recorded bucket indices, the selected within-bucket X,Y are independent uniform in [0,W) under the previous-level residual law. Thus P(d=0)=1/W, while P(d=d_0)=2(W-d_0)/W^2 for d_0>0. The extra accept rule gives the same probability 1/W for each allowed residual value before the odd-outcome factor of one half. In total the acceptance probability is 1/4 and the retained label is uniform on [0,W/2). For W=1, retain all odd rows with residual zero, giving probability 1/2. At this point analyze the accept rule as ideal exact private randomness. A bounded implementation is given below.

Take the first U accepted rows and abort on a shortage. The output residual labels are jointly independent uniform conditional on success. The pair acceptance indicators can be generated first, then the residuals of successful pairs, which have the common uniform law even given all acceptance indicators. The sign metadata is allowed to correlate with these residuals. It is unnecessary to condition on signs at any transition: choices and accept probabilities rely only on the residuals and separate randomness, and parity probabilities are one half for every fixed set of signs. Conditional on all classical metadata the retained row states are products of the labeled balanced qubits; the transition acts on disjoint pairs and preserves that product property.

Each bucket count has mean 17U/(4H) and falls below K with probability at most exp(-U/(544H)), by the multiplicative binomial lower tail at relative gap 1/34. The chance of some shortage is at most 2H exp(-U/(544H)) for one bank. Given enough rows, the number of accepts is binomial with 33U/8 trials and probability at least 1/4, so mean at least 33U/32. At relative gap 1/33 the probability of fewer than U accepts is at most exp(-U/2112).

## Depth-first schedule and abort bound

A level j>=1 call returns both the ordinary bank and the offset-a bank at its level. Assemble 51U_j/4 ordinary rows and 17U_j/4 offset-a rows by the following deterministic rule.

- If b_{j-1}=b_j, call level j-1 thirteen times sequentially. Retain the needed ordinary rows in their order, and collect the needed offset-a rows from the first five children.
- If b_{j-1}=b_j+4, call level j-1 once. It has 16U_j rows in each bank, from which take the required counts as prefixes.

Discard unused rows. Divide the ordinary rows into three consecutive equal streams of 17U_j/4, for the ordinary first arm, ordinary second arm and offset-a second arm respectively. The offset-a rows form their own first arm. Run both interval transitions with c=0 and c=a. Any lower call or transition shortage aborts the whole algorithm and outputs zero.

By induction, conditional on the successful return of any call, its two banks have jointly independent uniform residual labels and labeled qubit states as defined, conditional on full metadata for the states only. At the base this holds because the two raw blocks are independent and their success events are separate. At a nonbase call, the paired bank outputs of all successful child calls have independent product distributions, by induction and fresh acquisitions. In particular the two disjoint sets of input rows to the two transitions are jointly independent in their residuals. Their success conditioning is separate and the interval argument gives the claimed product output. No rule that chooses a subsequent call depends on residual values in its previously generated siblings, except for stopping after an actual reported failure. The fixed tree of potential calls can equivalently be analyzed by assigning each node its own fresh sources and processing it only when reached. Conditional on all required children succeeding in a subtree, its local failure probability is at most
```
4 B_j exp(-U_j/(544 B_j)) + 2 exp(-U_j/2112)
```
for an internal node, and at most 2 exp(-U_0/4) for a leaf. The local bound is uniform across locations and targets. The probability of some abort is bounded by the sum of local failure bounds over the potential nodes, considering the first failure in postorder or inducting with a union bound on child failure and then local failure.

Run one root call separately for each target a=2^j mod N with j=0,...,n+15. From each root retain the first row of its offset-a bank and release all others. At the root the residual label is zero, so the retained row is phi(sigma a). Apply X to it if sigma is negative, obtaining phi(a). For a fixed target, the tree has 13 children precisely at the first F level indices j=1,...,F, since exactly these transitions have b_{j-1}=b_j. Every larger level index has one child. Consequently there are 13^F leaves and at most (D+1)13^F potential nodes. The number of acquired raw copies across targets is at most R. Since b<=8n and D<=n, the total local-abort probability is bounded by
```
(n+16)(n+1) * 13^n * (4*2^(8n) exp(-481(n+1)) + 2 exp(-124(n+1))) < 1/100.
```
For example, use 13^n<exp(3n), 2^(8n)<exp(6n), n+16<=17 exp(n-1), n+1<=2 exp(n-1). The two terms are then bounded by 136 exp(-470n-483) and 68 exp(-119n-126). The local bounds also cover n=1 when D=0.

## From known phases to the full shift

Conditional on no abort in the ideal model, the retained n+16 qubits have the pure tensor product of the prescribed phi(2^j). As a b_d=n+16 bit register its amplitude at integer z is proportional to exp(2 pi i z s/N), since z is the binary sum of its individual place values. Apply the inverse binary Fourier transform, measure z', and output the nearest integer to Nz'/2^b_d reduced modulo N. Ties choose the smaller integer before reduction.

For any phase k/N, exact binary phase estimation with L controls has outcome probabilities bounded by 1/(4d^2) for nonzero circular distance d from 2^L k/N. The geometric-series formula gives this since sin(pi d/2^L)>=2d/2^L for d<=2^(L-1). With L=n+h, rounding reports k unless d>=2^(h-1). There are at most two outcomes in each unit interval of distances. Therefore error probability is at most sum_{j>=2^(h-1)} 1/(2j^2) <= 1/(2(2^(h-1)-1)) when h>=2. The final inverse transform is compiled with aggregate operator-norm error at most 1/1024. Using h=16 and norm telescoping gives final decoding error less than 1/512, conditional on no ideal abort. This reasoning makes no restrictions on N's arithmetic structure.

## Bounded random acceptance

For d>0 with d<W/2, draw a uniform integer in [0,2(W-d)) and accept exactly when it is below W. To draw it use uniform integers in [0,2W) from fresh Hadamard coin bits and reject values outside the smaller interval. A single try succeeds with probability greater than one half. Use at most L_c=ceil(log2 P)+20 tries, with
```
P=64(D+1) U_0 * 13^F * (n+16).
```
Abort if the cap is exhausted. There are fewer than P pair operations: at each of the (D+1)13^F potential nodes per target, the two transitions use at most 2*(33/8)U_0 pairs, and base nodes use none. The ideal exact randomness therefore differs from the bounded implementation with probability at most P * 2^-L_c <=2^-20 by coupling and union bound. The ideal output law was established by considering the uncapped draws, whose distribution is exactly uniform. The caps make the real work finite even for the rare branches where all draws miss.

## Counted readout and implementation

Use binary phase estimation of modular increment to implement the raw spectral readout. Let h=ceil(log2 R)+20 and L=n+h. Keep the branch qubit, apply controlled powers of the modular translation to the residue register, and measure the inverse Fourier transform of the controls. Controlled translation by each 2^i mod N is a reversible constant addition modulo N on residues below N and fixes other states, using linear arithmetic scratch. Compute the constants by modular doubling. Round the outcome as above and release the residue and controls. Compile the inverse transform with total operator-norm error at most 1/(2^20 R). This is uniform by computing the phases to logarithmic precision in R and applying a constructive Solovay–Kitaev compiler for fixed-dimensional Clifford+T gates. Controlled phase gates can be decomposed into a fixed number of single-qubit rotations and CNOTs. See Dawson and Nielsen, https://arxiv.org/abs/quant-ph/0505030.

In the exact phase estimation circuit, each eigenstate of modular translation remains unchanged in the residue register. The conditional distribution of the reported label and the retained qubit is therefore a classical mixture over latent exact k, with phi(k) retained given k. The rounding error of the label is at most 1/(2(2^(h-1)-1)), so this output interface differs from ideal spectral readout in trace distance at most that bound. Synthesis contributes at most its aggregate norm error, even before rounding and release. Their sum is less than 1/(2^18 R). Telescoping the adaptive instruments along the fixed cap of R attempted acquisitions gives total trace distance less than 2^-18 between the ideal and implemented protocols, preserving all previously kept rows and classical information. A stopped branch can be represented by a terminal flag and identity for all further calls. Together with the bounded random acceptance coupling, the actual probability of success is greater than 0.98. All sieve pairing gates, measurements and labels after acquisition are exact, and classical controllers are uniform.

## Joint cost

At each level hold at most a constant multiple of U_0 pending rows in local buffers, with a classical residual label and position index per row. Accumulating the inputs of a call takes one recursive child at a time, and a depth-first traversal has at most D+1 frames. Bucketing uses ordinary classical buffers indexed by bucket numbers, with O(U_j) row entries and O(B_j) counters per active transition. Each row descriptor and count occupies O(n) bits. One row qubit per stored row is retained, plus O(n) live scratch and controls for raw readout, and at most n+16 completed target rows. Addresses for both spaces have O(n) bits. Thus each peak space is bounded by a fixed polynomial of n times 2^b. Since b<=(21/10)sqrt(n)+4, each has envelope O(2^((43/20)sqrt(n))) by absorbing the polynomial.

Each call performs at most polynomial work per input or output row, plus a polynomial times B_j for bucket setup. Label arithmetic uses O(n)-bit integers. Direct classical bucket indexing obtains K selected positions with a constant number of scans or counters, counting all addressed accesses. A depth-first traversal moves a row by updating its descriptor and reclaims a measured or discarded row's slot. For the bounded correction draws, L_c=O(n) tries with O(n) bits and operations per try, up to polynomial address overhead, add only polynomial work per pair and O(n) scratch. Gate emission, thresholds, counters, measured outcomes, addresses and the complete memory initialization are counted. A sample costs n+1 and all sample acquisition circuits have polynomial size and generation cost because the guard size and control-register length are O(n). The final Fourier decoding has polynomial work. Consequently total work is O(poly(n) 2^b 13^F), and raw samples bounded by R have the same envelope.

For all sufficiently large n, D>=t: at D=t the summed reduction capacity is 2t(t-1)+t=(441/800)n+O(sqrt(n)), which is below n-1. For D>=t the exact reduction capacity equals
```
(D-t)(b+1) + 2t(t-1)+t.
```
Therefore
```
F = ceil([(n-1) - (2t(t-1)+t)]/(b+1))
  = (10/21 - 21/80) sqrt(n) + O(1).
```
Here b=(21/10)sqrt(n)+O(1) and t=b/4, so the term subtracted from n/(b+1) is b/8+O(1). The root exponent coefficient of 2^b 13^F is
```
21/10 + (10/21 - 21/80) log2(13) < 29/10.
```
For example 13^100<2^371 gives log2(13)<371/100, which suffices. The fixed slack absorbs every polynomial factor, giving O(2^((29/10)sqrt(n))) for work and for samples. All finitely many smaller lengths obey the same big-O with a larger absolute constant. There are no unbounded loops, even on branches with shortages or readout errors. All four resource envelopes have growth index exactly 1/2. The tolerance claim is zero among acquired copies and requires independent ideal coset states.

The pair-differencing primitive and the idea of a sieve by label collisions are classical DCP algorithmic ingredients, e.g. Kuperberg https://arxiv.org/abs/quant-ph/0302112 and Regev https://arxiv.org/abs/quant-ph/0406151. The finite interval buckets, recorded signed offsets, triangular-difference correction, shrinking bank budgets and exact target powers define this implementation for arbitrary moduli.
