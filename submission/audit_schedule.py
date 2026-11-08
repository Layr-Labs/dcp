"""Rational log interval and binary capacity diagnostic; no exponential arrays."""
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
from math import isqrt,ceil
from functools import lru_cache
import random,json

def asum(x,t):
 acc=F(0);power=x;square=x*x
 for v in range(t):acc+=2*power/F(2*v+1);power*=square
 return acc
@lru_cache(None)
def a2(t):return asum(F(1,3),t)
def rlog(n):
 j=n.bit_length()-1;u=(n-1).bit_length();t=2*u+10
 z=F(n-(1<<j),n+(1<<j));az=asum(z,t);aa=a2(t);delta=F(1,3**(2*t))
 lo=j+az/(aa+delta);hi=j+(az+delta)/aa
 assert aa>=F(2,3) and hi-lo<=4*delta<=F(1,n*n)
 return lo,hi

def caps(m,k,dl):return [dl+i-k-1 for i in range(m-1)]+[2*(dl+m-1)-1-k]
small=0
for dl in [3,5,9,17,33]:
 for m in range(1,40):
  k=(m-1).bit_length()+1
  if dl<k+1:continue
  cs=caps(m,k,dl);total=m*(dl-k)+m*(m-1)//2+dl-1
  assert sum(cs)==total and min(cs)>=0
  assert sum(2**(dl+i) for i in range(m))<2**(dl+m)
  for B in range(1,total+1):
   rem=B
   for c in reversed(cs):rem-=min(rem,c)
   assert rem==0;small+=1
ns=set(range(2,65));rng=random.Random(20261108)
for e in [48,49,50,63,64,65,95,96,97,127,128]:
 for off in [-1,0,1,17]:
  if 2**e+off>=2**48:ns.add(2**e+off)
for e in [192,256,384,512,768,1024]:ns.add(2**e)
for _ in range(35):
 e=rng.randrange(48,100);ns.add(2**e+rng.randrange(1<<32))
main=0
with localcontext() as ctx:
 ctx.prec=650;ln2=D(2).ln()
 for n in sorted(ns):
  lo,hi=rlog(n)
  l=D(n).ln()/ln2
  if n&(n-1):assert D(lo.numerator)/D(lo.denominator)<=l<=D(hi.numerator)/D(hi.denominator)
  else:assert lo==n.bit_length()-1 and hi>=lo
  r=isqrt(n-1)+1;m=ceil(F(r,4)/lo);k=(m-1).bit_length()+1
  dl=(n+1+m*k-m*(m-1)//2+m)//(m+1);H=dl+m-1
  assert n<=m*(dl-k)+m*(m-1)//2+dl-1<=n+m
  assert dl>=k+1
  if n<2**48:continue
  main+=1;u=(n-1).bit_length()
  assert H<=5*r*lo and (m+1)*H<=45*n
  K=2**13*(m+10*u+100);factor=3*2**13*n*K*dl
  Y=m+(factor-1).bit_length();assert Y<=2*r<=n
  assert m>=10*u+100 and K<=2**14*m
  assert Y<=m+2*u+32 and K//2**13>=Y+u+30
  sq=D(n).sqrt();f=4*sq*l+sq/(8*l)
  assert D(m)<=sq/(4*l)+3
  assert D(m+dl)<=f+l/2+7
  assert D(H)<=f+l/2+6
print(json.dumps({'small_greedy_cases':small,'rational_log_cases':len(ns),'main_schedule_cases':main,'all_checks_passed':True}))
