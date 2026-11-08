"""Branchwise ready/pending streaming checks at small group sizes.
This checks controller conservation/collimation, not the quantum instrument law.
"""
from collections import defaultdict,deque
from random import Random
from fractions import Fraction as F
import json
class Cutoff(Exception):pass
rng=Random(849201);total_groups=0;total_roots=0;cases=0;maxready=0;pending_changes=0
for W in [4,8,16,32]:
 for widths in [[0],[1],[3],[2,1],[0,2,1],[2,0,2]]:
  ell=len(widths);ps=[0]
  for b in widths:ps.append(ps[-1]+b)
  slots=[defaultdict(list) for _ in widths];ready=[deque() for _ in widths];pending=[None]*ell
  A=[0]*(ell+1);drop=[0]*ell;produced=[0]*ell;groups=[0]*ell
  def key(t,i):return ((t[1]-t[0])>>ps[i])%2**widths[i]
  def nextitem(i):
   global pending_changes,maxready
   if i==0:
    if A[0]>=50000:raise Cutoff()
    A[0]+=1;return (0,rng.randrange(2**(sum(widths)+6)))
   lev=i-1
   def deliver():
    A[i]+=1
    return ready[lev].popleft()
   if ready[lev]:return deliver()
   if pending[lev] is not None:item=pending[lev];pending[lev]=None
   else:item=nextitem(lev)
   while True:
    assert (item[1]-item[0])%2**ps[lev]==0
    k=key(item,lev);bucket=slots[lev][k]
    if len(bucket)<W-1:
     bucket.append(item);item=nextitem(lev);continue
    inputs=[*bucket,item];bucket.clear();groups[lev]+=1
    # Stress all legal output shapes, not their quantum probabilities.
    typ=rng.randrange(4)
    if typ in [0,1]:
     a,b=inputs[:2]
     ready[lev].append((a[0]+b[1],a[1]+b[0]))
     slots[lev][k].extend(inputs[2:]);drop[lev]+=2;produced[lev]+=1
    elif typ==2:
     u=rng.randrange(1,W//2)
     for j in range(u):
      a,b=inputs[2*j:2*j+2]
      ready[lev].append((a[0]+b[1],a[1]+b[0]))
     recycled=tuple(sum(t[j] for t in inputs[2*u:]) for j in [0,1])
     pending[lev]=recycled
     if key(recycled,lev)!=k:pending_changes+=1
     drop[lev]+=W-1;produced[lev]+=u
    else:
     item=tuple(sum(t[j] for t in inputs) for j in [0,1])
     drop[lev]+=W-1;continue
    assert len(ready[lev])<=W//2
    assert all((t[1]-t[0])%2**ps[i]==0 for t in ready[lev])
    maxready=max(maxready,len(ready[lev]));return deliver()
  for j in range(1000):
   try:root=nextitem(ell)
   except Cutoff:break
   assert (root[1]-root[0])%2**ps[-1]==0
   for i,b in enumerate(widths):
    occ=sum(map(len,slots[i].values()))+(pending[i] is not None)
    assert all(len(v)<=W-1 for v in slots[i].values())
    assert occ<=(W-1)*2**b+1
    assert A[i]==drop[i]+occ
    assert produced[i]==A[i+1]+len(ready[i])
    assert 2*A[i+1]<=A[i]
   assert sum(groups)<=A[0]
   total_roots+=1
  total_groups+=sum(groups);cases+=1
# New fixed-W schedule: exact rational endpoint inequalities.
a,b,d,y=map(F,['.4614','.8379','.4997','.4995']);C=F(10001,10000)
assert a*y+b*d+b*b/2==F(200041227,200000000)>F(10001,10000)
assert C*a+b==F(64967307,50000000)<F(6497,5000)
assert b+d==F(836,625)
assert F(3,32768)<F(1,10000)
print(json.dumps({'controller_cases':cases,'completed_roots':total_roots,'instrument_shapes':total_groups,'max_ready_tested':maxready,'pending_key_changes':pending_changes,'all_checks_passed':True}))
