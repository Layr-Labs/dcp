"""Exact clipped-auxiliary prefix capacities, including zero first windows."""
from fractions import Fraction as F
import json

def ceildiv(a,b):return (a+b-1)//b

def sums(M,A,H,dl,k):
 if M<=A:return M*(dl-k)+M*(M-1)//2+dl-1
 J=M-A;sb=A*(dl-k-1)+A*(A-1)//2
 t=min(J,H//2)
 return sb+J*(H-k)+(2*H*J-H*t+t*t)+H-1

def capacities(M,A,H,dl,k):
 out=[]
 for i in range(M):
  root=i==M-1
  if i<A:out.append(2*(dl+i)-1-k if root else dl+i-1-k)
  else:
   j=i-A;aux=min(H+1+2*j,2*H);out.append(2*H+aux-1-k if root else H+aux-k)
 return out

def prefix(B,Mmax,A,H,dl,k):
 lo,hi=1,Mmax
 while lo<hi:
  mid=(lo+hi)//2
  if sums(mid,A,H,dl,k)>=B:hi=mid
  else:lo=mid+1
 return lo
aux_sum_cases=0
for hh in range(3,65):
 for jj in range(2*hh+1):
  tt=min(jj,hh//2)
  assert 2*hh*jj-hh*tt+tt*tt==sum(min(hh+1+2*x,2*hh) for x in range(jj))
  aux_sum_cases+=1
small=0
for H in [24,32,48]:
 for dl in [H//2,2*H//3]:
  A=H-dl
  for L in [1,H//2,H//2+1,H]:
   mm=A+L;k=(mm-1).bit_length()+3
   if dl<k+1:continue
   sb=A*(dl-k-1)+A*(A-1)//2
   assert sb>=3*H-k
   last=0
   for M in range(1,mm+1):
    cs=capacities(M,A,H,dl,k)
    assert min(cs)>=0 and sum(cs)==sums(M,A,H,dl,k)>last
    last=sum(cs)
   for B in range(1,last+1):
    M=prefix(B,mm,A,H,dl,k);cs=capacities(M,A,H,dl,k);remain=B
    alloc=[0]*M
    for i in range(M-1,-1,-1):alloc[i]=min(remain,cs[i]);remain-=alloc[i]
    assert remain==0
    assert all(alloc[i]==cs[i] for i in range(A,M))
    small+=1
q,d,h=map(F,['1.2994','.52','.5595']);a=h-d;ell=(q-a)/2
C=q*d+q*q/2-(q+d-h)**2/4-(q+d-2*h)**2/4
assert C==F(80034491,80000000)>F(100001,100000)
assert q+d==F(9097,5000)
rs=set(range(2**24,2**24+5001))
for e in range(24,257):
 for off in [-1,0,1,17,9999]:
  if 2**e+off>=2**24:rs.add(2**e+off)
for r in rs:
 H=5595*r//10000;dl=ceildiv(5200*r,10000);target=ceildiv(12994*r,10000)
 A=H-dl;L=ceildiv(target-A,2);mm=A+L;height=A+2*L;k=(mm-1).bit_length()+3
 assert A>=F(r,32) and dl>=k+1 and L>=1
 assert target<=height<=target+1
 assert mm<=r and k<=r.bit_length()+4
 assert H>=k+2 and min(H+1+2*(L-1),2*H)==2*H
 assert L>H//2
 sb=A*(dl-k-1)+A*(A-1)//2
 assert sb>=3*H-k
 assert sums(mm,A,H,dl,k)>=r*r
 assert height<=q*r+2 and height+dl<=(q+d)*r+3
 assert H<=h*r
 assert F(7,10)*r>4*r.bit_length()+35
 assert 4*(mm+1)*H+2**13*(2*r+(r*r-1).bit_length()+30)<=8*((r-1)**2+1)
 Bs={1,r*r,(r*r)//2,sums(A,A,H,dl,k)}
 for j in [1,max(1,H//2-1),H//2,H//2+1,max(1,L//2),L]:
  s=sums(A+j,A,H,dl,k)
  Bs.update([s-1,s,s+1])
 for B in Bs:
  if not 1<=B<=r*r:continue
  M=prefix(B,mm,A,H,dl,k)
  assert sums(M,A,H,dl,k)>=B and (M==1 or sums(M-1,A,H,dl,k)<B)
  if M>A:
   J=M-A;t=min(J,H//2);allfour=J*(H-k)+(2*H*J-H*t+t*t)+H-1
   assert B>=allfour
print(json.dumps({'auxiliary_closed_sum_cases':aux_sum_cases,'small_greedy_cases':small,'main_schedule_cases':len(rs),'capacity_coefficient':str(C),'time_coefficient':str(q+d),'all_checks_passed':True}))
