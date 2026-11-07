# Robust single-copy Fourier correlation: a complete statistical lemma

This auxiliary file retains the earlier fixed-position `3/16` certificate
and its classical scan consequences. The streamed algorithm in `proof.md`
uses the same finite-score routine, deterministic sample count, and exact
label extractor, but its proved model is now the complete adaptive model
quoted there and its guarantee is `13/40` at threshold `27/160`. The main
proof directly controls ACTUAL conditional score means, including clean-label
bias, by an adaptive martingale. The older fixed-position concentration
argument below is not asserted as proof for that adaptive guarantee.

This evidence file establishes the robust measurement and finite-precision
statistical portion of one possible algorithm. It does not claim the
`2^{O(n^{1/3})}` research target or mathematical novelty. A classical exhaustive
scan of the predicate below already gives polynomial samples and workspace;
a separately proved quantum search can replace that scan. All parameter choices
below are fixed, not optimized after observing the input.

## Parameters and exact error model

Let `N >= 2`, `n = ceil(log2 N)`, and

```
M = 2^18 (n+1),   alpha = 1/64,   epsilon = 3/16,
D = 4096,        theta = 13/64,  delta = 1/(2^16 M).
```

Invoke the extractor below with the exact integer
`q=ceil(log2(2^16 M))` and its fixed repetition count
`r=512(q+ceil(log2(4n)))`. Then `2^(-q)<=delta`.

Acquire exactly `Q=M` source copies and process each by the same local
measurement, without adapting its circuit to previous measurement outcomes.
The fixed corruption promise is the following: there is an unknown fixed set
`B subset {1,...,M}`, with `|B| <= floor(epsilon M)`, such that the joint initial
state of all supplied registers is the tensor product of an independent ideal
`rho_s` in every position outside `B` and an arbitrary joint state on the
positions in `B`. The latter can be entangled across malformed positions and
with an inaccessible private environment. The set `B` and the malformed joint
state may depend on `N,s` and the algorithm, but not on the independent clean
source factors or the algorithm's private measurement coins. No operation by
the adversary acts on the clean factors. This is a fixed-position replacement
model, not a per-copy stochastic corruption probability and not unrestricted
adaptive tampering with clean copies.

This promise includes the clean-input problem by taking `B` empty. All
probability statements below are uniform in the choice of `N,s,B` and the
malformed joint state. Quantum memory held inside the inaccessible source is
not algorithmic storage, as specified in the pinned rules.

## Ideal Fourier record and its physical realization

Put `omega=exp(2 pi i/N)` and define

```
|chi_k> = N^(-1/2) sum_y omega^(-ky)|y>,
|phi_k,s> = (|0> + omega^(ks)|1>)/sqrt(2).
```

Expanding each basis vector in this orthonormal Fourier basis and averaging
over the mixed source's uniform offset cancels every cross term with distinct
Fourier labels. Consequently the exact equality

```
rho_s = (1/N) sum_(k=0)^(N-1)
        |phi_k,s><phi_k,s| tensor |chi_k><chi_k|
```

holds. This equality is only an analysis of the given mixed state: neither its
offset nor any purification is accessed by the algorithm.

The exact modular-translation label extractor proved in
`label-extraction.md` supplies a classical label `khat` and leaves the first
qubit untouched. Its required interface is: for every eigenstate `|chi_k>` it
outputs `khat=k` except with probability at most `delta`, using only the
already acquired source register, fresh zero ancillas, exact Clifford+T gates
and computational measurements. Its work and storage must be included by the
algorithm invoking this lemma. That evidence proves the interface by repeated
Hadamard tests of controlled modular translations, followed by binary phase
unwrapping; it does not assume a QFT oracle, a purification or further source
samples. The statistical proof here uses only this stated interface.

Choose an independent fair bit `b`. For `b=0` measure the first qubit in the
X basis; for `b=1` measure it in the Y basis. Record the resulting sign
`z in {-1,+1}`. These measurements use exact Clifford gates: H for X and
S-dagger followed by H for Y. The ideal record is `(k,b,z)`, while the actual
record is `(khat,b,z)`. For a clean copy the latent `k` is uniform, and

