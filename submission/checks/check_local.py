#!/usr/bin/env python3
"""Bounded exact identities supporting, not replacing, PROOF.md."""
import resource
resource.setrlimit(resource.RLIMIT_AS,(768<<20,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(50,)*2)
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations,product
from math import factorial,comb
from hashlib import sha256
from functools import lru_cache
import json,subprocess,time
from common import parameters,arity,clog

P=Path(__file__).resolve().parents[1]
started=time.process_time()
counts={}
def count(k, n=1): counts[k]=counts.get(k,0)+n

@lru_cache(maxsize=20000)
def gh(A,z,j):
    g=h=F(1)
    for _ in range(j):
        g,h=(1-F(2*z,A))*g+F(2*(A-z),A)*h,-F(2*z,A)*g+(1-F(2*z,A))*h
    assert F(z,A)*g*g+F(A-z,A)*h*h==1
    return g,h

def encode(D):
    C=tuple(sorted(D)); r=C.index(D[0]); rest=tuple(x for x in C if x!=D[0])
    return C,r,tuple(rest.index(x) for x in D[1:])

def decode(C,r,pi):
    rest=tuple(x for i,x in enumerate(C) if i!=r)
    return (C[r],)+tuple(rest[i] for i in pi)

# A separate direct reflection implementation checks the recurrence and every
# recovered column. The coherent endpoint register itself is never measured.
for A in (2,4,8):
    for m in range(1,A+1):
        fiber=tuple(range(m))
        for a in range(1,min(3,m)+1):
            z=m-a
            for j in range(4):
                g,h=gh(A,z,j)
                history_columns={}
                for D in permutations(fiber,a):
                    marked=set(fiber)-set(D)
                    vec=[F(1)]*A
                    for _ in range(j):
                        vec=[-x if y in marked else x for y,x in enumerate(vec)]
                        mean=sum(vec)/A
                        vec=[2*mean-x for x in vec]
                    assert all(x==(g if y in marked else h) for y,x in enumerate(vec))
                    for y in range(A):
                        if y in marked:continue
                        if y in fiber:
                            ell=D.index(y);history=('inside',ell)
                            cleared=y^D[ell]
                        else:
                            history=('outside',y);cleared=y^y
                        assert cleared==0
                        history_columns.setdefault(history,[]).append((D,vec[y]))
                        count('recovered_columns')
                for columns in history_columns.values():
                    assert len(columns)==factorial(m)//factorial(m-a)
                    assert all(coef==h for D,coef in columns)
                    count('scalar_identity_maps')
        if m>=4:
            rows={}
            for D in permutations(fiber,4):
                C,r,pi=encode(D)
                # Explicit compute-encode / XOR-decode cleanup.
                old=tuple(x^y for x,y in zip(D,decode(C,r,pi)))
                assert old==(0,0,0,0)
                rows.setdefault((C,pi),set()).add(r)
                labels={x:13+8*(x*x+7*x) for x in fiber}
                assert labels[D[0]]==labels[C[r]]
                count('old_index_cleanup_columns')
            assert all(rs=={0,1,2,3} for rs in rows.values())
            coeff_sq=F(1,(m-1)*(m-2)*(m-3))
            for x in fiber:
                assert sum(coeff_sq for C,pi in rows if x in C)==1
                count('subset_povm_diagonals')
            assert 6*coeff_sq==F(1,comb(m-1,3))

# Exact averaged schedule costs use probabilities from the rational recurrence.
# Costs and success may correlate within a trial; only independent fresh coins
# and scalar failure recovery are used by this recurrence.
for A in (4,8,16,32,64):
    jmax=1<<clog(A)//2 if clog(A)%2==0 else 1<<((clog(A)+1)//2)
    for z in range(1,A):
        failure=F(1);EH=F(0)
        for J in [1<<r for r in range(clog(jmax)+1)]:
            p=sum(F(z,A)*gh(A,z,j)[0]**2 for j in range(J))/J
            repeats=24 if J==jmax else 2
            for _ in range(repeats):
                EH+=failure*F(J+1,2)
                failure*=1-p
        assert failure<=F(3,4)**24
        assert EH*EH<=F(1600*A,z)
        count('exact_schedules')

# Full carries with common residues, including a negative difference.
for p in range(1,4):
    for b in range(1,4):
        for r0,r1 in product(range(1<<p),repeat=2):
            tables=[tuple(r0+(1<<p)*x for x in (7,2)),
                    tuple(r1+(1<<p)*x for x in (3,8,1,12))]
            rho=(r0+r1)%(1<<p);carry=(r0+r1)//(1<<p)
            for x,y in product(range(2),range(4)):
                full=tables[0][x]+tables[1][y]
                val=(carry+(tables[0][x]-r0)//(1<<p)+(tables[1][y]-r1)//(1<<p))%(1<<b)
                assert val==(full>>p)%(1<<b)
                assert (rho+(1<<p)*val)==full% (1<<(p+b))
                count('carry_predicates')

# Distinct binary incidence rows with arbitrary fixed carry offsets. Conditioning
# on a completed high table is deliberately absent.
for M in (2,4):
    for rows in ((0,1,3,7),(1,2,4,7),(0,2,5,6,7)):
        offsets={r:(r*r+3*r)//2 for r in rows}
        zs=[]
        for high in product(range(M),repeat=3):
            labels={r:(offsets[r]+sum(high[i] for i in range(3) if r>>i&1))%M for r in rows}
            for X in rows:
                zs.append(sum(labels[y]==labels[X] for y in rows if y!=X))
        lam=F(len(rows)-1,M)
        assert F(sum(zs),len(zs))==lam
        assert F(sum(z*z for z in zs),len(zs))-lam*lam==lam*(1-F(1,M))
        count('carry_incidence_moment_laws')

for M in (2,4):
    rowsets=((0,1,3,6),(1,2,4,7))
    for outcomes in product(range(2),repeat=2):
        hist={v:0 for v in product(range(M),repeat=2)}
        for high in product(range(M),repeat=6):
            ds=[]
            for j,eta in enumerate(outcomes):
                a,b=rowsets[j][2*eta:2*eta+2]
                ds.append((3+j+sum((((b>>i)&1)-((a>>i)&1))*high[3*j+i] for i in range(3)))%M)
            hist[tuple(ds)]+=1
        assert len(set(hist.values()))==1
        count('independent_qubitized_laws')

# A mixed one-bit pivot and genuinely nonlinear four-row lookup, with common
# constant offsets. Exact query support contains every measured full fiber.
for C in range(4):
    for delta in (1,3):
        for table in product(range(4),repeat=4):
            for residue in range(2):
                S={((residue-C-table[y])%2,y) for y in range(4)}
                coarse={(x,y) for x,y in product(range(2),range(4)) if (C+delta*x+table[y])%2==residue}
                assert S==coarse
                for e in range(residue,4,2):
                    full={(x,y) for x,y in product(range(2),range(4)) if (C+delta*x+table[y])%4==e}
                    assert full<=S
                count('mixed_query_supports')

# Large widths are NORMALIZED: do not allocate 2^b, 2^q or profiles at them.
widths=list(range(1,20001))+[2**j+d for j in range(16,257) for d in (-1,0,1)]
for b in widths:
    f,k,q,c,u,t=parameters(b)
    assert b+c+6<=q<=b+c+7
    assert 2*(f-1)-(f-1)//4<b+c+6
    assert f<=5*b and t<=b
    assert F(f*(8*b+8),8*b+7)<f+1
    assert F(2,63*(b+1))+F(3,64*(b+1)**3)<F(1,8*(b+1))
    assert (c+3)**2<=9*(b+1)
    assert F(1,1<<t)<=F(32*u,k)
    if t:assert 16*u*(1<<t)<=k<16*u*(1<<(t+1))
    # Rational square comparisons for all constants in the 512 certificate.
    assert 120**2*6<300**2 and 576**2<73**2*63 and 300+73<512
    if b>=4096:assert 12*(f+1)<=7*b
    if b<=512:
        direct=next(x for x in range(4,5*b+1) if 2*x-x//4>=b+c+6)
        assert direct==f
    count('normalized_parameter_certificates')

assert F(3,4)**8<F(1,8)
assert F(2401,5184)<F(1,2)
assert F(79,15625)*16384>42 and F(79,15625)>F(4,16384)
assert F(118,100)**2<F(177,125)
out={'status':'PASS','timestamp':subprocess.check_output(['date','+%Y-%m-%d %H:%M:%S %Z (%z)'],text=True).strip(),
     'counts':counts,'cpu_seconds_used':time.process_time()-started,
     'limits':{'cpu_seconds':50,'address_space_bytes':768<<20},
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'common_sha256':sha256((P/'checks/common.py').read_bytes()).hexdigest(),
     'scope':'Finite exact identities and normalized parameter guards; not a compiled circuit or all-N proof.'}
(P/'local-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
