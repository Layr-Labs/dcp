# Bank-first constant-depth collimation: DCP with malformed-copy tolerance 1/(1024 n) in 2^{n/5} poly(n) work

## 0. Theorem, error model and overview

Theorem. Fix N >= 2 and s in Z_N; n = ceil(log2 N); L = max(1, log2 n). Algorithm RB below, with the depth rule
ell = 5 (all parameters computed from N by integer arithmetic), acquires exactly Qbank copies, a number
fixed by N alone (Section 1). Under the adaptive malformed-copy model stated below with
  epsilon(n) = 1/(1024 n),
for every adversary of that model, including the one that corrupts nothing, it outputs the whole s with
unconditional probability > 0.99, and on EVERY branch it uses, with absolute constants, for all n >= 1:
  T   = O(n^5 L 2^{n/5}),   S_C = O(n 2^{n/5}),   S_Q = O(n^3 L),   Q = Qbank = O(n^2 L),
jointly for the same algorithm and configuration. The growth indices of these envelopes are 1, 1, 0, 0.

Error model (verbatim specification). Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

Overview. RB is a collimation sieve of constant width 2^{R0} and depth <= 5. It acquires all Qbank copies before any
measurement (Lemma BF) and uses them in a private uniformly random order, so each taken slot is malformed w.p.
<= epsilon' given the past (Lemma C1). A malformed slot spoils only its own root; honest roots have fair top bits
(Lemma 6). As epsilon m* <= 1/64, few records and votes are contaminated (Section 7), and the decoder (Lemma 9) and
the majority votes (Lemma 10) tolerate them.

Gate set: X, CNOT, Toffoli, H, S, S^dagger, with each Toffoli counted as 15 gates of its exact Clifford+T
circuit (7 T/T^dagger, 6 CNOT, 2 H); computational-basis measurement; fresh |0>. No other rotation, no QFT
over Z_N, no QRAM.

## 1. Parameters

d = floor(log2 N) (2^d <= N < 2^{d+1}, d >= 1); N = 2^a M with M odd. Depth rule ell = 5; v = 7 (the least v >= 4
with 2^v >= 16(ell + 1) = 96); R0 = max(ceil(n/5) + 7, 16); every register of a tree has width 2^{R0}; eta = 2^{-7}.
Schedule Sched(P), integer P >= 0: if P = 0, D = 0 (the tree is one leaf); if P >= 1, D = ceil(P/(R0 - 7)),
b_j = R0 - 7 for j <= D - 2 and b_{D-1} = P - (D-1)(R0 - 7), so 1 <= b_j <= R0 - 7 and sum_j b_j = P. m = 2^D R0.
(F1) If P <= n - 1 then D <= 5, as R0 - 7 >= ceil(n/5) and (n - 1)/ceil(n/5) < 5. D* and m* are D and m at
P* = max(n - 1, 0); every tree has P <= P*, so D <= D* <= 5 and m <= m*.
(F2) m* <= 16 n. If n <= 45: R0 = 16, D* = ceil((n - 1)/9), and D* = j >= 1 forces n >= 9j - 7 >= 2^j (j <= 5, and
the convex function 2^x - 9x + 7 is 0 at x = 1 and -6 at x = 5); so m* = 16 2^{D*} <= 16 n. If n >= 46:
R0 <= n/5 + 8 and D* <= 5, so m* <= 32 (n/5 + 8) < 16 n.
(F3) R0 <= max(n/5 + 8, 16), so 2^{R0} <= 2^8 max(2^{n/5}, 2^8). Word size: Lambda = 2(n + D* + R0) + 256.
Statistics: q = 2 m*, Mgrid = 2^20 (q + 1), hstat = ceil(log2(Mgrid + 1)) + ceil(log2(n + 7)) + 20, Kstat = 2^32 hstat,
J = n + 4, r_maj = 2^17 (ceil(log2(n + 1)) + 8) + 1 (odd), decoder accuracy e_dec = 5/32.
Odd part, used iff M > 1: P_o = d - 1, F = 2^{d-1}, f = 2^{d-1-a} (an integer: N >= 3 2^a gives d >= a + 1).
Two-adic part, used iff a >= 1. Initially r = 0 and u = 0.
Caps and bank (Section 9): tree cap Ctree = 64 m*; an odd stage starts at most K+ = floor(21 Kstat/20) trees, a
two-adic level at most 3 r_maj trees; Q* = 3 m* ((n+5) Kstat + n r_maj), W* (Section 9), Qcap = 2^11 Q*,
Wcap = 2^11 W*, Qbank = 2^11 Qcap = 2^22 Q*, key length kappa = 2 ceil(log2 Qbank) + 40; label tests
H_lab = ceil(log2(Qcap + 2)) + ceil(log2(n + 5)) + 14, F_lab = 512 H_lab. All are integers computed before the first
acquisition.
Tolerance: epsilon(n) = 1/(1024 n); by the model at most floor(epsilon Qbank) acquired copies are malformed.
epsilon' = epsilon/(1 - 2^{-11}).
(F4) epsilon m* <= 1/64 and epsilon' m* <= 1/63 (F2); epsilon' <= 1/1008 as m* >= 16.

Lemma 0 (words). Every integer the algorithm stores (table entries, labels, W, z, counters, caps, records, slot
indices, keys) has absolute value < 2^Lambda; products are formed in 2 Lambda-bit scratch words.
Proof. Put k = D* + R0, so m* <= 2^k. Table entries are sums of at most m* labels < 2N: < 2^{n + 1 + k}. By Section 1,
n + 5, hstat, H_lab and D* + 2 are < Lambda, r_maj < 2^18 Lambda, Mgrid <= 2^{k+22}, Kstat < 2^32 Lambda. So
Q* < 2^{k+34} Lambda^2, Qbank < 2^{k+56} Lambda^2, R* < 2^34 Lambda^2 (Section 9), and the five terms of W* (Section 9)
are < 2^{k+70} Lambda^7, 2^{k+56} Lambda^7, 2^{k+84} Lambda^6, 2^20 Lambda^5, 2^{k+68} Lambda^5: W* < 2^{k+85} Lambda^7.
Counters are <= Wcap + (largest allowance) <= 2 Wcap < 2^{k+97} Lambda^7, and k + 97 + 7 log2 Lambda < Lambda =
2n + 2k + 256 as 7 log2 Lambda < 159 + n + k. Slot indices are < Qbank; kappa < 2k + 154 + 4 log2 Lambda < Lambda.
The decoder's fixed-point values have 128 fractional bits and absolute value < 64; its integer operands
(c^2 <= 239^2, Taylor denominators, iota' 2^128, C_iota, S_iota) are < 2^Lambda (Section 6). []

## 2. Source copies and labels

Let chi_k = N^{-1/2} sum_y e^{2 pi i k y/N} |y>. Writing |x> in this basis and averaging over x:
  rho_s = (1/N) sum_k |phi_{k,s}><phi_{k,s}| (x) |chi_k><chi_k|,  phi_{k,s} = (|0> + e^{-2 pi i k s/N}|1>)/sqrt2
(cross terms k != k' vanish because sum_x e^{-2 pi i (k-k') x/N} = 0).

