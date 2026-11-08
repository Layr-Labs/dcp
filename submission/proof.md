# Bank-first log-depth collimation at depth 46 ceil(log2 n): DCP with malformed-copy tolerance (log2 n)/(11837676818611 n^47) in 2^{n/(46 log2 n)} poly(n) work

## 0. Theorem, error model and key idea

Theorem. Fix N >= 2 and s in Z_N; n = ceil(log2 N); L = max(1, log2 n). Algorithm RB below, with the depth rule
ell = 46 ceil(log2 n) for n >= 4096 and ell = 3 below (all parameters computed from N by integer arithmetic), acquires exactly Qbank copies, a number
fixed by N alone (Section 1). Under the adaptive malformed-copy model stated below with
  epsilon(n) = (log2 n)/(11837676818611 n^47),
for every adversary of that model, including the one that corrupts nothing, it outputs the whole s with
unconditional probability > 0.99, and on EVERY branch it uses, with absolute constants, for all n >= 1:
  T   = O(n^51 L^3 2^{n/(46L)}),   S_C = O(n L^2 2^{n/(46L)}),   S_Q = O(n^49),   Q = Qbank = O(n^48),
jointly for the same algorithm and configuration. The growth indices of these envelopes are 1, 1, 0, 0.
(Polynomial degrees are not optimised; Section 9 derives them.)

Error model (verbatim specification). Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

Key idea. (Credits for this construction are in the final section.)
RB is the constant-width collimation sieve of the public submission B (04669374-610b-497e-ae9b-c856335731ce),
whose Sections 1-9 and Appendix P are restated in full below; changes are marked "RB". Width R0 = n/ell + O(log ell) instead of
(23/32) sqrt n gives depth <= ell, m* = O(2^ell n/ell) copies per root and T = 2^{n/(46L)} poly(n). Robustness:
(1) bank first (Lemma BF, the argument of Lemma 0 of the public submission R24, f892f7ea-957b-4dde-8374-dab2736231d0) reduces the adaptive
adversary to fixed malformed sets; (2) a private uniform order makes each taken slot malformed w.p. <= epsilon' =
epsilon/(1 - 2^{-11}) given the past (Lemma C1); (3) a malformed slot spoils only its own root, honest roots keep B's
fair top bits (Lemmas 6a-7), every record has conditional mean in [-1, 1] (Lemma 9(c)), and with epsilon m* <= 1/64 the
contaminated fractions (Section 7) are tolerated by B's decoder at accuracy 5/32 (Lemma 10) and by majority votes
(Lemma 11). The price is the bank: S_Q <= Qbank (n+1) + O(n) (Lemma 5) and Q = Qbank, both polynomial.

Gate set: X, CNOT, Toffoli, H, S, S^dagger, with each Toffoli counted as 15 gates of its exact Clifford+T
circuit (7 T/T^dagger, 6 CNOT, 2 H); computational-basis measurement; fresh |0>. No other rotation, no QFT
over Z_N, no QRAM.

Conventions (added in this entry, on every branch). round(z) = floor(z + 1/2) for every real or dyadic z, so
round is a fixed integer function with ties going up. Applied to a value in [0, M) or [0, N) and reduced mod M
or N, it is defined for every input, including half-integers such as M G_0 = M/2 on failure branches.
"The closer of" two candidates always takes the first candidate on ties (as in Lemma 1).

## 1. Parameters

d = floor(log2 N) (so 2^d <= N < 2^{d+1}, d >= 1); N = 2^a M with M odd.
Depth rule. ell = 3 if n < 4096; ell = 46 ceil(log2 n) (ell >= 72) if n >= 4096.
Width (RB). v = the least integer v >= 4 with 2^v >= 16 (ell + 1); R0 = max(ceil(n/ell) + v, 2v + 2); R_j = R0 for
all j; eta = 2^{-v}, f0 = 2^v/(2^v - 1). (RB: B's merge-failure bound eps is called eta here; epsilon is the
malformed fraction.)
Schedule Sched(P), integer P >= 0. If P = 0: D = 0 and no merges. If P >= 1: D = ceil(P/(R0 - v)),
b_j = R0 - v for 0 <= j <= D-2, b_{D-1} = P - (D-1)(R0 - v) (so 1 <= b_{D-1} <= R0 - v, sum_j b_j = P). m = 2^D R0.
Facts. (F1) R0 - v >= R0/2 (if R0 = 2v + 2 then R0 - v = v + 2; otherwise R0 > 2v + 2).
(F2') If P <= n - 1 then D <= ell: in both cases R0 - v >= ceil(n/ell) (if R0 = 2v + 2 then 2v + 2 >= ceil(n/ell) + v),
so P/(R0 - v) <= (n - 1)/ceil(n/ell) < ell. Hence 16(D + 1) <= 16(ell + 1) <= 2^v.
(F3) f0^D <= (1 - 1/(16(D+1)))^{-D} <= e^{D/(16D+15)} < e^{1/16} < 2.
D and m are non-decreasing in P; v and R0 depend on n only. D*, R0*, m* denote the values for
P* = max(n-1, 0) (R0* = R0); every tree below has P <= P*, hence D <= D* <= ell, m <= m*.
(F4') m* <= 11837676818611 n^47/log2 n for every n >= 2. For 2 <= n < 4096, ell = 3 and the inherited estimates m* <= 28 for n <= 7 and m* <= 14n for n >= 8 are below this bound.
For n >= 4096: ell = 46 ceil(L). Put c = 12 = 6 + ceil(log2 46) and m0 = ceil(L) >= 12. If L is integral, 2^(m0+c) >= 16(46m0 + 1); if L is not integral, m0 >= 13 and 2^(m0-1+c) >= 16(46m0 + 1). Both inequalities hold at m0 = 12 or 13, and the ratio of the left side to 16(46m0 + 1) increases with m0. Thus v <= L + c. Also ell < 46L + 46, so 2^{D*} <= 2^ell < 70368744177664n^46. Consequently
R0 = max(ceil(n/ell) + v, 2v + 2) <= n/(46L) + 2L + 2c + 2 = n/(46L) + 2L + 26;
both branches follow from v <= L + c and ell >= 46L.
Hence m* = 2^{D*}R0 < 70368744177664n^46(n/(46L) + 2L + 26) <= 11837676818611n^47/L, because L(2L+26)/2^L decreases for L >= 12 and its value at 12 is 600/4096.
(F5') 2^{D*} <= 2^ell, and 2^v < 32 (ell + 1) (v is least, or v = 4), so 2^{R0*} <= 2^{v + 1} max(2^{n/ell}, 2^{v + 1})
< 64 (ell + 1) max(2^{n/ell}, 64 (ell + 1)).
Word bound: Lambda = 2(n + D* + R0*) + 256.
Statistical parameters (defined for every N): q = 2 m*, Mgrid = 2^20 (q + 1),
hstat = ceil(log2(Mgrid + 1)) + ceil(log2(n + 7)) + 20, Kstat = 2^32 hstat, J = n + 4,
r_maj = 2^17 (ceil(log2(n + 1)) + 8) + 1 (odd; RB: larger than in B, for Lemma 11). Decoder accuracy (RB): e_dec = 5/32.
Odd part, used iff M > 1: P_o = d - 1, F = 2^{d-1}, f = 2^{d-1-a} (an integer: N >= 3 2^a gives d >= a + 1).
Two-adic part, used iff a >= 1. Initially r = 0 and u = 0.
Caps and bank (Section 9; RB). Tree cap Ctree = 64 m*. Stage tree caps: an odd stage starts at most
K+ = floor(21 Kstat/20) trees, a two-adic level at most 3 r_maj trees. Q* = 3 m* ((n+5) Kstat + n r_maj),
W* (Section 9), slot cap Qcap = 2^11 Q*, Wcap = 2^11 W*, bank size Qbank = 2^11 Qcap = 2^22 Q*, key length
kappa = 2 ceil(log2 Qbank) + 40. Label tests: H_lab = ceil(log2(Qcap + 2)) + ceil(log2(n + 5)) + 14,
F_lab = 512 H_lab. All are integers computed before the first acquisition.
Tolerance (RB). epsilon(n) = (log2 n)/(11837676818611 n^47). By the model at most floor(epsilon Qbank) of the Qbank acquired copies are
malformed. Put epsilon' = epsilon/(1 - 2^{-11}).
(F6) epsilon m* <= 1/64, hence epsilon' m* <= 1/63: for n >= 2, m* <= 11837676818611 n^47/log2 n (F4') gives epsilon m* <= 11837676818611/757611316391104 = 1/64; epsilon is 0 at n = 1.


Lemma 0 (words). Every integer the algorithm stores (table entries, labels, W, z, counters, caps, records)
has absolute value < 2^Lambda; every product is formed in a 2 Lambda-bit scratch word.
Proof. Table entries are sums of at most m* labels < 2N: < 2^{n + 1 + D* + log2 R0*}. Write k = D* + R0*. From the
definitions above, n + 5, hstat, H_lab and D* + 2 are < Lambda, r_maj < 2^{18} Lambda, m* <= 2^k, Mgrid <= 2^{k+22} and
Kstat < 2^32 Lambda.
Hence Q* = 3 m* ((n+5) Kstat + n r_maj) < 2^{k+34} Lambda^2, Qbank = 2^22 Q* < 2^{k+56} Lambda^2 and
R* = 2(n+5) Kstat + 3n r_maj < 2^{34} Lambda^2 (Section 9),
and, term by term in the formula for W* (Section 9): Q* c_copy < 2^{k+70} Lambda^7, the tree term < 2^{k+56} Lambda^7,
(n+5) c_est < 2^{k+84} Lambda^6, c_set < 2^{20} Lambda^5 and c_bank < 2^{k+68} Lambda^5, so W* < 2^{k+85} Lambda^7. Counters are at most
Wcap + (largest allowance) <= 2 Wcap, so log2(2 Wcap) < k + 97 + 7 log2 Lambda < Lambda (as 7 log2 Lambda <
159 + (Lambda - 256)/2 for Lambda >= 256 and Lambda - 256 = 2(n + k)).
(RB) Slot indices are < Qbank < 2^Lambda, and keys have kappa < 2k + 154 + 4 log2 Lambda < Lambda bits
(4 log2 Lambda < 2n + 102).
The normalised fixed-point values of the decoder (Section 6) have 128 fractional bits and absolute value < 64 (by
the evaluation order given there); its integer operands (c^2 <= 239^2, Taylor denominators, iota' 2^128, C_iota,
S_iota) are below 2^Lambda. []

## 2. Source copies and labels

Let chi_k = N^{-1/2} sum_y e^{2 pi i k y/N} |y>. Writing |x> in this basis and averaging over x:
  rho_s = (1/N) sum_k |phi_{k,s}><phi_{k,s}| (x) |chi_k><chi_k|,  phi_{k,s} = (|0> + e^{-2 pi i k s/N}|1>)/sqrt2.
(Cross terms k != k' vanish because sum_x e^{-2 pi i (k-k') x/N} = 0.)