```
E[z | k,b=0] = cos(2 pi k s/N),
E[z | k,b=1] = sin(2 pi k s/N).
```

The latent ideal records of all clean positions are independent, because the
clean source factors and all chosen coins are independent. By the extractor
interface, the probability that any clean actual label differs from its
latent ideal label is at most `M delta = 2^-16`. We couple actual and ideal
records before conditioning on success. We do not condition on the extractors
succeeding and then incorrectly assume that the labels remain uniform.

On a malformed copy the decoder and measurement still produce a classical
record in the same bounded alphabet. Any out-of-range label is mapped to 0.
We need no distributional property, independence or eigenstate hypothesis
for these malformed records.

## Orthogonality gives a uniform constant gap

For a candidate `t in {0,...,N-1}`, define a bounded score for one record by

```
h_t(k,0,z) = z cos(2 pi k t/N),
h_t(k,1,z) = z sin(2 pi k t/N).
```

The score lies in `[-1,1]`. For an ideal clean record its expectation is

```
E h_t = (1/(2N)) sum_k [cos(2 pi k s/N) cos(2 pi k t/N)
                        + sin(2 pi k s/N) sin(2 pi k t/N)]
      = (1/(2N)) sum_k cos(2 pi k(s-t)/N)
      = 1/2, if t=s, and 0 otherwise.
```

The last identity is the finite geometric-series identity: if `s-t` is
nonzero modulo N, then `r=omega^(s-t) !=1`, `r^N=1`, and
`sum_(k=0)^(N-1) r^k=(1-r^N)/(1-r)=0`. This proves the assertion for every
composite or prime N alike; it needs no factorization or primality hypothesis.

## Concentration and arbitrary malformed records

Write `L=M-|B|`. For independent random variables `X_j in [-1,1]`,

```
Pr[ | L^(-1) sum_j X_j - L^(-1) sum_j E X_j | > a ]
    <= 2 exp(-L a^2/2).
```

For completeness, let `f(lambda)=log E exp(lambda(X-EX))`. Then `f(0)=0`,
`f'(0)=0`, and `f''(lambda)` is the variance of a tilted distribution
supported in `[-1,1]`, hence at most 1. Integrating twice gives
`f(lambda)<=lambda^2/2`. Independence, exponential Markov inequality and
optimization at `lambda=a` give the upper tail `exp(-L a^2/2)`; replacing X
by -X gives the lower tail. The bound therefore applies without an unstated
distribution assumption.

Apply it with `a=alpha=1/64` to the clean ideal scores for every one of N
candidates. Their simultaneous event has failure probability at most

```
2N exp(-L/8192)
 <= 2*2^n exp(-26(n+1))
 < 1/256,
```

since `L >= 13M/16` and `n>=1`. This union bound concerns the ideal latent
records; the separate label coupling above transfers it to actual clean
records at an additional failure cost at most `2^-16`.

On that simultaneous event, let `A_t` be the average over all M actual
records using exact real scores. Malformed scores are each between -1 and 1,
regardless of their joint correlations. Set `beta=|B|/M <=3/16`. The correct
candidate obeys

```
A_s >= (1-beta)(1/2-alpha)-beta >= 211/1024.
```

Every wrong candidate obeys

```
A_t <= (1-beta)alpha+beta <= 205/1024.
```

Thus the fixed threshold `theta=13/64=208/1024` separates the correct
candidate from all others. A deterministic approximation of each record's
score with error at most `1/1024` changes any average by at most `1/1024`.
The approximate correct score is at least `210/1024`; every wrong score is
at most `206/1024`. Consequently the Boolean predicate

```
F(t) = [ approximate average score > 13/64 ]
```

has the unique satisfying candidate `t=s` except with probability at most
`1/256 + 2^-16`. This is a joint, unconditional guarantee. A subsequent
search algorithm with conditional failure at most eta has full-secret
success at least `1-1/256-2^-16-eta` by a union bound.

## Fully finite score evaluation, with no real-arithmetic oracle

The following deterministic routine returns a signed integer `a_t` between
`-D` and `D` so that `a_t/D` approximates `h_t` to `1/1024`.

