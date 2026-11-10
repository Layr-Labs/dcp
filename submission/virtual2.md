# Offset-aware logarithmic schedule

ell=H0=A=ceil(262087r/453948+(9843/873620)ceil(log2r)+64), v=ceil((14/15)ceil(log2r)), dl=A+v.

# Reference algorithm P, part2: chunks and constant-slack schedule

Sections7.3/8 give the current chunk and schedule proofs; cyclic-window
merges are reproduced in window_merge.md. IFC1 lineage1294d17f-2acf-4e10-9996-6b4375388f49
uses e-man07 MW433a6df9d-08d8-488b-a3f7-01f5f32373a4 and
CW1cfe82a87-0d65-454e-b1df-4789dc95aab4. Its window r,r' differ from
the global r=ceil(sqrt n); all labels are stored in full.

## 7.3 The chunked pool (P Section 7.3)

Sizes (Section 8): D_ell = C_ell and D_i = min(2^cb, ceil(RHO ell D_(i+1)/(ell - 1))) for i = ell-1, ..., 0;
YIELDS Yd_i = ceil((ell - 1) D_i/(RHO ell)); RUN CAPS Rc_ell = 1 and Rc_i = ceil(Rc_(i+1) D_(i+1)/Yd_i). Put
rho = RHO ell/(ell - 1), so D_i <= ceil(rho D_(i+1)) and D_i/Yd_i <= rho.

Each level i < ell keeps a BUFFER Bf_i, a list of labeled qubits, initially empty, and a counter of its runs.
REQUEST(i+1), for 0 <= i < ell, returns exactly D_(i+1) qubits:
- while |Bf_i| < D_(i+1): if level i has already run Rc_i times, ABORT; obtain an input chunk of D_i qubits, from the
  supplier if i = 0 (leaf qubits, Section 11) and by REQUEST(i) otherwise; run FWLEVEL on it with Cin = D_i,
  p = pp_i and c = pb_i (bucket_level.md); if its OUTPUT has fewer than Yd_i qubits, ABORT; otherwise append OUTPUT,
  in order of production, to Bf_i;
- remove the first D_(i+1) qubits of Bf_i and return them, in order.
The FINAL POOL is REQUEST(ell), so C_ell qubits. Then every qubit left in a buffer is measured, reset and released.

Lemma 7.3 (chunked pool). (a) Every run at level i has exactly D_i inputs, all collimated to pp_i, and satisfies the
hypotheses of Lemma 7.2; every returned qubit of REQUEST(i+1) is collimated to pp_(i+1).
(b) If no run yields fewer than its Yd_i, the run-cap ABORT does not occur: level i runs at most Rc_i times.
(c) At all times |Bf_i| < D_(i+1) + D_i/2, and P holds at most 3(ell + 1) 2^cb pool qubits.
(d) At most C_0 := Rc_0 D_0 leaf qubits are requested from the supplier, N_i := Rc_i D_i <= C_0 for every i, and
C_0 <= (ell + 1) rho^ell (C_ell + 1) <= 8 (ell + 1) RHO^ell C_ell.
Moreover C_0<=64 RHO^ell C_ell, with no factor ell.
(e) In the ideal outer run with the global key cap omitted, conditional
on everything before a run at level i, its yield ABORT probability is at
most2 exp(-C_ell/(10 ell^2 w^2)). Thus the batch's pool-yield ABORT
probability, excluding supplier/global-key failures, is at most
2(ell+1)C_0 exp(-C_ell/(10 ell^2 w^2)). Accepted seeds have the exact FW
law independently of private retries; actual global key failure is the
separate event bounded in seed_retry.md.


Proof. (a) A level0 chunk is collimated to pp_0=0; a higher chunk is
OUTPUT of lower runs, collimated to pp_i. Its fixed E_i=2^(pb_i) is at most
D_i/(4w ell) by pbmax_i, and D_i>=C_ell>=2^H>=4w ell by the size facts.
The work-conserving stopping condition supplies S_end<=(w-1)E_i directly,
so Lemma7.2 of bucket_level.md applies without a round-count condition.
Every returned good qubit is collimated to pp_(i+1). ell>=2.

