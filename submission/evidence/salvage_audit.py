"""Exact finite four-input salvage diagnostics; not asymptotic certification."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import isqrt
import cmath,json
from pathlib import Path

def corr(m,d):return F(2*m**3+m,3)-m*d*d+F(d**3-d,2)
def primary(m,d):
    if d>=m//2:return F(0)
    return F(1) if d==0 else F(m,2*(m-d))
def salvage(m,d):
    if d>=m//2:return F(0)
    return F(1) if d==0 else corr(m,0)/(2*corr(m,d))

def group_law(m):
    law=defaultdict(F)
    for a,b,c,d in product(range(m),repeat=4):
        base=F(1,m**4)
        for f1,f2 in product((0,1),repeat=2):
            if f1==f2==0:
                delta=abs(a+b-c-d);p=salvage(m,delta)
                law[(f1,f2,0),()]+=base*F(1,4)*(1-F(1,2)*p)
                if p:law[(f1,f2,1),(delta,)]+=base*F(1,8)*p
            else:
                p1=primary(m,abs(a-b)) if f1 else F(0)
                p2=primary(m,abs(c-d)) if f2 else F(0)
                for k1,k2 in product((0,1),repeat=2):
                    probability=(p1 if k1 else 1-p1)*(p2 if k2 else 1-p2)
                    if not probability:continue
                    labels=(() if not k1 else (abs(a-b),))+(() if not k2 else (abs(c-d),))
                    law[(f1,f2,k1,k2),labels]+=base*F(1,4)*probability
    patterns=defaultdict(dict)
    for (flags,labels),p in law.items():
        if p:patterns[flags][labels]=p
    assert sum(law.values())==1
    checks=0
    for flags,rows in patterns.items():
        count=len(next(iter(rows)))
        total=sum(rows.values());expected=total/F(m//2)**count
        for labels in product(range(m//2),repeat=count):
            assert rows.get(labels,F(0))==expected
            checks+=1
    mean=sum(len(labels)*p for (flags,labels),p in law.items())
    assert mean==F(13,24)+F(1,48*m*m)
    return checks,len(patterns),str(mean)


def capacity(ell):return ell+sum(72*j//25 for j in range(ell))
def parameters(n,m):
    low,high=1,m-1
    while low<high:
        mid=(low+high)//2
        if capacity(mid)>=m-1:high=mid
        else:low=mid+1
    ell=low;target=m-1-ell
    lam=(1024*(n+1)-1).bit_length();final=(1<<32)*lam
    lengths=[(final*739**t+100**t-1)//100**t for t in range(ell,-1,-1)]
    widths=[];remaining=target
    for i in range(ell):
        b=min(72*(ell-i-1)//25,remaining);widths.append(b);remaining-=b
    assert remaining==0
    return ell,final,lengths,widths


def main():
    correlation_checks=0
    for m in range(2,65,2):
        triangle=[min(s+1,2*m-1-s) for s in range(2*m-1)]
        c0=sum(t*t for t in triangle)
        for d in range(m+1):
            actual=sum(triangle[i]*triangle[i+d] for i in range(len(triangle)-d))
            assert actual==corr(m,d)
            correlation_checks+=1
        for d in range(m//2):assert 2*corr(m,d)>=c0
    laws=[]
    for m in (4,8):
        count,patterns,mean=group_law(m)
        laws.append(dict(middle_width=m,conditional_output_records=count,flag_patterns=patterns,exact_mean_outputs=mean))
    # Exact phase-state density identities, including common nonzero offsets.
    phase_checks=0;max_error=0.0
    for modulus in (5,8,13):
        for secret in range(modulus):
            for a,b,c,d in product(range(4),repeat=4):
                offset=3;scale=2
                f1=2*offset+scale*(a+b);f2=2*offset+scale*(c+d)
                z1=cmath.exp(2j*cmath.pi*secret*f1/modulus)
                z2=cmath.exp(2j*cmath.pi*secret*f2/modulus)
                v=[z2/2**0.5,z1/2**0.5]
                if f1<f2:v.reverse()
                expected=cmath.exp(2j*cmath.pi*secret*scale*abs(a+b-c-d)/modulus)
                for i in (0,1):
                    for j in (0,1):
                        w=[1/2**0.5,expected/2**0.5]
                        error=abs(v[i]*v[j].conjugate()-w[i]*w[j].conjugate())
                        max_error=max(max_error,error);assert error<1e-12
                phase_checks+=1
    parameter_cases=stage_checks=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            assert 0<=m-1-ell and capacity(ell)>=m-1
            assert capacity(ell-1)<m-1
            assert 36*max(0,ell-2)**2<=25*n
            assert sum(widths)==m-1-ell
            assert sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                t=ell-i;k=1<<b;qpower=F(739,100)**(t-1)
                assert k<=qpower
                lower=F(13,96)*(lengths[i]-3*k)
                upper=F(lengths[i],2)
                gap=lower-lengths[i+1]
                assert gap>=final*qpower/4096
                assert upper<=4*final*qpower
                assert gap*gap/(4*upper)>=F(final,1<<28)
                assert width-b>=2
                width-=b+1;stage_checks+=1
            assert width==1
            parameter_cases+=1
    partial=F(842,1215)
    assert F(69,100)<partial and partial+F(1,6804)<F(347,500)
    assert 739*2707>8*250000
    x=F(57,500)*F(347,500)
    exp_upper=1+x+x*x/(2*(1-x/3))
    assert 739*exp_upper<800
    assert F(1443,500)*F(5,6)==F(481,200)
    assert F(13,96)*F(739,100)-1==F(7,9600)
    assert F(7,9600)>F(1,2048)
    out=dict(scope='Finite exact instrument/parameter and numerical density diagnostics; no asymptotic or device certification.',
             triangle_correlation_counts=correlation_checks,conditional_group_laws=laws,
             sum_salvage_density_checks=phase_checks,maximum_numeric_density_error=max_error,
             parameter_cases=parameter_cases,exact_stage_margin_checks=stage_checks,
             exact_exponential_coefficient='481/200')
    Path(__file__).with_name('salvage_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