Bank and order (RB). The first operation involving sources acquires all Qbank raw (n+1)-qubit copies into a
bank of slots 1..Qbank, in this deterministic order. The algorithm makes NO measurement, private random draw,
source transformation or abort decision until the last copy has arrived (the setup before it is deterministic and
reads no source). Then it draws, for every slot, a kappa-bit key from kappa fresh fair coins (measure H|0>) and sorts
the slots by (key, slot index); pi(1), pi(2), ... is the resulting order. The t-th source call of the run takes slot
pi(t) ("takes a slot"); every "acquire a copy" of B below means this.

Lemma BF (bank first; the argument of Lemma 0 of R24, f892f7ea-957b-4dde-8374-dab2736231d0). For this schedule every
adversary of the model produces a mixture of fixed-position inputs: a set Bad of at most floor(epsilon(n) Qbank)
malformed slots, an arbitrary joint state of those slots (with a purification the algorithm never accesses), and
independent rho_s factors on all other slots, tensor-independent of the malformed subsystem; Bad and its state may
depend on N and s. Hence it suffices to prove the success bound for every such fixed Bad.
Proof. Record each delivery's clean/malformed decision in a hidden classical register. As the algorithm makes no
measurement and no private draw before the last delivery, there is no algorithm outcome on which the adversary's
decisions could depend. By induction over j, conditioned on the decisions for deliveries 1..j, the unnormalised
joint operator of the delivered slots and the adversary's system is (tensor product of rho_s over the clean
delivered slots) (x) (a positive operator on the malformed delivered slots and the adversary's system): a private
instrument of the adversary acts on the second factor only (it may steer earlier malformed slots but cannot touch a
clean factor); a malformed delivery moves a subsystem of the second factor into slot j; a clean delivery appends a
fresh rho_s in tensor product with everything, by the model's promise. Summing over instrument outcomes (countably
many) preserves this form. After the last delivery trace out the adversary's system and condition on the decision
record: this is a finite convex mixture over sets Bad of states of the stated form, and the pathwise cap gives
|Bad| <= floor(epsilon Qbank). Every later operation of the algorithm acts on the bank and its own workspace, so its
output law is the same mixture of its output laws for fixed Bad. []

Ties (RB). Two given slots get equal keys w.p. 2^{-kappa}, so some tie occurs w.p. <= Qbank^2 2^{-kappa-1} <= 2^{-41}.
In the analysis let pi' be the order obtained by sorting by key and breaking ties by an independent uniformly random
order. pi' is a uniformly random permutation of the slots, independent of the bank and of all other randomness, and
pi' = pi unless a tie occurs.
Lazy exposure (RB). The run reads the order only through the slots it takes: before it takes its t-th slot pi'(t),
no operation depends on pi'(t), ..., pi'(Qbank) (the keys and the stored order serve nothing else). So, given pi', the
law of everything the run produces before taking slot t depends on pi' only through pi'(1..t-1); as pi' is uniform
and independent of the bank, Bayes' rule makes pi'(t) uniform on the untaken slots given Bad, pi'(1..t-1) and all
those data. Every history, past or sigma-field of Sections 3-9 (H, G_t, F_{i-1}, "given its history") is generated by
Bad, the taken slots, their labels and the run's other outcomes, coins and data, never by the keys or the untaken
part of the order.

Lemma 1 (label extraction; the Kitaev test design follows RLQGR2/QSR16, the decoder is trig-free).
Let T_b: |y> -> |y + b mod N> for y < N, identity for N <= y < 2^n. T_b chi_k = e^{-2 pi i k b/N} chi_k.
Procedure on the data register of one copy: for j = 0..J run F_lab tests in the X basis and F_lab in the Y
basis. A test prepares |+> = H|0>, applies T_{-2^j mod N} controlled by it (P3), applies H (X basis) or
S^dagger then H (Y basis), measures (+1/-1) and resets the ancilla. Let x_j, y_j be the two means.
Quadrant decoder: c_j = 1/8, 3/8, 5/8, 7/8 for (x_j >= 0, y_j >= 0), (< 0, >= 0), (< 0, < 0), (>= 0, < 0).
Unwrap: g_J = c_J; for j = J-1..0, g_j = whichever of g_{j+1}/2 and (g_{j+1}+1)/2 is circularly closer to c_j
(tie: the first). Output k^ = round(N g_0) mod N (dyadic rationals with J + 3 bits; exact).
Claim: on input chi_k (with any spectator), k^ = k except w.p. <= 4(n+5) e^{-F_lab/512}; the eigenstate and
spectators are unchanged.
Proof. Conditioned on k the tests are i.i.d. with means cos(2 pi 2^j k/N) (X) and sin(2 pi 2^j k/N) (Y):
controlled T_{-2^j} maps |+>|chi_k> to (|0> + e^{2 pi i 2^j k/N}|1>)/sqrt2 |chi_k>. By Hoeffding each mean is
within 1/16 of its expectation except w.p. 2 e^{-F_lab/512}; union over 2(J+1) means. On that event, with
lambda_j = 2^j k/N mod 1, at most one of x_j, y_j has the wrong sign (|cos| and |sin| cannot both be < 1/16),
and a wrong sign forces lambda_j within arcsin(1/16)/(2 pi) < 0.01 of the axis on which the wrongly signed
coordinate vanishes (e.g. a wrong sign of x_j puts 2 pi lambda_j within arcsin(1/16) of +-pi/2); so c_j has
circular error e_1 <= 1/8 + 0.01 = 0.135 (e_1 is local to this lemma). Unwrapping: if g_{j+1} has error e <= 0.135, one candidate is
within e/2 of lambda_j and the other is 1/2 away from that one; the right one is chosen because
e/2 + e_1 < 1/2 - e/2 - e_1 (0.405 < 1/2), and the error halves. So |g_0 - k/N|_circ <= 0.135 2^{-J}, and
N 0.135 2^{-n-4} < 1/2 gives k^ = k. Tests act on chi_k by phases only. []
With F_lab = 512 H_lab and at most Qcap calls (RB: Qcap caps the taken slots), the union bound is <= 4(n+5) Qcap e^{-H_lab}
= 4(n+5) Qcap 2^{-H_lab} (2/e)^{H_lab} <= 2^{-12} (2/e)^{14} < 2^{-18} (as 2^{H_lab} >= 2^{14}(Qcap + 2)(n + 5) and H_lab >= 14).
Cost per copy: 2(J+1) F_lab tests, each a controlled modular addition (P3) plus at most 5 gates, so at most
1024 (n+5) H_lab (600(n+2) + 5) <= 2^{18} Lambda^2 H_lab gates and measurements; classically, the J + 1
constants -2^j mod N (by modular doubling), the 2(J+1) outcome counts, the decoder and the relabelling below
(one product and one division of Lambda-bit words) take at most 2^{13} Lambda^2 H_lab bit operations.

