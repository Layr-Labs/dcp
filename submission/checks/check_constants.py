"""Exact constants for the draft; finite checks do not prove the whole solver."""
from fractions import Fraction as F
from pathlib import Path
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(45,45))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
start=time.process_time()
rho=F(3,4)
assert rho**4<F(1,2)
z=F(1,2**28)
bad_size=F(4096,9)*z*(1+z)/(1-z)**3
assert 9*rho**128<z and bad_size<F(1,2**18)
loss=F(1,1536)+F(1,24576)
assert loss==F(17,24576)<F(1,1024)
assert (F(1023,1024))**2>F(1,4)
assert 2*rho**4<F(3,4)
assert F(7,8)**16<F(1,4)
assert F(18,1)/((F(3,256))**2) == 131072
coarse=F(1,2**22)+F(1,2**18)+F(1,2**64)+F(1,2**24)+F(1,2**12)
assert coarse<F(1,2**11)
exception=F(1,2**256)+F(1,64)+F(1,2**62)+F(1,2**80)+coarse+F(1,2**80)+F(1,2**115)+F(1,2**76)
assert exception<F(3,128)
assert F(91,128)-exception>F(11,16)>F(2,3)


def ceil_log2(x):return (x-1).bit_length()


def levels(n):
    d=1<<n;lo,hi=0,n
    while lo<hi:
        mid=(lo+hi+1)//2
        if (64*n*3**mid)**2<=d:lo=mid
        else:hi=mid-1
    return lo


cases=0
for n in list(range(64,4097))+[8192,10000,20000]:
    d=1<<n;K=levels(n);A=3**K;H=128*K
    assert 1<=K<=n and 9*K>=n
    assert (64*n*A)**2<=d<(192*n*A)**2
    assert n-32*K<-64
    a=ceil_log2(2**24*(H+1));ell=2**17*a
    assert 4*H<=2**(a-22)
    r=ceil_log2(2**24*H*ell)
    assert H*ell<=2**(r-24)
    k_shadow=3*2**22*(n+32);Q=2**18*k_shadow
    assert Q%3==0
    cases+=1

# A coarse preparation cost recurrence in oracle units, not primitive gates.
cost=1
for j in range(1,1001):
    cost=3*cost+128*(j+1)
    assert cost<=161*3**j

# Physically possible N=4 clean shadow records, built from their Born probabilities.
# Each record is (Fourier label, X/Y basis, measured sign). At s=0 the X sign
# is +, and Y is fair. Duplicating this 16-record bank preserves every full mean.
cos4=(1,0,-1,0);sin4=(0,1,0,-1)
records=[]
for w in range(4):
    records += [(w,0,1)]*2 + [(w,1,1),(w,1,-1)]
assert len(records)==16


def score(record,t,u):
    w,beta,sign=record;cs=(cos4,sin4)[beta]
    return F(sign,10)*(11*(cs[(w*t)%4]-cs[(w*u)%4])
        +cs[(w*(2*t-u))%4]-cs[(w*(2*u-t))%4])


def canonical_first_wins(bank):
    # Classes {0,2} and {1,3}; first class has canonical representative 0.
    f=max(min(sum((score(r,t,u)for r in bank),F(0))/len(bank)for u in (1,3))for t in (0,2))
    return f>=0,f


full_wins,full_f=canonical_first_wins(records)
bad_record=(1,1,1)
sketch_wins,sketch_f=canonical_first_wins([bad_record,bad_record])
assert bad_record in records and full_wins and not sketch_wins
assert full_f==F(11,20) and sketch_f==F(-6,5)
assert full_f-F(1,1024)>F(1,64) and sketch_f+F(1,1024)<0
# All four secrets, including odd ones, use the same positive phase convention.
secret_fixtures=[]
for secret in range(4):
    bank=[]
    for w in range(4):
        for beta,cs in enumerate((cos4,sin4)):
            for sign in (1,-1):bank +=[(w,beta,sign)]*(1+sign*cs[(w*secret)%4])
    assert len(bank)==16
    for u in range(4):
        if (u-secret)%4 not in (0,2):
            assert sum((score(r,secret,u)for r in bank),F(0))/16==F(11,20)
    winner,margin=canonical_first_wins(bank)
    assert (0 if winner else 1)==secret%2
    misleading=next(r for r in bank if (0 if canonical_first_wins([r])[0]else 1)!=secret%2)
    secret_fixtures.append(dict(secret=secret,true_class=secret%2,full_score=str(margin),misleading_record=misleading))
# If pivot 0 is visited first, this sketch admits 1; the last pivot is wrong,
# but the full-shadow champion over [0,1] is 0. This is an interface fixture,
# not the production n<64 branch, which uses the inherited decoder.
out=dict(all_passed=True,arithmetic='exact fractions and integers',parameter_cases=cases,
    bad_size_bound=str(bad_size),relative_loss_bound=str(loss),coarse_failure_bound=str(coarse),
    main_success_lower=str(F(91,128)-exception),success_exceeds_11_16=True,
    all_secret_shadow_checks=secret_fixtures,
    physical_shadow_fixture=dict(modulus=4,secret=0,records=records,full_class_score=str(full_f),
        repeated_sketch_record=bad_record,sketch_class_score=str(sketch_f),visited=[0,1],
        last_pivot=1,full_shadow_champion=0,finite_precision_signs_preserved=True),
    scope='Constants and a clean-record comparison fixture; no production circuit or complete solver replay.',
    cpu_seconds=time.process_time()-start)
Path(__file__).with_name('constant-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ('main_success_lower','physical_shadow_fixture')},indent=2))
print('fixture_full_and_sketch',full_f,sketch_f)
