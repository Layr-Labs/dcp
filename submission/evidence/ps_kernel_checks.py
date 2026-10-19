"""Exact finite checks of the polynomial-space combination kernel.
These checks supplement the proof; they do not constitute asymptotic certification.
"""
from collections import defaultdict,Counter
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,gcd,isqrt
from pathlib import Path
import json

def coefficient(k,B,z):
    if z<0:return 0
    return sum((-1)**h*comb(k,h)*comb(z-h*B+k-1,k-1)
               for h in range(k+1) if z-h*B>=0)

def difference_mass(j,B,t):
    return F(coefficient(2*j,B,t+j*(B-1)),B**(2*j))

def subset_sum(v,u):
    return sum(x for i,x in enumerate(u) if (v>>i)&1)

def flatten_checks():
    cases=0; smallest=None
    for B in (4,8,16,32):
        for j in range(1,7):
            counts=[1]
            for _ in range(2*j):
                nxt=[0]*(len(counts)+B-1)
                for a,c in enumerate(counts):
                    for x in range(B):nxt[a+x]+=c
                counts=nxt
            assert sum(counts)==B**(2*j)
            for z,c in enumerate(counts):assert coefficient(2*j,B,z)==c
            r=2*j
            for t in range(B//2):
                p=difference_mass(j,B,t)
                assert p==difference_mass(j,B,-t)
                assert p>=F(1,64*r*B)
                observed=p if t==0 else 2*p
                coin=F(1,64*r*B)/observed
                assert 0<coin<=1
                assert observed*coin==F(1,64*r*B)
                ratio=p*64*r*B
                smallest=ratio if smallest is None else min(smallest,ratio)
                cases+=1
    return {'coefficient_and_flattening_cases':cases,'minimum_density_to_lower_bound_ratio':str(smallest)}

def moment_checks():
    tested=0; maximum=F(0)
    for r,K in ((3,2),(4,2),(4,4),(5,2),(5,4),(6,2)):
        D=1<<r; lam=F(D,K)
        pairs=[(v,w) for v in range(D) for w in range(v+1,D)
               if v.bit_count()==w.bit_count()]
        moments={pair:[0,0,0] for pair in pairs}
        for u in product(range(K),repeat=r):
            bucket=defaultdict(list)
            for v in range(D):bucket[(v.bit_count(),subset_sum(v,u)%K)].append(v)
            key={v:(weight,residue) for (weight,residue),vs in bucket.items() for v in vs}
            for v,w in pairs:
                if key[v]!=key[w]:continue
                m=len(bucket[key[v]]); a=moments[(v,w)]
                a[0]+=1;a[1]+=m;a[2]+=m*m
        for (v,w),(count,total,squares) in moments.items():
            assert count==K**(r-1)
            mean=F(total,count)
            expected=2+F(comb(r,v.bit_count())-2,K)
            variance=F(squares,count)-mean*mean
            assert mean==expected
            assert variance<=2*lam
            maximum=max(maximum,variance/(2*lam))
            tested+=1
    return {'conditional_bucket_moment_cases':tested,'maximum_variance_to_bound_ratio':str(maximum)}

def exact_kernel():
    r,B,K,H=4,8,2,4
    D=1<<r
    pairs=[(v,w) for v in range(D) for w in range(v+1,D) if v.bit_count()==w.bit_count()]
    Bnext=B//(2*K); actual=[F(0)]*Bnext; ideal=[F(0)]*Bnext
    clipped=0
    for u in product(range(B),repeat=r):
        sums=[subset_sum(v,u) for v in range(D)]
        sizes=Counter((v.bit_count(),sums[v]%K) for v in range(D))
        for v,w in pairs:
            if (sums[v]-sums[w])%K:continue
            delta=abs(sums[v]-sums[w])
            if delta>=B//2:continue
            j=(v^w).bit_count()//2
            mass=difference_mass(j,B,delta)*(1 if delta==0 else 2)
            flatten=F(1,64*r*B)/mass
            piece=F(2,D*(H-1))*flatten/F(B**r)
            ideal[delta//K]+=piece
            if sizes[(v.bit_count(),sums[v]%K)]<=H:actual[delta//K]+=piece
            else:clipped+=1
    expected=F(2*len(pairs),D*(H-1)*64*r*B)
    assert all(x==expected for x in ideal)
    assert all(0<=a<=b for a,b in zip(actual,ideal))
    assert clipped>0
    # XOR matching: each unordered pair occurs for exactly one nonzero mask.
    matching_cases=0
    for m in range(2,34):
        P=1<<(m-1).bit_length()
        for x,y in combinations(range(m),2):
            masks=[a for a in range(1,P) if (x^a)==y]
            assert masks==[x^y]
            matching_cases+=1
    return {'ideal_uniform_mass_per_label':str(expected),
            'clipped_kernel_mass_per_label':[str(x) for x in actual],
            'clip_exercised_input_pair_cases':clipped,'xor_matching_pairs':matching_cases,
            'scope':'Small artificial cap tests kernel domination; production H=16*2^(r-l).'}

def source_conversion():
    cases=0
    for N in range(2,97):
        for D in range(1,N+1):
            if N%D:continue
            Q=N//D
            for r in range(D):
                for u in range(Q):
                    s=r+D*u
                    actual=Counter()
                    for x in range(N):
                        z=((x+s)%N-r)%N
                        a,ra=divmod(x,D);b,rb=divmod(z,D)
                        assert ra==rb
                        actual[(ra,a,b)]+=1
                    expected=Counter({(t,a,(a+u)%Q):1 for t in range(D) for a in range(Q)})
                    assert actual==expected
                    cases+=1
    return cases

def crt_frequency():
    cases=0
    for N in range(3,1025):
        n=(N-1).bit_length();m=N.bit_length()-1
        b=isqrt((n+1)*(n+1))
        # Exercise every allowable J, rather than just one fixed schedule.
        v=(N&-N).bit_length()-1;M=N>>v
        if M==1:continue
        for J in range(v,m):
            A=1<<J
            for h in range(n+3):
                a=pow(2,J-v-h,M)
                t=(a if a&1 else a+M)%N
                assert gcd(t,N)==1
                assert (A*pow(t,-1,N))%N==((1<<v)*pow(2,h,M))%N
                cases+=1
    return cases

def reconstruction_and_parameters():
    cases=0; parameters_checked=0
    for n in list(range(1,257))+[512,1024,4096,16384]:
        h=(n+1).bit_length()
        value=(n+1)*h
        b=isqrt(value)+(isqrt(value)**2<value)
        d=(n+b)//(b+1)
        q=512*(d+2)*h
        rmax=b+q
        retry=(1<<40)*(n+2)**12
        roots=(1<<20)*(n+2)**8*(1<<(4*(d+2)))
        R=16*roots*(retry*(rmax+1))**(d+2)
        assert rmax+1<=(1<<10)*(n+2)**2
        assert R.bit_length()<=64*(d+2)*h
        assert (256*R).bit_length()<=q
        assert retry//(8192*rmax*rmax)>(256*R).bit_length()
        parameters_checked+=1
    for N in range(2,2049):
        n=(N-1).bit_length();h=(n+1).bit_length()
        z=(n+1)*h;b=isqrt(z)+(isqrt(z)**2<z)
        for secret in (range(N) if N<=96 else (0,1,N//2,N-1)):
            a,D,Q=0,1,N
            iterations=0
            while Q>1:
                m=Q.bit_length()-1
                ell=(m+b-1)//(b+1)
                J=m-1-ell
                v=(Q&-Q).bit_length()-1
                kappa=(secret-a)//D
                assert (secret-a)%D==0
                if v<=J:
                    modulus=Q>>v
                    residue=kappa%modulus
                else:
                    modulus=Q//(1<<J)
                    assert modulus<1<<(ell+2)
                    residue=kappa%modulus
                a+=D*residue;D*=modulus;Q=N//D
                iterations+=1
                assert N%D==0 and 0<=a<D and a==secret%D
                assert iterations<=n+1
            assert a==secret
            cases+=1
    compression=0
    for r in range(2,9):
        for v in range(1<<r):
            for w in range(v+1,1<<r):
                if v.bit_count()!=w.bit_count():continue
                diff=v^w;pivot=(diff&-diff).bit_length()-1
                def transform(x):
                    x^=v
                    if (x>>pivot)&1:x^=diff^(1<<pivot)
                    return x
                assert transform(v)==0
                assert transform(w)==1<<pivot
                compression+=1
    return {'full_secret_reconstruction_cases':cases,
            'global_parameter_cap_cases':parameters_checked,
            'exact_two_mask_compressions':compression}

def main():
    result={'scope':'Finite exact diagnostics; no official review or asymptotic proof.',
            **flatten_checks(),**moment_checks(),'kernel':exact_kernel(),
            'source_conversion_configurations':source_conversion(),
            'all_modulus_crt_frequency_cases':crt_frequency(),**reconstruction_and_parameters()}
    Path(__file__).with_name('ps_kernel_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
