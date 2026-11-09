# Model X tolerance for PARTROOT196-E: one-time-pad label purification (the fifth claim)

## X.0 Provenance and what is new

The error model ("model X", coherent label steering) and the one-time-pad transformation
OTP (acquire-all, in-place swap shuffle, block merge with a one-time-pad label, robust finite
tester, Theorem B.4 and Lemmas B.1-B.3) are kshitij-hash's, from public submission
e5cb989c-2ea7-4a6f-b9db-edfaf0d14ab8 (OTP-LIMIT64-BANK-9999, `proof.md` Sections A and B),
which applies them to a different base algorithm (F-LIMIT64) at eps0 = 9999/10000. Everything
used is restated and re-proved below, so this file is self-contained; no step relies on that
submission's verdict.

New here: (1) the proof that PARTROOT196 (`virtual.md`, `proof.md`, byte-identical to public
submission 3315027c-4ec3-4352-80e5-f8f384e286f1) satisfies the label-first interface; (2) the
block parameters for the constant eps0 = 1 - 1/y^2 with y = 10^128 - 184; (3) the physical
realization inside PARTROOT196's counted bank and the resource accounting that ends at the
common bound of `virtual.md` (15.1), so that `envelope.md` Lemma E.3 applies unchanged.

References: "virtual k" is `virtual.md` Section k, "physical k" is `proof.md` Section k, "E.k" is
`envelope.md`, "X.k" is this file. P denotes PARTROOT196 as specified in virtual 0-13 and
realized by physical 0-11; P' = OTP(P) is the algorithm of this snapshot.

## X.1 Error model of the fifth structured claim (exact text)

Coherent label-steering model (model X) with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. An ideal copy is the (n+1)-qubit state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}|, psi_{x,s} = (|0,x> + |1,x+s>)/sqrt2, x in Z/NZ. Let V_s = span{psi_{x,s} : x in Z/NZ} (dimension N) and Pi_s its orthogonal projector, so rho_s = Pi_s/N. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy C is an (n+1)-qubit system supplied from the adversary's system whose support lies in V_s: conditioned on every outcome of every measurement made before its delivery (by the algorithm or the adversary), the joint state w of C and all other systems (the adversary's system and the other malformed copies, including copies the adversary delivers later) satisfies (Pi_s)_C w (Pi_s)_C = w. Apart from this a malformed copy is arbitrary: pure or mixed, entangled with the adversary's system and with other malformed copies, and dependent on all the information above. Equivalently, since V_s = span{phi_k(s) (x) chi_k : k in Z/NZ} with chi_k = N^(-1/2) sum_u exp(2 pi i k u/N)|u> and phi_k(s) = (|0> + exp(-2 pi i k s/N)|1>)/sqrt2, the adversary may steer the Fourier labels k coherently and arbitrarily while each label's coin qubit is exact. Examples: |+>|chi_0> (which lies in V_t for every t), phi_k(s)|chi_k> for chosen k, their superpositions and entangled versions, and any mixture of the psi_{x,s} (non-uniform or repeated source randomness x). Excluded: every state with support outside V_s, in particular coin dephasing, coin phase flips and Regev's registers |b,x>. At its delivery, and conditioned on all outcomes obtained before it, a malformed copy is in tensor product with clean copies, with the algorithm's workspace and with every qubit the algorithm prepares after its delivery (including the qubits that generate its random bits). Every copy that is not malformed is clean: at the moment of its delivery it is exactly rho_s in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace). The adversary's decision for copy j and the state it supplies as copy j are determined by N, s, the algorithm's description, its private system and the outcomes obtained before copy j is delivered; they do not depend on any random bit the algorithm generates after that delivery. Hence, for an algorithm that acquires all Q copies before it generates any random bit or obtains any measurement outcome that is not a fixed function of N, the set of malformed positions and the malformed contents are independent of all of its private randomness. The adversary interacts with the algorithm only by supplying copies; after delivery it cannot act on the copy or on the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

