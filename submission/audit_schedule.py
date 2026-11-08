"""Finite exact cap/capacity/field/envelope diagnostics, not an asymptotic proof."""
from math import isqrt
from fractions import Fraction as F
from decimal import Decimal as DD,localcontext
import random,json
q=F(141421,100000);d0=1/q-q/2;t=q+d0
assert q*d0+q*q/2==1 and 128*q>169
ceil=lambda x:-(-x.numerator//x.denominator)
small=weighted=0
for m in [16,32,64,128,256]:
 for D in [1,2,m//8,m//4,m//2]:
  for k in [4,7,10]:
   base=4*D+4*(k+1);dl=base+k+1;H=dl+m-1-D
   ls=[min(dl+i,H) for i in range(m)]+[1]
   cs=[2*ls[i]-ls[i+1]-k for i in range(m)]
   clin=(m+1)*dl+m*(m-1)//2-1-m*k
   assert min(cs)>0 and sum(cs)==clin-D*(D+1)//2
   assert sum((m-1-i+4)*(1<<ls[i]) for i in range(m))<=4*(D+5)**2*(1<<H)
   weighted+=1
   for B in set(range(1,min(500,sum(cs))+1))|{sum(cs),sum(cs)//2,cs[-1],cs[-1]+1}:
    if B>sum(cs):continue
    rem=B
    for cap in reversed(cs):rem-=min(rem,cap)
    assert rem==0;small+=1
ns=set();rng=random.Random(20261108)
for e in [128,129,160,192,256,384,512,768,1024]:
 for off in [-1,0,1,17]:
  if 2**e+off>=2**128:ns.add(2**e+off)
for ee in [64,80,128,192,256]:
 rr=2**ee+1
 for off in [-1,0,1]:ns.add(rr*rr+off)
for _ in range(35):
 e=rng.randrange(128,256);ns.add(2**e+rng.randrange(1<<32))
main=fields=0
with localcontext() as ctx:
 ctx.prec=900;ln2=DD(2).ln();qd=DD(q.numerator)/DD(q.denominator);td=DD(t.numerator)/DD(t.denominator)
 for n in sorted(ns):
  r=isqrt(n-1)+1;m=ceil(q*r);u=(n-1).bit_length();k=(m-1).bit_length()+1;s0=k+1
  base=ceil(d0*r)+64;dl=base+s0;D=isqrt(128*m)-1;H=dl+m-1-D;gw=(dl-1).bit_length()
  assert 1<=D<m//2 and base>=4*D+4*s0 and dl<=2*base
  assert base>=4*u and gw<=base//4 and m+gw+u<=H and F(H)<=t*r+1 and 2*H<=3*r and 2*(m+1)<=3*r and (m+1)*H<=4*n
  clin=(m+1)*dl+m*(m-1)//2-1-m*k;total=clin-D*(D+1)//2
  assert clin>=n+64*m+s0+63 and D*(D+1)<=128*m and total>=n
  kc=8192*(m+10*u+100);kp=8192*(u+100)
  cc=32*dl*(kc+u+16);cf=32*dl*(kp+u+16);Y=m+(cc-1).bit_length()
  assert m>=10*u+100 and kc<=2**14*m and kc*dl<=2**16*n and cc<=2**22*n
  assert Y<=m+u+23 and 2*Y<=n and Y+6<=n and kc//8192>=Y+u+30
  l=DD(n).ln()/ln2;root=DD(n).sqrt();quarter=root.sqrt()
  b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
  assert 1<<b0<=n and DD(Lblk)<=4*DD(n)/l
  assert DD((Y+6)*cc+2*Lblk*cf+kp)<=2**32*DD(n)*root
  assert DD(H)<=td*root-13*quarter+l/2+80
  assert DD(m+dl)<=td*root+l/2+73 and DD(m)<=qd*root+3
  assert DD(cf)<=2**24*root*l and DD((Y+6)*cc+2*n*cf+kp)<=2**30*DD(n)*root*l
  def tail(i):
   if i==m:return 0
   kk=m-1-i;v=max(kk-1-D,0)
   return (kk+2)*H-2*max(kk-D,0)-v*(v+1)//2-1-(kk+1)*k
  assert tail(0)==total
  for B in {1,n//2,n,min(n,2*H-1-k),min(n,2*H-k)}:
   for i in {0,m//2,m-2,m-1,m,m-1-D,m-D,m-2-D}:
    rem=min(B,tail(i));prec=rem+1+i+gw
    assert 1<=prec<=3*n
    if i<m:
     assert rem<=(m-i+1)*H and prec<=(m-i+2)*H
     nxt=min(B,tail(i+1));bits=rem-nxt;lam=min(dl+i,H);lp=min(dl+i+1,H) if i<m-1 else 1
     assert 0<=bits<=2*lam-lp-k and nxt+2+i+gw==prec+1-bits
    fields+=1
  main+=1
mgf_cases=0
with localcontext() as ctx:
 ctx.prec=150
 for mm in range(1,97):
  kk=max(4,(mm-1).bit_length()+1);pp=DD(1)/DD(2**kk)
  for ss in [DD(1)/32,DD(1)/16,DD(1)/8]:
   yy=ss/DD(2**mm)
   for ii in range(1,mm+1):
    aa=2*yy;assert aa<DD(1)/2
    yy=aa+(1-pp).ln()-(1-pp*aa.exp()).ln()
    assert yy<=(1+2*pp)**ii*ss/DD(2**(mm-ii))
   assert yy<3*ss;mgf_cases+=1
print(json.dumps(dict(capped_greedy_cases=small,weighted_plateau_cases=weighted,main_cap_schedule_cases=main,precision_field_cases=fields,mgf_recurrence_cases=mgf_cases,all_checks_passed=True)))


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