(b) Induct downward. Level ell is requested once (Rc_ell = 1). Suppose level i + 1 runs (or, for i + 1 = ell, is requested)
at most Rc_(i+1) times, so level i receives at most R' <= Rc_(i+1) requests of D_(i+1). If level i runs R times, then
when its last run starts, the requests completed before the current one removed at most (R' - 1) D_(i+1) qubits, the
R - 1 earlier runs appended at least (R - 1) Yd_i, and the buffer held fewer than D_(i+1). So (R - 1) Yd_i < R' D_(i+1),
R <= ceil(R' D_(i+1)/Yd_i) <= Rc_i.
(c) A run appends at most D_i/2 qubits (Section 7.2: |OUTPUT| <= Cin/2) and starts only while |Bf_i| < D_(i+1). At
any time each level holds its buffer and at most one chunk in process (its LIVE and OUTPUT lists, at most D_i
qubits), and the final pool has C_ell <= 2^cb qubits; with D_i <= 2^cb the total is below
sum_i (D_(i+1) + D_i/2 + D_i) + C_ell <= 3 (ell + 1) 2^cb.
(d) The supplier serves at most Rc_0 chunks of D_0. N_(i-1) = ceil(N_i/Yd_(i-1)) D_(i-1) >= N_i D_(i-1)/Yd_(i-1) >= N_i,
so N_i <= N_0 = C_0; and N_(i-1) <= rho N_i + D_(i-1), with N_ell = C_ell. From D_i <= rho D_(i+1) + 1 and rho >= 2,
D_i + 1 <= rho (D_(i+1) + 1), so D_i <= rho^(ell-i) (C_ell + 1). Hence
C_0 <= rho^ell C_ell + sum_(i<ell) rho^i D_i <= (ell + 1) rho^ell (C_ell + 1), and rho^ell <= 4 RHO^ell
((1 - 1/ell)^(-ell) <= 4) and C_ell + 1 <= 2 C_ell.
For the sharper bound put L=2^cb. On every main-branch length,
2<=rho<=3 and L>=6: ell>=r/2, r>=2^20 and RHO=2+8/r
give the first bound, and (F1) gives the second. Before saturation, D_i=ceil(rho D_(i+1))
and Yd_i=ceil(D_i/rho)>=D_(i+1). Starting with Rc_ell=1, the new
ceiling recurrence therefore keeps Rc_i=1 at every unsaturated level.
If no level saturates then C_0=D_0<=rho^ell(C_ell+1)<=2rho^ell C_ell.
Otherwise let j be the largest saturated index, allowing j=ell.
All i<=j have D_i=L and Yd_i=Y=ceil(L/rho); put a_c=L/Y.
Since rho>=2, Y<=L/2+1<=2L/3, so 3/2<=a_c<=rho<=3.
At the first saturated level Rc_j<=ceil(a_c)<=3 (and Rc_ell=1
if j=ell). For i<j, Rc_i=ceil(a_c Rc_(i+1))<=a_c Rc_(i+1)+1.
Summing the geometric tail gives Rc_0<=a_c^j(Rc_j+1/(a_c-1))
<=5rho^j. Independently D_i+1<=rho(D_(i+1)+1), hence
L=D_j<=rho^(ell-j)(C_ell+1). Consequently C_0=Rc_0L
<=10rho^ell C_ell<=40RHO^ell C_ell<64RHO^ell C_ell.
This also covers a saturated final pool. The weaker bound above is
retained for size facts that already use it. The strengthened estimate
uses exact ceilings rather than spending one surplus run at each
integer equality; it does not rely on average supplier demand.
(e) Work in the ideal outer process omitting the key cap and private retry state.
Lemma7.2 with Cin=D_i holds conditional on the logical past for ANY labels; its yield event is
S < (ell - 1) D_i/(RHO ell), and S is an integer, so S < Yd_i is the same event. D_i >= C_ell, since D_i >= min(2^cb, 2 D_(i+1)).
Number the runs of level i in order; the k-th, if it occurs, aborts with conditional probability at most the stated
bound, and there are at most Rc_i runs before the first abort by (b). Summing over k <= Rc_i and i, with
sum_i Rc_i <= sum_i N_i <= (ell + 1) C_0, gives the batch bound. QED.

Fixed input sizes are the point of (e): each run's input count D_i is fixed by the schedule, not by the outcomes of the
level, so Lemma 7.2 applies verbatim to every run. The demand pattern (which runs occur, and when) depends on earlier
outcomes; the bound conditions on all of it.

### Geometric total input work

Every D_i>=C_ell>=6, rho>=2 and Yd_i=ceil(D_i/rho) imply
Yd_i<=D_i/2+1<=2D_i/3. Hence the fixed profile satisfies
N_i=Rc_iD_i>=N_(i+1)D_i/Yd_i>=(3/2)N_(i+1).
Therefore sum_(i<ell)N_i<=3C_0 per batch. Actual executed chunk inputs
are no greater than this fixed profile, including every abort branch.
Across at most5r batches sum Cin<=15rC_0. This is a deterministic count,
not an average-yield or independence assumption.

## 8. The schedule (P Section 8)

Parameters. RHO=2+8/r is the exact rational from Lemma K; q=w/2 and
w=2^ceil(log2 n). K retains (11.0), and the new pool budget is C_ell=2^8 K2^H dl.
The chunk sizes, yields and run caps are in Section 7.3, and Y=ceil(log2 C_0).
Each FWLEVEL stops when no key bucket has w records. For ell<=r,

    RHO^ell <= 64*2^ell.                                       (8.5)

Indeed (1+4/r)^ell<=exp(4)<64; exp(1)<11/4 and (11/4)^4<64 suffice. For completeness, sum terms through 1/3! in the exponential series and bound its tail by (1/24)/(1-1/5); the result is 261/96<11/4.
Put sig=209/181, d0=262087/453948, c=9843/873620, z=ceil(log2r),
A=ceil(d0 r+c z+64), e=2d0=262087/226974.
Set v=(14z+14)//15, ell=H0=A, dl=A+v. Compute A=(273880915r+5344749z+30834417899)//474375660 exactly.
Write l=log2r and A_*=d0 r+c l+64, so A_*<=A<=A_*+c+1.

Size facts(F1)-(F6), r>=2^20 and l=log2r:
(F1) n<=r^2, Lg<=2l+1, r0>=r-1,
 sig r-80l-43<=cb<=sig sqrt n-40log2n.
(F2) Lam=cb-24>=sig r-80l-67>=r/2,
 a=Lam-A-v>=(sig-d0)r-(81+c)l-(133+c)>=1.
(F3) H0-a=2A+v-Lam>=(2d0-sig)r+(2c+14/15)l+128>=4,
 2d0-sig=1/226974, H0<=H<=H0+1, dl+2<=Lam,
 2JI<=2A+v-Lam+1<=Lam-3,
 a+JI<=(Lam-v+1)/2<=sig r/2+1, a+JI+1<=r.
(F4) dl<=r, C_ell<=3*2^21 r^2 2^H,
 log2 C_ell<=H+2l+23<=d0 r+(c+3)l+c+95<=cb.
 Also0<cb-H<=ell and C_ell>=2^H>=4w ell.
(F5) dl>=r/2>=kappa+2, Lam>=kappa+2. Nonroot binary output
 exponent is at least dl, and nonroot four-input exponent is Lam.
(F6) The loose chunk bound gives
 log2 C_0<=log2(8(ell+1))+ell+6+log2 C_ell
 <=e r+(2c+4)l+2c+170<=2r-1. Hence Y<=2r<=n.
 Also w<=2n<=2r^2, q<=n and ell,dl<=r.

Every size comparison reduces to a positive linear term in r minus fixed
logarithmic terms and constants. It is positive at r=2^20 and remains so:
its derivative is positive, using ln2>1/2. The displayed formulas give
explicit sufficient endpoint checks, with no asymptotic distribution assumption.

Level capacities.
- FW level i (0 <= i < ell): pbmax_i is the largest integer b with 2^b * 4 w ell <= D_i.
- Phase A, binary, 0 <= i <= a-1: input exponent lam_i = dl + i, output exponent lam_(i+1) (so lam_a = Lam), capacity
  tbmax_i = dl + i - kappa - 1; as the ROOT of a binary tree (output exponent 1) level a - 1 has capacity
  rootA = 2 (dl + a - 1) - kappa - 1.
- Phase I, four-input, 0 <= j <= JI-1: input exponent Lam, fiber exponent l_j = Lam + 1 + 2j, r_j = 2 Lam - l_j =
  Lam - 1 - 2j; capacity bI_j = 2 Lam + 1 + 2j - kappa with output exponent Lam, or rootI_j = 3 Lam + 2j - kappa as
  the root (output exponent 1). These are substitutions: bI_j = r_j + (2 l_j - Lam - kappa), rootI_j = r_j + (2 l_j - 1 - kappa).

Put CP = sum_i pbmax_i, CA = sum_(i<a) tbmax_i, CA0 = sum_(i<a-1) tbmax_i + rootA, and for 1 <= JI' <= JI,
SI(JI') = sum_(j<JI'-1) bI_j + rootI_(JI'-1). Direct expansion gives SI(JI') = 2 Lam JI' + JI'^2 + Lam - kappa JI' - 1 and
SI(JI') - SI(JI'-1) = 2 Lam + 2 JI' - 1 - kappa <= 3 Lam for JI' >= 2.

For every binary level with b_i <= tbmax_i, and for the binary root with b <= rootA,

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.4)

Lemma 8.1 (capacity). For n >= 2^40: CP + CA + SI(JI) >= r^2 >= n, and CP >= 4 Lam.

Proof. Pool. Put beta=2z+19. Since K>=2^14r and dl>=r/2,
 C_ell=256K2^Hdl>=2^(H+21)r^2>=2^(H+beta).
The last inequality uses r>2^(z-1). The exact chunk recurrence gives
 D_i>=2^min(cb,H+beta+ell-i).
All main-branch lengths satisfy 0<cb-H-beta<ell by(F1)-(F4);
subtracting beta=O(logr) preserves the endpoint/monotonicity bounds.
With g=ceil(log2(4w ell))<=3l+4, integration of min(cb,H+beta+t)
gives CP>=ell cb-(cb-H-beta)^2/2-ell g.

Tree. CA=a dl+a^2/2-a(kappa+3/2), and SI(JI)>=2Lam JI+JI^2-kappa JI.
With a=Lam-dl, 2JI=H-a, U=H+dl, this implies

 CP+CA+SI(JI)>=F-[ell g+kappa(a+JI)+(3/2)a],
 F=ell cb-(cb-H-beta)^2/2+U^2/4+U Lam/2-Lam^2/4-dl^2/2.

Put x=80l+43,y=80l+67,A_*=d0 r+c l+64,beta_*=2l+19.
Use lower cb=sig r-x,Lam=sig r-y,H=ell=A_*,dl=A_*+(14/15)l,
beta=beta_*. On the box to actual values,
cb>=H+beta, cb<=H+beta+ell, U>=Lam, H+Lam>=dl.
The partial derivatives in cb,Lam,H,dl,ell,beta are respectively
ell-(cb-H-beta), (U-Lam)/2, (cb-H-beta)+(U+Lam)/2,
(U+Lam)/2-dl, cb, cb-H-beta; all nonnegative.
At the baseline exact simplification gives
 F=2A_*cb-cb^2/2+A_*Lam-Lam^2/4+(14/15)l Lam/2-(14/15)^2 l^2/4
 +beta_*(cb-A_*)-beta_*^2/2.
The r^2 coefficient is3d0 sig-3sig^2/4=1. The r l loss is paid exactly:
 3sig c+(7/15)sig+2(sig-d0)-80(3d0-3sig/2)-3d0=0.
Indeed ell g+kappa(a+JI)+(3/2)a is at most
 3d0 r l+[4d0+10sig+(3/2)(sig-d0)]r
 +(c l+c+65)(3l+4)+20.
The constant r margin after x,y and beta terms is
 M=192sig-43(2d0-sig)-67(d0-sig/2)+19(sig-d0)
   -4d0-10sig-(3/2)(sig-d0)=276sig-(349/2)d0>200.
The remaining loss is the positive quadratic
 R(l)=(2c l+128)x+(c l+64)y+x^2/2+y^2/4
 +(c l+c+65)(3l+4)+20+(7/15)l y+(49/225)l^2
 +(2l+19)(x+c l+64)+(2l+19)^2/2.
It is bounded coefficientwise by6000l^2+24000l+16000,
whose value at20 is below4*2^20. R'/R<=2/l<ln2 for l>=20,
so R(l)/2^l decreases. Capacity therefore exceeds r^2+196r.

For CP alone use ell,H>=r/2, cb>=sig r-x and cb<=sig r:
 ell cb-(cb-H-beta)^2/2
 >=[sig/2-(sig-1/2)^2/2-x/(2r)]r^2>r^2/3,
since x/r<=1/500. As ell g<=r(3l+4),4Lam<=5r and
r/3>=3l+9, this proves CP>=4Lam. All endpoint inequalities hold
at r=2^20 and persist by differentiation of linear-minus-log functions.

Bit allocation. Given an integer B with 1 <= B <= n, the TREE SHAPE and the bits are fixed as follows.
- If B <= CP + CA0, the tree is BINARY: Phase A levels 0, ..., a-1 with root a - 1 (output height a). Allocate exactly B
  bits greedily: first pb_0, ..., pb_(ell-1) in that order, pb_i = min(pbmax_i, bits still unallocated), then
  tb_(a-1) = min(rootA, still unallocated), then tb_(a-2), ..., tb_0 likewise with tbmax_i.
- Otherwise let JI' be the least integer in [1, JI] with CP + CA + SI(JI') >= B (it exists by Lemma 8.1). The tree is
  FULL: Phase A levels 0, ..., a-1 (none a root) and Phase I levels 0, ..., JI'-1 with root JI' - 1, output height
  a + 2 JI'. Phase I level j gets exactly bI_j bits for j < JI' - 1 and the root gets rootI_(JI'-1). The other
  B' = B - SI(JI') bits are allocated greedily to pb_0, ..., pb_(ell-1), then tb_(a-1), ..., tb_0 with tbmax_i.
  Here 0 <= B' <= CP + CA: the upper bound is the choice of JI'; for JI' = 1, B > CP + CA0 >= CP >= 4 Lam > SI(1); for
  JI' >= 2, minimality gives B > CP + CA + SI(JI' - 1) and SI(JI') - SI(JI' - 1) <= 3 Lam <= CP.