1. Compute `r=kt mod N` exactly by schoolbook multiplication and long
   division of O(n)-bit integers, using O(n^2) Boolean work.
2. Compute a dyadic approximation to `r/N` with 32 fractional bits. Approximate
   `2 pi` by a fixed rational to 32 fractional bits. The latter rational is
   computed by the controller from Machin's identity
   `pi/4=4 arctan(1/5)-arctan(1/239)` using 32 terms of each alternating
   arctangent series; their alternating-series remainders explicitly bound
   its error. This is uniform fixed preprocessing, not instance advice.
3. Evaluate the sine or cosine Taylor polynomial through degree 512 at the
   resulting rational angle using exact rational arithmetic. On `[0,8]` the
   Taylor remainder is at most `8^513/513! < 2^-400`: indeed the last 256
   factors of 513! are all at least 256, giving the weaker sufficient bound
   `8^513/256^256 = 2^-509`. The 32-bit angle approximation changes sine or
   cosine by less than `2^-20`, since their derivatives have magnitude at
   most 1. All numbers in this step have a fixed finite number of bits,
   independent of n; the large constant cost is counted.
4. Multiply by z, round to the nearest multiple of `1/D`, and clip to
   `[-1,1]`. Rounding adds at most `1/8192`; clipping cannot increase error
   relative to the true score. The total error is less than `1/1024`.

The arctangent and Taylor identities in this paragraph can also be checked
directly from their power series and derivatives; they supply no hypothesis
about the input. Signs from b,z are classical. The score comparison becomes
the exact integer comparison

```
sum_(j=1)^M a_(t,j) > 832 M,
```

since `D*(13/64)=832`. There is no precision-dependent probability in this
evaluation.

Each record evaluation has O(n^2) Boolean work plus an absolute constant,
and O(n^2) workspace suffices. A reversible implementation retains Boolean
gate outputs, copies the answer, and reverses; NOT, CNOT and Toffoli suffice,
and Toffoli has an exact constant-size Clifford+T decomposition. Inputs k,b,z
can be classically fixed constants in a streamed gate generator. There is no
quantum-addressed lookup table or uncharged QRAM. A candidate score needs an
O(log M)-bit accumulator after multiplication by the fixed D; scores can be
added and uncomputed one record at a time. Thus a reversible predicate has
O(M n^2) logic operations, O(n^2) qubits, and O(n^2) classical bits including
the M records. The challenge's address charge multiplies gate generation,
memory accesses and gates by O(log(n+2)); all work is summed.

For a purely classical exhaustive scan, predicate evaluation for N candidates
therefore costs `O(N n^3 log(n+2))`, hence
`O(2^n n^4)`, and peak stored records require `O(n^2)` classical bits. Exact
label extraction uses the one acquired copy repeatedly, so the full sample
count is exactly `M=O(n)`. Its separate polynomial preprocessing cost is
absorbed by the exponential scan. The scan itself needs no stored quantum
predicate; it can release each source register immediately after its local
measurement. Its quantum storage is the linear-space decoder's O(n) qubits.

The resulting exhaustive-correlation envelopes are
`[2^n n^4, n^2, n, n]` with growth indices `[1,0,0,0]` and fractional guarantee
`3/16` under the exact model above. A Grover variant must instead include its
coherent arithmetic workspace and prove its own search success and costs;
the statistical lemma does not silently transfer the scan's O(n) quantum
workspace to that variant.

## Applicability and limitations

This proof requires only the stated mixed source, a label extractor with the
explicit uniform interface, exact modular arithmetic, and independent private
measurement coins. Its concentration and orthogonality arguments are included
above rather than imported as unexplained literature claims. The interface is
proved separately in the same submission snapshot in `label-extraction.md`;
that file must accompany any claim using this evidence. No assertion is made
for adversaries that entangle malformed registers with the supposedly ideal
clean factors, choose replacements after inspecting private clean measurement
records, or alter the controller. The positive fraction is a proved guarantee,
not a claim of maximal robustness. The exponential-time scan has time index 1
and does not advance the index toward the stated one-third target.
