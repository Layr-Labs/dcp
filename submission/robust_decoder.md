# Clean wide-top coarse batch for NONPOWER-CUBE

Part of the SAME complete proof/algorithm as proof.md. All logs base2.
Parameters Cc64dl2m,Cf16dl2m,YceilLogCc,E8u,htopY+E12,PhtopY8,
Kc32768(P+u+100), bmaxfloor(H/2)-1024u, r=b+ceilLogn5, A4Lblk
are exactly proof0/8/13. Source promise is independent ideal copies.
Only the following ONE wide coarse batch is run; no adaptive coupling,
low-only verifier or chain controller from a material source is run.
All physical transforms/measurements/caps below are explicit and charged.

## F. One wide-top coarse batch

This section REPLACES the staged coarse bootstrap. Compute from N before
source access htop=Y+E+12,P=htop+Y+8 and
 Kc=32768(P+u+100).
These definitions are also used when the odd component is skipped,so the
raw source cap is fixed and padded. If M=1 put s1=0 without coarse roots.
Otherwise M>=3. Set h=min(htop,floor(log2M)),B=dn-h. In this main range
1<=h<=htop<=2m and B>=1. Since dn=a2+floor(log2M),B>=a2.
Compute gamma=2^(B-a2) modM and the CRT unit alpha with
 alpha=1 mod2^a2, gamma*alpha=1 modM.
Both exist by ordinary extended Euclid/CRT. Supply a qubit by applying
Mult_alpha,LE,accepting iff k<2^dn,and X on its control. Acceptance>1/2
and the accepted k is uniform on[0,2^dn)=[0,2^(B+h)). The ordinary
KNOWN-label one-qubit root of proof9,with cap Cc=64dl2^m,then has phase
 2pi*2^B W*alpha*s/N =2pi W*s1/M (mod2pi).
Here W is computed from its ordinary full high-part table. Here h=O(m); proof8 proves its actual fields fit the tapered memory
bound. There is no low-only verification kernel in this clean algorithm. Every selected supplier rejection and failed merge counts in Cc.

Run exactly Kc such capped roots at these FIXED parameters. On completion
measure a fresh fair X/Y basis,record(W,beta,Z) with Z=+1 or-1; missing
roots give scorezero. Reset ALL quantum work between roots. The expected
selected cost of an uncapped ideal root is<=6dl2^m,so missing probability
is<=3/32. The ordinary unused-top-label law proof10 still holds for this
larger h; its completed structural transcript G excludes the unused tau.

Dirichlet lemma. Conditional G and completion,write
 W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,
with independent uniform tau_v in{0,...,2^h-1},nonempty union,and all
coefficients +/-1. This is exactly the incidence-vector proof10,which
does not require h<=b0. For circular delta not an integer,put Lh=2^h.
The characteristic magnitude of one uniform tau is
 |sin(pi Lh delta)/(Lh sin(pi delta))|.
All other independent factors have magnitude<=1 and the cst contributes
only a phase. Therefore
 |E exp(2pi i delta W)|
  <=min(1,1/(Lh |sin(pi delta)|))
  <=min(1,1/(2Lh dist(delta,Z))).                 (F.1)
At integer delta use value1. These are finite geometric sums,not a
continuous-frequency oracle. Caps/completion inspect only low structural
bits and retain the top-label law. The supplier rejects only outside its
whole dyadic accepted interval,so accepted high labels remain uniform.

For a candidate theta' the ideal exact-trig score is Z*cs_beta(Wtheta')
on completion and0 on missing. Fresh fair beta averaging gives its mean
(1/2)E[1_complete cos(2pi W(theta-theta'))],where theta=s1/M.
The ACTUAL score uses proof4's rational tab_beta with error<1/625.
Concretely,LARGE candidate c contributes
 Z*tab_beta(((W*c) mod2^P)/2^P),
and SMALL candidate a contributesZ*tab_beta(((W*a) modM)/M).
Modulo is the least nonnegative residue,also for negative W; missing
records contribute0. Both are finite rational arguments in[0,1).
All candidates are streamed classically; frequencies and denominators
are known integers,so no unknown rotation or quantum memory lookup occurs.

LARGE odd component: floor(log2M)>=htop. Then h=htop. Enumerate ALL
candidates theta'=c/2^P,0<=c<2^P,scoring each by the Kc records. Choose
the smallest maximum and call its point z. There is a closest gridpoint
with distance<=2^(-P-1). Since |W|<=2^h Cc<=2^(h+Y),its phase error
is<=2pi/512<pi/128; its exact score mean is at least
 (1-3/32)*(1/2)cos(pi/128) >=28971/64000,
using cos(pi/128)>=999/1000 (the elementary bound with pi<22/7 suffices).
Any candidate at circular distance>=4/2^h has by F.1 characteristic
magnitude<=1/8,thus score mean<=1/16,which is certainly<=71/200.
This bound holds conditional on every G before averaging. If the good
score event below holds,the maximizing z satisfies
 dist(z,theta)<4/2^h=2^(-Y-E-10).
Set chat=floor(Mz+1/2) modM and the known rational
 R0=M2^(-Y-E-8)+1/2.
Then the true signed lift t0 congruent s1-chat modM satisfies |t0|<=R0.
Because M>=2^htop=2^(Y+E+12),R0>=1 andR0/M<=2^(-Y-E-7)<1/2.
This is the signed invariant used in proof11. Proceed to its sequential
Jtarget-bit odd data loop.

SMALL odd component: floor(log2M)<htop. Then h=floor(log2M)>=1,
Lh=2^h<=M<2Lh. Enumerate the EXACT candidates theta'=a/M,
0<=a<M,score each,choose the smallest maximizing a and return it as s1.
No odd controller is run. True mean is at least(1-3/32)/2=29/64.
For a false candidate,circular delta>=1/M>1/(2Lh). By the geometric-sum
formula and monotonic sine on[0,pi/2],
 |E exp(2pi i delta W)|<=1/[Lh sin(pi/(2Lh))]<=1/sqrt2<71/100.
Indeed Lh>=2,and sin(x)/x>=2sqrt2/pi on0<x<=pi/4,so the middle
reciprocal is<=1/sqrt2. The last strict rational bound follows from
10000<2*71². The false score mean is thus<=71/200. This treats all odd
M>=3,including M=3,h=1; B>=1 still follows from the MAIN input range.
The exact candidate grid has M<2^htop<=2^P points and is a finite loop.

Clean ideal-label score event. All Kc reference records are independent
fresh capped roots at FIXED parameters, including their fresh basis coins.
Each exact-trig score lies in[-1,1]. Hoeffding deviation1/64 has
probability<=2exp(-Kc/8192) per candidate. Since grid size<=2^P and
Kc/8192=4(P+u+100), the union bound is<2^-20. The near-versus-far
mean gap for both grids is at least6251/64000. Table error costs2/625
in normalized score pairs, and6251/64000>2/64+2/625. Thus actual
finite-table scores choose the correct SMALL secret or a LARGE centre
with the proved radius. All records exist before scoring and no later
copy is acquired based on any candidate score. These probabilities are
for the clean IDEAL-LABEL reference, not the physical run conditioned
on no LE error; proof13 couples the latter until its first label error.

