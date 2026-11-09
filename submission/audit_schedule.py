from math import isqrt
from fractions import Fraction as F
import json
beta=F(107,130);eta=F(13,10);q=F(86,65);d0=F(3,130)
assert F(1,4)+beta/2+beta*beta/2-d0*d0/2==1
count=0
for lg in [32768,32769,33024,65536,131072]:
 for offset in [-1,0,1]:
  n=(1<<lg)+offset
  if n<1<<32768:continue
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);k=n+(n%2==0);j=isqrt(k)
  m0=(107*r+129)//130;m=m0+256*L;ell=dl=(r+1)//2;w=r//2-128*L;H=13*r//10-512*L;kap=(m-1).bit_length()+1
  growing=min(m,max(0,H-dl+1));widthsum=growing*dl+growing*(growing-1)//2+(m-growing)*H
  capacity=ell*w+dl+widthsum-1-m*kap
  A=256*L;B=512*L+1
  loss=64*r*L+F(r,2)+1+d0*B*r+F(B*B,2)+A*B+m*(kap+1)
  assert r>2**20*L and H>dl and H<dl+m and dl>=kap+1 and m<r and w<m
  assert loss<80*r*L and A*eta*r>300*r*L and capacity>=n
  assert F(m+ell)+F(7*ell,j)<=q*r+256*L+31
  assert F(m+dl)<=q*r+256*L+2
  assert F(m+ell)+F(7*ell,j)<F(7,5)*r
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,closedRoundedCappedProfiles=count,leadingTimeAndCopies='86/65',leadingClassical='13/10',intendedTOuterPower=330,intendedQOuterPower=260,intendedSCOuterPower=-500,mathematicalVerdictExternal=True)))
