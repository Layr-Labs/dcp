# Counted eigenlabel extraction with fixed rational directions

This lemma is used twice by MSR8: on honest source data with modulus K=N,
and on an ordinary maximally mixed register with K=2^p for gradient preparation.
It is adapted from the fully reproduced RLQGR2 extraction argument, in the
standard Kitaev eigenvalue-measurement setting (quant-ph/9511026v1).
All needed implementation and bounds are given here.

Let d=ceil(log2 K), K>=2, and chi_a=K^(-1/2)sum_y exp(2pi i a y/K)|y>.
For a planned maximum C calls to this routine, set J=d+4,
h=ceil(log2(C(J+1)+2))+20, and F=2^24 h.
Translation T_b adds b modulo K on valid data and is identity on invalid
encodings. On chi_a its eigenvalue is exp(-2pi i ab/K).
A fresh |+> ancilla controlling T_(-2^j), then measured in X or Y, has mean
cos(2pi*2^j*a/K) or sin thereof. X measurement is H then computational Z;
Y is S^dagger,H,Z. Conditioned on a the eigenstate and any product spectator
are unchanged and test outcomes are independent. The input may be an ensemble
sum_a p_a sigma_a tensor |chi_a><chi_a|, with arbitrary spectators sigma_a.
The claim is uniform in a and therefore in every such ensemble.

For each j=0,...,J take F tests in EACH basis. Decode their empirical means
x_j,y_j using64 rational direction pairs C_r,S_r approximating
cos(2pi r/64),sin(2pi r/64) to eta=2^(-16). Choose least r maximizing
x_j C_r+y_j S_r. If both means have error<=delta=1/1024, computed dot
products differ from exact cosine of angle difference by<=2eta+2delta<1/256.
The nearest grid point has exact dot>=1-(pi/64)^2/2>=511/512 (pi<4).
A point at circular phase distance>=1/16 has dot<=cos(pi/8)<=31/32,
since1-cos(pi/8)=2sin^2(pi/16)>=1/32 using concavity sin u>=2u/pi.
The gap15/512 is larger than twice1/256, so decoded circular error<1/16.

Generate the direction constants once by counted finite rational operations:
pi=16arctan(1/5)-4arctan(1/239), first64 alternating terms, then first256
sine/cosine Taylor terms at2pi r/64, rounded to denominator2^20, ties downward.
Arctangent error<=16/(129*5^129)+4/(129*239^129)<2^(-100).
Angles are<8; bounds8^512/512!,8^513/513!<2^(-40) and angle error give a
safe total truncation error2^(-30). Rounding adds<=2^(-21), below eta.
Clamp to[-1,1]. The Machin identity follows by tangent addition with the
resulting quarter-pi angle in(0,pi/2). Generation, all rational bit work,
storage and access are a fixed finite counted constant, not advice.

For independent observations in[-1,1], the centered log MGF has second
derivative a tilted variance<=1 and value/first derivative zero at zero.
Integrating twice and optimizing Markov gives
Pr(|mean-Emean|>delta)<=2exp(-F delta^2/2)=2exp(-8h).
Union over2C(J+1) means bounds ANY label error during the planned calls by
4C(J+1)exp(-8h)<4*2^(-160)<1/2048. This uniform bound applies to every
ideal eigenspace input. It controls the actual latent label in each call;
simultaneous success on all K possible labels is not required. J=d+4,
rather than an added d in h, supplies the final bit precision. It is not a claim about arbitrary malformed data.

For unwrapping set g_J=r_J/64. For j=J-1,...,0 choose the closer in circular
distance to r_j/64 of(g_(j+1)+b)/2, b=0,1; ties use b=0.
Given next error e<1/16, the good lift is within e/2 of the true prior phase
and within1/16+e/2<3/32 of the decoded one; the wrong lift is farther than
13/32. The error halves at every step. Final error<(1/16)2^(-J)
<=2^(-d-8)<1/(2K). Round K*g_0 to nearest integer modulo K, ties downward.
It equals a under these conditions. All numerators/denominators have O(d)
bits. Even on malformed input this finite procedure returns a label in[0,K).
No correctness test, retry or postselection is part of this subroutine.

Translations have O(d) exact Boolean gates/wires by ripple comparisons,
addition and selection, with identity extension outside[0,K). Clean reversible
evaluation retains gate values, XORs output and reverses. Apply a permutation
in place by compute-swap-inverse. NOT/CNOT/Toffoli with exact constant-size
Clifford+T decomposition implement all fixed-arity Boolean gates. Reuse O(d)
quantum scratch and one test ancilla. Residues2^j mod K and all constants
are generated with counted integer arithmetic. Every reset, test, address,
controller step and failed/discarded invocation is charged. In MSR8,
log2(C+2)=O(n), d=O(n), F=O(n), so each invocation has polynomial charged work and
O(n) active quantum scratch; the main proof gives the complete allocation.
No Fourier transform, real rotation, purification access, inverse source or
quantum-addressed lookup is assumed.