Remarks (not part of the text). (a) The psi_(x,s), x in Z/NZ, are an orthonormal basis of V_s,
so rho_s = Pi_s/N. (b) With |u> = N^(-1/2) sum_k omega^(-ku) chi_k (virtual 3),
psi_(x,t) = N^(-1/2) sum_k omega^(-kx) phi_k(t) (x) chi_k, a unitary change of basis, so
V_t = span{phi_k(t) (x) chi_k : k in Z/NZ}. (c) |+> (x) chi_0 = phi_0(t) (x) chi_0 lies in V_t for every
t; such copies pass every candidate of the finite tester of virtual 13, which is therefore
replaced (X.6). (d) If malformed copies C_1, ..., C_r each satisfy the support condition, their
joint state is invariant under Pi_s (x) ... (x) Pi_s, since the projectors act on different
systems. The support condition for C, and "clean copy in tensor product with everything else",
are preserved by every operation on other systems and by conditioning on their outcomes,
because these commute with (Pi_s)_C.

## X.2 PARTROOT196 is a label-first base

**Definition.** A LABEL-FIRST base is an algorithm A with a cap Qcap computed from N before its
first acquisition such that:
- (i) A makes at most Qcap acquisitions on every branch;
- (ii) each acquisition is followed at once by a transform, then by LE (virtual 5) on the data
  register, and A uses the copy in no other way. The transform is a unitary U on the copy
  register, chosen from A's past, with U V_t = V_(u(t)) for every t, for a known bijection u of
  Z/NZ. LE ends by resetting the data register. Afterwards A uses only the LE output k
  (classically) and the control qubit, the COIN;
- (iii) A's correctness is proved for its IDEAL run, in which each acquisition-transform-LE
  returns (k, coin) with k uniform on Z/NZ and independent of everything before it, and the coin
  exactly phi_k(u(s)), in tensor product with everything else; the actual run differs from the
  ideal run only through the LE coupling term.

**Lemma X.1.** The main branch (n >= 2^512) of P is label-first, with Qcap = 4 n C0 + K and
ideal failure probability at most deltaP = 2^-10 + 3*2^-40 + 2^-20 + 2^-128.

*Proof.* (i) Physical 2 and virtual 13 compute Qcap = 4nC0 + K before LE and before any
acquisition, and virtual 13 proves Q <= Qcap on EVERY branch.

(ii) Virtual 13 runs virtual 11 and then virtual 12; it states that dynamic compilation and
identity trials acquire no copies. Hence every acquisition is one of:
- the supplier of virtual 11: acquire, apply Mult_(alpha_j), run LE to obtain k, accept iff
  k < 2^dn (else discard the coin), and on acceptance apply X to the control;
- a leaf qubit of virtual 12 (both the wd = 1 case and the BATCH case): acquire, apply
  Shift_(sh_g), run LE, apply X to the control, and use kk = k mod 2^wd as the label.
PARTADAPT (virtual 7), BATCH, TREE (virtual 9) and the decoders (virtual 11-12) act only on
pool qubits, i.e. coins, and on classical labels. By (T1), Mult_alpha maps psi_(x,t) to
psi_(alpha x, alpha t), so U V_t = V_(alpha t); by (T2), Shift_c maps psi_(x,t) to psi_(x, t-c), so
U V_t = V_(t-c). Both bijections of Z/NZ are known. (Both transforms are the identity on encodings
>= N, which V_t does not involve.) LE resets the data register (virtual 5).

(iii) Virtual 3 (latent-label model) and the "probability-only ideal runs" paragraph of virtual 5
define the ideal run: every LE output is replaced by the latent label, which is uniform and
independent per copy, with coin phi_k(u(s)) in product with everything. Virtual 13 bounds the
failure probability by pool exhaustion 2^-10, yield abort 2^-40, supplier abort 2^-40, decoder
2^-20, 2-adic miss 2^-40, the identity-cap coupling 2^-128 and the LE coupling 2^-10. All terms
except the LE coupling are statements about the ideal run of P (the identity-cap coupling of
virtual 7.2 concerns pool qubits only). Their sum is deltaP. ∎

## X.3 Constants and block parameters

Let y = 10^128 - 184, aX = y^2 and eps0 = 1 - 1/aX = 1 - 1/y^2. Then aX < 10^256 < 2^851, and

    eps0^aX = (1 - 1/aX)^aX < e^(-1) < 1/2,                                        (X.1)

since 1 - x < e^(-x) for x > 0. On the main branch put

    LX = ceil(log2 Qcap),  wX = aX (LX + 12),  QX = wX Qcap,
    hX = ceil(log2(QX (n + 5))) + 12,  nbX = 2 ceil(log2 QX) + 20.                  (X.2)

