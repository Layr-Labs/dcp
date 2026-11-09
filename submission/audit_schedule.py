"""Exact finite diagnostics only; mathematical proof and genuine review separate."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal as D,localcontext
import json
q=F(141421,100000);d0=F(100759,28284200000);tc=F(39999899241,28284200000)
assert q*d0+q*q/2==1 and d0+q==tc

def ceil(x):return -(-x.numerator//x.denominator)
def floor_sum(nn,mm,aa,bb=0):
 out=0
 while True:
  qa,aa=divmod(aa,mm);qb,bb=divmod(bb,mm)
  out+=qa*nn*(nn-1)//2+qb*nn;top=aa*nn+bb
  if top<mm:return out
  nn,bb=divmod(top,mm);aa,mm=mm,aa

def params(n):
 r=isqrt(n-1)+1;m=ceil(q*r);u=(n-1).bit_length();kap=(m-1).bit_length()+1
 ss=(2*kap+2)//3+2;base=ceil(d0*r);dl=base+ss;H=base+m-1;LL=m//(4*ss)
 h0=(2*m+2)//3+24*u;vv=m-h0;sig=(vv-1).bit_length()+2
 return r,m,u,kap,ss,base,dl,H,LL,h0,vv,sig
ns={2**e for e in [48,49,64,96,128,192,256,512,1024]}
for e in [48,49,64,96]:
 for off in [-1,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
for e in [24,32,64,128,256]:
 for off in [-1,0,1]:ns.add(((1<<e)+1)**2+off)
main=0
with localcontext() as ctx:
 ctx.prec=800;ln2=D(2).ln()
 for n in sorted(ns):
  r,m,u,kap,ss,base,dl,H,LL,h0,vv,sig=params(n)
  assert (r-1)**2<n<=r*r and q*r<=m<q*r+1
  assert kap>=8 and ss<=kap+1 and base>=kap+1 and base>=ss
  assert m>=8*ss*ss and LL>=2*ss and LL<=m-1 and dl<=2*base
  gw=(dl-1).bit_length();assert gw<=base-1 and m+gw<=H
  assert H<=tc*r+1 and 2*H<=3*r and 2*(m+1)<=3*r and (m+1)*H<=4*n
  AA=ss*LL-floor_sum(LL,LL,ss);assert 0<=AA<=m//4
  BB=(m+1)*base+m*(m-1)//2-1
  cap=BB+m*ss+ss-AA-kap*h0-2
  assert m>=288*u+12 and 4*h0<=3*m
  assert cap>=n and cap>=BB+F(7*m,4)-kap*(24*u+1)+ss-2
  assert BB>=r*r+(d0-q/2)*r-1
  W=base+h0+min(ss,(m-1-h0)*ss//LL)
  assert vv>=128 and W>=2*vv+2*sig+64*u and W>=2*u+1
  assert base+ss-1-kap>0 and 2*H-3>0
  Kc=8192*(m+10*u+100);Kp=8192*(u+100)
  assert Kc<=2**14*m and Kc*dl<=2**16*n
  cc=256*dl*(Kc+u+16);cp=256*dl*(Kp+u+16)
  YY=m+(cc-1).bit_length()
  assert cc<=2**25*n and YY<=m+u+26 and 2*YY<=n
  assert Kc//8192>=YY+u+30 and YY+6<=n
  qcoef=(YY+6)*cc+2*n*cp+Kp
  ll=D(n).ln()/ln2
  assert D(qcoef)<=D(2**50)*D(n)*D(n).sqrt()*ll
  FF=D(tc.numerator)/D(tc.denominator)*D(n).sqrt()
  assert D(H)<=FF+3
  assert D(ss)<=ll/3+D(17)/3 and m+dl==H+ss+1 and D(m+dl)<=FF+ll/3+10
  for ii in {0,1,h0-1,h0,h0+1,m-2,m-1}:
   kk=m-1-ii;la=base+ii+min(ss,kk*ss//LL)
   assert la<=dl+ii and la<=H-(kk+1)//2
  main+=1
print(json.dumps(dict(actual_hybrid_main_geometry_cases=main,all_main_geometry_passed=True)))
# Finite moderate schedules: compare direct integer sums and greedy budgets.
small=0
for m in [512,1024,2048,4096]:
 kap=(m-1).bit_length()+1;ss=(2*kap+2)//3+2;LL=m//(4*ss);h0=(2*m+2)//3+24
 if LL<2*ss:continue
 for base in [kap+2,3*kap+100]:
  dl=base+ss;H=base+m-1
  ls=[base+i+min(ss,(m-1-i)*ss//LL)for i in range(m)]+[1]
  cs=[2*ls[i-1]-ls[i]-(kap if i<=h0 else 2 if i==m else 0)for i in range(1,m+1)]
  AA=ss*LL-floor_sum(LL,LL,ss)
  exact=(m+1)*base+m*(m-1)//2-1+m*ss+ss-AA-kap*h0-2
  assert min(cs)>0 and sum(cs)==exact and ls[0]==dl and ls[-2]==H
  assert all(ls[i+1]-ls[i] in [0,1]for i in range(m-1))
  assert sum((m-1-i+4)*H*(1<<ls[i])for i in range(m))<=19*H*(1<<H)
  for B in {1,2,exact//2,exact-1,exact}:
   left=B
   for cc in reversed(cs):left-=min(left,cc)
   assert left==0;small+=1
print(json.dumps(dict(direct_hybrid_capacity_greedy_cases=small,all_direct_schedule_checks_passed=True)))
# New variable-width late margins. No fake linear-width assumption.
levels=0;roots=0
for vv in [128,129,192,256]:
 sig=(vv-1).bit_length()+2
 for uu in [1,2,8,48]:
  WW=2*vv+2*sig+64*uu
  for stride in [1,2,5]:
   ls=[WW+jj//stride for jj in range(vv)];Ms=[(1<<la)-(jj+1)*(1<<(la+jj-vv-sig))for jj,la in enumerate(ls)]
   assert all(F(7,8)<=F(Ms[jj],1<<ls[jj])<1 for jj in range(vv))
   total=F(0)
   for jj in range(1,vv):
    de=F(jj,1<<(vv+sig+1-jj));ze=F(1,1<<(vv+sig-jj));EE=1<<ls[jj]
    assert (1-de)**2*EE-Ms[jj]==(ze+de*de)*EE
    extra=F(2,1<<(ls[jj]//2))+F(2,EE)+4/(ze*ze*EE)
    ei=2*ze+2*de*de+extra;total+=ei;assert (ze+de*de)*EE>=2;levels+=1
   assert total<F(1,64)
   resid=2*vv*F(1,1<<(WW//2))+2*vv*F(1,1<<WW)+F(1<<(2*vv+2*sig+2),3*(1<<WW))
   assert resid<F(1,768)
   HH=ls[-1];bb=2*HH-3
   assert F(1<<(bb+1),Ms[-1]**2)<=F(16,49);roots+=1
print(json.dumps(dict(variable_width_late_margin_levels=levels,root_retention_cases=roots,all_late_margin_checks_passed=True)))
# Exact universal MGF/cap constants and conditional cost correlation toy.
assert 4*F(8,7)*F(32,31)*F(49,17)<16
assert F(16,27)**2<F(1,2) and F(4,3)<2
couplings=0
for cost,threshold in [(1,1),(3,2),(8,3)]:
 for uu in range(8):
  for high in [0,1]:
   failure=uu<threshold;upper=uu<3
   assert not failure or upper
   couplings+=1
 # Conditional failure varies with cost, but upper probability does not.
 assert sum(uu<threshold for uu in range(8))==threshold
 assert sum(uu<3 for uu in range(8))==3
assert F(1,8)!=F(3,8)
for RR in [1,2,17,8192]:
 for uu in [1,2,48,128]:
  assert (16*RR-64*(RR+uu+16))*1<=-64*(uu+16)
  assert 64*(RR+uu+16)>=2*(uu+12)
print(json.dumps(dict(low_cost_correlated_coupling_cases=couplings,uniform_MGF_and_tail_constants_passed=True)))
meta=json.loads(Path(__file__).with_name('submission.json').read_text())
assert meta['claims'][0]['structured']['bound']['nPower']=='10/3'
assert meta['claims'][0]['structured']['bound']['logPower']=='0'
assert meta['claims'][4]['structured']['expression']=='0'
for c in meta['claims']:assert c['evidence']==['proof.md','nonpower_merge.md']
print(json.dumps(dict(all_hybrid_checks_passed=True,proof_and_genuine_review_still_required=True)))

# Reused finite checks for the identical arbitrary-length maps/unit-minor law.
"""Finite supplements to PRIVATE nonpower-merge derivation; no uniform certification."""
from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
import json
minor=joint=variance=intervals=margin=roots=0
for d in [2,3,4]:
 vv=list(product([0,1],repeat=d))[1:]
 for a,b in combinations(vv,2):
  assert any(abs(a[i]*b[j]-a[j]*b[i])==1 for i,j in combinations(range(d),2));minor+=1
  for q in [2,4]:
   hist=Counter()
   for tau in product(range(q),repeat=d):
    x=(sum(t*v for t,v in zip(tau,a))+1)%q;y=(sum(t*v for t,v in zip(tau,b))+2)%q
    hist[x,y]+=1
   assert len(hist)==q*q and set(hist.values())=={q**(d-2)};joint+=1
# Two disjoint children, each support{0,e1,e2}; one zero pair form.
forms=[(a[0],a[1],b[0],b[1])for a in [(0,0),(1,0),(0,1)]for b in [(0,0),(1,0),(0,1)]]
for q in [2,4,8]:
 S=[0]*q;S2=[0]*q;num=q**4;V=len(forms)
 for tau in product(range(q),repeat=4):
  counts=[0]*q
  for j,f in enumerate(forms):counts[(sum(t*v for t,v in zip(tau,f))+j//3+2*(j%3))%q]+=1
  for r,v in enumerate(counts):S[r]+=v;S2[r]+=v*v
 for r in range(q):
  mean=F(S[r],num);var=F(S2[r],num)-mean*mean;mu=F(V,q)
  assert abs(mean-mu)<=1 and var<=mu;variance+=1
# Exact dyadic lengths and exponent inequalities, with only moderate bitlengths.
for m in [2,3,4,8,16,32,64,128]:
 for u in [1,2,8,48]:
  base=16*m+64*u;H=base+m-1
  M=[(1<<(base+i))-(1<<(base+2*i-m-2))for i in range(m)]
  assert all(F(M[i],1<<(base+i))==1-F(1,1<<(m+2-i))for i in range(m))
  total=F(0)
  for i in range(1,m):
   de=F(1,1<<(m+3-i));E=1<<(base+i)
   extra=F(2,1<<((base+i)//2))+F(2,E)+4/(de**4*E)
   assert extra<=de**2
   assert 2*de**2+extra<=3*de**2;total+=3*de**2
   c=base+i-2
   for k in {0,1,c//2,c}:
    mu=F((1<<k)*(1-de)**2*E);out=M[i];gap=mu-(1<<k)*out
    assert gap==(1<<k)*de**2*E and gap>1
    bound=gap/mu+F(1,1<<((base+i-1)//2))+1/mu+out/(gap-1)**2
    assert bound<=3*de**2;margin+=1
  assert total<=F(1,64)
  for dd in [1,H//2,H-1]:
   cap=2*H-dd-2;rootfail=F((1<<cap)*(1<<dd),M[-1]**2)
   assert rootfail==F(16,49);roots+=1
  assert F(16,15)*F(64,63)*F(49,33)<3
# Linear selected-rank interval walker: only first rectangle needsdivision.
def walk(groups,start,length):
 out=[];at=0;first=True
 for AA,BB in groups:
  size=len(AA)*len(BB)
  if start>=at+size:at+=size;continue
  if first:ia,ib=divmod(start-at,len(BB));first=False
  else:ia=ib=0
  while ia<len(AA) and len(out)<length:
   out.append((AA[ia],BB[ib]));ib+=1
   if ib==len(BB):ib=0;ia+=1
  at+=size
  if len(out)==length:return out
 return out
for na in [3,5,7]:
 for nb in [3,6,7]:
  LA=[(a*a+2*a)%17 for a in range(na)];LB=[(b*b+3*b)%19 for b in range(nb)]
  for q in [1,2,4,8]:
   for r in range(q):
    groups=[]
    for s in range(q):
     AA=[a for a in range(na)if LA[a]%q==s];BB=[bb for bb in range(nb)if LB[bb]%q==(r-s)%q]
     if AA and BB:groups.append((AA,BB))
    flat=[(a,bb)for AA,BB in groups for a in AA for bb in BB]
    assert len(flat)==sum((LA[a]+LB[bb])%q==r for a in range(na)for bb in range(nb))
    for outsize in [1,2,3,5,7]:
     for block in range(len(flat)//outsize):
      got=walk(groups,block*outsize,outsize)
      assert got==flat[block*outsize:(block+1)*outsize]
      assert len(set(got))==outsize
      for j,(a,bb) in enumerate(got):
       rank=flat.index((a,bb));assert divmod(rank,outsize)==(block,j)
       hi=(LA[a]+LB[bb]-r)//q;assert LA[a]+LB[bb]==r+q*hi
      intervals+=1
print(json.dumps(dict(binary_unit_minor_cases=minor,joint_affine_uniform_cases=joint,exact_bucket_mean_variance_cases=variance,dyadic_Chebyshev_margin_cases=margin,root_distribution_free_fraction_cases=roots,nonpower_selected_interval_reindex_cases=intervals,all_finite_research_checks_passed=True,uniform_proof_and_genuine_review_still_required=True)))

assert 3*(F(1,2**16)+F(1,2**12))+F(1,2**20)+F(1,2**30)+F(1,2**40)+F(1,2**10)<F(1,2**8)
# Actual block endpoints and total caps (integer coefficients, never giant 2^m).
blockgeom=0
for n in sorted(ns):
 if n<2**128:continue
 r,m,u,kap,ss,base,dl,H,LL,h0,vv,sig=params(n)
 gw=(dl-1).bit_length();b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
 assert base>=4*u and base>=32 and 4*gw<=base and 4*b0<=base
 assert m+gw+b0<=H and b0>=1 and Lblk*b0>=n and (Lblk-1)*b0<n
 Kc=8192*(m+10*u+100);Kp=8192*(u+100)
 cc=256*dl*(Kc+u+16);cp=256*dl*(Kp+u+16);Y=m+(cc-1).bit_length()
 qc=(Y+6)*cc+2*Lblk*cp+Kp
 assert Kp<=Kc and Y+6+2*Lblk<=3*n
 with localcontext() as ctx:
  ctx.prec=800
  assert D(qc)<=D(2**50)*D(n)*D(n).sqrt()
 assert 8192*(u+100)>=288*(2*u+30) # e^-x<=2^-x, n exp(-K/288)<=2^-30/n
 blockgeom+=1
# Uniform modular frequencies survive arbitrary offsets and +/- incidences.
from itertools import product
uniformcases=0
for b in range(1,6):
 mod=1<<b
 for coeff in [(1,),(-1,),(1,-1),(1,1),(-1,-1)]:
  for offset in [0,1,mod-1]:
   counts=[0]*mod
   for ts in product(range(mod),repeat=len(coeff)):
    counts[(offset+sum(a*t for a,t in zip(coeff,ts)))%mod]+=1
   assert len(set(counts))==1;uniformcases+=1
# Physical CRT identity for every small odd modulus, including composite.
phasecases=0
for M in range(3,64,2):
 for b in range(1,6):
  two=1<<b;K0=pow(-two,-1,M);J=(two*K0+1)//M
  assert two*K0+1==M*J and J%2==1 and 1<=J<=two
  for j in [0,1,3,7]:
   for aa in [0,1,3]:
    N=(1<<aa)*M;dn=N.bit_length()-1;B=dn-b
    if B<aa+1:continue
    gamma=pow(2,B-aa,M);am=(K0*pow(2,-j,M)*pow(gamma,-1,M))%M
    alpha=am
    while alpha%(1<<aa)!=1%(1<<aa):alpha+=M
    assert 0<alpha<N and (gamma*alpha-K0*pow(2,-j,M))%M==0
    for t in [-11,-1,0,1,9]:
     for W in [-5,-1,0,1,4]:
      residual=(pow(2,j,M)*t)%M
      lhs=F((1<<B)*W*alpha*residual,N)
      rhs=F(K0*W*t,M)
      assert (lhs-rhs).denominator==1
      assert rhs==F(J*W*t,two)-F(W*t,two*M)
      phasecases+=1
# Signed-digit reconstruction, all signs and partial final blocks.
signedcases=0
for bits in range(2,11):
 for bs in [1,2,3,5]:
  for t0 in range(-(1<<(bits-1))+1,1<<(bits-1)):
   low=0;j=0;R=max(1,abs(t0))
   while j<bits:
    b=min(bs,bits-j);t=(t0-low)//(1<<j);a=t%(1<<b)
    assert abs(t)<=R
    low+=a<<j;j+=b
   lift=low if low<(1<<(bits-1)) else low-(1<<bits)
   assert lift==t0;signedcases+=1
# Exact Fourier orthogonality via residue counts gives true expectation1/2,
# wrong expectation0 for every distinct candidate; no numerical precision premise.
scorecases=0
for b in range(1,7):
 mod=1<<b
 for J in range(1,mod,2):
  assert sorted((J*w)%mod for w in range(mod))==list(range(mod))
  for delta in range(1,mod):
   from math import gcd
   g=gcd(delta,mod);ct=[0]*mod
   for w in range(mod):ct[(J*w*delta)%mod]+=1
   assert all(ct[k]==(g if k%g==0 else 0)for k in range(mod))
   assert mod//g>=2;scorecases+=1
print(json.dumps(dict(block_geometry_cases=blockgeom,uniform_topblock_incidence_cases=uniformcases,physical_CRT_phase_cases=phasecases,signed_block_reconstruction_cases=signedcases,exact_character_sum_cases=scorecases,all_new_block_checks_passed=True)))
