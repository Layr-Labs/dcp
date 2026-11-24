# Truncated variable-depth collimation with a coherent terminal block

Use the branchwise algorithm in variable-profile.md. The other files
give the detailed gate implementation and score laws relied on there.
For conflict resolution, variable-profile.md determines every actual
parameter, including the depth, leaf bound, terminal width, per-record
guards, search repetitions, and total acquisitions. The fixed-depth
configuration and the bank wrappers in the archives are superseded.
The proof uses only clean copies, so the declared malformed fraction is
zero. In the absence of malformed systems, the declared exact input
promise is the independent ideal DCP product.

For every N>=2, let n=ceil(log2 N) and L=log2 n. The result is
full-secret recovery of at least 7/8, simultaneous with the bounds

    T=O(2^((177/250) sqrt(n L))),
    S_C=O(n^2),
    S_Q=O(n),
    Q=O(2^((681/1000) sqrt(n L))).

The respective exact growth indices are 1/2, 0, 0, 1/2. Each bound
holds on every execution branch of the same uniform algorithm.