By virtual 14, log2 Qcap = O(sqrt n); hence log2 QX <= 851 + log2(LX + 12) + log2 Qcap = O(sqrt n),
and LX, wX, QX, hX, nbX are O(n)-bit integers at all main lengths. LE_X denotes virtual 5's LE with
h_e replaced by hX and its test count by F_X = 2^21 hX. wX is the OTP block size.

## X.4 The algorithm P' on the main branch

1. ACQUIRE-ALL. Compute every parameter of physical 2 and (X.2) by exact deterministic integer
   arithmetic, initialize the bank prefix (physical 2, 4) and the store ST[0..QX-1] of QX
   registers of n+1 wires to zero, then acquire QX copies, in order, into ST[0], ..., ST[QX-1].
   Every operation before the last acquisition is a deterministic classical computation from N
   or an initialization of fresh wires; no random bit is drawn and no measurement is made whose
   outcome is not a fixed function of N.
2. SHUFFLE. For i = QX-1 down to 1: draw nbX fair bits (H on a fresh |0>, measure), with value R;
   put j = R mod (i+1); SWAP the registers ST[i] and ST[j] in place (3(n+1) CNOTs). The classical
   state is i, R, j; no permutation is stored.
3. RUN P. Run P (virtual 11-13, realized by physical 2-10) with one substitution: the v-th time P
   would acquire a copy, apply its transform U and run LE, P' runs BLOCK(v, U). For t = 0, ..., wX-1:
   take c_t = ST[v wX + t], apply U to it, and run LE_X on its data register, obtaining kh_t. If
   t = 0, the control of c_0 becomes the accumulator Acc and K := kh_0. If t >= 1, apply a CNOT
   from Acc to the control of c_t, measure that control in the computational basis with outcome
   sig_t, reset it, and put K := K + kh_t mod N if sig_t = 0 and K := K - kh_t mod N if sig_t = 1.
   BLOCK hands (K, Acc) to P as LE's output and the copy's control; P continues unchanged (accept
   rule, X on the control, pools, PARTADAPT, tree, decoders).
4. At the end, or at any ABORT, release the store.

P makes at most Qcap requests (X.2 (i)), so v < Qcap. BLOCK's classical state is v, t, K, kh_t,
sig_t. All randomness of P' (SHUFFLE bits, P's coins, PARTADAPT outcomes, every measurement)
arises after step 1.

## X.5 Sampling, purification and success on the main branch

Fix N, s and a model-X adversary with fraction eps0. Let B be the set of malformed acquisition
positions and Pm the SHUFFLE permutation (ST[p] holds the copy acquired at position Pm(p)). Let E
be the event that for every v < Qcap the block {Pm(v wX + t) : t < wX} contains a clean position.

**Lemma X.2 (sampling).** (a) Pm is within total variation 2^-20 of a uniform permutation that is
independent of B, the copies and the adversary. (b) If Pm is uniform and independent of B, then
Pr[not E] <= 2^-12.

*Proof.* (a) By step 1 and the timing clause of model X, B and all copies are determined by N, s,
the algorithm's description and the adversary's system. The fair bits come later from fresh
qubits in tensor product with every copy, so they are exactly fair and independent of all of
this. With R uniform on [0, 2^nbX), each value of j = R mod (i+1) has floor or ceiling of
2^nbX/(i+1) preimages, so the law of j is within total variation (i+1)/2^nbX of uniform on [0, i].
Swap Fisher-Yates with exactly uniform j gives a uniform permutation; coupling the j one by one,
the total variation is at most sum_(i=1)^(QX-1) (i+1)/2^nbX <= QX^2/2^nbX <= 2^-20.
(b) Block v is a uniform wX-subset of the QX positions, independent of B, and |B| <= eps0 QX. For
0 <= t < wX, (|B| - t)/(QX - t) <= |B|/QX <= eps0, so by (X.1)

    Pr[block v inside B] <= eps0^wX = (eps0^aX)^(LX+12) <= 2^-(LX+12) <= 2^-12/Qcap,

using 2^LX >= Qcap. A union bound over the Qcap blocks gives 2^-12. ∎

