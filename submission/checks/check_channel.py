#!/usr/bin/env python3
"""Exact ambient-space U reflection and recovered Kraus columns, including scratch."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import itertools,json,resource,sys
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(60,)*2)
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'replay'))
from check_preparation import pivot_indices,operations,run,subset_label
counts=dict(ambient_reflection_columns=0,grover_columns=0,failed_Kraus_columns=0,success_edges=0,phase_labels=0)
def had(v,bit):
 out=v[:];d=1<<bit
 for i in range(len(v)):
  if not i&d:out[i],out[i|d]=v[i]+v[i|d],v[i]-v[i|d]
 return out
def perm(v,ops,q,t,inv=False):
 out=[F(0)]*len(v)
 for idx,x in enumerate(v):
  y,z=run(ops,idx&((1<<q)-1),idx>>q,1<<t,inverse=inv)
  out[y|(z<<q)]+=x
 return out
def reflect(v,ops,q,t,free):
 v=perm(v,ops,q,t,True)
 for bit in free:v=had(v,bit)
 v=[x if i==0 else -x for i,x in enumerate(v)]
 for bit in free:v=had(v,bit)
 v=perm(v,ops,q,t)
 return [x/(1<<len(free)) for x in v]
for b,q,labels in [(1,3,(1,0,1)),(2,3,(1,2,3)),(2,4,(1,2,1,1)),(3,4,(1,2,4,3)),(3,5,(1,2,0,5,6))]:
 M=1<<b;pivs=pivot_indices(labels,b)
 fibers={}
 for x in range(1<<q):fibers.setdefault(subset_label(labels,x,M),set()).add(x)
 for t in range(len(pivs)+1):
  ps=pivs[:t];free=[j for j in range(q) if j not in ps];A=1<<len(free)
  for r in range(1<<t):
   ops=operations(labels,ps,r);S={x for x in range(1<<q) if subset_label(labels,x,1<<t)==r}
   assert len(S)==A
   # Every ambient basis column, including dirty scratch/pivots.
   for basis in range(1<<(q+t)):
    vec=[F(0)]*(1<<(q+t));vec[basis]=1
    got=reflect(vec,ops,q,t,free)
    expected=[F(2,A) if basis in S and i in S else F(0) for i in range(len(vec))]
    expected[basis]-=1
    assert got==expected;counts['ambient_reflection_columns']+=1
   for e,Fiber in fibers.items():
    if e%(1<<t)!=r:continue
    m=len(Fiber);z=m-1;g=h=F(1)
    for j in range(4):
     for x in Fiber:
      vec=[F(1) if y in S else F(0) for y in range(1<<(q+t))]
      for _ in range(j):
       vec=[-a if y in Fiber and y!=x else a for y,a in enumerate(vec)]
       vec=reflect(vec,ops,q,t,free)
      assert all(a==(g if y in Fiber and y!=x else h) if y in S else a==0 for y,a in enumerate(vec))
      counts['grover_columns']+=1
      # Each diagonal or outside failure record acts by SAME h on every x.
      assert vec[x]==h
      for y in S-Fiber:assert vec[y]==h
      counts['failed_Kraus_columns']+=1+len(S-Fiber)
     for u,v in itertools.combinations(sorted(Fiber),2):
      assert u!=v
      counts['success_edges']+=1
      # Distinct full signed lifts; low congruence never replaces phase.
      full=[a+M*(idx-2) for idx,a in enumerate(labels)]
      Au=sum(a*((u>>idx)&1) for idx,a in enumerate(full))
      Av=sum(a*((v>>idx)&1) for idx,a in enumerate(full))
      assert (Av-Au)%M==0
      counts['phase_labels']+=1
     g,h=(1-F(2*z,A))*g+2*(1-F(z,A))*h,-F(2*z,A)*g+(1-F(2*z,A))*h
result=dict(status='PASS',counts=counts,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),limits=dict(address_space_bytes=512<<20,cpu_seconds=60),scope='Exact finite rational ambient reflection and Kraus columns. Not a full Clifford+T compilation or asymptotic proof.')
(HERE/'results'/'channel.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
