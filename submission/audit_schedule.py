"""Exact closed-profile diagnostics, not a mathematical review or circuit run."""
from math import isqrt
from fractions import Fraction as F
import json
beta=F(67,80);eta=q=F(13,10);b0=F(107,80);d0=F(3,80)
assert q/2+beta*beta/2-d0*d0/2==1 and b0-q==d0
count=0
for lg in [32768,32769,33024,65536,131072]:
 for offset in [-1,0,1]:
  n=(1<<lg)+offset
  if n<1<<32768:continue
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);k=n+(n%2==0);j=isqrt(k)
  m0=(67*r+79)//80;m=m0+256*L;ell=13*r//10-m-16*L;dl=(r+1)//2;w=r//2-128*L;H=13*r//10-512*L;kap=(m-1).bit_length()+1
  growing=min(m,max(0,H-dl+1));widthsum=growing*dl+growing*(growing-1)//2+(m-growing)*H
  capacity=ell*w+dl+widthsum-1-m*kap
  A=256*L;Bc=512*L+1
  loss=136*r*L+F(3*r,2)+1+d0*Bc*r+F(Bc*Bc,2)+A*Bc+m*(kap+1)
  assert r>2**20*L and 0<2*w<r<2*m and m<F(84,100)*r and F(45,100)*r<ell<r
  assert H>dl and H<dl+m and dl>=kap+1 and w<m and k*ell<n*n
  assert loss<160*r*L and F(1024,5)*r*L>loss and capacity>=n
  assert m+ell==13*r//10-16*L
  assert F(m+ell)+F(7*ell,j)<=q*r-16*L+28
  assert F(m+dl)<=b0*r+256*L+2
  assert q*r-16*L+28+6*r.bit_length()+43<=2*r-1
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,closedRoundedProfiles=count,literalTimeCoefficient='107/80',literalTimePower=262,literalSourcePower=-10,literalClassicalPower=-500,mathematicalVerdictExternal=True)))