After extraction apply X to the control: it becomes q_k(s/N) = (|0> + e^{2 pi i k s/N}|1>)/sqrt2 up to a
global phase; the data register is reset. (RB) On a malformed slot the same procedure runs; it outputs some
k^ in [0, N), and the control qubit is left in some state, possibly entangled with the rest of the bad block.
Ideal reference process: the same algorithm, running the same tests at the same cost, but with each HONEST slot's
extraction output k^ replaced by its true eigenlabel k (for a fixed Bad of Lemma BF, in the analysis one may insert,
right after the bank is acquired, the projective measurement {|chi_k><chi_k|} on the data register of every honest
slot: it leaves rho_s unchanged (rho_s is block diagonal in this basis), and every later operation on that register
(controlled T_b, then reset) is diagonal in the chi basis or discards the register, so the joint law of all
outcomes is unchanged; k is then a classical random variable, uniform on [0, N) and independent of the past).
Coupling the two processes (same
eigenlabels, test outcomes and later measurement outcomes), they agree, counters and outputs included, until
the first honest extraction whose output k^ differs from k. On every branch at most Qcap extractions happen, each
honest one errs w.p. <= 4(n+5) e^{-F_lab/512} given the past, so the two runs coincide except w.p. < 2^{-18}. Sections 3-8
analyse the ideal process for a fixed Bad: there each honest slot has a label uniform on [0, N), independent of
the labels of all other slots, of the bad block, of the order and of all private coins; a malformed slot's label
is whatever its extraction outputs.

Units (classical relabelling). For a known unit alpha mod N and an extracted label k put k' = alpha^{-1} k mod N.
Since k s == k' (alpha s) mod N, the qubit q_k(s/N) equals q_{k'}((alpha s mod N)/N): it is a copy with label k'
for the secret alpha s mod N, and k' is uniform on [0, N) and independent of the history when k is. No quantum
operation is needed.

## 3. Phase vectors and the merge

A register of width 2^R is a classical pair of integer tables (K_i, L_i), i in [0, 2^R), and the R-qubit
state 2^{-R/2} sum_i e^{2 pi i K_i theta} |i> up to a global phase.
Invariant (I): entry i corresponds to a binary incidence vector x^{(i)} over the copies used by the register;
distinct entries have distinct vectors; K_i = sum_j x_j k_j and L_i = sum_j x_j l_j as UNREDUCED integers,
where copy j carries its integer label k_j and its low part l_j (defined in Sections 6 and 8).
"P pinned bits" means all L_i are congruent modulo 2^P.
Leaf: R0 copies, qubit e holding q_{k_e}(theta); a register of width 2^{R0} with x^{(i)} = binary digits of i
(tables by doubling); 0 pinned bits.

