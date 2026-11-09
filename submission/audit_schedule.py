"""Closed integer diagnostics only; the accompanying proof supplies uniform claims."""
import gmpy2,json
from fractions import Fraction as F

def cd(a,b):return -(-a//b)
def windows(A,B,D,count):
 pos=min(count,max(0,cd(A,B)));out=0
 for s in range(D):
  z=max(0,cd(pos-s,D));out+=z*cd(A-B*s,D)-B*z*(z-1)//2
 return out

def params(n):
 r=int(gmpy2.isqrt(n));r+=r*r<n;u,exact=gmpy2.iroot(gmpy2.mpz(n)**49,100);U=int(u)+(not exact)
 w=3*r//20-16*U;y7=cd(3*w,4);y11=cd(35*w,34);y16=cd(7*w,8);y22=cd(1533*r,10000);mu=2*w+y7+y11+y16+y22;kap=(mu-1).bit_length()+3;c0=kap+1
 return r,U,w,y7,y11,y16,y22,mu,kap,c0

def capacity(w,y7,y11,y16,y22,mu,kap,c0):
 fixed=w*c0+w*(w-1)//2+w*(c0+w)+(6*y7+10*y11+15*y16+21*y22)*(c0+w)+c0-1-mu*kap
 return fixed-windows(10*w,14,5,y7)-windows(15*w,17,5,y11)-windows(7*w,8,2,y16)-windows(25*w,22,5,y22)

def check(n):
 r,U,w,y7,y11,y16,y22,mu,kap,c0=params(n);Lg=(n-1).bit_length();C=capacity(w,y7,y11,y16,y22,mu,kap,c0);A=F(963807,41888);Bc=F(1264301,113220)
 assert U>=Lg and U*2**325<=r and 100000*w>=14999*r and w>=3200 and 64*c0<=w and mu<=2*r
 assert C>=A*w*w+21*w*y22-19*w>=n
 assert A*F(14999,100000)**2+21*F(14999,100000)*F(1533,10000)==F(419089234349967,418880000000000)
 assert Bc==2+F(3,4)*F(379,135)+F(35,34)*F(128,37)+F(7,2)
 assert Bc*F(3,20)+F(165,37)*F(1533,10000)==F(1112693,471750)
 assert 7**135<2**379 and 11**37<2**128
 assert 2*w<=2*(c0+w)-kap-1 and 3*w<=3*(c0+w)-kap-1 and cd(7*w,2)<=4*(c0+w)-kap-1
 assert 5*w<=5*(c0+w)-kap-1
 assert w*w>=21*(c0+w)
 assert (16*Bc)*U-14*Lg>=160*U and (16*Bc)*U-3*Lg>=172*U and 16*U-2*Lg>=12*U
 assert F(237,100)*r+4*r.bit_length()+48<=3*r-1
 return dict(nBits=n.bit_length(),capacity=True,windows=True,nativePolynomials=True)

if __name__=='__main__':
 out=[]
 for e in [32768,32769,32800,40000,65536]:
  for d in [-1,0,1]:
   n=(1<<e)+d
   if n>=1<<32768:out.append(check(n))
 for w in range(1,70):
  y7=cd(3*w,4);y11=cd(35*w,34);y16=cd(7*w,8);y22=w;mu=2*w+y7+y11+y16+y22;kap=(mu-1).bit_length()+3;c0=kap+1
  lams=list(range(c0,c0+w))+[c0+w]*(w+y7+y11+y16+y22);fs=[2]*(2*w)+[7]*y7+[11]*y11+[16]*y16+[22]*y22
  vs=[0]*(2*w)+[max(0,cd(10*w-14*j,5))for j in range(y7)]+[max(0,cd(15*w-17*j,5))for j in range(y11)]+[max(0,cd(7*w-8*j,2))for j in range(y16)]+[max(0,cd(25*w-22*j,5))for j in range(y22)]
  direct=sum((f-1)*l-v-kap for f,l,v in zip(fs,lams,vs))+c0-1
  assert direct==capacity(w,y7,y11,y16,y22,mu,kap,c0)
 for L in [16,32,1024]:
  assert 2*L+1+(2+F(1,L))*(4*L+2)<=13*L
  assert L*L+2*L+1+(2+F(1,L))*(L+16*L*L)<=36*L*L
  assert 16*L*L+(2+F(1,L))*(L+39*L**4)<=118*L**4
  assert 16*L**3+2*L+1+(2+F(1,L))*(L+121*L**7)<=250*L**7
  assert 16*L**4+2*L*L+2*L+1+(2+F(1,L))*(L+253*L**11)<=525*L**11
 print(json.dumps(dict(giantChecks=out,directCapacitySums=69,stepTableSizes=[16,32,1024],diagnosticOnly=True)))
