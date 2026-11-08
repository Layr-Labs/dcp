"""Exact capped-tree checks; the pairing-capacity contribution is zero.
The index-stack plus root qubits are checked separately from O(n) scratch.
"""
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
alpha,beta,delta,h,y,c=map(F,['0','1.2994','.126','1.2995','0','1'])
cap=alpha*y+beta*delta+beta*beta/2-(beta+delta-h)**2/2
assert cap==F(40000767,40000000)>F(100001,100000)
assert c*alpha+beta==F(6497,5000)==F(6497,5000)
assert beta+delta==F(7127,5000)
assert F(2**24,100000)>F(208,5)
assert F(1,100000)>F(21,10*2**24)
rs=set(range(2**24,2**24+5001))
for k in range(24,257):
 for off in [-1,0,1,17,9999]:
  if 2**k+off>=2**24:rs.add(2**k+off)
for r in rs:
 ell=0;m=ceildiv(12994*r,10000)
 dl=ceildiv(1260*r,10000);H=2599*r//2000;w=0
 kappa=(m-1).bit_length()+1
 assert dl<=H<dl+m and w<m
 assert dl>=kappa+1
 capacity=ell*w+dl+capped_sum(dl,m,H)-1-m*kappa
 assert capacity>=r*r
 assert m<=F(13,10)*r and ell<=F(461,1000)*r
 assert kappa+2<=r.bit_length()+4
 assert m<=F(6497,5000)*r+1
 assert m+dl<=F(7127,5000)*r+2
 assert H<=h*r and w<=y*r
 assert H-w>2*r.bit_length()
 assert F(7,10)*r>4*r.bit_length()+35
 assert ell==0
 K=2**13*(2*r+(r*r-1).bit_length()+30)
 assert 2*(m+1)*H+K<=4*((r-1)**2+1)
print(json.dumps({'small_closed_sum_cases':small,'main_schedule_cases':len(rs),'all_checks_passed':True,'capacity_coefficient':str(cap),'time_tree_coefficient':str(beta+delta),'classical_table_cap':str(h)}))
