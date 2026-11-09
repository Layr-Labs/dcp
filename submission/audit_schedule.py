from pathlib import Path
import json
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal as D,localcontext
q=F(141421,100000);d0=F(100759,28284200000);t=q+d0
ceil=lambda x:-(-x.numerator//x.denominator)
def floorsum(nn,mm,aa):
 out=0;bb=0
 while True:
  qa,aa=divmod(aa,mm);qb,bb=divmod(bb,mm);out+=qa*nn*(nn-1)//2+qb*nn;top=aa*nn+bb
  if top<mm:return out
  nn,bb=divmod(top,mm);aa,mm=mm,aa
ns={2**e for e in [128,129,192,256,512,1024]}
for e in [128,129,192,256]:
 for off in [-1,1,17]:
  if 2**e+off>=2**128:ns.add(2**e+off)
for e in [64,96,128,256]:
 for off in [-1,0,1]:ns.add(((1<<e)+1)**2+off)
count=0
with localcontext() as ctx:
 ctx.prec=800
 for n in sorted(ns):
  r=isqrt(n-1)+1;m=ceil(q*r);u=(n-1).bit_length();kap=(m-1).bit_length()+1;s=(2*kap+2)//3+2
  base=ceil(d0*r)+64;dl=base+s;Hlin=base+m-1;capD=isqrt(128*m)-1;H=Hlin-capD;L=m//(4*s)
  h0=(2*m+2)//3+24*u;v=m-h0;sig=(v-1).bit_length()+2;gw=(dl-1).bit_length();b0=n.bit_length()-1
  assert 4*capD<m and 4*h0<=3*m and h0<m-capD
  assert 8*s*s*(capD+2)<=m and (capD+1)*s<L
  assert base>=4*capD+4*s and base>=4*u and 4*gw<=base and 4*b0<=base
  assert base>=4*capD+4*u+4*s and m+gw+b0<=H
  assert dl<=2*base and (m+1)*H<=4*n
  AA=s*L-floorsum(L,L,s);BB=(m+1)*base+m*(m-1)//2-1
  loss=capD*(capD+1)//2;capacity=BB+m*s+s-AA-kap*h0-2-loss
  assert loss<=64*m and capacity>=n+64
  W=base+h0+min(s,(m-1-h0)*s//L)
  assert W<H and W>=2*v+2*sig+64*u
  kc=8192*(m+10*u+100);kp=8192*(u+100)
  assert kc<=2**14*m and kc*dl<=2**16*n
  cc=256*dl*(kc+u+16);Y=m+(cc-1).bit_length()
  assert cc<=2**25*n and Y<=m+u+26 and kc//8192>=Y+u+30
  sq=D(n).sqrt();quarter=sq.sqrt();FF=D(t.numerator)/D(t.denominator)*sq;ll=D(n).ln()/D(2).ln()
  assert D(m+dl)<=FF+ll/3+74
  assert D(capD)>13*quarter-2 and D(H)<=FF-13*quarter+69
  for k in {0,1,capD-1,capD,capD+1,2*capD,m-h0-1,m-1}:
   lam=min(base+m-1-k+min(s,k*s//L),H)
   assert lam<=H-max((k+1)//2-capD,0)
  count+=1
# Exact cap loss and frame sum on enumerable moderate schedules, scaledslack.
small=0
for m in [4096,8192,16384]:
 for s in [2,3,4]:
  L=m//(4*s);Dcap=min(isqrt(m),L//s-2)
  if Dcap<=0:continue
  base=1000;Hlin=base+m-1;H=Hlin-Dcap
  ls=[base+i+min(s,(m-1-i)*s//L)for i in range(m)]
  cs=[min(z,H)for z in ls]
  assert sum(a-b for a,b in zip(ls,cs))==Dcap*(Dcap+1)//2
  frame=F(0)
  for i,la in enumerate(cs):frame+=F(m-1-i+4,1<<(H-la))
  assert frame<=16*(Dcap+5)**2;small+=1
print(dict(actual_cap_main_geometries=count,exact_loss_and_plateau_checks=small,all_actual_cap_diagnostics_passed=True,not_a_reviewed_algorithm=True))

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
print(json.dumps(dict(block_geometry_cases=count,uniform_topblock_incidence_cases=uniformcases,physical_CRT_phase_cases=phasecases,signed_block_reconstruction_cases=signedcases,exact_character_sum_cases=scorecases,all_new_block_checks_passed=True)))

assert F(128)*q>F(67,5)**2 and F(67,5)-13==F(2,5)
print(json.dumps(dict(exact_strict_cap_margin_passed=True,physical_configuration_unchanged=True,uniform_proof_and_fresh_review_required=True)))