Bank and order. The first operation involving sources acquires all Qbank raw (n+1)-qubit copies into slots
1..Qbank, in this order. The algorithm makes NO measurement, private random draw, source transformation or abort
decision until the last copy has arrived (the setup before it is deterministic and reads no source). Then it draws
for every slot a kappa-bit key from kappa fresh fair coins (measure H|0>) and sorts the slots by (key, slot index);
pi(1), pi(2), ... is the resulting order. The t-th source call takes slot pi(t) ("takes a slot"); every "acquire a
copy" below means this.

Lemma BF (bank first). For this schedule every adversary of the model produces a mixture of fixed-position inputs: a set Bad of at most
floor(epsilon(n) Qbank) malformed slots, an arbitrary joint state of those slots (with a purification the algorithm
never accesses), and independent rho_s factors on all other slots, tensor-independent of the malformed subsystem;
Bad and its state may depend on N and s. So it suffices to prove the success bound for every fixed Bad.
Proof. Record each delivery's clean/malformed decision in a hidden classical register. The algorithm makes no
measurement and no private draw before the last delivery, so no algorithm outcome exists on which the decisions could
depend. By induction over j, conditioned on the decisions for deliveries 1..j, the unnormalised joint operator of the
delivered slots and the adversary's system is (tensor product of rho_s over the clean delivered slots) (x) (a positive
operator on the malformed delivered slots and the adversary's system): a private instrument of the adversary acts on
the second factor only; a malformed delivery moves a subsystem of the second factor into slot j; a clean delivery
appends a fresh rho_s in tensor product with everything, by the model's promise; summing over (countably many)
instrument outcomes preserves the form. After the last delivery trace out the adversary's system and condition on the
decision record: this is a finite convex mixture over sets Bad of states of the stated form, and the pathwise cap
gives |Bad| <= floor(epsilon Qbank). Every later operation acts on the bank and the algorithm's workspace, so the
output law is the same mixture of the output laws for fixed Bad. []

Ties. Two given slots get equal keys w.p. 2^{-kappa}, so some tie occurs w.p. <= Qbank^2 2^{-kappa-1} <= 2^{-41}. In the
analysis pi' sorts by key and breaks ties by an independent uniform order: pi' is a uniform permutation of the slots,
independent of the bank and of all other randomness, and pi' = pi unless a tie occurs.
Lazy exposure. The order is read only to take slots: before the run takes its t-th slot pi'(t), no operation depends on pi'(t), ..., pi'(Qbank). So, given
pi', the law of everything the run produces before taking slot t depends on pi' only through pi'(1..t-1); as pi' is
uniform and independent of the bank, Bayes' rule makes pi'(t) uniform on the untaken slots given Bad, pi'(1..t-1) and
all those data. Every history, past or sigma-field below (H, G_t, F_{i-1}, "given its history") is generated by Bad,
the taken slots, their labels and the run's other outcomes, coins and data, never by the keys or the untaken part of
the order.

