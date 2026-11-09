from fractions import Fraction as F
import gmpy2,json

def ceildiv(a,b):return -(-a//b)
def params(n):
 r=int(gmpy2.isqrt(n));r+=r*r<n
 z,exact=gmpy2.iroot(gmpy2.mpz(n)**49,100);U=int(z)+(not exact)
 t=r//10-16*U;y1=ceildiv(3*t,2);y4=ceildiv(3*t,10);y7=ceildiv(193*r,400);mu=3*t+y1+y4+y7;kap=(mu-1).bit_length()+3;c0=kap+1
 return r,U,t,y1,y4,y7,mu,kap,c0

def cap(t,y1,y4,y7,mu,kap,c0):
 a=3*t*c0+3*t*(3*t-1)//2
 wc=3*t*y1-y1*(y1-1)
 pos=min(y7,ceildiv(27*t,14));ws=0
 for s in range(5):
  count=max(0,ceildiv(pos-s,5));ws+=count*ceildiv(27*t-14*s,5)-7*count*(count-1)
 return a+3*(y1+y4)*(c0+3*t)+6*y7*(c0+3*t)-wc-ws+c0-1-mu*kap

def check(n):
 r,U,t,y1,y4,y7,mu,kap,c0=params(n);L=(n-1).bit_length();C=cap(t,y1,y4,y7,mu,kap,c0)
 assert U>=L and U*2**325<=r
 assert 100000*t>=9999*r and t>=2100 and 64*c0<=t and mu<=2*r
 assert C>=F(927,70)*t*t+18*t*y7-11*t>=n
 assert F(927,70)*F(9999,100000)**2+18*F(9999,100000)*F(193,400)==F(700570665927,700000000000)
 assert 7**135<2**379 and F(33,5)*F(1,10)+F(379,135)*F(193,400)==F(108787,54000)
 assert 3*t*(3*t-1)//2>=6*(c0+3*t)
 assert F(528,5)*U-7*L>=96*U and F(528,5)*U-3*L>=100*U
 assert 48*U-2*L>=40*U
 return dict(nBits=n.bit_length(),capacity=True,windowGuards=True,polynomialAbsorption=True)
if __name__=='__main__':
 out=[]
 for e in [32768,32769,32800,40000,65536]:
  for delta in [-1,0,1]:
   n=(1<<e)+delta
   if n<1<<32768:continue
   out.append(check(n))
 print(json.dumps(dict(checks=out,diagnosticOnly=True)))
# Independent direct finite sums check the closed-form capacity used above.
for t in range(1,50):
 y1=ceildiv(3*t,2);y4=ceildiv(3*t,10);y7=2*t;mu=3*t+y1+y4+y7;kap=(mu-1).bit_length()+3;c0=kap+1
 lams=list(range(c0,c0+3*t))+[c0+3*t]*(y1+y4+y7)
 arities=[2]*(3*t)+[4]*(y1+y4)+[7]*y7
 windows=[0]*(3*t)+[max(0,3*t-2*j)for j in range(y1)]+[0]*y4+[max(0,ceildiv(27*t-14*j,5))for j in range(y7)]
 direct=sum((f-1)*l-v-kap for f,l,v in zip(arities,lams,windows))+c0-1
 assert direct==cap(t,y1,y4,y7,mu,kap,c0)
print('Independent direct capacity sums: 49 PASS')
