"""Exact diagnostics for the new lower-source-flow profile; not a proof verdict."""
from math import isqrt
from fractions import Fraction as F
import json
a=F(1336661,1000000);gap=(a-F(1,2)-F(9,10**7))**2-F(7,10);assert gap>0
count=0
for lg in [32768,32769,33024,65536,131072]:
 for offset in [-1,0,1]:
  n=(1<<lg)+offset
  if n<1<<32768:continue
  L=(n-1).bit_length();r=isqrt(n)+(isqrt(n)**2<n);target=(7*r*r+9)//10;m0=isqrt(target)+(isqrt(target)**2<target)
  k=n+(n%2==0);j=isqrt(k);m=m0+256*L;ell=13*r//10-m-16*L;dl=(r+1)//2;w=r//2-128*L;kap=(m-1).bit_length()+1
  capacity=ell*w+m*dl+m*(m-1)//2+dl-1-m*kap
  loss=136*r*L+F(3*r,2)+1+m*(kap+1)
  assert 10*m0*m0>=7*r*r and 10*(m0-1)**2<7*r*r
  assert 0<2*w<r<2*m and m<r and 0<ell<r and dl>=kap+1 and k*ell<n*n
  assert loss<140*r*L and 256*L*m0>200*r*L and capacity>=n
  assert m+ell==13*r//10-16*L
  assert F(m+ell)+F(7*ell,j)<=F(13,10)*r-16*L+28
  assert F(m+dl)<=(a-F(9,10**7))*r+256*L+2
  assert F(13,10)*r-16*L+28+6*r.bit_length()+43<=2*r-1
  assert (1024*L+128)*10**8<isqrt(n) and n>10**800
  count+=1
print(json.dumps(dict(diagnosticOnly=True,passed=True,closedMainProfiles=count,exactLeadingGapSquared=str(gap),literalQOuterPower=-10,actualSourceGeometryLogShift=-16,mathematicalVerdictExternal=True)))