Lemma 1 (label extraction). Let T_b|y> = |y + b mod N> for y < N, identity for N <= y < 2^n; T_b chi_k =
e^{-2 pi i k b/N} chi_k. On the data register of a copy, for j = 0..J, run F_lab tests in the X basis and F_lab in the
Y basis: prepare |+> = H|0>, apply T_{-2^j mod N} controlled by it (P3), apply H (X) or S^dagger then H (Y), measure
(+1/-1), reset. Let x_j, y_j be the two means; c_j = 1/8, 3/8, 5/8, 7/8 for (x_j >= 0, y_j >= 0), (< 0, >= 0),
(< 0, < 0), (>= 0, < 0); g_J = c_J and, for j = J-1..0, g_j = the one of g_{j+1}/2, (g_{j+1}+1)/2 circularly closer
to c_j (tie: the first); output k^ = round(N g_0) mod N (exact dyadic arithmetic). On input chi_k (any spectator),
k^ = k except w.p. <= 4(n+5) e^{-F_lab/512}; the eigenstate and spectators are unchanged.
Proof. Controlled T_{-2^j} maps |+>|chi_k> to (|0> + e^{2 pi i lambda_j}|1>)/sqrt2 |chi_k>, lambda_j = 2^j k/N mod 1,
so given k the tests are i.i.d. with means cos(2 pi lambda_j) (X) and sin(2 pi lambda_j) (Y), and act on chi_k by
phases only. By Hoeffding all 2(J+1) means are within 1/16 of their expectations except w.p. 4(J+1) e^{-F_lab/512}.
Then at most one of x_j, y_j has the wrong sign, and only if 2 pi lambda_j is within arcsin(1/16) of the axis where
that coordinate vanishes; so c_j is circularly within 1/8 + 0.01 = 0.135 of lambda_j. If g_{j+1} is within
e <= 0.135 of lambda_{j+1}, one candidate is within e/2 of lambda_j and the other is 1/2 away from it, and
e/2 + 0.135 < 1/2 - e/2 - 0.135 picks the right one: the error halves. So |g_0 - k/N|_circ <= 0.135 2^{-J} < 1/(2N). []
With F_lab = 512 H_lab and at most Qcap calls, all honest extractions are right except w.p. <= 4(n+5) Qcap e^{-H_lab} <=
2^{-12} (2/e)^{14} < 2^{-18} (as 2^{H_lab} >= 2^{14}(Qcap + 2)(n + 5) and H_lab >= 14). Cost per copy: 2(J+1) F_lab
tests of <= 600(n+2) + 5 gates (P3), <= 2^{18} Lambda^2 H_lab gates and measurements (n + 5 <= Lambda/2); classically
(constants -2^j mod N by doubling, counts, quadrant decoder, relabelling) <= 2^{13} Lambda^2 H_lab bit operations.
After extraction apply X to the control: it becomes q_k(s/N) = (|0> + e^{2 pi i k s/N}|1>)/sqrt2 up to a global phase;
the data register is reset. On a malformed slot the procedure outputs some k^ in [0, N) and leaves the control in some
state, possibly entangled with the rest of the bad block.
Ideal process. For a fixed Bad, measuring {|chi_k><chi_k|} on the data register of every honest slot right after the
bank is acquired changes no outcome law (rho_s is block diagonal in this basis, and every later operation on that
register is diagonal in it or discards it); each honest slot then has a classical label k, uniform on [0, N) and
independent of the other slots, the bad block, the order and all coins. The ideal process is the algorithm with each
honest extraction output replaced by k (same tests, same cost). Coupled on the same labels and outcomes, the two
agree, counters and outputs included, until the first honest extraction with k^ != k: except w.p. < 2^{-18}.
Sections 3-8 analyse the ideal process; a malformed slot's label is whatever its extraction outputs.
Units. For a known unit alpha mod N and a label k put k' = alpha^{-1} k mod N. As k s == k' (alpha s) mod N, the qubit
q_k(s/N) equals q_{k'}((alpha s mod N)/N): a copy with label k' for the secret alpha s mod N; k' is uniform on [0, N)
and independent of the history when k is. No quantum operation is needed.

## 3. Phase vectors and the merge

A register of width 2^R is a classical pair of integer tables (K_i, L_i), i in [0, 2^R), and the R-qubit state
2^{-R/2} sum_i e^{2 pi i K_i theta} |i> up to a global phase. Invariant (I): entry i corresponds to a binary incidence
vector x^{(i)} over the register's copies; distinct entries have distinct vectors; K_i = sum_j x_j k_j and
L_i = sum_j x_j l_j as UNREDUCED integers, where copy j has label k_j and low part l_j (Sections 6, 8). "P pinned bits"
means all L_i are congruent mod 2^P. Leaf: R0 copies, qubit e holding q_{k_e}(theta); width 2^{R0}, x^{(i)} = binary
digits of i (tables by doubling), 0 pinned bits.

Merge(A, B, P, b, W'), A = (K, L) of width W1 = 2^{R1}, B = (K', L') of width W2 = 2^{R2}, both with P pinned bits,
b >= 1, W' = 2^{R'} <= W1 W2. Let c = L_0 mod 2^P, c' = L'_0 mod 2^P, rho(i) = ((L_i - c)/2^P) mod 2^b,
rho'(j) = ((L'_j - c')/2^P) mod 2^b. Classically: stable sort of j by rho'(j) (ties by index); pos(j) = rank of j; for
each residue sigma < 2^b, start(sigma) and size(sigma) of its block (start = 0 if empty).
Quantum steps on |i>|j> (lookups are P2; tables are 0 at unused addresses):
 (a) Look up rho(i) into a b-qubit register A and rho'(j) into a b-qubit register B; add B into A mod 2^b; MEASURE A,
     outcome y; clear B by the same lookup; reset A using y. The state is uniform over
     S_y = {(i,j): rho(i) + rho'(j) == y mod 2^b} with unchanged phases. Classically compute
     off(i) = sum_{i'<i} size(y - rho(i')) and G(i) = off(i) - start(y - rho(i)).
 (b) Look up pos(j) into a fresh register p of R1 + R2 qubits; look up pos^{-1}(p) and XOR it into j, which becomes 0.
 (c) Look up G(i) (mod 2^{R1+R2}) into a scratch register, add it into p mod 2^{R1+R2}, clear the scratch by the same
     lookup. On S_y, p holds idx(i,j) = off(i) + pos(j) - start(y - rho(i)), a bijection S_y -> [0, |S_y|) (for fixed
     i it maps the partners of i onto [off(i), off(i+1))).
 (d) MEASURE the top R1 + R2 - R' qubits of p, outcome beta. If (beta + 1) W' > |S_y| the merge FAILS (all its registers
     are measured and discarded). Otherwise reset the measured qubits using beta; the low R' qubits hold t = idx - beta W'.
 (e) Look up I_beta(t) = (the i of the pair with index beta W' + t) and XOR it into i, which becomes 0 on the support.
Output: width W' on the t qubits, K''_t = K_{i(t)} + K'_{j(t)}, L''_t = L_{i(t)} + L'_{j(t)}, P + b pinned bits
(L_i + L'_j == c + c' + 2^P y mod 2^{P+b} on S_y). Each step is a permutation of basis states or a computational-basis
measurement, so the output state is exactly 2^{-R'/2} sum_t e^{2 pi i K''_t theta}|t> up to a global phase, and (I)
holds (an output entry is a pair of entries of registers on disjoint copies).

Lemma 2 (merge cost). For R1 = R2 = R' = R and b <= R - 1 (all merges below have R = R0), one attempt uses at most
2^{R+13}(R + 1) gates and measurements, 2^{R+9} Lambda^2 classical bit operations, O(R) scratch qubits and 2^{R+6} Lambda
classical bits.
Proof. Eight lookups over <= 2^{R+1} entries with index width <= 2R and data width <= 2R + 1, at most 2^{R+1}(130R + 1)
gates each by P2; two adders of width <= 2R (P3); <= 4R measurements and resets; <= 64(R + 1) operations for scratch
and failure discards. Classically: a sort of 2^R keys (P4) and the arrays start, size, pos, pos^{-1}, off, G, I_beta and
the output tables (scan r = beta W' .. (beta + 1) W' - 1, keeping the i with off(i) <= r < off(i) + size(y - rho(i)),
j = pos^{-1}(start(y - rho(i)) + r - off(i))), O(Lambda) bit operations per entry. []

Lemma 3 (yield). For ANY tables, Pr[merge fails] < 2^b W'/(W1 W2).
Proof. Magnitudes are uniform, so y has probability |S_y|/(W1 W2) and, given y, idx is uniform on [0, |S_y|); failure
means idx falls in the last, partial block, of size |S_y| mod W' < W'. Sum over the 2^b values of y. []
A register is contaminated if its copy set contains a malformed slot, honest otherwise. Tables and (I) are always as
stated; the quantum state, and hence Lemma 3, are claimed only for merges of two honest registers. A merge with a
contaminated input may fail with any probability; a failure discards both inputs.

## 4. The constant-width tree

Tree(P): a level-0 node is a leaf; a level-(j+1) node runs Merge(A, B, P_j, b_j, 2^{R0}) on two independently built
level-j nodes, P_j = b_0 + ... + b_{j-1}, and on failure builds two fresh level-j nodes and retries. Evaluation is
depth-first; the root has level D, width 2^{R0} and P pinned bits. Tree cap: a Tree(P) that has taken Ctree slots
(rejected trials included) and is not finished is abandoned (its registers are measured and discarded; no root).
As b_j <= R0 - 7, Lemma 3 gives failure < 2^{b_j - R0} <= eta for an attempt on two honest inputs, given any history.

Lemma 4 (expected counts). In the process U'' of Section 9 (each taken slot malformed w.p. <= epsilon' given the past,
Lemma C1), for one Tree(P), from any history and ignoring the cap Ctree: the expected numbers of leaves built and of
merge attempts at child level j are <= (6/5) 2^D and <= (6/5) 2^{D-j-1} < 2^{D-j}, and the expected number of slots taken
is <= (5/2) m (odd part), <= (5/4) m (two-adic part). So (Markov) the cap discards a tree w.p. < 1/25 (odd), < 1/50
(two-adic), given its history.
Proof. Expected slots per kept copy: s0 = 1 (two-adic); in the odd part a taken slot is kept w.p. >= (1 - epsilon') 2^d/N
> (1 - epsilon')/2 given the past (Section 6), so s0 < 2/(1 - epsilon') < 2.002 (F4). Let g_j bound the expected slots
to complete a level-j node from any history; g_0 = s0 R0 (Wald). Each attempt of a level-(j+1) node builds two fresh
level-j children (expected cost <= 2 g_j) and fails w.p. < eta if both are honest, w.p. <= 1 otherwise; a child is
contaminated only if a malformed slot was taken while it was built, w.p. <= epsilon' times the expected slots (Wald with
Lemma C1). So an attempt fails w.p. <= p_j = eta + 2 epsilon' g_j given the past, g_{j+1} <= 2 g_j/(1 - p_j), and a
level-(j+1) node builds <= 2/(1 - p_j) level-j nodes in expectation. If
g_i <= (6/5) 2^i g_0 for i < j, then sum_{i<j} 2 epsilon' g_i < (12/5) epsilon' s0 m <= (12/5)(2.002)/63 < 0.077 (F4),
sum_{i<j} eta <= 5/128 < 0.04, each p_i < 0.085, and prod_{i<j}(1 - p_i)^{-1} <= exp(sum_i p_i/(1 - max_i p_i)) <= exp(0.117/0.915) < 1.14 < 6/5, closing
the induction. The same product bounds leaves (<= 1.14 2^D), attempts (<= 1.14 2^{D-j-1}) and slots (<= 1.14 s0 m, i.e.
<= 2.29 m, resp. 1.14 m). Markov: (5/2) m*/(64 m*) < 1/25 and (5/4)/64 < 1/50. []

Lemma 5 (space). Depth-first evaluation holds at most one finished register per level. Qubits in use: held registers,
D R0 <= (P/(R0 - 7) + 1) R0 <= 2n + R0 (R0 >= 14); one merge (<= 12 R0 qubits with scratch) or one leaf under assembly (<= R0
copies) plus one copy under extraction (<= 4n + 12 qubits with test ancilla and P3 scratch); O(1) qubits of a root;
the bank. So S_Q <= Qbank (n+1) + 6n + 13 R0 + 16. Classically: held tables <= 2 D 2^{R0} Lambda bits, merge tables
<= 2^{R0+6} Lambda.

Lemma 6 (phase blindness). Fix Bad and work in U'' (Section 9: the ideal process without global and stage tree caps).
 (a) Let Gh be a set of honest slots whose extraction has ended, none of which has been in a root measured in the X or
     Y basis. Given all labels and all outcomes so far, the law of the next measurement (y, beta, t, a discard, an
     extraction test of a slot not in Gh, a basis coin, or the X/Y measurement of a root without a qubit of Gh) does
     not depend on the top bits T of Gh.
 (b) Fix a tree; let H be the history before it starts. Its structural transcript is: the slots it takes (in order),
     the labels of its malformed slots, the parts l and h of the labels of its honest slots, its rejection record
     (odd part: a trial is rejected iff bit d of its label is 1), its computational-basis outcomes (y, beta, discards,
     t) and its classical choices; it EXCLUDES the top bits T of its honest slots, the K tables, Delta, W and the root
     outcome Z. Given H and the transcript, the T bits of the tree's kept honest slots are i.i.d. fair bits.
 (c) If the root is honest, then given H and the transcript the T bits of the copies in the final tree are i.i.d. fair.
Proof. (a) Purify the bad block (analysis only). Given its label, an honest slot is a product state; its extraction
tests act on its data register and fresh ancillas, leave it unchanged (Lemma 1) and are independent of everything else;
afterwards its control qubit is 2^{-1/2} sum_{a in {0,1}} e^{2 pi i a phi_g}|a>, phi_g = k_g theta mod 1, in tensor
product with the rest, and T_g enters only through phi_g. At every time the joint pure state is
  [c sum_{(a, z) in S} e^{2 pi i sum_g a_g phi_g} |sigma(a, z)> (x) |omega_z>] (x) |u>,   a in {0,1}^{Gh'},
where Gh' is the set of slots of Gh extracted so far and |u> is the product state of the other slots of Gh, which no
operation has touched (bank slots are touched only when taken); z runs over basis states of the other qubits of the
registers holding a qubit of Gh' (a merged register holds the qubits of both inputs); c > 0; sigma is injective on S
into basis states of those registers; the unnormalised omega_z live on everything else (other registers, other untaken
slots, ancillas, the purification); and S, c, sigma, omega_z are determined by the outcomes so far, not by the phi_g.
This holds when Gh' is empty and is preserved: extracting a slot of Gh acts on its factor of |u> and fresh ancillas,
with outcomes depending on its label only, and adds a coordinate a_g (S -> S x {0,1}, c -> c 2^{-1/2}); a permutation
of basis states of registers (lookups, XORs, adders, moves, fresh ancillas, resets after a measurement) changes sigma;
merging a register holding a qubit of Gh' with another moves the latter's basis state into z; every other operation
acts on the omega_z only. A computational-basis measurement of a function f of register basis states gives y w.p.
c^2 sum_{(a,z) in S: f(sigma(a,z)) = y} ||omega_z||^2 (sigma is injective) and restricts S; a measurement on the omega
side with projector Pi has probability c^2 sum_{(a,z) in S} <omega_z|Pi|omega_z> and replaces omega_z by Pi omega_z (c
rescaled in both cases). Both laws are free of the phases, and the form is kept.
(b) Each honest slot the tree takes is untouched before, so its label is uniform given H and the choice of the slot
(Section 2); for a kept label T is fair and independent of (l, h) (Sections 6, 8). Every classical choice reads only
the transcript (acceptance: bit d; leaf composition: acceptance order; rho, rho', sort, pos, start, size, off, G:
L tables, P, y; failure test and retry: |S_y|; root entries x = 2t, y = 2t + 1: t; tree cap: the slot counter). By
(a), with Gh = the tree's honest slots extracted so far, the law of each transcript measurement given the past and all
labels is free of their T bits. Their extraction tests are outside the transcript: given the labels they are
independent of everything else and the ideal process ignores them, so integrating them out changes no law above. By
induction over the steps the law of the transcript given H and all labels is free of those T bits; Bayes' rule.
(c) The copies of the final tree are determined by the transcript and, for an honest root, are kept honest slots of
the tree; apply (b). []

## 5. Root and the unused top bits

Root(P): build Tree(P) and MEASURE the top R0 - 1 qubits of the root (outcome t). The remaining qubit is
(e^{2 pi i K_x theta}|0> + e^{2 pi i K_y theta}|1>)/sqrt2 for the entries x = 2t, y = 2t + 1, i.e. q_Delta(theta) with
Delta = K_y - K_x up to a global phase. The width is even, so a root never fails. Labels (instantiated in Sections 6
and 8): every copy used by a tree has label k = l + F' T + 2F' h with 0 <= l < F' = 2^P, T in {0,1}, h >= 0; the tree
uses only l.

Lemma 7 (root frequency of an honest root). Let c = x^{(y)} - x^{(x)} in {-1,0,1}^m (nonzero by (I)), h = |supp c| >= 1.
Then Delta = F' W with W = De + sum_j c_j T_j + 2 sum_j c_j h_j, De = (L_y - L_x)/F' an integer (P pinned bits). Given
the conditioning of Lemma 6(c), W minus a known integer is sum_{supp c} c_j T_j, so (i) W mod 2 is a fair bit, and
(ii) E e^{2 pi i W delta} = e^{2 pi i mu delta} cos(pi delta)^h for a real mu fixed by the conditioning and every real
delta, since E e^{2 pi i c_j T_j delta} = e^{pi i c_j delta} cos(pi delta) for c_j = +-1. []
In the odd part every kept label is < 2F' (a classical test, also for malformed slots), so for EVERY root
|W| = |Delta|/F' < 2m <= q.

## 6. Odd part: r = s mod M (only if M > 1)

For stage j = 0..J let alpha_j be the unit with alpha_j == 2^j mod M and alpha_j == 1 mod 2^a (CRT by extended Euclid);
compute alpha_j^{-1} mod N. Stage source: take a slot, extract its label, relabel it to k = alpha_j^{-1} (label) mod N
(Section 2); if k >= 2^d discard the copy and repeat; otherwise l = k mod F, T = k >> (d-1), h = 0 (P = P_o, F' = F). A
kept honest label is uniform on [0, 2F), so l and T are independent and T is fair; an honest slot is kept w.p.
2^d/N > 1/2.
Each stage collects Kstat records, one per non-discarded tree (a stage that would start more than K+ trees aborts the
run): Root(P_o) on the stage source, W = Delta/F (exact), a fresh fair coin (measure H|0>) chooses the basis, measure
X (H, then Z) or Y (S^dagger, H, then Z), record (W, basis, Z). The root qubit is q_{FW}(theta_j),
theta_j = (alpha_j s mod N)/N, i.e. its phase is W phi_j with phi_j = F alpha_j s/N mod 1 = f (alpha_j s mod M)/M mod 1
= 2^j vartheta, vartheta = f r/M mod 1.

Lemma 8 (scores). For a record and u in [0,1) let S_u = 2Z cos(2 pi W u) (X) or 2Z sin(2 pi W u) (Y).
 (a) For an honest root, E[S_u | W] = cos(2 pi W (phi - u)); at the grid point u0 = k0/Mgrid nearest to phi,
     E S_{u0} >= 1 - 2^{-37} (|W| < q gives |2 pi W (phi - u0)| < pi/2^20).
 (b) For an honest root and u at circular distance >= 5/32 from phi, E S_u <= cos(5 pi/32) < 0.8820, also given the
     history before the tree and its transcript.
 (c) For ANY record let G be generated by everything before its basis coin (W included). Then
     E[S_u | G] = cos(2 pi W u) <X> + sin(2 pi W u) <Y> with <X>, <Y> the X and Y expectations of the root qubit given
     G, <X>^2 + <Y>^2 <= 1; so |E[S_u | F]| <= 1 for every sigma-field F contained in G.
Proof. (a) Average over the coin. (b) Lemma 7(ii), conditioned as in Lemma 6(c), with delta the representative of phi - u in (-1/2, 1/2]:
E S_u = E[cos(2 pi mu delta) cos(pi delta)^h] <= cos(pi delta) <= cos(5 pi/32), as 0 <= cos(pi delta) <= 1, h >= 1.
(c) The coin is fresh, fair and independent of G; then Cauchy-Schwarz and the tower property. []

Decoder. For iota in [0, Mgrid), integers C_iota, S_iota within 1 of 2^30 cos(2 pi iota/Mgrid), 2^30 sin(2 pi iota/Mgrid)
are computed on demand (no table is stored). Octants: A = Mgrid/8 (an integer), o = floor(8 iota/Mgrid), r = iota - oA,
iota' = r (o even) or A - r (o odd); with (c, s) = (cos x, sin x), x = 2 pi iota'/Mgrid in [0, pi/4], the pair
(cos, sin)(2 pi iota/Mgrid) is (c, s), (s, c), (-s, c), (-c, s), (-c, -s), (-s, -c), (s, -c), (c, -s) for o = 0..7.
Fixed point with 128 fractional bits, each product or quotient rounded down (error <= 2^{-128}):
pi^ = 16 A_5 - 4 A_239, A_c = sum_{k<40} (-1)^k p_k/(2k+1), p_0 = 1/c, p_{k+1} = p_k/c^2 (terms <= 1, each with error
<= 2^{-126}; truncation < 2^{-190}), so |pi^ - pi| <= 800 2^{-126} + 2^{-188} < 2^{-115}; x = 2 pi^ (iota'/Mgrid) and
x2 = x^2 have errors <= 2^{-113} and 2^{-111}; cos x and sin x by 24 alternating Taylor terms t_0 = 1,
t_{k+1} = t_k x2/((2k+1)(2k+2)), resp. t_0 = x, t_{k+1} = t_k x2/((2k+2)(2k+3)), all <= 1, whose errors obey
e_{k+1} <= e_k/2 + 2^{-111} + 2^{-127}, so e_k < 2^{-109} and each sum is within 24 2^{-109} + 2^{-219} + 2^{-113}
< 2^{-103}; C_iota = round(2^30 cos^), S_iota = round(2^30 sin^), error <= 1/2 + 2^{-73}. All values are < 64 in
absolute value. Cost per entry: 8 comparisons and one division of <= 2 Lambda-bit words and <= 1024 operations on
<= 400-bit words (<= 8 400^2 bit operations each): <= 2^{28} Lambda^2 bit operations.
For each grid index k in increasing order compute Sigma_k = sum over the Kstat records of 2Z C_iota (X) or 2Z S_iota
(Y), iota = W k mod Mgrid (kept per record, updated by adding W mod Mgrid); keep only the best (k*, Sigma_{k*}),
replacing it on a strict increase. Output u^ = k*/Mgrid (least maximiser). Sigma_k/(2^30 Kstat) is within 2^{-29} of
the empirical mean of S_{k/Mgrid}.

Lemma 9 (robust estimate). In U'' (Section 9), except w.p. < 2^{-150}: every odd stage with at most Kstat/20
contaminated records has |u^ - phi_j|_circ < 5/32.
Proof. Fix a stage; in U'' it has exactly Kstat records. For its k-th tree let E_k be generated by the history H_k
before the tree and the tree's transcript (Lemma 6(b)); let k_i be the tree of the i-th record; {k_i = k} is in E_k
(it is decided by which of trees 1..k are discarded). Let F_{i-1} be the sigma-field of the events A whose
intersection with {k_i = k} is in E_k for every k. Then F_{i-1} is contained in F_i (E_k is contained in H_{k'} for k < k'; F_{Kstat}
is everything at the end of the stage) and in the field G of Lemma 8(c) for record i; S_u^{(i)} is F_i-measurable; on
{k_i = k}, E[S_u^{(i)} | F_{i-1}] is the conditional mean of tree k's score given E_k; and whether record i is honest
is F_{i-1}-measurable (Bad is fixed; the transcript lists the slots). By Lemma 8, on {record i honest}
E[S_u^{(i)} | F_{i-1}] >= 1 - 2^{-37} at u0 and <= cos(5 pi/32) at every u with |u - phi_j|_circ >= 5/32, and for every
record |E[S_u^{(i)} | F_{i-1}]| <= 1. For fixed u, X_i = S_u^{(i)} - E[S_u^{(i)} | F_{i-1}] are martingale differences
with |X_i| <= 3 and E[X_i^2 | F_{i-1}] <= 4; by Freedman, Pr[|sum_i X_i| >= t Kstat] <= 2 exp(-t^2 Kstat/(8 + 2t)), and
with t = 2^{-8} this is <= 2 e^{-2^{-20} Kstat} = 2 e^{-2^{12} hstat}. A union bound over the Mgrid grid points and J + 1 stages gives
<= 2 (n+5) Mgrid e^{-2^{12} hstat} < 2^{-150} (hstat >= log2(Mgrid + 1) + log2(n + 7) + 20). On the complement, if beta <= 1/20 of the stage's records are
contaminated, the normalised score of u0 is >= (1 - beta)(1 - 2^{-37}) - beta - t - 2^{-29} and that of every u at
distance >= 5/32 is <= (1 - beta) cos(5 pi/32) + beta + t + 2^{-29}; the difference is
>= (19/20)(0.1179) - 1/10 - 2^{-7} - 2^{-28} > 0.004, so the least maximiser is within 5/32 of phi_j. []
Unwrapping (as in Lemma 1; e + 2 e_dec <= 15/32 < 1/2 for e <= e_dec = 5/32): G_J = u^_J; G_j = the closer of
G_{j+1}/2 and (G_{j+1}+1)/2 to u^_j; then |G_0 - vartheta|_circ < 2^{-J} 5/32 < 2^{-n-6}, so round(M G_0) mod M = f r mod M
(M <= 2^n), and r = (f r) f^{-1} mod M.

## 7. Malformed slots: dominating marks, counts and contamination

Distinct roots use disjoint slots, so the contaminated roots of any period are at most the malformed slots taken in it.
Work in U'' (Section 9) for a fixed Bad; let G_{t-1} be generated by Bad, pi'(1..t-1), the analysis coins U_1..U_{t-1}
below and everything the run produces before it takes its t-th slot (slot t), keys and stored order excluded
(Section 2); G_0, G_1, ... is a filtration.

Lemma C1 (dominating marks). p_t = Pr[slot t is malformed | G_{t-1}] <= epsilon' for every t. Hence, with fresh uniform
U_t (analysis only), the marks c_t = 1 if slot t is malformed or U_t < (epsilon' - p_t)/(1 - p_t), c_t = 0 otherwise,
satisfy Pr[c_t = 1 | G_{t-1}] = epsilon' with c_1..c_{t-1} G_{t-1}-measurable: they are i.i.d. Bernoulli(epsilon'),
c_t = 1 whenever slot t is malformed, and for every stopping time tau of (G_t) and integer s, c_{tau+1} + ... + c_{tau+s}
is Binomial(s, epsilon').
Proof. For t <= Qcap, by lazy exposure (Section 2) pi'(t) is uniform on the Qbank - t + 1 untaken slots given G_{t-1},
so p_t = (|Bad| - b)/(Qbank - t + 1) <= epsilon Qbank/(Qbank - Qcap) = epsilon' (b = malformed slots among slots
1..t-1). For t > Qcap, U'' takes fresh clean copies: p_t = 0; if the run ends before slot t, put p_t = 0. []

Lemma C2 (counts). In U'', except w.p. < 2^{-200}: (a) every odd stage reaches Kstat records within K+ trees and
(b) takes at most (11/4) Kstat m* slots; (c) every two-adic level reaches r_maj odd-W roots within 3 r_maj trees and
(d) takes at most 5 r_maj m* slots. In particular no stage or level of U'' exceeds its stage tree cap.
Proof. Chernoff: if X is dominated by a Binomial with mean <= mu, Pr[X >= (1 + delta) mu] <= exp(-delta^2 mu/(2 + delta)).
Note Kstat >= 2^{36}.
(a) A tree is discarded w.p. < 1/25 given its history (Lemma 4), so the discards among the first K+ trees are dominated
by Binomial(K+, 1/25), mean < 0.0421 Kstat, while failure needs K+ - Kstat + 1 >= 0.0499 Kstat discards: probability
<= exp(-0.00066 Kstat).
(b) Let Z_k be the slots taken by the k-th tree of the stage (k <= K+; 0 if none). Given everything before it,
E Z_k <= (5/2) m* (Lemma 4) and 0 <= Z_k <= 64 m*. By Azuma-Hoeffding, sum_k (Z_k - E[Z_k | past]) >= Kstat m*/8 has
probability <= exp(-2 (Kstat m*/8)^2/(K+ (64 m*)^2)) <= exp(-Kstat/137626); otherwise sum_k Z_k <= (21/20)(5/2) Kstat m*
+ Kstat m*/8 = (11/4) Kstat m*, and on (a) the stage's trees are among its first K+.
(c) A tree of a level yields an honest odd-W root w.p. > (1/2)(1 - 1/50 - (5/4)/63) > 0.48 given its history (discard
< 1/50 by Lemma 4; contamination <= epsilon' (5/4) m* <= (5/4)/63 by Wald and Lemma C1; W odd w.p. 1/2 for an honest
root by Lemmas 6(c), 7(i)). So by Hoeffding fewer than r_maj of 3 r_maj trees give one w.p.
<= exp(-6 r_maj (0.48 - 1/3)^2) < exp(-0.129 r_maj).
(d) As (b), on (c), with 3 r_maj trees and E Z_k <= (5/4) m*: an excess >= (5/4) r_maj m* over (15/4) r_maj m* has
probability <= exp(-2 (5/4)^2 r_maj^2/(3 r_maj 64^2)) = exp(-r_maj/3932.16).
As Kstat >= 2^32 (log2(n + 1) + 8) and r_maj >= 2^17 (log2(n + 1) + 8), each of these bounds is
<= e^{-33 (log2(n+1) + 8)} < 2^{-300}/(n + 5); a union bound over the n + 5 stages and n levels gives the claim. []

Lemma C3 (contamination). In U'', on the event of Lemma C2 and except w.p. < 2^{-200}: every odd stage has at most
Kstat/20 contaminated records, and every two-adic level at most (3/10) r_maj contaminated roots among its r_maj counted
(odd-W) roots.
Proof. Let tau be the slot count at the start of a stage (a stopping time) and B = (11/4) Kstat m* (an integer, as
4 | Kstat). A stage's contaminated records are at most the marks over its slots, which on Lemma C2(b) lie among slots
tau + 1, ..., tau + B; so on C2(b) their number is at most the fixed-length window sum c_{tau+1} + ... + c_{tau+B}, which
by Lemma C1 is Binomial(B, epsilon') (no conditioning on C2(b)): mean <= (11/4) Kstat/63 < 0.0437 Kstat (F4), and
exceeding Kstat/20 (delta > 0.144) has probability <= exp(-0.00042 Kstat). Likewise, with tau the slot count at the
start of a level, its contaminated counted roots are on C2(d) at most c_{tau+1} + ... + c_{tau+5 r_maj m*}, Binomial with
mean <= 5 r_maj/63 < 0.0794 r_maj, and reaching (3/10) r_maj (delta > 2.77) has probability <= exp(-0.127 r_maj).
Each is < 2^{-300}/(n + 5) as in Lemma C2; union over stages and levels. []

## 8. Two-adic part: s = r + M u, u in [0, 2^a) (only if a >= 1)

For level l = 0..a-1 the low l bits t_low of u are set; w = a - l, P = w - 1, s0 = r + M t_low. If r and t_low are
correct then s - s0 = M 2^l u', u' = u >> l. Source: take a slot, extract k (no unit, no rejection); low part
k mod 2^{w-1}, T = bit w-1 of k, h = k >> w; for an honest slot these are independent and T is fair as 2^w | N
(F' = 2^{w-1}). Repeat Root(P): the qubit has phase Delta s/N = Delta s0/N + Delta u'/2^w, Delta = 2^{w-1} W (Lemma 7).
If W is even, measure the qubit in the computational basis and discard it. If W is odd, Delta u'/2^w == u'_0/2 mod 1,
u'_0 = bit l of u, so the phase is gamma + u'_0/2 with gamma = z/N, z = Delta s0 mod N. Vote: o = floor(8z/N); if
o in {0,3,4,7} measure X, sigma = +1 for o in {0,7} and -1 for o in {3,4}; otherwise measure Y, sigma = +1 for o in {1,2}
and -1 for o in {5,6}; the vote is 0 if Z sigma = +1, else 1. Stop after r_maj odd-W roots (a discarded tree gives no
root; a level that would start more than 3 r_maj trees aborts the run); bit l of u = the majority vote.

Lemma 10 (robust votes). In U'', suppose r and bits 0..l-1 of u are correct. Given everything before the vote of an
HONEST root (including gamma), the vote equals u'_0 w.p. (1 + |g|)/2 >= (1 + 2^{-1/2})/2 > 0.853, g = cos(2 pi gamma)
(X) or sin(2 pi gamma) (Y), as |g| >= 2^{-1/2} on the chosen octants. Whether a root is honest is known before its vote (Bad is fixed; the slots taken are
recorded).
Let Y_1, Y_2, ... indicate that the honest counted votes of the level, in time order, are correct, continued by
independent Bernoulli(0.853) indicators (analysis only) if there are fewer than h0 = ceil((7/10) r_maj). Then
Y_1 + ... + Y_h0 dominates Binomial(h0, 0.853) and is < (5/7) h0 w.p. <= e^{-2 h0 (0.853 - 5/7)^2} <= e^{-0.0269 r_maj}.
Otherwise, on the events of Lemmas C2 and C3, at least h0 of the r_maj counted votes are honest, all of Y_1..Y_h0 are
real, and at least (5/7) h0 >= r_maj/2 > (r_maj - 1)/2 counted votes are correct: the majority is correct. Over the
levels: <= n e^{-0.0269 r_maj} < 2^{-1000}. Output s = r + M u. []

## 9. Accounting, caps and failure budget

Charges. Allocated bits and qubits S <= 2^{D* + R0 + 36} Lambda^2 + 4 Qbank Lambda at all times (Lemma 5; Kstat records
of 2 Lambda + 2 bits with their running iota; the bank, Qbank (n+1) qubits, with keys and order, Qbank (kappa + Lambda)
bits). So each gate, measurement, reset, bit operation or indexed access (at most three addresses) costs at most
1 + 3 ceil(log2(S + 2)) <= 2 Lambda (with k = D* + R0, log2(S + 2) < k + 60 + 3 log2 Lambda by Lemma 0, and 3k + 184 + 9 log2 Lambda <=
2 Lambda = 4n + 4k + 512). Gates are streamed, never stored: the controller emits each as its type and at most three
addresses, computed in at most 8 Lambda bit operations; so a gate or measurement costs at most 18 Lambda^2 in all, and
a bit operation at most 2 Lambda.
Blocks and allowances (each bounds the charged cost of its block, including address charges, gate generation and the
accumulator update and test):

| block | allowance | why it suffices |
|---|---|---|
| slot: take, extract, relabel, reset | c_copy = 2^36 Lambda^4 H_lab | Lemma 1: 2^18 Lambda^2 H_lab gates, 2^13 Lambda^2 H_lab bit operations, n + 1 acquisition units |
| leaf (tables from held copies) | c_leaf = 2^20 Lambda^4 2^{R0} | 2^{R0+1} additions of Lambda-bit words |
| merge attempt (recursion and retry control included) | c_j = 2^20 Lambda^4 2^{R0} | Lemma 2: 2^{R0+14} Lambda gates and 2^{R0+9} Lambda^2 bit operations, <= 2^{R0+19} Lambda^3 + 2^{R0+10} Lambda^3 |
| root: index, W, coin, record or vote, z, octant; discards of an abandoned tree | c_root = 2^20 Lambda^4 | O(1) products of 2 Lambda-bit words; <= 13 R0 + 2n discarded qubits |
| decoder stage | c_est = 2^30 Lambda^4 Mgrid Kstat | Mgrid Kstat entries of 2^28 Lambda^2 bit operations and updates of 32 Lambda |
| setup and finish: parameters, CRT, units and inverses, f^{-1} mod M, unwrapping, two-adic updates, output | c_set = 2^20 Lambda^4 (n + 5) | O(1) extended Euclids (2 Lambda division steps of 16 Lambda^2 bit operations) and products per stage, O(n) other word operations |
| bank: acquisition, Qbank kappa coins, sort | c_bank = 2^12 Lambda^3 Qbank | < 3 Lambda Qbank gates and measurements (n + 1 + 2 kappa < 3 Lambda), sort of Qbank records of 2 Lambda bits (8 Qbank Lambda^2 bit operations, P4) |
| cleanup | c_cl = 2^41 Lambda^4 2^{D* + R0} + 2^7 Lambda^3 Qbank | at most S resets or measurements; c_cl <= W* |

Control. The controller runs the setup (deterministic, cost <= c_set) and the bank block (deterministic, cost
<= c_bank), sets A = c_set + c_bank (which also reserves the finish), and afterwards, before a block starts, adds its
allowance to the accumulator A and, before taking a slot, 1 to a slot counter; if A > Wcap or the counter > Qcap it
runs cleanup and outputs 0. The tree cap and the stage tree caps are tested by counters in the same way. As
c_set + c_bank <= W* < Wcap, setup and bank never abort. So on every branch Q = Qbank, at most Qcap slots are taken, and
T <= Wcap + max allowance + c_cl.
The process U''. U'' is the ideal process for a fixed Bad (ideal labels, order pi') without the global tests
(A > Wcap, counter > Qcap) and without stage tree caps (an odd stage runs until Kstat records, a level until r_maj odd-W
roots); every slot it takes after the Qcap-th is a fresh clean copy; its tree cap is the algorithm's. Until its slot
counter first exceeds Qcap, its accumulator first exceeds Wcap, or a stage or level first exceeds its stage tree cap,
U'' coincides with the ideal algorithm with order pi'.
Expectations in U''. The expected number of trees is <= (25/24) Kstat per odd stage (discards < 1/25) and
<= r_maj/0.48 < (21/10) r_maj per level (Lemma C2(c)), so at most R* = 2 (n + 5) Kstat + 3 n r_maj in all. By Lemma 4 a
tree takes <= (5/2) m*, resp. (5/4) m*, slots in expectation, and its expected leaf and merge allowance is <= sum_{j<D} 2^{D-j} c_j +
2^{D+1} c_leaf <= 2^{21} Lambda^4 (D + 1) 2^{D+R0}, increasing in D. Hence (Wald) the expected number of slots taken is
<= Q* ((5/2)(25/24) < 3, (5/4)(21/10) < 3) and E A <= W* with
  W* = Q* c_copy + R* (2^{21} Lambda^4 (D* + 1) 2^{D* + R0} + c_root) + (n + 5) c_est + c_set + c_bank.
Asymptotics (F1, F3): D* <= 5, 2^{R0} = O(2^{n/5}), m*, Lambda, Mgrid = O(n); hstat, H_lab, kappa, Kstat, r_maj = O(L)
with L = max(1, log2 n); Q* = O(n^2 L), R* = O(n L). So
  Q   = Qbank = 2^22 Q* = O(n^2 L),   S_Q <= Qbank (n+1) + O(n) = O(n^3 L)   (Lemma 5),
  T   = O(Q* Lambda^4 H_lab + R* Lambda^4 2^{R0} + n Lambda^4 Mgrid Kstat + Lambda^3 Qbank)
      = O(n^6 L^2 + n^5 L 2^{n/5} + n^6 L + n^5 L) = O(n^5 L 2^{n/5})   (n L <= C 2^{n/5} for all n),
  S_C = O(Lambda 2^{R0} + Kstat Lambda + Qbank (kappa + Lambda)) = O(n 2^{n/5} + n^3 L) = O(n 2^{n/5}).

Failure budget. Fix Bad (Lemma BF).
(1) The algorithm coincides with its ideal-label version except w.p. < 2^{-18} (Lemma 1).
(2) The order pi coincides with pi' except w.p. <= 2^{-41} (ties).
(3) The ideal algorithm with order pi' coincides with U'' until U'' first takes more than Qcap slots, its accumulator
first exceeds Wcap, or a stage or level first exceeds its stage tree cap; by Markov the first two have probability
<= 2^{-11} each (E slots <= Q*, E A <= W*), and the third is excluded by Lemma C2. (Thus phase blindness, Lemma 6, is
analysed in U'' without conditioning on the global or stage abort events; their probabilities are charged here.)
(4) In U'': Lemma C2 fails w.p. < 2^{-200}, Lemma C3 w.p. < 2^{-200}, Lemma 9 w.p. < 2^{-150}, Lemma 10 w.p.
< 2^{-1000}; on the complement r and u are correct (Sections 6, 8).
Total < 2^{-18} + 2^{-41} + 2^{-10} + 2^{-149} < 2^{-9}: success > 0.99 for every Bad, hence under the adaptive model
(Lemma BF), including the clean problem (Bad empty).

## Appendix P: primitive circuits (exact, gate set of Section 0)

| primitive | construction | cost |
|---|---|---|
| P1: flag ^= [x == e], x of l qubits, e classical | X on the zero bits of e; AND of l qubits by l - 1 Toffolis into l - 1 ancillas; CNOT to the flag; uncompute | <= 30(l - 1) + 2l + 1 <= 32 l gates |
| P2: lookup, z ^= tau(x) for tau: [0, E) -> {0,1}^w (identity for x >= E) | for each e < E: P1 for e into a flag, CNOTs from the flag to the 1-bits of tau(e), P1 again; an involution reading each entry once | <= E (64 l + w) gates, l ancillas |
| P3: adder mod 2^w | ripple-carry addition (Cuccaro et al.) | <= 40 w gates, one ancilla |
| P3: comparator g ^= [y < c], c classical | load c into a w-bit scratch by X gates, borrow chain of y - c with one ancilla, copy the borrow to g, uncompute, unload | <= 80 w gates |
| P3: y -> y + c mod N controlled by ctrl (c < N classical, y of n bits; identity if y >= N or ctrl = 0) | steps 1-8 below on Y = (y, 0), w = n + 1, a w-bit scratch and flags g, h, t, e | 6 comparators, 2 adders, 4w controlled loads, 4 Toffolis, 2 X: <= 600 (n + 2) gates, <= 2n + 8 ancillas |
| P4: classical | w-bit addition or comparison; multiplication or division; merge sort of E records of w bits | <= 4w; <= 8 w^2; <= 4 E ceil(log2 E) w bit operations |

Controlled modular addition: 1. g ^= [Y < N]; 2. h ^= ctrl AND g; 3. load c into the scratch controlled by h, add it into
Y, unload (Y = y + c < 2N if h = 1); 4. e ^= [Y < N], t ^= h AND (NOT e), e ^= [Y < N]; 5. load N controlled by t,
subtract it from Y, unload (Y = y + c - tN < N); 6. e ^= [Y < c], t ^= h AND e, e ^= [Y < c] (this clears t: if h = 1,
t = 1 iff y + c >= N iff the new Y < c); 7. h ^= ctrl AND g (clears h; g is unchanged); 8. g ^= [Y < N] (clears g: a
valid y stays < N, an invalid y is untouched).