Merge(A, B, P, b, W') with A = (K, L) of width W1 = 2^{R1}, B = (K', L') of width W2 = 2^{R2}, both with P pinned
bits, 1 <= b, W' = 2^{R'} <= W1 W2. Let c = L_0 mod 2^P, c' = L'_0 mod 2^P, rho(i) = ((L_i - c)/2^P) mod 2^b,
rho'(j) = ((L'_j - c')/2^P) mod 2^b (exact: L_i == c mod 2^P and 0 <= c <= L_i).
Classical preprocessing: stable sort of j by rho'(j) (ties by index j); pos(j) = rank of j; for each residue
sigma < 2^b, start(sigma) and size(sigma) of its block (start = 0 if empty).
Quantum steps on |i>|j> (lookups are P2; every table is defined on its whole address space, 0 at unused
addresses):
 (a) Look up rho(i) into a b-qubit register A and rho'(j) into a b-qubit register B; add B into A mod 2^b;
     MEASURE A, outcome y; clear B by the same lookup on j; reset A using y. The state is uniform over
     S_y = {(i,j): rho(i) + rho'(j) == y mod 2^b} with unchanged phases. Classically compute
     off(i) = sum_{i'<i} size(y - rho(i')) and G(i) = off(i) - start(y - rho(i)).
 (b) Look up pos(j) into a fresh register p of R1 + R2 qubits; look up pos^{-1}(p) (W2 entries) and XOR it into
     the j register, which becomes 0.
 (c) Look up G(i) (as a residue mod 2^{R1+R2}) into a scratch register, add it into p mod 2^{R1+R2}, clear the
     scratch by the same lookup. On S_y, p now holds idx(i,j) = off(i) + pos(j) - start(y - rho(i)), a
     bijection S_y -> [0, |S_y|) (for fixed i it maps the partners of i onto [off(i), off(i+1))).
 (d) MEASURE the top R1 + R2 - R' qubits of p, outcome beta. If (beta + 1) W' > |S_y| the merge FAILS (all its
     registers are measured and discarded). Otherwise reset the measured qubits using beta; the low R'
     qubits of p hold t = idx - beta W'.
 (e) Look up I_beta(t) = (the i of the pair with index beta W' + t) and XOR it into the i register:
     |i, t> -> |i XOR I_beta(t), t>, a permutation that clears i on the support.
Output: the register of width W' on the t qubits with K''_t = K_{i(t)} + K'_{j(t)}, L''_t = L_{i(t)} + L'_{j(t)},
P + b pinned bits (L_i + L'_j == c + c' + 2^P y mod 2^{P+b} on S_y). Each step is a permutation of basis states
or a computational-basis measurement, so the output state is exactly 2^{-R'/2} sum_t e^{2 pi i K''_t theta}|t>
up to a global phase, and (I) holds (an output entry is a pair of entries of registers on disjoint copies).

Lemma 2 (cost of a scheduled merge). For R1 = R2 = R, R' in {R, R + 1} and b <= R - 1 (all merges of Section 4),
one attempt uses at most 2^{R+13} (R + 1) quantum gates and measurements, at most 2^{R+9} Lambda^2 classical
bit operations, O(R) scratch qubits and at most 2^{R+6} Lambda classical bits.
Proof. Eight lookups (three in (a), two in (b), two in (c), one in (e)), each over at most 2^{R+1} entries with
index width <= 2R and data width <= 2R + 1: by P2 at most 2^{R+1}(128 R + 2R + 1) gates each, total
<= 2^{R+12}(R + 1); two adders of width <= 2R (P3), at most 4R measurements and resets, and at most 64(R + 1)
operations to initialise scratch and, on failure, to measure and discard all registers. Classically:
sort 2^R keys of <= 2R bits (P3), the arrays start, size (2^b <= 2^R entries), pos, pos^{-1}, off, G (prefix sums
of Lambda-bit numbers), I_beta and the output tables (scan a local index t = beta W', ..., (beta + 1) W' - 1 in order, keeping the i
with off(i) <= t < off(i) + size(y - rho(i)), skipping empty intervals, and setting j = pos^{-1}(start(y - rho(i)) + t - off(i));
only the retained block is visited, with two Lambda-bit additions per output entry): each O(Lambda) bit operations per entry, at most 2^{R+9} Lambda^2 in total. []

Lemma 3 (distribution-free yield). For ANY tables, Pr[merge fails] < 2^b W'/(W1 W2).
Proof. Magnitudes are uniform, so y has probability |S_y|/(W1 W2), and given y the value idx is uniform on
[0, |S_y|). Failure means idx falls in the last, partial block, of size |S_y| mod W' < W'.
Hence Pr[fail] = sum_y (|S_y| mod W')/(W1 W2) < 2^b W'/(W1 W2). []
(RB) A register is contaminated if its copy set (Invariant (I)) contains a malformed slot, and honest otherwise.
For every register the tables and (I) are as stated; the stated quantum state, and hence Lemma 3, are claimed
only for merges of two honest registers. A merge with a contaminated input may fail with any probability; a
failure discards both inputs.

## 4. The constant-width tree

Tree(P): a level-0 node is a leaf; a level-(j+1) node runs Merge(A, B, P_j, b_j, 2^{R_{j+1}}) on two
independently built level-j nodes, P_j = b_0 + ... + b_{j-1}; on failure it builds two fresh level-j nodes and
retries. Evaluation is depth-first. The root node has level D, width 2^{R_D} and exactly P pinned bits.
(RB) Tree cap: if a Tree(P) has taken Ctree slots (all its source calls, rejected trials included) and is not
finished, it is abandoned: all its held registers are measured and discarded and it gives no root (a discarded tree).
Since b_j <= R0 - v = 2R_j - R_{j+1} - v (so also b_j <= R_j - 1), Lemma 3 gives failure
< 2^{b_j + R_{j+1} - 2R_j} <= 2^{-v} = eta for every attempt on two honest inputs, conditioned on any history.

Lemma 4 (expected counts; RB). Assume (F6) and work in the process U'' of Section 9, where every taken slot is
malformed w.p. <= epsilon' given the past (Lemma C1; pasts as in Section 2). For one Tree(P), from any history and ignoring
the cap Ctree (which only stops a tree earlier): the expected number of leaves built is <= (6/5) 2^D, the expected
number of merge attempts at child level j is <= (6/5) 2^{D-j-1} < 2^{D-j}, and the expected number of slots taken is
<= (5/2) m in the odd part and <= (5/4) m in the two-adic part. Consequently (Markov) a tree is discarded by the cap
Ctree w.p. < 1/25 in the odd part and < 1/50 in the two-adic part, given its history.
Proof. Let s0 be the expected number of slots per kept copy, from any history: s0 = 1 in the two-adic part; in the
odd part a taken slot is kept w.p. >= (1 - epsilon') 2^d/N > (1 - epsilon')/2 given the past (an honest label is
kept w.p. 2^d/N, Section 6), so s0 < 2/(1 - epsilon') < 2.003 (epsilon' <= 1/(63 m*) <= 1/882 as m* >= 2v + 2 >= 14).
Let g_j bound the expected number of slots needed to complete one level-j node, from any history; g_0 = s0 R0 (Wald).
A level-(j+1) node repeats attempts, each building two fresh level-j children (expected cost <= 2 g_j) and merging
them. An attempt fails w.p. < eta if both children are honest (Lemma 3, for any tables) and w.p. <= 1 otherwise; a
child is contaminated only if a malformed slot was taken while it was built, which has probability at most
epsilon' times the expected number of slots taken (Wald with Lemma C1). So, given the past, an attempt fails w.p.
<= p_j = eta + 2 epsilon' g_j, the expected number of attempts is <= 1/(1 - p_j), g_{j+1} <= 2 g_j/(1 - p_j), and the
expected number of level-j nodes built per level-(j+1) node is <= 2/(1 - p_j). Suppose g_i <= (6/5) 2^i g_0 for i < j.
Then sum_{i<j} 2 epsilon' g_i < (12/5) epsilon' 2^D g_0 = (12/5) epsilon' s0 m <= (12/5)(2.003)/63 < 0.077 (F6),
sum_{i<j} eta <= D/(16(D+1)) < 1/16 (F2'), every p_i <= 2^{-6} + 0.077 < 0.093 (v >= 6 as ell >= 3), and
prod_{i<j} (1 - p_i)^{-1} <= exp(sum_i p_i/(1 - max_i p_i)) <= exp(0.1395/0.907) < 1.17 < 6/5, which gives
g_j <= (6/5) 2^j g_0 and closes the induction. The same product bounds the counts: leaves <= 1.17 * 2^D, attempts at
child level j <= 1.17 * 2^{D-j-1}, slots <= 1.17 s0 m, i.e. <= 2.35 m (odd) and <= 1.17 m (two-adic). Markov:
Pr[slots >= Ctree] <= (5/2) m*/(64 m*) < 1/25, resp. (5/4)/64 < 1/50. []

Lemma 5 (space). Depth-first evaluation holds at most one finished register per level. At any time the
qubits in use are: held registers, sum_{j<D} R_j = D R0 <= (P/(R0 - v) + 1) R0 <= 2n + R0 (F1); and either one merge
(two inputs, p, A, B, lookup data and flag ancillas: <= 12 R_D qubits) or one leaf under assembly (<= R0 held
copies) plus one copy under extraction (control, n data qubits, one test ancilla and the P3 scratch of a
controlled modular addition, at most 4n + 12 qubits); plus O(1) qubits of a root. So, with the bank (RB), S_Q <= Qbank (n+1) + 6n + 13 R0 + 16
(copies in use are bank slots, so this counts them twice).
Classically: held tables <= sum_{j<D} 2^{R_j+1} Lambda = 2 D 2^{R0} Lambda bits, merge tables <= 2^{R0+6} Lambda.

Lemma 6a (phase blindness; RB). Fix Bad; ideal process. Let Gh be a set of honest slots whose extraction has ended
and none of which has been in a root whose qubit was measured in the X or Y basis. Conditioned on all labels and on
all outcomes so far, the law of the next measurement of the algorithm (a residue y, a block beta, a root index t, a
discard measurement, an extraction test of a slot not in Gh, a basis coin, or the X/Y measurement of a root without
a qubit of Gh) does not depend on the top bits T of the slots in Gh.
Proof. Purify the bad block and keep the purification in the analysis. Given its label, an honest slot is a product
state; its extraction tests act on its data register and fresh ancillas, leave it unchanged (Lemma 1), and are
independent of everything else; when its extraction ends, its control qubit is 2^{-1/2} sum_{a in {0,1}} e^{2 pi i a phi_g}|a>
with phi_g = k_g theta mod 1, in tensor product with the rest, and T_g enters only through phi_g. At every time the
joint pure state has the form
  [c sum over (a, z) in S of e^{2 pi i sum_g a_g phi_g} |sigma(a, z)> (x) |omega_z>] (x) |u>,   a in {0,1}^{Gh'},
where Gh' is the set of slots of Gh extracted so far and |u> is the product state (given the labels) of the slots of
Gh not yet extracted, which no operation has touched (bank slots are touched only when taken); z runs over
computational basis states of the other qubits of the registers that contain a qubit of Gh' (registers are tracked
logically: a merged register holds the qubits of both inputs); S is a set of pairs (a, z), c > 0, sigma is injective
on S into computational basis states of those registers, and the unnormalised omega_z live on everything else (other
registers, the other untaken slots, ancillas, the purification). S, c, sigma and the omega_z are determined by the
outcomes so far and do not depend on the phases phi_g (g in Gh): the slots of Gh outside Gh' sit in |u>, not in
the omega_z. This holds before the first slot of Gh is extracted (Gh' empty) and is preserved: the extraction of a
slot of Gh acts on its own factor of |u> and fresh ancillas, leaves that factor unchanged and has outcomes depending
on its label only; its control qubit then leaves |u> and adds a coordinate a_g (S becomes S x {0,1}, c becomes
c 2^{-1/2}); a permutation of
computational basis states of registers (lookups, XORs, adders, moves, fresh |0> ancillas, resets after a
measurement) changes sigma; a merge of a register holding a qubit of Gh' with another register moves the latter's
basis state into z (expand omega_z in that basis); every other operation (extraction of a slot not in Gh', coins,
the X/Y measurement of a root without a qubit of Gh') acts on the omega_z only. A computational-basis measurement of a
function f of the basis states of registers gives y with probability c^2 sum_{(a,z) in S: f(sigma(a,z)) = y} ||omega_z||^2
(cross terms vanish as sigma is injective) and restricts S to those pairs (c rescaled); a measurement on the omega
side with projector Pi has probability c^2 sum_{(a,z) in S} <omega_z|Pi|omega_z> and replaces each omega_z by Pi omega_z
(c rescaled). Both probabilities are free of the phases, and the form is kept. []

Lemma 6 (structural transcript; RB). Fix Bad; ideal process. Fix a tree and condition on the history H before it
starts (all classical data produced so far, including earlier records and votes). The tree's structural transcript
consists of the slots it takes (in order), the labels of its malformed slots, the low parts l and the parts h of
the labels of its honest slots, its rejection record (odd part: a trial is rejected iff bit d of its label is 1),
the outcomes of its computational-basis measurements (residues y, blocks beta, discards, the root index t), and all
classical choices (leaf composition, sorting with ties by index, block tests, retries, the tree cap, the final
entries x, y). It EXCLUDES the top bits T of its honest slots, the K tables, Delta, W and the root qubit's outcome Z.
Claim: conditioned on H and on the transcript, the top bits T of the tree's kept honest slots are i.i.d. fair bits.
Proof. Every honest slot the tree takes is untouched before, so its label is uniform given H and the choice of
the slot (Section 2), and for a kept label T is a fair bit independent of (l, h) (Sections 6 and 8: the odd-part acceptance reads bit d only, and a kept label is
uniform on [0, 2^d)). Every classical choice of the tree reads only L tables, malformed labels, rejection bits,
counters and earlier outcomes; and by Lemma 6a (Gh = the tree's honest slots extracted so far; none has been in a
measured root) the conditional law of each transcript measurement given the past and all labels does not depend on
the T bits of the tree's honest slots. The transcript excludes the extraction tests of the tree's honest slots:
given the labels they are independent of everything else, and the ideal process never reads them (it uses the true
label), so integrating them out changes no conditional law above. By induction over the steps, the conditional law
of the transcript given H and all labels does not depend on those T bits, and Bayes' rule gives the claim. []
What each decision reads (all from the structural transcript; none reads T, h, K, W or Z):
  acceptance of a copy ............ bit d of its label (odd part only; in the rejection record)
  leaf composition ................ the order of acceptance
  residues rho, rho' .............. L tables and P
  sort order, pos, start, size .... rho' (ties by index)
  measured residue y .............. law: |S_y|/(W1 W2), a function of rho, rho'
  off, G .......................... rho, y, sizes
  block beta, failure test ........ law: uniform idx on [0, |S_y|); test reads |S_y|
  retry ........................... the failure test
  root index t .................... law: uniform on [0, W_D/2)
  root entries x = 2t, y = 2t + 1 . t
  tree cap ........................ the tree's slot counter (RB); the global caps and the stage tree caps
                                    are absent in the process U'' analysed here (Section 9)
(RB) The laws in this table are those of honest registers; for a register with a malformed slot they are its Born
probabilities. The proof of Lemma 6 uses only Lemma 6a, which covers both.

## 5. Root and the unused top bits

Root(P): build Tree(P), MEASURE the top R_D - 1 qubits of the root register (outcome t; uniform for an honest root). The
remaining qubit is (e^{2 pi i K_x theta}|0> + e^{2 pi i K_y theta}|1>)/sqrt2 for the entries x = 2t, y = 2t + 1,
i.e. q_Delta(theta) with Delta = K_y - K_x up to a global phase. W_D is even, so the root never fails.

Labels in the analysis (Sections 6 and 8 instantiate this): every copy used by a tree has an integer label
k = l + F' T + 2F' h with 0 <= l < F' = 2^P, T in {0,1}, h >= 0; the tree uses only l (the stream of Lemma 6).

Lemma 7 (top bits; RB). In the process U'' of Section 9 (fixed Bad, ideal labels, order pi'): if a tree's root is
honest, then conditioned on H, the tree's structural transcript and all l's and h's of its slots, the top bits T of
the copies in the final tree are i.i.d. fair bits.
Proof. The index set I of the copies in the final tree is a function of the transcript; for an honest root every
copy in I is a kept honest slot of the tree. Apply Lemma 6. []

Lemma 8 (root frequency; for an honest root, RB). Let c = x^{(y)} - x^{(x)} in {-1,0,1}^m (nonzero by (I)) and h = |supp c| >= 1.
Then Delta = F' W with the integer W = De + sum_j c_j T_j + 2 sum_j c_j h_j, where De = (L_y - L_x)/F' is an
integer (P pinned bits). Conditioned as in Lemma 7, W minus a known integer equals sum_{supp c} c_j T_j, so
 (i) W mod 2 is a fair bit, and
 (ii) E e^{2 pi i W delta} = e^{2 pi i mu delta} cos(pi delta)^h for a real mu fixed by the conditioning and
     every real delta.
Proof. Expand Delta = sum c_j k_j. (i): sum_{supp c} T_j has fair parity. (ii): E e^{2 pi i c_j T_j delta}
= e^{pi i c_j delta} cos(pi delta) for c_j = +-1, and independence (Lemma 7). []
In the odd part every kept label is < 2F' (a classical test, also for malformed slots), so for EVERY root
|W| = |Delta|/F' < 2m <= q.

## 6. Odd part: r = s mod M (only if M > 1)

For stage j = 0..J let alpha_j be the unit with alpha_j == 2^j mod M and alpha_j == 1 mod 2^a (CRT by
extended Euclid), and compute alpha_j^{-1} mod N. Stage source: take a slot, extract its label, relabel it
to k = alpha_j^{-1} (label) mod N (Section 2); if k >= 2^d discard the copy and repeat (success probability
2^d/N > 1/2); otherwise l = k mod F, T = k >> (d-1), h = 0. A kept honest label is uniform
on [0, 2F), so l and T are independent and T is fair (P = P_o, F' = F).
Each stage collects Kstat records, one per non-discarded tree (RB: a stage that would start more than K+ trees
aborts the run): Root(P_o) on the stage source, W = Delta/F (exact division), a fresh fair
coin (measure H|0>) chooses the basis, measure X (H, then Z) or Y (S^dagger, H, then Z), record (W, basis, Z). The root qubit
is q_{FW}(theta_j) with theta_j = (alpha_j s mod N)/N, i.e. its phase is W phi_j with
phi_j = F alpha_j s/N mod 1 = f (alpha_j s mod M)/M mod 1 = 2^j vartheta, vartheta = f r/M mod 1.

Lemma 9 (known-frequency scores). For a record of an honest root (RB; (c) for every record) and u in [0,1) let S_u = 2Z cos(2 pi W u) (X) or 2Z sin(2 pi W u) (Y).
 (a) E[S_u | W] = cos(2 pi W (phi - u)); for the grid point u0 = k0/Mgrid nearest to phi, E S_{u0} >= 1 - 2^{-37}
     (|W| < q gives |2 pi W (phi - u0)| < pi/2^20).
 (b) If the circular distance of u from phi is >= 5/32 (RB), then E S_u <= cos(5 pi/32) < 0.8820, also conditionally
     on the history before the tree and the tree's structural transcript.
 (c) (RB) For ANY record let G be generated by everything before its basis coin (W included). Then
     E[S_u | G] = cos(2 pi W u) <X> + sin(2 pi W u) <Y>, where <X>, <Y> are the expectations of the X and Y outcomes
     of the root qubit's state given G, <X>^2 + <Y>^2 <= 1; so |E[S_u | F]| <= 1 for every sigma-field F contained in G.
Proof. (a) averaging the basis coin. (b) Lemma 8(ii) with delta the representative of phi - u in (-1/2, 1/2],
conditioned as in Lemma 7: E S_u = E[cos(2 pi mu delta) cos(pi delta)^h] <= cos(pi delta) <= cos(5 pi/32), since
0 <= cos(pi delta) <= 1 and h >= 1. (c) the coin is fresh, fair and independent of G: E[2Z cos(.) | G, X chosen] = 2 cos(.) <X>, etc.; then
Cauchy-Schwarz, and the tower property for F. []

Decoder. For iota in [0, Mgrid), integers C_iota, S_iota with |C_iota - 2^30 cos(2 pi iota/Mgrid)| <= 1 and
|S_iota - 2^30 sin(2 pi iota/Mgrid)| <= 1, computed on demand (no table is stored) as follows. Octant reduction: A = Mgrid/8 (an integer),
o = floor(8 iota/Mgrid) (by comparisons of 8 iota with multiples of Mgrid), rho_oct = iota - o A, iota' = rho_oct for even o and
A - rho_oct for odd o; with (cx, sx) = (cos x, sin x), x = 2 pi iota'/Mgrid in [0, pi/4], the pair (cos, sin)(2 pi iota/Mgrid) is
(cx, sx), (sx, cx), (-sx, cx), (-cx, sx), (-cx, -sx), (-sx, -cx), (sx, -cx), (cx, -sx) for o = 0, ..., 7 (rho_oct, cx, sx are local to the Decoder). Fixed-point values carry 128 fractional bits; every multiplication or division by an
integer or fixed-point value is rounded down (error <= 2^{-128} each); no factorial is stored.
 - pi^ = 16 A_5 - 4 A_239, A_c = sum_{k<40} (-1)^k p_k/(2k+1) with p_0 = 1/c, p_{k+1} = p_k/c^2 (all terms <= 1).
   Truncation < 2^{-190}; each p_k has error <= 2^{-127} and each term <= 2^{-126}, so |pi^ - pi| <= 20 * 40 * 2^{-126} + 2^{-188} < 2^{-115}.
 - y = iota'/Mgrid (one division, y in [0, 1/8]); x = 2 pi^ y in [0, pi/4 + 2^{-114}]; error of x <= 2^{-113}; x2 = x^2,
   error <= 2^{-111}.
 - cos: t_0 = 1, t_{k+1} = t_k x2/((2k+1)(2k+2)); sin: t_0 = x, t_{k+1} = t_k x2/((2k+2)(2k+3)); 24 terms with
   alternating signs. All t_k <= 1. The error e_k of t_k obeys e_{k+1} <= e_k/2 + 2^{-111} + 2^{-127}, so e_k < 2^{-109},
   and each sum has rounding error < 24 * 2^{-109} < 2^{-104}; truncation < 2^{-219}; the error of x adds <= 2^{-113}.
 - C_iota = round(2^30 cos^), S_iota = round(2^30 sin^): error <= 1/2 + 2^{30} 2^{-103} = 1/2 + 2^{-73}.
Every normalised fixed-point value has absolute value < 64. Cost per entry: 8 comparisons and one division of
<= 2 Lambda-bit words and <= 1024 operations (pi^ included) on <= 400-bit words, each <= 8 * 400^2 bit operations:
<= 2^{28} Lambda^2 bit operations in total (Lambda >= 256).
For each grid index k in increasing order compute Sigma_k = sum over the Kstat stored records of 2Z C_iota (X)
or 2Z S_iota (Y) with iota = (W k) mod Mgrid (kept per record and updated by adding W mod Mgrid as k increases),
computing each C_iota or S_iota on demand; keep only the best pair (k*, Sigma_{k*}) so far, replacing it only on
a strict increase. Output u^ = k*/Mgrid for the least maximiser k*. Sigma_k/(2^30 Kstat) differs from the empirical mean of S_{k/Mgrid} by <= 2^{-29}.
Lemma 10 (robust estimate; RB). In U'' (Section 9), except w.p. < 2^{-150}: every odd stage with at most Kstat/20
contaminated records has |u^ - phi_j|_circ < 5/32 (so on the event of Lemma C3 every stage has it).
Proof. Fix a stage; in U'' it has exactly Kstat records. For its k-th tree let E_k be generated by the history H_k
before the tree starts and the tree's structural transcript (Lemma 6), and let k_i be the tree of the i-th record;
{k_i = k} is in E_k (it is decided by which of trees 1..k are discarded). Let F_{i-1} be the sigma-field of the events
A whose intersection with {k_i = k} is in E_k for every k. Then F_{i-1} is contained in F_i (E_k is contained in H_{k'} for k < k'; F_{Kstat} is everything at the end of the stage), the
i-th record's score S_u^{(i)} is F_i-measurable, F_{i-1} is contained in the field G of Lemma 9(c) for that record, and
on {k_i = k}, E[S_u^{(i)} | F_{i-1}] is the conditional mean of tree k's score given E_k; whether the record is honest is F_{i-1}-measurable (Bad is fixed and
the transcript lists the slots taken). By Lemma 9(a), (b) (with Lemma 7), on {record i honest}
E[S_u^{(i)} | F_{i-1}] >= 1 - 2^{-37} at the grid point u0 nearest to phi_j and <= cos(5 pi/32) at every u with
|u - phi_j|_circ >= 5/32; for every record |E[S_u^{(i)} | F_{i-1}]| <= 1 (Lemma 9(c)). For fixed u,
X_i = S_u^{(i)} - E[S_u^{(i)} | F_{i-1}] is a martingale difference with |X_i| <= 3 and
E[X_i^2 | F_{i-1}] <= 4. Freedman's inequality gives Pr[|sum_i X_i| >= t Kstat] <= 2 exp(-t^2 Kstat/(8 + 2t)); with
t = 2^{-8} this is <= 2 e^{-2^{-20} Kstat} = 2 e^{-2^{12} hstat}. A union bound over the Mgrid grid points and the
J + 1 stages gives <= 2 (n+5) Mgrid e^{-2^{12} hstat} < 2^{-150} (hstat >= log2(Mgrid + 1) + log2(n + 7) + 20). On the
complement, in a stage whose fraction beta of contaminated records is <= 1/20, the normalised score (Decoder) of u0 is
>= (1 - beta)(1 - 2^{-37}) - beta - t - 2^{-29}, and that of every u at distance >= 5/32 is
<= (1 - beta) cos(5 pi/32) + beta + t + 2^{-29}; the difference is >= (19/20)(0.1179) - 1/10 - 2^{-7} - 2^{-28} > 0.004.
So the least maximiser is within 5/32 of phi_j. []
Unwrapping (as in Lemma 1 with e_dec = 5/32 (RB), which satisfies e + 2 e_dec <= 15/32 < 1/2 for e <= e_dec): G_J = u^_J; G_j = the closer of
G_{j+1}/2 and (G_{j+1}+1)/2 to u^_j (tie: the first); then |G_0 - vartheta|_circ < 2^{-J} 5/32 < 2^{-n-6}, so round(M G_0) mod M = f r mod M
(M <= 2^n), and the algorithm sets r := (round(M G_0) mod M) f^{-1} mod M.

## 7. Malformed slots: dominating marks, counts and contamination (RB)

Distinct roots use disjoint slots, so the contaminated roots (Section 3) of any period are at most the malformed
slots taken in it. Work in U'' (Section 9) for a fixed Bad; let G_{t-1} be generated by Bad, pi'(1..t-1), the
analysis coins U_1..U_{t-1} below and everything the run produces before it takes its t-th slot (slot t), keys and
stored order excluded (Section 2); G_0, G_1, ... is a filtration.

Lemma C1 (dominating marks). Let p_t = Pr[slot t is malformed | G_{t-1}]. Then p_t <= epsilon' for every t. Hence,
with fresh uniform U_t (analysis only), the marks c_t = 1 if slot t is malformed or U_t < (epsilon' - p_t)/(1 - p_t),
and c_t = 0 otherwise, satisfy Pr[c_t = 1 | G_{t-1}] = epsilon' with c_1..c_{t-1} G_{t-1}-measurable: they are i.i.d.
Bernoulli(epsilon'), c_t = 1 whenever slot t is malformed, and for every stopping time tau of (G_t) and integer s the
sum of c_{tau+1}..c_{tau+s} is Binomial(s, epsilon').
Proof. For t <= Qcap, by lazy exposure (Section 2; the U's are independent of the run) pi'(t) is uniform on the
Qbank - t + 1 untaken slots given G_{t-1}; so p_t = (|Bad| - b)/(Qbank - t + 1) <= epsilon Qbank/(Qbank - Qcap) = epsilon',
where b is the number of malformed slots among slots 1..t-1. For t > Qcap, U'' takes
fresh clean copies, so p_t = 0; if the run ends before slot t, put p_t = 0. []

Lemma C2 (counts). Assume (F6). In U'', except w.p. < 2^{-200}:
 (a) every odd stage reaches Kstat records within K+ trees, and (b) takes at most (11/4) Kstat m* slots;
 (c) every two-adic level reaches r_maj odd-W roots within 3 r_maj trees, and (d) takes at most 5 r_maj m* slots.
In particular no stage or level of U'' starts more trees than its stage tree cap.
Proof. Chernoff: if X is dominated by a Binomial with mean at most mu (its tail is increasing in the success
probability), then Pr[X >= (1 + delta) mu] <= exp(-delta^2 mu/(2 + delta)). Note Kstat >= 2^{36} and r_maj >= 2^{20}.
(a) A tree is discarded w.p. < 1/25 given its history (Lemma 4), so the discards among the first K+ trees of a stage
are dominated by Binomial(K+, 1/25), with mean < 0.0421 Kstat, while K+ - Kstat >= Kstat/20 - 1 >= 0.0499 Kstat
discards are needed to fail: probability <= exp(-0.00066 Kstat) <= exp(-2^{25}).
(b) For k = 1..K+ let Z_k be the number of slots taken by the k-th tree of the stage (0 if there is none). Given
everything before that tree, E Z_k <= (5/2) m* (Lemma 4) and 0 <= Z_k <= Ctree = 64 m*. By Azuma-Hoeffding,
sum_k (Z_k - E[Z_k | past]) >= Kstat m*/8 has probability <= exp(-2 (Kstat m*/8)^2/(K+ (64 m*)^2)) <= exp(-Kstat/137626)
<= exp(-2^{18}); otherwise sum_k Z_k <= (21/20)(5/2) Kstat m* + Kstat m*/8 = (11/4) Kstat m*, and on (a) the stage's
trees are among its first K+.
(c) A tree of a level yields an honest root with odd W w.p. > (1/2)(1 - 1/50 - (5/4)/63) > 0.48 given its history: it
is discarded w.p. < 1/50 (Lemma 4), contaminated w.p. <= epsilon' (5/4) m* <= (5/4)/63 (Wald with Lemma C1), and an
honest root's W is odd w.p. 1/2 given the history and its transcript (Lemmas 7, 8(i)). So the honest odd-W roots
among 3 r_maj trees dominate Binomial(3 r_maj, 0.48), and by Hoeffding they number < r_maj w.p.
<= exp(-6 r_maj (0.48 - 1/3)^2) < exp(-0.129 r_maj) <= exp(-2^{17}).
(d) As (b), on (c), with 3 r_maj trees and E Z_k <= (5/4) m*: the excess over (15/4) r_maj m* is >= (5/4) r_maj m* w.p.
<= exp(-2 (5/4)^2 r_maj^2/(3 r_maj 64^2)) = exp(-r_maj/3932.16) <= exp(-33 (ceil(log2(n+1)) + 8)).
As Kstat >= 2^32 (log2(n + 1) + 8) and r_maj >= 2^17 (log2(n + 1) + 8), each term above is at most
e^{-33 (log2(n+1) + 8)} < 2^{-300}/(n + 5), and a union bound over the n + 5 stages and n levels gives the claim. []

Lemma C3 (contamination). Assume (F6). In U'', on the event of Lemma C2 and except w.p. < 2^{-200}: every odd stage
has at most Kstat/20 contaminated records, and every two-adic level has at most (3/10) r_maj contaminated roots
among its r_maj counted (odd-W) roots.
Proof. The contaminated records of a stage are at most the malformed slots the stage takes, hence at most the marks
over its slots. On Lemma C2(b) these slots lie among the (11/4) Kstat m* slots after the start of the stage (a stopping
time), so by Lemma C1 the count is dominated by Binomial((11/4) Kstat m*, epsilon'), with mean
<= (11/4) Kstat/63 < 0.0437 Kstat (F6); exceeding Kstat/20 = (1 + delta) 0.0437 Kstat (delta > 0.144) has probability
<= exp(-0.00042 Kstat) <= exp(-2^{24}). In a level, the contaminated counted roots are at most the marks over its at
most 5 r_maj m* slots (Lemma C2(d)): mean <= 5 r_maj/63 < 0.0794 r_maj, and reaching (3/10) r_maj (delta > 2.77) has
probability <= exp(-0.127 r_maj) <= exp(-2^{17}). Each term is < 2^{-300}/(n + 5) as in Lemma C2; union over stages and
levels. []

## 8. Two-adic part: s = r + M u, u in [0, 2^a) (only if a >= 1)

For level l = 0..a-1 the low l bits t_low of u have been set; w = a - l, P = w - 1, s0 = r + M t_low. If r and
t_low are correct then s - s0 = M 2^l u' with u' = u >> l. Source: take a slot, extract k (no unit, no
rejection); low part k mod 2^{w-1}, T = bit w-1 of k, h = k >> w; for an honest slot these are independent and T is fair because
2^w | N (F' = 2^{w-1}). Repeat Root(P): it gives the qubit with phase Delta s/N = Delta s0/N + Delta u'/2^w and
Delta = 2^{w-1} W (Lemma 8). If W is even, measure the qubit in the computational basis and discard it. If W is odd, Delta u'/2^w == u'/2 ==
u'_0/2 mod 1, where u'_0 is bit l of u, so the phase is gamma + u'_0/2 with gamma = z/N, z = Delta s0 mod N.
Vote: o = floor(8z/N). If o in {0,3,4,7} measure X and let sigma = +1 for o in {0,7}, -1 for o in {3,4};
otherwise measure Y and let sigma = +1 for o in {1,2}, -1 for o in {5,6}. The vote is 0 if Z sigma = +1, else 1.
Stop after r_maj odd-W roots (RB: a discarded tree gives no root; a level that would start more than 3 r_maj
trees aborts the run); set bit l of u to the majority vote.
Lemma 11 (robust votes; RB). In U'', suppose r and bits 0..l-1 of u are correct. Conditioned on everything before
a vote of an HONEST root (including its gamma), the vote equals u'_0 w.p. (1 + |g|)/2 >= (1 + 2^{-1/2})/2 > 0.853,
where g = cos(2 pi gamma) (X) or sin(2 pi gamma) (Y), and |g| >= 2^{-1/2} on the chosen octants. Whether a root is
honest is known before its vote (Bad is fixed; the slots taken are recorded). Let Y_1, Y_2, ... indicate that the
honest counted votes of the level, in time order, are correct, continued by independent Bernoulli(0.853) indicators
(analysis only) if there are fewer than h0 = ceil((7/10) r_maj). Then Y_1 + ... + Y_h0 dominates Binomial(h0, 0.853), so
it is < (5/7) h0 w.p. <= e^{-2 h0 (0.853 - 5/7)^2} <= e^{-0.0269 r_maj}. Otherwise, on the events of Lemmas C2 and C3, at
most (3/10) r_maj of the r_maj counted votes are contaminated, so at least h0 are honest, all of Y_1..Y_h0 are real,
and at least (5/7) h0 >= r_maj/2 > (r_maj - 1)/2 counted votes are correct: the majority is correct. Bounding the first
wrong level: in total <= n e^{-0.0269 r_maj} < 2^{-1000}. Output s = r + M u. []

## 9. Accounting, caps and failure budget

Per-operation charge. Allocated bits and qubits S <= 2^{D* + R0* + 36} Lambda^2 + 4 Qbank Lambda at all times
(every register has width <= 2^{R_{D*}} <= 2^{D* + R0*}; Lemma 5, records Kstat (2 Lambda + 2) bits for the records
and their running iota, Mgrid <= 2^{22} m*; RB: the bank, Qbank (n+1) qubits, and its keys and order,
Qbank (kappa + Lambda) bits), so each gate, measurement, reset, classical bit operation or indexed access (at most
three addresses) costs at most 1 + 3 ceil(log2(S + 2)) <= 2 Lambda (RB: log2(S + 2) < k + 60 + 3 log2 Lambda by
Lemma 0, and 3k + 184 + 9 log2 Lambda <= 2 Lambda = 4n + 4k + 512).
Blocks and allowances. Each allowance bounds the charged cost of its block, including address charges, the
accumulator update and comparison below, and the generation of every gate by the controller. Gates are
streamed, never stored: the controller emits a gate as its type and at most three qubit addresses, computed
from loop counters and the table entry being read in at most 8 Lambda bit operations, each charged <= 2 Lambda.
So one gate costs at most 2 Lambda + 16 Lambda^2 <= 18 Lambda^2 in total; this is why the allowances carry Lambda^4.
  slot (take a slot, extraction Lemma 1, relabel, reset):      c_copy = 2^36 Lambda^4 H_lab,
  leaf (tables of one leaf from held copies):                  c_leaf = 2^20 Lambda^4 2^{R0},
  merge attempt at child level j (Lemma 2):                    c_j    = 2^20 Lambda^4 2^{R_{j+1}},
  root (index measurement, W, record or vote, z, octant):      c_root = 2^20 Lambda^4,
  decoder stage (Kstat Mgrid on-demand entries and updates):  c_est  = 2^30 Lambda^4 Mgrid Kstat,
  setup and finish (parameters, CRT, units and inverses,
    f^{-1} mod M, unwrapping, output):                          c_set  = 2^20 Lambda^4 (n + 5),
  bank (RB: acquire Qbank copies, Qbank kappa coins, sort):    c_bank = 2^12 Lambda^3 Qbank,
  cleanup (release everything; RB):                            c_cl   = 2^41 Lambda^4 2^{D* + R0*} + 2^7 Lambda^3 Qbank.
(Check: a merge attempt has <= 2^{R_j+14} Lambda gates (Lemma 2), at <= 18 Lambda^2 each, plus <= 2^{R_j+9} Lambda^2
bit operations at <= 2 Lambda each: <= 2^{R_j+19} Lambda^3 + 2^{R_j+10} Lambda^3 <= c_j. A copy has <= 2^{18} Lambda^2 H_lab
gates and <= 2^{13} Lambda^2 H_lab bit operations (Lemma 1), plus n + 1 for the acquisition: <= 2^{24} Lambda^4 H_lab.
A root needs O(1) products of 2 Lambda-bit words. A decoder stage needs Mgrid Kstat on-demand entries of
<= 2^{28} Lambda^2 bit operations each (Section 6) and <= 32 Lambda per score update:
<= 2^{29} Lambda^3 Mgrid Kstat + 64 Lambda^2 Mgrid Kstat <= c_est. Setup: each extended Euclid on words < 2^Lambda takes
<= 2 Lambda division steps of <= 16 Lambda^2 bit operations, so <= 2^6 Lambda^4 charged per Euclid and O(1) Euclids
and products per stage. Parameters: ell by one bit length (RB), v as the least v >= 4 with
2^v >= 16(ell+1), D = ceil(P/(R0 - v)) by one division, ceil(log2 .) by bit lengths, the caps as O(1) products:
O(n) word operations of <= 16 Lambda^2 bit operations each. Unwrapping is O(J) word operations. All within c_set.
Bank (RB): Qbank (n+1) acquisition units, Qbank kappa coin gates and as many measurements, and a merge sort of Qbank
records of kappa + Lambda <= 2 Lambda bits (<= 8 Qbank ceil(log2 Qbank) Lambda <= 8 Qbank Lambda^2 bit operations, Appendix P),
at <= 18 Lambda^2 per gate or measurement (fewer than 3 Lambda Qbank of them, as n + 1 + 2 kappa < 3 Lambda) and
<= 2 Lambda per bit operation: <= 54 Lambda^3 Qbank + 16 Lambda^3 Qbank <= c_bank. Cleanup (RB): at most S bits and qubits,
each released by one reset or measurement at <= 18 Lambda^2 < 2^5 Lambda^2: <= c_cl, and c_cl <= W*. Reading pi(t) and the tree and stage counters are inside c_copy
and c_root; the measure-and-discard of an abandoned tree (<= 13 R0 + 2n qubits) is inside c_root, charged once per tree. Bookkeeping: the recursion and retry control of a merge
attempt (O(1) counters of <= Lambda bits) is inside c_j; per two-adic level the update of s0, the schedule and the
majority count (O(1) word operations; n levels) are inside c_set; the basis coin and vote of a root are inside c_root.)
Control: the controller first runs the setup (deterministic, charged cost <= c_set; it computes all parameters,
caps and units), then the bank block (Section 2; deterministic cost <= c_bank), and sets A = c_set + c_bank, which
also reserves the finish (unwrapping, CRT, output). Afterwards, before a block starts, it adds the block's allowance
to the accumulator A and, before taking a slot, 1 to a slot counter; if A > Wcap or the counter > Qcap it runs
cleanup and outputs 0; the tree cap and the stage tree caps (Sections 4, 6, 8) are tested by counters in the same
way. (c_set + c_bank <= W* < Wcap, so setup and bank never abort. The process U'' of the analysis uses mathematical
counters; Lemma 0 concerns the algorithm.)
So on every branch Q = Qbank, at most Qcap slots are taken, and T <= Wcap + max allowance + c_cl.
The process U'' (RB). U'' is the ideal process for a fixed Bad (Lemma BF; ideal labels, Section 2; the uniform order
pi') without the two global tests (A > Wcap, slot counter > Qcap), in which every slot taken after the Qcap-th is a
fresh clean copy, and which has no stage tree caps: an odd stage runs until it has Kstat records, a two-adic level
until it has r_maj odd-W roots (analysis devices; U'' always completes every stage and level). Its tree cap is the
algorithm's. Until its slot counter first exceeds Qcap, its accumulator first exceeds Wcap or a stage or level first
starts more trees than its stage tree cap, U'' coincides with the ideal algorithm with order pi'.
Expected allowance in U''. Let R* = 2 (n + 5) Kstat + 3 n r_maj, which bounds the expected number of trees (below). By Lemma 4 the expected slots per tree are <= (5/2) m*, resp. (5/4) m*; the
expected number of trees is <= (25/24) Kstat per odd stage (discards < 1/25) and <= r_maj/0.48 < (21/10) r_maj per
two-adic level (Lemma C2(c)). Hence
  Q* = 3 m* ((n+5) Kstat + n r_maj)   >= the expected number of slots taken ((5/2)(25/24) < 3, (5/4)(21/10) < 3),
  W* = Q* c_copy + R* (2^{21} Lambda^4 (D* + 1) 2^{D* + R0*} + c_root) + (n + 5) c_est + c_set + c_bank,
since by Lemma 4 (RB) one tree's expected allowance is <= sum_{j<D} 2^{D-j} c_j + 2^{D+1} c_leaf
<= (2^{D+1} - 2) 2^{20} Lambda^4 2^{R0} + 2^{D+1} 2^{20} Lambda^4 2^{R0} <= 2^{21} Lambda^4 (D + 1) 2^{D+R0} for D >= 1;
for D = 0 the tree is one leaf, with allowance c_leaf <= 2^{21} Lambda^4 2^{R0}. The bound is increasing in D.
Hence E_{U''}[A] <= W* and E_{U''}[slots taken] <= Q*.
Asymptotics (F4', F5'), L = max(1, log2 n): for n >= 4096, ell = 46 ceil(log2 n) lies in [36L, 46L + 46), so
2^{D*} < 70368744177664n^46, D* + 1 = O(L), 2^v = O(L), R0 = ceil(n/ell) + v, and 2^{R0*} = O(L 2^{n/(46L)}); m* = O(n^47/L), Lambda = O(n), Mgrid = O(n^47/L);
hstat, H_lab, kappa, Kstat and r_maj are O(L); Q* = O(m* n L) = O(n^48). Thus Q = Qbank = O(n^48), S_Q = O(n^49), T = O(n^52 L + n^51 L^3 2^{n/(46L)}  + n^52 + n^51) = O(n^51 L^3 2^{n/(46L)}), and S_C = O(n L^2 2^{n/(46L)}  + n^49) = O(n L^2 2^{n/(46L)}). For n < 4096 all polynomial bounds hold after enlarging constants.


Failure budget (RB). Fix Bad (Lemma BF); it suffices to bound the failure probability for each Bad.
(1) The actual algorithm coincides with its ideal-label version except w.p. < 2^{-18} (Lemma 1).
(2) The ideal-label algorithm with the order pi coincides with the one with the order pi' except w.p. <= 2^{-41}
(ties, Section 2).
(3) The latter coincides with U'' until U'' first takes more than Qcap slots, its accumulator first exceeds Wcap,
or a stage or level first exceeds its stage tree cap; by Markov the first two have probability <= 2^{-11} each
(E_{U''} slots <= Q*, E_{U''} A <= W*), and the third is excluded by Lemma C2. (This also removes any dependence of
the abort decisions on the top bits.)
(4) In U'': Lemma C2 fails w.p. < 2^{-200} (this covers the stage tree caps), Lemma C3 w.p. < 2^{-200},
Lemma 10 w.p. < 2^{-150} and Lemma 11 w.p. < 2^{-1000}; on the complement, r and u are correct (Sections 6, 8).
Total < 2^{-18} + 2^{-41} + 2^{-10} + 2^{-149} < 2^{-9}: success > 0.99 for every Bad, hence under the adaptive model
(Lemma BF), including the clean problem (Bad empty).

## Appendix P: primitive circuits (exact, gate set of Section 0)
P1 (equality flag). flag ^= [x == e] for an l-qubit x and classical e: X on the zero bits of e, an AND of l qubits
by l - 1 Toffolis into l - 1 ancillas, CNOT to the flag, uncompute: <= 30(l - 1) + 2l + 1 <= 32 l gates.
P2 (lookup). For a classical table tau: [0, E) -> {0,1}^w, |x>|z> -> |x>|z XOR tau(x)> (identity for x >= E) is the
product over e < E of: P1 for e into a flag, CNOTs from the flag to the 1-bits of tau(e), P1 again. Cost
<= E (64 l + w) gates, l ancillas; an involution. Its emission reads each table entry once.
P3 (arithmetic, w-bit words). Ripple-carry addition mod 2^w (Cuccaro et al.): <= 40w gates, one ancilla.
Comparator g ^= [y < c] with a classical c: load c into a w-bit scratch by X gates, carry chain of the
subtraction y - c with one borrow ancilla, copy the borrow to g, uncompute, unload: <= 80 w gates.
Controlled modular addition y -> y + c mod N of a classical c < N on an n-bit y, controlled by a qubit ctrl,
identity when y >= N or ctrl = 0. Work on Y = (y, 0) with w = n + 1 bits, a w-bit scratch and flags g, h, t, e:
  1. g ^= [Y < N];  2. h ^= ctrl AND g;  3. load c into the scratch controlled by h, add it into Y, unload
  (now Y = y + c < 2N if h = 1);  4. e ^= [Y < N], t ^= h AND (NOT e), e ^= [Y < N];  5. load N controlled by t,
  subtract it from Y, unload (now Y = y + c - tN < N);  6. e ^= [Y < c], t ^= h AND e, e ^= [Y < c] (this clears t:
  if h = 1, t = 1 iff y + c >= N iff the new Y < c);  7. h ^= ctrl AND g (clears h; g is unchanged);
  8. g ^= [Y < N] (clears g: a valid y stays < N, an invalid y is untouched).
  Count: 6 comparators, 2 adders, 4 w controlled loads, 4 Toffolis and 2 X: <= 564 w + 70 <= 600 (n + 2) gates;
  ancillas <= 2n + 8.
Classical: w-bit addition/comparison <= 4w, multiplication/division <= 8w^2 bit operations; merge sort of E
records of w bits <= 4 E ceil(log2 E) w bit operations.


## Provenance and parameter record

Algorithm RB, the collimation sieve, decoder, primitive circuits, bank-first reduction, and adaptive-corruption analysis are inherited from the credited public DCP submissions identified in the proof's algorithm discussion. This entry restates their needed lemmas and specifies the changed parameter rule ell = 46 ceil(log2 n) for n >= 4096, with ell = 3 below. Its tolerated fraction is epsilon(n) = (log2 n)/(11837676818611 n^47). The depth-dependent bound m* <= 11837676818611n^47/log2 n implies epsilon m* <= 1/64.

Section 9 gives T = O(n^51 L^3 2^(n/(46L))), S_C = O(n L^2 2^(n/(46L))), S_Q = O(n^49), and Q = Qbank = O(n^48) jointly on every branch. The scalar growth-index score remains 1. This is an explicit parameter extension of RB, not a claim of a new core algorithm or a measured runtime improvement.
