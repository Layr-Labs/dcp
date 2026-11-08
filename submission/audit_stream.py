from collections import defaultdict
from fractions import Fraction as F
from random import Random
import json
# Independent exact basis check of the inherited instrument's f/h formulas.
for x in range(8):
 bits=[(x>>j)&1 for j in range(3)]
 e1=bits[0]^bits[1];e2=bits[0]^bits[2]
 outcomes=[]
 for c in [0,1]:
  l1=(e1&e2)^((e1^e2)&c)
  l0=(e1&e2&c)^(e1&(1-e2))^((1-e1)&e2&(1-c))
  h=(e1&e2&l0)^((e1^e2)&l1)
  l=2*l1+l0
  assert (c^h)==(c if e1==e2==0 else 0)
  outcomes.append(l)
  if l:
   ab=[j for j in range(3) if j!=l-1]
   assert bits[ab[0]]!=bits[ab[1]]
 if e1==e2==0:assert outcomes==[0,0]
 else:assert len(set(outcomes))==2 and 0 not in outcomes
# Distribution-independent streaming flow and key collimation checks.
rng=Random(19373);cases=0;groups=0
for widths in ([0],[1],[4],[0,1,2],[2,2,2],[3,0,2]):
 ell=len(widths);ps=[0]
 for b in widths:ps.append(ps[-1]+b)
 slots=[defaultdict(list) for _ in widths];A=[0]*(ell+1);O=[0]*ell;G=[0]*ell
 def key(t,i):return ((t[1]-t[0])>>ps[i])%2**widths[i]
 def inject(t,i):
  A[i]+=1
  assert (t[1]-t[0])%2**ps[i]==0
  if i==ell:return
  while True:
   k=key(t,i);bucket=slots[i][k]
   if len(bucket)<2:bucket.append(t);return
   triple=[*bucket,t];bucket.clear();G[i]+=1
   l=rng.randrange(4)
   if l:
    a,b=[j for j in range(3) if j!=l-1]
    good=(triple[a][0]+triple[b][1],triple[a][1]+triple[b][0])
    leftover=triple[l-1]
    assert key(leftover,i)==k
    slots[i][k].append(leftover)
    O[i]+=1;inject(good,i+1);return
   t=tuple(sum(u[j] for u in triple) for j in [0,1])
   assert (t[1]-t[0])%2**ps[i]==0
 for j in range(20000):
  inject((0,rng.randrange(2**(sum(widths)+4))),0)
  for i,b in enumerate(widths):
   occ=sum(map(len,slots[i].values()))
   assert occ<=2*2**b
   assert all(len(v)<=2 for v in slots[i].values())
   assert A[i]==2*G[i]+occ
   assert O[i]==A[i+1]
  cases+=1
 groups+=sum(G)
# Exact schedule constants for the proposed streaming TRIAD configuration.
a,b,d,w=map(F,['.183','1.0404','.3533','.4995'])
assert a*w+b*d+b*b/2==F(10001979,10000000)>F(10001,10000)
assert F(75,53)*a+b==F(344331,265000)<F(12994,10000)
assert b+d==F(13937,10000)
assert 3**41<2**65 and 3**53>2**84
print(json.dumps({'source_injections':cases,'instrument_applications':groups,'all_checks_passed':True,'source_coefficient_upper':str(F(75,53)*a+b),'tree_coefficient':str(b+d)}))