**Lemma X.3 (purification).** Condition on B and on a Pm in E. Consider the run in which each
LE_X output is replaced by the virtual label defined in (L1). In that run the joint law of P's
transcript (all of P's measurement outcomes, classical decisions and output) equals its law in
P's ideal run; conditional on any prefix of the transcript and on all OTP-internal records, the
state of P's registers equals the ideal-run state given the prefix, in tensor product with the
adversary's system, the store and those records.

*Proof.* (L1) Exact coin. LE_X acts on the data register only through ancilla-controlled
translations Tr_c, which are diagonal in the chi basis (Tr_c chi_k = omega^(-kc) chi_k, virtual 5),
then measures its ancillas and resets the data register. So a complete chi-basis measurement of
the data register inserted just before LE_X changes neither the joint law of all outcomes nor
the state of any other system; its outcome is the virtual label k_t. Given k_t, the data register
is chi_(k_t), and virtual 5 applies verbatim: LE_X returns k_t except with probability at most
4(n+5) 2^(-hX). If c_t is malformed, then by model X and remark (d) the joint state just before U
is supported on V_s (x) (rest); after U it is supported on V_(s') (x) (rest) with s' = u(s). By
remark (b) every vector there is sum_k phi_k(s') (x) chi_k (x) |e_k>, and projecting the data on
chi_k leaves phi_k(s') (x) chi_k (x) |e_k>. So given k_t = k the coin is exactly phi_k(s'), in
tensor product with every other system; the law of k_t is arbitrary. If c_t is clean, it is rho_s
in tensor product with everything, U gives rho_(s'), and by virtual (3.1) k_t is uniform and
independent of everything else, with coin phi_(k_t)(s').

(L2) Merge. phi_K (x) phi_k = (|00> + w^k |01> + w^K |10> + w^(K+k) |11>)/2 with w = omega^(-s').
After a CNOT from the first qubit to the second, the second qubit's outcome 0 leaves
(|0> + w^(K+k)|1>)/sqrt2 = phi_(K+k)(s') and outcome 1 leaves, up to a global phase,
(|0> + w^(K-k)|1>)/sqrt2 = phi_(K-k)(s'), each with probability exactly 1/2, independently of
K, k, s' and everything else. So, given its virtual labels and signs, BLOCK ends with Acc exactly
phi_K(s'), K = k_0 + sum_(t>=1) (-1)^(sig_t) k_t mod N.

(L3) One-time pad. The virtual-label measurements of a block act on data registers that nothing
else in the block touches, so they commute with the CNOTs and coin measurements and may be taken
first. On E, let t* be the first clean position of the block. By (L1), k_(t*) is uniform and
independent of the past, of the other labels of the block (whose joint law is arbitrary) and, by
(L2), of the signs. Given all of these, K = +-k_(t*) + c mod N with the sign and c fixed, a
bijective function of k_(t*), so K is uniform on Z/NZ. Hence, conditional on the whole past (P's
transcript, the adversary and all earlier OTP records), BLOCK returns K uniform and independent
of that past, with Acc exactly phi_K(s') in tensor product with everything else: the ideal return
of X.2 (iii). The other labels, signs and LE_X outcomes are records P never reads.

(L4) Induction over P's steps. P's own steps act only on P's registers and fresh ancillas, which
by induction are in the ideal-run state given the transcript prefix, in tensor product with the
rest; so their outcome laws are the ideal ones and depend neither on the OTP records nor on the
adversary. A BLOCK step is an ideal return by (L3). So the conditional law of each next transcript
entry, given the prefix and all hidden records, is the ideal one given the prefix; averaging over
the hidden records proves the lemma. ∎

Sigma-fields. P's proofs condition on sigma-fields of P's transcript: G of virtual 10 (which
already excludes LE's internal coins and outcomes), "the past of the stage" in virtual 11, and
"everything before" in virtual 6, 7 and 9. For P' these are generated by P's transcript alone:
the block labels K are P's leaf labels, and every BLOCK internal (individual labels, LE_X
outcomes, signs, SHUFFLE bits, B and Pm) is excluded, exactly as virtual 10 excludes LE scratch.
By Lemma X.3 every statement of P about the law of its ideal run holds for P' conditional on B
and on Pm in E, including the ideal-run failure bounds summed in deltaP.

**Theorem X.4 (main branch).** For every N with n >= 2^512, every s and every model-X adversary
with fraction eps0 (including the one that corrupts nothing), P' outputs s with probability at
least 1 - 2^-8.

*Proof.* The failure probability is at most: the SHUFFLE total variation 2^-20 and Pr[not E] <=
2^-12 (Lemma X.2); P's ideal-run failure on E, at most deltaP (Lemmas X.1, X.3); and the LE_X
coupling 4(n+5) QX 2^(-hX) <= 2^-10, since on E the actual run equals the virtual-label run unless
some LE_X call errs, and LE_X's bound holds given any virtual label. The total is
2^-20 + 2^-12 + 2^-10 + 3*2^-40 + 2^-20 + 2^-128 + 2^-10 < 2^-8. ∎

## X.6 Robust finite branch (n < 2^512)

Put wf = aX (2n + 15) and Qf = N (n + 10) wf. ACQUIRE-ALL Qf copies into a store of Qf registers
(after deterministic setup only), and SHUFFLE with nbf = 2 ceil(log2 Qf) + 20. Candidate
cand = 0, ..., N-1 owns the (n+10) wf registers ST[cand (n+10) wf + i], i < (n+10) wf. For each owned
register in turn apply Shift_cand and measure its control in X; reject cand at the first minus,
leaving its remaining registers unused. Output the first cand not rejected, or 0. The classical
state is cand, i and the SHUFFLE words, all O(n)-bit.

**Lemma X.5.** For every N >= 2 with n < 2^512, every s and every model-X adversary with fraction
eps0, this outputs s with probability at least 1 - 2^-10 - 2^-12 - 2^-20 > 1 - 2^-8.

*Proof.* s is never rejected: Shift_s maps V_s onto V_0 = |+> (x) span{|x>} (psi_(x,0) = |+>|x>),
so every copy, clean (rho_0 = |+><+| (x) I/N) or malformed (joint state supported on
|+> (x) C^N (x) rest), has control exactly |+>. For cand != s a clean copy becomes rho_d with
d = s - cand != 0; its control is I/2, because the off-diagonal term (1/(2N)) sum_x <x + d|x> is 0;
the copy is in tensor product with everything, so its outcome is a fair bit independent of all
other outcomes. Cut each candidate's registers into n+10 runs of wf consecutive registers; there
are N(n+10) <= 2^(2n+3) runs. As in Lemma X.2 with wf in place of wX, each run is inside B with
probability at most eps0^wf <= 2^-(2n+15) by (X.1), so some run holds no clean copy with
probability at most 2^-12 + 2^-20. Otherwise every wrong candidate meets at least n+10 clean
copies before it can survive, and survives only if all show plus: probability at most 2^-(n+10).
The output is wrong only if some cand < s survives: at most N 2^-(n+10) <= 2^-10. ∎

This replaces the finite tester of virtual 13 and physical 2. Lengths below 2^512 form a finite
set of N; every branch there has finite caps (at most Qf acquisitions, Qf(n+1) store wires), so
they change only absolute constants.

## X.7 Physical realization and resources

The counted-bank wrapper of physical 2-10 is run around P' instead of P, as follows.
- Store. ST is one fixed counted wire region of QX(n+1) wires placed after the rounded prefix of
  physical 4, initialized to zero together with the prefix and before any source request. It is
  touched only by gates, SWAPs, measurements and resets at classically known addresses (v, t, i,
  j are classical words), each paying the physical 9 address debit.
- ACQUIRE-ALL. Each acquisition uses the counted source register of physical 4 and three CNOTs
  per wire into ST[p], as physical 4 does for mapped source slots; the SWAP preserves any state
  exactly, malformed or clean.
- SHUFFLE draws fair bits on the reserved coin wire of physical 4 (H, measure, reset).
- BLOCK applies U and LE_X to store registers in place, with LE_X's ancillas allocated as P's LE
  scratch (physical 4). Its merge CNOT and measurement act on Acc and the control of c_t. At the
  end Acc is swapped (three CNOTs) into the mapped control slot that P's acquisition would have
  filled, and the n mapped data slots stay zero, which is P's state after its own LE (virtual 5
  resets the data register). K is written where P records LE's output.
- Classical state. v, t, K, kh_t, sig_t, i, R, j and the parameters (X.2) are constant many
  O(n)-bit staged words, which physical 8 allows; all long records stay counted basis qubits. So
  S_C = O(n) on every branch.
- Correctness. Physical 7 proves pi o Phi_physical = Phi_P o pi at aligned steps for an arbitrary
  reference R, by linearity. Take R to contain the adversary's system and every not-yet-used
  store register. The store operations are applied verbatim at known addresses, so the same
  identity holds with P' for P, and the reduced logical state and output law of the physical
  algorithm equal those of P'. Theorem X.4 and Lemma X.5 therefore hold for the physical
  algorithm.
- Source requests. Physical 10's one-for-one sentence is replaced by: every physical acquisition
  is one of the QX (main branch) or Qf (finite branch) acquisitions of ACQUIRE-ALL; P's original
  source requests are served by BLOCK from the store and make no acquisition.

**Theorem X.6 (resources).** On every execution branch, for all main lengths and an absolute
constant C_X,

    T, S_Q, Q <= C_X * 2^((2/sqrt3) sqrt n + 512 n^(7/16)),     S_C = O(n).

*Proof.* Samples: Q = QX = aX (LX + 12) Qcap exactly. Physical 10 and virtual 15 give
Qcap <= C n^3 2^u, so LX = O(u + log n) = O(sqrt n) and Q <= C aX n^4 2^u eventually.

Quantum space: S_Q(P') <= S_Q(P) + QX(n+1) + O(1) <= C n^88 2^u + C aX n^5 2^u <= C' n^88 2^u
(physical 8).

Time: the virtual work of P' is T_P plus, per store copy, one SWAP pass O(n), U O(n^2), LE_X
O(n^2 hX) = O(n^(5/2)) and an O(n)-bit addition, plus nbX fair bits, an O(n)-bit division and a
SWAP per SHUFFLE step, plus QX acquisitions with debit n+1. This adds O(n^(5/2) QX) = O(aX n^(13/2) 2^u)
core steps. Physical 9-10 charge every virtual action, including source transfers and the store
initialization, by the same n^160 allowance and keep the generation-count argument (all
quantities still have logarithm O(sqrt n)). Hence

    T_physical <= C n^160 (n^20 2^(u+16F) + aX n^(13/2) 2^u + n^88 2^u) <= C'' n^248 2^(u+16F),

the bound virtual 15 starts from. With u <= (2/sqrt3) sqrt n + 64 n^(7/16) (virtual 8.8),
u + 16F <= (2/sqrt3) sqrt n + 192 n^(7/16) (virtual 8.9) and 248 log2 n <= 248 n^(7/16), all three
are at most C_X 2^((2/sqrt3) sqrt n + 512 n^(7/16)). aX is an absolute integer, so C_X is absolute.
S_C = O(n) was shown above. ∎

Hence `envelope.md` Lemma E.3 and E.4, applied to P', give T, S_Q, Q = O(E(n)) and S_C = O(n)
jointly, with the finite branch absorbed into the constant.

## X.8 Tolerance integers and the fifth claim

Direct integer multiplication (also checked in Wolfram Language) gives

    y - 1 = 10^128 - 185 = 5335141990128885426609730276678720277683416502358554958365713865 * 1453784502951732741565122088722888544641192403053171515669467 * 12893
    y + 1 = 10^128 - 183 = 719055566230248251667422218800112619090393319415209063256198417 * 577059380141468332193372098822704305647887763344885788274559561 * 241
    y     = 10^128 - 184 = 5075877125918923237102883636467494305708529717425087531949658494 * 9850514257858070894700972904055977636084650030052055871926891182 * 2

(the factors need not be prime; each has at most 64 digits). Hence the supported expression of
the fifth claim, numerator the six factors of y - 1 and y + 1 and denominator the square of the
product of the three factors of y, equals (y - 1)(y + 1)/y^2 = 1 - 1/y^2 = eps0, a constant in
(0, 1) with normalized numerator and denominator of 256 digits.

**Fifth claim.** Under model X with fraction eps0 = 1 - 1/(10^128 - 184)^2: for every N >= 2 (no
threshold), every s and every model-X adversary, including the one that corrupts nothing (the
clean problem), P' outputs the entire s with probability at least 1 - 2^-8 > 1 - 2^-7 > 2/3
(Theorem X.4, Lemma X.5), and the four resource bounds of claims 0-3 hold on every execution
branch (Theorem X.6 with E.3-E.4). eps0 enters only through (X.1) and |B| <= eps0 Q.

Scope. Model X excludes every coin error (coin dephasing, phase flips, Regev's registers);
nothing is claimed under models admitting them. The tolerance comparison is meaningful only
against rows with the identical model X text.
