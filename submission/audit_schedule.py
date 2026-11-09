"""Exact fractional-root tapered capacity, fields and complete-envelope diagnostic."""
from math import gcd
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json,random
NUM=2;DEN=5
def rootm(n):
 target=n**NUM
 lo=0;hi=1<<((target.bit_length()+DEN-1)//DEN)
 while lo+1<hi:
  mid=(lo+hi)//2
  if mid**DEN>=target:hi=mid
  else:lo=mid
 assert (hi-1)**DEN<target<=hi**DEN
 return hi
roots=0
for n in range(1,5001):
 mm=rootm(n);assert (mm-1)**DEN<n**NUM<=mm**DEN;roots+=1
for ee in range(1,65):
 rr=(1<<ee)+1;nn=rr**DEN
 for n in [nn-1,nn,nn+1]:
  mm=rootm(n);assert (mm-1)**DEN<n**NUM<=mm**DEN;roots+=1
def floor_sum(nn,mm,aa,bb=0):
 ans=0
 while True:
  qa,aa=divmod(aa,mm);qb,bb=divmod(bb,mm)
  ans+=qa*nn*(nn-1)//2+qb*nn
  top=aa*nn+bb
  if top<mm:return ans
  nn,bb=divmod(top,mm);aa,mm=mm,aa
floor_checks=0
for mm in range(1,33):
 for aa in range(33):
  for nn in range(17):
   assert floor_sum(nn,mm,aa)==sum(aa*ii//mm for ii in range(nn))
   floor_checks+=1
small=0;geometric_cases=0
for base in [4,9,17,33]:
 for k in [1,2,3]:
  s0=k+1
  if base<s0:continue
  for m in [32,64,96,128,192,256]:
   LL=m//(4*s0)
   if LL<2*s0:continue
   dl=base+s0;H=base+m-1
   def lift(kk):return min(s0,kk*s0//LL)
   ls=[base+ii+lift(m-1-ii) for ii in range(m)]+[1]
   cs=[2*ls[ii]-ls[ii+1]-k for ii in range(m)]
   AA=s0*LL-floor_sum(LL,LL,s0)
   total=(m+1)*base+m*(m-1)//2-1+m+s0-AA
   assert min(cs)>0 and sum(cs)==total
   assert ls[0]==dl and ls[-2]==H
   assert all(ls[ii+1]-ls[ii] in [0,1] for ii in range(m-1))
   assert sum((m-1-ii+4)*H*(1<<ls[ii]) for ii in range(m))<=19*H*(1<<H)
   geometric_cases+=1
   Bs=set(range(1,min(500,total)+1))|{total,total-1,total//2,cs[-1],cs[-1]+1}
   for BV in Bs:
    if not 1<=BV<=total:continue
    rem=BV
    for cap in reversed(cs):rem-=min(rem,cap)
    assert rem==0;small+=1
ns=set();rng=random.Random(20261108)
for e in [48,49,50,63,64,65,95,96,97,127,128]:
 for off in [-1,0,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
for e in [192,256,384,512,768,1024]:ns.add(2**e)
for _ in range(35):
 e=rng.randrange(48,100);ns.add(2**e+rng.randrange(1<<32))

for ee in [8,16,24,32,64]:
 rr=2**ee+1
 for off in [-1,0,1]:
  nn=rr**DEN+off
  if nn>=2**48:ns.add(nn)
main=0;field_cases=0
with localcontext() as ctx:
 ctx.prec=900;ln2=D(2).ln()
 for n in sorted(ns):
  m=rootm(n);u=(n-1).bit_length();k=(m-1).bit_length()+1
  den=2*(m+1);base=(2*n-m*(m+1)+den-1)//den+1;s0=k+1
  dl=base+s0;H=base+m-1;LL=m//(4*s0)
  assert LL>=2*s0 and LL<=m-1 and base>=s0 and base>=4
  l=D(n).ln()/ln2
  if m**DEN==n**NUM:aa=D(m)
  else:aa=(D(n).ln()*NUM/DEN).exp()
  tt=(D(n).ln()*(DEN-NUM)/DEN).exp()
  assert aa<=m<aa+1 and tt/2<=base and H<=2*tt
  assert (m+1)*H<=4*n and m>=10*u+100
  AA=s0*LL-floor_sum(LL,LL,s0)
  B0=(m+1)*base+m*(m-1)//2-1
  total=B0+m+s0-AA
  assert B0>=n and total>=n and AA<=s0*LL and 4*s0*LL<=m
  K=8192*(m+10*u+100);Kp=8192*(u+100)
  ctcoef=65536*dl;Y=m+(ctcoef-1).bit_length();extra=4*u
  b0=n.bit_length()-1;Lblk=(n+b0-1)//b0;A=4*Lblk
  roots_count=K*(Y+6+extra)+A
  assert K<=2**14*m and K*dl<=2**16*n
  assert Y<=m+u+16 and 2*Y<=n and K//8192>=Y+u+30
  assert l/(D(n)**(D(1)/5))<=2
  assert D(roots_count)<=D(2**19)*D(n)/l
  assert D(ctcoef*roots_count+Kp)<=D(2**38)*D(n)*tt/l
  FF=tt+aa/2-(D(n).ln()*(DEN-2*NUM)/DEN).exp()
  assert H<=FF+3 and m+dl<=FF+l*NUM/DEN+8 and m<=aa+1
  r=(n**5-1).bit_length();assert r<=5*u and r<H and total-(r-1)>=n
  total-=r-1
  gw=(dl-1).bit_length();rootcap=2*H-r-k
  assert base>=4*u and gw<=base//4 and m+gw+u<=H
  def lift(kk):return min(s0,kk*s0//LL)
  def liftpref(jj):return floor_sum(min(jj,LL),LL,s0)+s0*max(0,jj-LL)
  def tail(ii):
   if ii==m:return 0
   kk=m-1-ii;count=kk+1
   return (count+1)*H-kk-kk*(kk+1)//2+lift(kk)+liftpref(count)-r-count*k
  assert base>=4*u and base>=32 and gw<=base//4 and m+gw+u<=H
  b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
  assert Lblk*b0>=n and (Lblk-1)*b0<n
  assert tail(0)==total
  for BV in {1,n//2,n,min(n,rootcap),min(n,rootcap+1)}:
   for ii in {0,m//2,max(0,m-2),m-1,m,m-1-LL,m-1-LL//2,m-LL}:
    rem=min(BV,tail(ii));prec=rem+u+ii+gw
    assert 1<=prec<=3*n
    if ii<m:
     assert rem<=(m-ii+1)*H and prec<=(m-ii+2)*H
     nxt=min(BV,tail(ii+1));bits=rem-nxt
     lam=base+ii+lift(m-1-ii);lp=base+ii+1+lift(m-2-ii) if ii<m-1 else r
     assert 2*lam+(m-1-ii)<=2*H
     assert 0<=bits<=2*lam-lp-k and nxt+u+1+ii+gw==prec+1-bits
    field_cases+=1
  main+=1
mgf_cases=0
with localcontext() as ctx:
 ctx.prec=150
 for mm in range(1,97):
  kk=max(4,(mm-1).bit_length()+1);pp=D(1)/D(2**kk)
  for ss in [D(1)/32,D(1)/16,D(1)/8]:
   yy=ss/D(2**mm)
   for ii in range(1,mm+1):
    aa=2*yy;assert aa<D(1)/2
    yy=aa+(1-pp).ln()-(1-pp*aa.exp()).ln()
    assert yy<=(1+2*pp)**ii*ss/D(2**(mm-ii))
   assert yy<3*ss;mgf_cases+=1
print(json.dumps(dict(integer_fractional_root_cases=roots,floor_sum_reference_cases=floor_checks,tapered_greedy_cases=small,main_schedule_cases=main,mgf_recurrence_cases=mgf_cases,weighted_taper_frame_cases=geometric_cases,precision_field_cases=field_cases,all_checks_passed=True)))

from fractions import Fraction as F
from math import gcd,cos,sin,pi
from itertools import product
import json,random
# Unused top-block incidence with a nonempty signed unit support.
uniform=0
for b in range(1,6):
 mod=1<<b
 for signs in [(1,),(-1,),(1,1),(1,-1),(-1,-1),(1,-1,1)]:
  counts=[0]*mod
  for tau in product(range(mod),repeat=len(signs)):counts[sum(a*x for a,x in zip(signs,tau))%mod]+=1
  assert len(set(counts))==1;uniform+=1
# Exact modular phase identity, including unknown 2-adic component.
crt=0;identity=0
for M in range(3,130,2):
 for b in range(1,min(7,M.bit_length()-1)):
  mod=1<<b;K0=pow(-mod,-1,M);J=(mod*K0+1)//M
  assert mod*K0+1==J*M and J%2==1 and gcd(K0,M)==1
  for j in [0,1,3,6]:
   for W in [-11,-1,0,1,6,17]:
    for t in [-37,-1,0,1,31]:
     assert F(K0*W*t,M)==F(J*W*t,mod)-F(W*t,mod*M);identity+=1
   for a2 in [0,1,3]:
    N=(1<<a2)*M;dn=N.bit_length()-1;B=dn-b
    assert B>=a2
    gamma=pow(2,B-a2,M);v=K0*pow(2,-j,M)*pow(gamma,-1,M)%M
    alpha=v+M*((1-v)*pow(M,-1,1<<a2)%(1<<a2)) if a2 else v
    assert gcd(alpha,N)==1 and gamma*alpha%M==K0*pow(2,-j,M)%M
    for t in [-37,-1,0,1,31]:
     for two in [0,1,(1<<a2)-1]:
      # residual secret moduloM is2^j*t; arbitrary two-adic lift cancels.
      residual=(pow(2,j,M)*t%M)+M*two
      for W in [-5,-1,0,1,7]:
       delta=F((1<<B)*W*alpha*residual,N)-F(K0*W*t,M)
       assert delta.denominator==1;crt+=1
# Signed blocks including negative residuals and every boundary length.
signed=0
for n in range(2,33):
 b0=n.bit_length()-1
 for t0 in sorted(set(range(-min(50,1<<(n-1))+1,min(50,1<<(n-1))))|{-(1<<(n-1))+1,(1<<(n-1))-1,0}):
  low=0;j=0;t=t0
  while j<n:
   b=min(b0,n-j);a=t%(1<<b);low+=a<<j;t=(t-a)//(1<<b);j+=b
  got=low if low<1<<(n-1) else low-(1<<n)
  assert got==t0;signed+=1
# Two-adic direct and collimated block labels, exact phase modulointegers.
twoadic=0
for wd in range(1,11):
 for b in range(1,wd+1):
  B=wd-b
  for rem in range(1<<min(wd,5)):
   for W in range(1<<min(b,5)):
    assert F((1<<B)*W*rem,1<<wd)==F(W*rem,1<<b);twoadic+=1
# Orthogonality and tabulated-score gap, including adversarial bounded phase noise.
score=0
for b in range(1,8):
 mod=1<<b
 for J in [1,3,mod-1]:
  for v in [0,1,mod//2,mod-1]:
   for a in sorted({0,1,mod//2,mod-1,(v+1)%mod}):
    if a==v:continue
    gap=0
    for W in range(mod):
     theta=2*pi*((J*W*v)%mod)/mod
     eta=(1 if W%2 else -1)/16
     obs=[cos(theta+eta),sin(theta+eta)]
     for beta,fun in enumerate([cos,sin]):
      def table(c):
       xx=((J*W*c)%mod)/mod;idx=int(4096*xx)
       return round(fun(2*pi*idx/4096)*(1<<24))/(1<<24)
      gap+=obs[beta]*(table(v)-table(a))/(2*mod)
    assert gap>0.25;score+=1
print(json.dumps(dict(uniform_top_block_incidence_cases=uniform,modular_phase_identity_cases=identity,crt_physical_supplier_cases=crt,signed_block_reconstruction_cases=signed,two_adic_block_phase_cases=twoadic,uniform_frequency_noisy_score_cases=score,all_checks_passed=True)))

from fractions import Fraction as F
from itertools import product
from math import sqrt,cos,sin,pi
from cmath import exp
import random,json
rng=random.Random(60216)
worst=0;variance=0;uniformprep=0;permutations=0
for q in [2,4,8,16]:
 for D in [2,4,8,16,32,64]:
  for case in range(5):
   freqs=[rng.randrange(q) for _ in range(D)];bins=[[i for i,f in enumerate(freqs) if f==z] for z in range(q)]
   p=[len(b)/D for b in bins];theory=sum(sqrt(x) for x in p)**2/q
   ranks={i:(z,r) for z,b in enumerate(bins) for r,i in enumerate(b)}
   assert len(ranks)==D and len(set(ranks.values()))==D;permutations+=1
   for v in range(q):
    # Explicitly compress rank-uniform pieces then inverse Fourier transform.
    compressed=[sum(exp(2j*pi*freqs[i]*v/q)/sqrt(D) for i in b)/sqrt(len(b)) if b else 0j for b in bins]
    probs=[abs(sum(compressed[z]*exp(-2j*pi*z*out/q) for z in range(q))/sqrt(q))**2 for out in range(q)]
    assert abs(sum(probs)-1)<1e-12 and abs(probs[v]-theory)<1e-12;worst+=1
for q in [2,4,8]:
 for k in [1,2,3]:
  vectors=list(product([0,1],repeat=k))
  for D in [2,4,8]:
   if D>len(vectors):continue
   vecs=vectors[:D];val=F(0)
   for tau in product(range(q),repeat=k):
    ws=[sum(a*b for a,b in zip(v,tau))%q for v in vecs];counts=[ws.count(z) for z in range(q)]
    val+=q*sum((F(a,D)-F(1,q))**2 for a in counts)
   val/=q**k
   assert val==F(q-1,D);variance+=1
for count in range(1,129):
 width=(count-1).bit_length()
 # Recursive prefix count ratios are the exact squared rotation amplitudes.
 amps={0:1.0}
 for level in range(width):
  nxt={};remaining=width-level-1
  for prefix,a in amps.items():
   start=prefix<<(remaining+1);total=max(0,min(count-start,1<<(remaining+1)))
   for bit in [0,1]:
    sub=max(0,min(count-start-bit*(1<<remaining),1<<remaining))
    nxt[(prefix<<1)|bit]=a*sqrt(sub/total) if total else 0
  amps=nxt
 assert all(abs(a-(1/sqrt(count) if idx<count else 0))<1e-14 for idx,a in amps.items());uniformprep+=1
print(json.dumps(dict(covariant_worst_secret_measurement_cases=worst,exact_conditional_collision_variance_cases=variance,explicit_index_bin_rank_permutations=permutations,binary_prefix_uniform_state_preparations=uniformprep,all_checks_passed=True)))

from math import sin,cos,sqrt,atan2,pi
from cmath import exp
import json

def ry(v,bit,t):
 out=v[:];c=cos(t/2);s=sin(t/2)
 for a in range(len(v)):
  if a&(1<<bit):continue
  b=a|(1<<bit);out[a]=c*v[a]-s*v[b];out[b]=s*v[a]+c*v[b]
 return out

def rz(v,bit,t):return [a*exp((1j if idx&(1<<bit) else -1j)*t/2) for idx,a in enumerate(v)]
def cx(v):return [v[a^1] if a&2 else v[a] for a in range(4)]
controlled=0
for t in [0,pi/16,-pi/8,pi/3,pi,2*pi,1.135]:
 for a in range(4):
  v=[complex(i==a) for i in range(4)];actual=cx(ry(cx(ry(v,0,t/2)),0,-t/2));target=ry(v,0,t) if a&2 else v
  assert max(abs(x-y) for x,y in zip(actual,target))<1e-14;controlled+=1
  actual=cx(rz(cx(rz(rz(v,0,t/2),1,t/2)),0,-t/2));target=[x*exp(-1j*t/4)*(exp(1j*t) if i==3 else 1) for i,x in enumerate(v)]
  assert max(abs(x-y) for x,y in zip(actual,target))<1e-14;controlled+=1
uniform=0
for r in range(1,7):
 D=1<<r
 for count in range(1,D+1):
  gates=[]
  for level in range(r):
   rem=r-level-1
   for prefix in range(1<<level):
    start=prefix<<(rem+1);total=max(0,min(count-start,1<<(rem+1)));left=max(0,min(count-start,1<<rem));right=total-left
    t=2*atan2(sqrt(right),sqrt(left)) if total else 0
    gates.append((prefix,rem,t))
  def run(state,gates):
   v=state[:]
   for prefix,rem,t in gates:
    c=cos(t/2);s=sin(t/2)
    for low in range(1<<rem):
     a=(prefix<<(rem+1))|low;b=a|(1<<rem);aa=v[a];bb=v[b];v[a]=c*aa-s*bb;v[b]=s*aa+c*bb
   return v
  start=[complex(i==0) for i in range(D)];got=run(start,gates);target=[1/sqrt(count) if i<count else 0 for i in range(D)]
  assert max(abs(x-y) for x,y in zip(got,target))<1e-14
  inv=run(target,[(p,b,-t) for p,b,t in reversed(gates)])
  assert max(abs(x-y) for x,y in zip(inv,start))<1e-14;uniform+=1
print(json.dumps(dict(controlled_rotation_and_phase_decompositions=controlled,full_prefix_controlled_forward_inverse_circuits=uniform,all_checks_passed=True)))