So every allocation exhausts B, every Phase I level is FULL, and every other level gets at most its capacity.
Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell, then the tree levels in order of height (Phase A levels
0, ..., a-1, then Phase I levels 0, ..., JI'-1), each starting where the previous ends. The last ends at B, so every bit
read below has position below B.

MERGE4I parameters. At Phase I level j put lam = Lam, l = l_j, r = r_j, r' = b_j - r_j and lam' = Lam (j < JI' - 1) or
1 (the root); since the level is full, r' = 2 l_j - lam' - kappa. The preconditions of Section A hold: Lam >= kappa + 2
(F5); Lam + 1 <= l_j <= 2 Lam, since 2j <= 2 JI - 2 <= Lam - 1 (F3); r_j = 2 Lam - l_j; lam' >= 1;
r' >= 2 (Lam + 1) - Lam - kappa >= 3 (F5); l_j >= kappa + 3. kappa here is the constant20 of Section0; failure bounds are CorollaryB.3, and
mu4 = 2^(lam' + kappa), Cp = 8 mu4 + 1 <= 2^(Lam + kappa + 4) = 2^cb.

## A and B. Cyclic-window merges and failure analysis

The complete current MERGE4I algorithm, failure identity and fresh-digit
bounds are in window_merge.md (P SectionsA/B). The original implicit-fiber
stream/listing construction is retained there with its credited lineage;
the cyclic-window completion and lower cutoff replace block truncation.
