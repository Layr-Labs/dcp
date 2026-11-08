"""Stable radix/query joins checked against independent sorting and pair fibres.
Python integers are diagnostic references, not the bit-cost implementation.
"""
from bisect import bisect_left
import random,json

def radix(keys,lam,b):
 E=1<<lam;assert len(keys)==E and all(0<=k<(1<<b) for k in keys)
 wd=lam;bd=1<<wd
 assert b<=2*lam and len(range(0,b,wd))<=2;order=list(range(E))
 for shift in range(0,b,wd):
  counts=[0]*bd
  for x in order:counts[(keys[x]>>shift)&(bd-1)]+=1
  pos=[];acc=0
  for c in counts:pos.append(acc);acc+=c
  nxt=[None]*E
  for x in order:
   digit=(keys[x]>>shift)&(bd-1);nxt[pos[digit]]=x;pos[digit]+=1
  order=nxt
 return order

def joined(aa,bb,car,e,lam,b):
 E=1<<lam;mod=1<<b;order=radix(bb,lam,b)
 tx=[(e-car-a)%mod for a in aa];query=radix(tx,lam,b)
 lo=[None]*E;cnt=[None]*E;qi=di=0
 while qi<E:
  key=tx[query[qi]];qend=qi+1
  while qend<E and tx[query[qend]]==key:qend+=1
  while di<E and bb[order[di]]<key:di+=1
  dend=di
  while dend<E and bb[order[dend]]==key:dend+=1
  for z in range(qi,qend):lo[query[z]]=di;cnt[query[z]]=dend-di
  di=dend;qi=qend
 return order,lo,cnt

rng=random.Random(20261108);cases=0;empty=0;zeros=0;nontrivial=0
for lam in range(1,9):
 E=1<<lam
 for b in sorted({0,1,2,max(0,lam-1),lam,lam+1,2*lam}):
  mod=1<<b
  for pattern in range(16):
   if pattern==0:aa=[0]*E;bb=[0]*E
   elif pattern==1:aa=[(x*3)%mod for x in range(E)];bb=[(E-x-1)%mod for x in range(E)]
   elif pattern==2:aa=[(x//3)%mod for x in range(E)];bb=[(x//5)%mod for x in range(E)]
   else:aa=[rng.randrange(mod) for _ in range(E)];bb=[rng.randrange(mod) for _ in range(E)]
   car=pattern%2;e=rng.randrange(mod)
   order,lo,cnt=joined(aa,bb,car,e,lam,b)
   assert order==sorted(range(E),key=lambda y:(bb[y],y))
   sorted_keys=[bb[y] for y in order];pos=[None]*E
   for j,y in enumerate(order):pos[y]=j
   offset=0;ranks=[]
   for x in range(E):
    target=(e-car-aa[x])%mod
    partners=[y for y in range(E) if (aa[x]+bb[y]+car)%mod==e]
    assert lo[x]==bisect_left(sorted_keys,target) and cnt[x]==len(partners)
    if not partners:empty+=1
    for y in partners:ranks.append(offset+pos[y]-lo[x])
    offset+=cnt[x]
   assert sorted(ranks)==list(range(offset))
   if b==0:zeros+=1
   if offset and len(set(aa+bb))>1:nontrivial+=1
   cases+=1
storage_cases=storage_pairs=carry_cases=storage_zero=0
for lam in range(1,5):
 E=1<<lam
 for pp in [0,1,3,8,13]:
  for ww in [1,2,5,9]:
   for bb in sorted({0,1,min(ww,lam),min(ww,2*lam)}):
    if bb>ww:continue
    for pattern in range(6):
     ca=rng.randrange(1<<pp);cb=rng.randrange(1<<pp)
     if pattern==0:ca=cb=(1<<pp)-1
     ha=[rng.randrange(1<<ww) for _ in range(E)]
     hb=[rng.randrange(1<<ww) for _ in range(E)]
     if pattern==0:ha=hb=[(1<<ww)-1]*E
     car=(ca+cb)>>pp;mod=1<<bb;e=rng.randrange(mod)
     order,lo,cnt=joined([x%mod for x in ha],[y%mod for y in hb],car,e,lam,bb)
     cp=((ca+cb)%(1<<pp))+(e<<pp)
     assert 0<=cp<(1<<(pp+bb))
     rows=[];pos={y:j for j,y in enumerate(order)};off=0
     for x in range(E):
      for y in range(E):
       full=(ca+(ha[x]<<pp))+(cb+(hb[y]<<pp))
       if (full>>pp)%mod!=e:continue
       sv=ha[x]+hb[y]+car;hp=sv>>bb
       assert hp<(1<<(ww+1-bb))
       assert cp+(hp<<(pp+bb))==full
       rows.append((off+pos[y]-lo[x],hp,full));storage_pairs+=1
      off+=cnt[x]
     rows.sort()
     if len(rows)>=2:
      z=2*rng.randrange(len(rows)//2);a,bv=rows[z:z+2]
      assert a[0]+1==bv[0]
      assert (bv[2]-a[2])%(1<<(pp+bb))==0
      assert bv[1]-a[1]==(bv[2]-a[2])//(1<<(pp+bb))
     if car:carry_cases+=1
     if bb==0:storage_zero+=1
     storage_cases+=1
print(json.dumps({'radix_join_cases':cases,'zero_width_cases':zeros,'empty_query_fibres':empty,'nontrivial_nonempty_cases':nontrivial,'highpart_storage_cases':storage_cases,'highpart_pairs_verified':storage_pairs,'carry_one_cases':carry_cases,'storage_zero_window_cases':storage_zero,'all_checks_passed':True}))
