"""Exact integer-root capacity, rounded envelopes, fields and demand diagnostics."""
from math import isqrt
from decimal import Decimal as D,localcontext
import random,json
def root9(x):
 lo=0;hi=1<<((x.bit_length()+8)//9)
 while lo+1<hi:
  mid=(lo+hi)//2
  if mid**9>=x:hi=mid
  else:lo=mid
 assert (hi-1)**9<x<=hi**9
 return hi
roots=0
for n in range(1,5001):
 mm=root9(n**4);assert (mm-1)**9<n**4<=mm**9;roots+=1
for ee in range(1,129):
 rr=(1<<ee)+1;nn=isqrt(isqrt(rr**9))
 for n in [nn-1,nn,nn+1]:
  mm=root9(n**4);assert (mm-1)**9<n**4<=mm**9;roots+=1
def caps(m,k,dl):return [dl+i-k-1 for i in range(m-1)]+[2*(dl+m-1)-1-k]
small=0;geometric_cases=0
for dl in [3,5,9,17,33]:
 for m in range(1,40):
  k=(m-1).bit_length()+1
  if dl<k+1:continue
  cs=caps(m,k,dl);total=m*(dl-k)+m*(m-1)//2+dl-1
  assert sum(cs)==total and min(cs)>=0
  HH=dl+m-1
  assert sum((1<<(dl+i))*(m-i+3)*HH for i in range(m))<10*HH*(1<<HH)
  geometric_cases+=1
  for B in range(1,total+1):
   rem=B
   for c in reversed(cs):rem-=min(rem,c)
   assert rem==0;small+=1
ns=set();rng=random.Random(20261108)
for e in [48,49,50,63,64,65,95,96,97,127,128]:
 for off in [-1,0,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
for e in [192,256,384,512,768,1024]:ns.add(2**e)
for _ in range(35):
 e=rng.randrange(48,100);ns.add(2**e+rng.randrange(1<<32))
main=0;field_cases=0
with localcontext() as ctx:
 ctx.prec=650;ln2=D(2).ln()
 for n in sorted(ns):
  m=root9(n**4);u=(n-1).bit_length();k=(m-1).bit_length()+1
  dl=(n+1+m*k-m*(m-1)//2+m)//(m+1);H=dl+m-1
  l=D(n.bit_length()-1) if n&(n-1)==0 else D(n).ln()/ln2
  if m**9==n**4:
   a=D(m);t=D(n//m);bb=D(root9(n))
  else:
   nnlog=D(n).ln();a=(nnlog*4/9).exp();t=(nnlog*5/9).exp();bb=(nnlog/9).exp()
  assert a<=D(m)<a+1
  assert 4*m*m<=n and m*m+k<=n and dl>=k+1 and m>=10*u+100
  assert t/2<=dl<=2*t and H<=2*t and (m+1)*H<=4*n
  assert n<=m*(dl-k)+m*(m-1)//2+dl-1<=n+m
  K=8192*(m+10*u+100);Kp=8192*(u+100)
  factor=32*dl*(K+u+16);fp=32*dl*(Kp+u+16);Y=m+(factor-1).bit_length()
  assert K<=2**14*m and K*dl<=2**16*n and factor<=2**22*n
  assert Y<=m+u+23 and 2*Y<=n and Y+6<=n
  assert K//8192>=Y+u+30
  assert D(fp)<=2**24*t*l
  assert D((Y+6)*factor+2*n*fp+Kp)<=2**30*D(n)*t*l
  g=t+a/2-bb
  assert D(m+dl)<=g+4*l/9+7 and D(H)<=g+4*l/9+6
  gw=(dl-1).bit_length();rootcap=2*H-1-k
  def tail(ii):
   if ii==m:return 0
   tt=m-1-ii
   return rootcap+tt*(dl-k-1)+tt*(ii+m-2)//2
  assert tail(0)==m*(dl-k)+m*(m-1)//2+dl-1
  for BV in {1,n//2,n,min(n,rootcap),min(n,rootcap+1)}:
   for ii in {0,m//2,max(0,m-2),m-1,m}:
    rem=min(BV,tail(ii));prec=rem+1+ii+gw
    assert 1<=prec<=3*n
    if ii<m:
     assert rem<=(m-ii+1)*H and prec<=(m-ii+2)*H
     nxt=min(BV,tail(ii+1));bits=rem-nxt
     cap=dl+ii-k-1 if ii<m-1 else rootcap
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
print(json.dumps(dict(integer_root_cases=roots,small_greedy_cases=small,main_schedule_cases=main,mgf_recurrence_cases=mgf_cases,geometric_frame_cases=geometric_cases,precision_field_cases=field_cases,all_checks_passed=True)))
