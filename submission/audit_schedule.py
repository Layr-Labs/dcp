"""Exact finite checks for the capped streaming-FW schedule."""
from fractions import Fraction as F
import json

def ceildiv(a,b):return (a+b-1)//b

def capped_sum(dl,m,H):
 t=min(m,max(0,H-dl))
 return t*dl+t*(t-1)//2+(m-t)*H

small=0
for m in range(1,65):
 for dl in range(2,9):
  for H in range(dl,dl+m+2):
   assert capped_sum(dl,m,H)==sum(min(dl+i,H) for i in range(m))
   lam=[min(dl+i,H) for i in range(m)]+[1]
   kappa=1
   capacities=[2*lam[i]-lam[i+1]-kappa for i in range(m)]
   assert min(capacities)>=0
   assert sum(capacities)==dl+capped_sum(dl,m,H)-1-m*kappa
   small+=1
alpha,beta,delta,h,y,c=map(F,['.4605','.8388','.4995','1.2995','.4995','1.0001'])
cap=alpha*y+beta*delta+beta*beta/2-(beta+delta-h)**2/2
assert cap==F(20000807,20000000)>F(100001,100000)
assert c*alpha+beta==F(25986921,20000000)<F(6497,5000)
assert beta+delta==F(13383,10000)
assert F(2**24,100000)>29
assert F(1,100000)>F(3,2*2**24)
rs=set(range(2**24,2**24+5001))
for k in range(24,257):
 for off in [-1,0,1,17,9999]:
  if 2**k+off>=2**24:rs.add(2**k+off)
for r in rs:
 ell=ceildiv(4605*r,10000);m=ceildiv(8388*r,10000)
 dl=ceildiv(4995*r,10000);H=2599*r//2000;w=999*r//2000
 kappa=(m-1).bit_length()+1
 assert dl<=H<dl+m and w<m
 assert dl>=kappa+1
 capacity=ell*w+dl+capped_sum(dl,m,H)-1-m*kappa
 assert capacity>=r*r
 assert m<=F(84,100)*r and ell<=F(461,1000)*r
 assert kappa+2<=r.bit_length()+4
 assert c*ell+m<F(6497,5000)*r+F(21,10)
 assert m+dl<=F(13383,10000)*r+2
 assert H<=h*r and w<=y*r
 assert H-w>2*r.bit_length()
 assert F(7,10)*r>4*r.bit_length()+35
 assert 2**28<=16*r and ell<r/2
 assert 3*2**14*dl*r>24000*r*r
print(json.dumps({'small_closed_sum_cases':small,'main_schedule_cases':len(rs),'all_checks_passed':True,'capacity_coefficient':str(cap),'time_tree_coefficient':str(beta+delta),'classical_table_cap':str(h)}))
