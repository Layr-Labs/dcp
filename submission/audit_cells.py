"""Exact small-group fractional-cover and type checks; no quantum hardware."""
from fractions import Fraction as F
from itertools import combinations,product
from math import factorial,comb
import json

def matchings(xs):
 if not xs:yield ();return
 a=xs[0]
 for j in range(1,len(xs)):
  b=xs[j]
  for rest in matchings(xs[1:j]+xs[j+1:]):yield ((a,b),)+rest

counts=0
for W in [4,6,8]:
 q=W//2;weights=[F(0)]*(2**W);types={}
 def addcell(support,weight,gamma,drop):
  global counts
  support=set(support);counts+=1
  for x in support:weights[x]+=weight
  types[gamma,drop]=types.get((gamma,drop),F(0))+weight*len(support)/2**W
 for a,b in combinations(range(W),2):
  addcell([x for x in range(2**W) if ((x>>a)^(x>>b))&1],F(1,q*q),1,2)
 for u in range(1,q):
  for selected in combinations(range(W),2*u):
   block=set(range(W))-set(selected)
   for pairs in matchings(selected):
    support=[]
    for values in product([0,1],repeat=u+1):
     x=sum(values[-1]<<j for j in block)
     for v,(a,b) in zip(values,pairs):x+=(v<<a)+((1-v)<<b)
     support.append(x)
    weight=F((q-u)**2*factorial(W-2*u),q*q*factorial(W-u))
    addcell(support,weight,u,W-1)
 addcell([0,2**W-1],F(1),0,W-1)
 assert all(t==1 for t in weights)
 assert sum(types.values())==1
 gamma=sum(g*p for (g,d),p in types.items());drop=sum(d*p for (g,d),p in types.items())
 b=F(comb(W,q),2**W)
 assert gamma==F(3,2)-F(1,W)-b
 assert drop==F(3*(W-1),W)
 assert all(2*g<=d for g,d in types)
for q in range(1,129):
 assert 2*sum(j**3*comb(2*q,q+j) for j in range(1,q+1))==q*q*comb(2*q,q)
 b=F(comb(2*q,q),4**q)
 assert b*b*(3*q+1)<=1
W=2**28;q=W//2;s=20066
assert s*s<=3*q+1
assert F(3,2)-F(1,W)-F(1,s)>=F(8192,16385)*F(3*(W-1),W)
assert (3*s-32770)*W+16382*s>0
print(json.dumps({'enumerated_cells':counts,'basis_inputs':sum(2**W for W in [4,6,8]),'cubic_identity_cases':128,'large_group_rational_bound_passed':True,'all_checks_passed':True}))
