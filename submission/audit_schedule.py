"""Exact lower-rational log, saturation and caps; finite diagnostic, not proof."""
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json

def ceil(x):return -(-x.numerator//x.denominator)
def rlog(n):
 j=n.bit_length()-1;u=(n-1).bit_length();t=2*u+10
 if n==1<<j:return F(j)
 z=F(n-(1<<j),n+(1<<j))
 def aa(x):
  s=F(0);v=x
  for k in range(t):s+=2*v/(2*k+1);v*=x*x
  return s
 return j+aa(z)/(aa(F(1,3))+F(1,3**(2*t)))
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

ns={2**e for e in [48,49,63,64,96,127,128,192,256,384,512,768,1024]}
for e in [48,49,63,64,95,96,127,128]:
 for off in [-1,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
cases=0
with localcontext() as ctx:
 ctx.prec=800;ln2=D(2).ln()
 for n in sorted(ns):
  ell=rlog(n);m=ceil(ell*ell);u=(n-1).bit_length();k=(m-1).bit_length()+1
  den=2*(m+1);base=(2*n-m*(m+1)+den-1)//den+1;s0=k+1;dl=base+s0;H=base+m-1;LL=m//(4*s0)
  assert LL>=2*s0 and base>=s0 and base>=4
  l=D(n).ln()/ln2 if n&(n-1) else D(n.bit_length()-1)
  ed=D(ell.numerator)/D(ell.denominator)
  assert l-D(1)/D(n*n)<=ed<=l+D('1e-790')
  assert l*l-1<m<=l*l+1 and m+1>l*l and m>=10*u+100
  assert m*m+k<=n and dl>=k+1
  t=D(n)/(l*l)
  assert t/2<=dl<=2*t and H<=2*t and (m+1)*H<=4*n
  total=(m+1)*dl+m*(m-1)//2-1-m*k
  AA=s0*LL-floor_sum(LL,LL,s0);B0=(m+1)*base+m*(m-1)//2-1
  total=B0+m+s0-AA
  assert B0>=n and total>=n and 4*s0*LL<=m
  kc=8192*(m+10*u+100);kp=8192*(u+100)
  cc=32*dl*(kc+u+16);cf=32*dl*(kp+u+16);Y=m+(cc-1).bit_length()
  assert kc<=2**14*m and kc*dl<=2**16*n and cc<=2**22*n
  assert Y<=m+u+23 and 2*Y<=n and Y+6<=n
  assert kc//8192>=Y+u+30
  assert D(cf)<=2**24*D(n)/l
  qcoef=(Y+6)*cc+2*n*cf+kp
  assert D(qcoef)<=2**30*D(n*n)/l
  ff=D(n)/(l*l)+l*l/2;ll=l.ln()/ln2
  assert m+dl<=ff+2*ll+6 and H<=ff+2
  assert (dl-1).bit_length()+1<=base and m+(dl-1).bit_length()<=H
  def lift(kk):return min(s0,kk*s0//LL)
  def tail(ii):
   if ii==m:return 0
   kk=m-1-ii;count=kk+1
   pref=floor_sum(min(count,LL),LL,s0)+s0*max(0,count-LL)
   return (count+1)*H-kk-kk*(kk+1)//2+lift(kk)+pref-1-count*k
  assert base>=4*u and base>=32 and (dl-1).bit_length()<=base//4 and m+(dl-1).bit_length()+u<=H
  b0=n.bit_length()-1;Lblk=(n+b0-1)//b0
  assert Lblk*b0>=n and (Lblk-1)*b0<n
  assert base>=4*u and base>=32 and (dl-1).bit_length()<=base//4 and m+(dl-1).bit_length()+u<=H
  assert tail(0)==total
  for ii in {0,m//2,m-2,m-1,m,m-1-LL,m-LL}:
   rem=min(n,tail(ii));gw=(dl-1).bit_length();prec=rem+u+ii+gw
   assert 1<=prec<=3*n
   if ii<m:
    assert rem<=(m-ii+1)*H and prec<=(m-ii+2)*H
    nxt=min(n,tail(ii+1));bits=rem-nxt
    lam=base+ii+lift(m-1-ii);lp=base+ii+1+lift(m-2-ii) if ii<m-1 else 1
    assert 0<=bits<=2*lam-lp-k and nxt+u+1+ii+gw==prec+1-bits
  cases+=1
print(json.dumps(dict(exact_rational_log_schedule_cases=cases,floor_sum_reference_cases=floor_checks,tapered_greedy_cases=small,weighted_taper_frame_cases=geometric_cases,all_checks_passed=True)))

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
