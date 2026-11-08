"""Exact near-sqrt(2) saturated dimensions and uniform-envelope diagnostics."""
from math import isqrt
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json
q=F(141421,100000);t=1/q+q/2;d0=1/q-q/2
assert d0>0 and q*q<2
root_cases=0
for nn in range(1,5001):
 rr=isqrt(nn-1)+1;mm=(141421*rr+99999)//100000
 assert (rr-1)**2<nn<=rr*rr
 assert (mm-1)*100000<141421*rr<=mm*100000
 root_cases+=1


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
rs=set(range(2**24,2**24+65))
for ee in [24,25,32,48,64,96,128,192,256,384,512]:
 for off in [-1,0,1,17,99999]:
  if 2**ee+off>=2**24:rs.add(2**ee+off)
for aa in [168,1024,100000,10**20]:
 for off in [-1,0,1]:rs.add(100000*aa+off)
ns={nn for rr in rs for nn in [rr*rr,(rr-1)*(rr-1)+1] if nn>=2**48}
main=0;field_cases=0
with localcontext() as ctx:
 ctx.prec=900;ln2=D(2).ln();qd=D(q.numerator)/D(q.denominator);td=D(t.numerator)/D(t.denominator)
 for n in sorted(ns):
  r=isqrt(n-1)+1;m=(141421*r+99999)//100000
  u=(n-1).bit_length();k=(m-1).bit_length()+1
  base=(100759*r+28284199999)//28284200000;s0=k+1;dl=base+s0;H=base+m-1;LL=m//(4*s0)
  assert LL>=2*s0 and LL<=m-1 and base>=s0 and base>=4
  assert dl>=k+2 and base>=d0*r and base<d0*r+1
  assert 2*H<=3*r and 2*(m+1)<=3*r and (m+1)*H<=4*n
  AA=s0*LL-floor_sum(LL,LL,s0)
  total=(m+1)*base+m*(m-1)//2-1+m+s0-AA
  assert AA<=s0*LL and 4*s0*LL<=m
  assert total>=r*r>=n
  assert m>=10*u+100
  K=8192*(m+10*u+100);Kp=8192*(u+100)
  factor=32*dl*(K+u+16);fp=32*dl*(Kp+u+16);Y=m+(factor-1).bit_length()
  assert K<=2**14*m and K*dl<=2**16*n and factor<=2**22*n
  assert Y<=m+u+23 and 2*Y<=n and Y+6<=n and K//8192>=Y+u+30
  assert fp<=2**24*r*u
  assert (Y+6)*factor+2*n*fp+Kp<=2**30*n*r*u
  l=D(n).ln()/ln2;rt=D(n).sqrt()
  assert D(m+dl)<=td*rt+l/2+9 and D(H)<=td*rt+3
  assert D(m)<=qd*rt+3
  gw=(dl-1).bit_length();rootcap=2*H-1-k
  assert gw+1<=base and m+gw<=H
  def lift(kk):return min(s0,kk*s0//LL)
  def liftpref(jj):return floor_sum(min(jj,LL),LL,s0)+s0*max(0,jj-LL)
  def tail(ii):
   if ii==m:return 0
   kk=m-1-ii;count=kk+1
   return (count+1)*H-kk-kk*(kk+1)//2+lift(kk)+liftpref(count)-1-count*k
  assert tail(0)==total
  for BV in {1,n//2,n,min(n,rootcap),min(n,rootcap+1)}:
   for ii in {0,m//2,max(0,m-2),m-1,m,m-1-LL,m-1-LL//2,m-LL}:
    rem=min(BV,tail(ii));prec=rem+1+ii+gw
    assert 1<=prec<=3*n
    if ii<m:
     assert rem<=(m-ii+1)*H and prec<=(m-ii+2)*H
     nxt=min(BV,tail(ii+1));bits=rem-nxt
     lam=base+ii+lift(m-1-ii);lp=base+ii+1+lift(m-2-ii) if ii<m-1 else 1
     assert 2*lam+(m-1-ii)<=2*H
     cap=2*lam-lp-k
     assert 0<=bits<=cap and nxt+2+ii+gw==prec+1-bits
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
print(json.dumps(dict(integer_sqrt_and_rational_ceiling_cases=root_cases,floor_sum_reference_cases=floor_checks,tapered_greedy_cases=small,main_schedule_cases=main,mgf_recurrence_cases=mgf_cases,weighted_taper_frame_cases=geometric_cases,precision_field_cases=field_cases,all_checks_passed=True)))
