"""Exact finite pooled-sum instrument and quota diagnostics; not proof certification."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import math,json
from pathlib import Path

def corr(m,d):return F(2*m**3+m,3)-m*d*d+F(d**3-d,2)
def primary(m,d):return F(0) if d>=m//2 else (F(1) if d==0 else F(m,2*(m-d)))
def rescue(m,d):return F(0) if d>=m//2 else (F(1) if d==0 else corr(m,0)/(2*corr(m,d)))

def pooled_law(m,pairs):
    rows=defaultdict(F)
    for values in product(range(m),repeat=2*pairs):
        diffs=[abs(values[2*i]-values[2*i+1]) for i in range(pairs)]
        sums=[values[2*i]+values[2*i+1] for i in range(pairs)]
        weights=[(F(1,2),primary(m,d)/2,(1-primary(m,d))/2) for d in diffs]
        for cats in product(range(3),repeat=pairs): #0sum,1keptdifference,2discardeddifference
            probability=F(1,m**(2*pairs))
            for i,c in enumerate(cats):probability*=weights[i][c]
            if not probability:continue
            out=tuple(diffs[i] for i,c in enumerate(cats) if c==1)
            sum_positions=[i for i,c in enumerate(cats) if c==0]
            deltas=[abs(sums[sum_positions[j]]-sums[sum_positions[j+1]]) for j in range(0,len(sum_positions)-1,2)]
            probabilities=[rescue(m,d)/2 for d in deltas]
            for flags in product((0,1),repeat=len(deltas)):
                weight=probability
                for flag,prob in zip(flags,probabilities):weight*=prob if flag else 1-prob
                if weight:
                    labels=out+tuple(d for flag,d in zip(flags,deltas) if flag)
                    rows[(cats,flags),labels]+=weight
    assert sum(rows.values())==1
    patterns=defaultdict(dict)
    for (flags,labels),weight in rows.items():patterns[flags][labels]=weight
    records=0
    for flags,values in patterns.items():
        count=len(next(iter(values)));total=sum(values.values())
        expected=total/F(m//2)**count
        for labels in product(range(m//2),repeat=count):
            assert values.get(labels,F(0))==expected
            records+=1
    mean=sum(len(labels)*prob for (flags,labels),prob in rows.items())
    assert mean==F(7*pairs-1,24)+F(pairs-1,48*m*m)
    return len(patterns),records,str(mean)


def capacity(e):return e+sum(25*j//9 for j in range(e))
def parameters(n,m):
    lo,hi=1,m-1
    while lo<hi:
        mid=(lo+hi)//2
        if capacity(mid)>=m-1:hi=mid
        else:lo=mid+1
    ell=lo;lam=(1024*(n+1)-1).bit_length();final=(1<<36)*lam
    lengths=[(final*55**t+8**t-1)//8**t for t in range(ell,-1,-1)]
    widths=[];remaining=m-1-ell
    for i in range(ell):
        b=min(25*(ell-i-1)//9,remaining);widths.append(b);remaining-=b
    assert remaining==0
    return ell,final,lengths,widths


def main():
    patterns,records,mean=pooled_law(4,3)
    flags_checked=0
    for pairs in range(1,17):
        total=0
        for bits in range(1<<pairs):
            positions=[i for i in range(pairs) if bits>>i&1]
            z=len(positions);u=z//2
            actual_pairs=list(zip(positions[::2],positions[1::2]))
            assert len(actual_pairs)==u
            assert pairs-z+u<=pairs and z-2*u<=1
            total+=u;flags_checked+=1
        assert F(total,1<<pairs)==F(pairs-1,4)
    kernel_checks=0
    for m in range(4,65,2):
        tri=[min(s+1,2*m-1-s) for s in range(2*m-1)]
        for d in range(m+1):
            assert sum(tri[i]*tri[i+d] for i in range(len(tri)-d))==corr(m,d)
            kernel_checks+=1
        for d in range(m//2):assert 2*corr(m,d)>=corr(m,0)
    eps=F(1,4096);q=F(55,8)
    assert q*(F(7,48)-eps/6)-1==F(457,196608)>F(1,512)
    parameter_cases=stage_checks=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            assert capacity(ell)>=m-1>capacity(ell-1)
            assert 1000000*max(0,ell-2)**2<=720801*n
            assert sum(widths)==m-1-ell and sum(lengths[:-1])<2*lengths[0]
            width=m
            for i,b in enumerate(widths):
                qp=q**(ell-i-1);buckets=1<<b
                assert buckets<=qp
                pairs=F(lengths[i]-buckets,2)
                primary_lower=(1-eps)*pairs/4
                sum_lower=(1-eps)*pairs/2
                rescues_lower=(sum_lower-buckets)/2
                output_lower=primary_lower+(1-eps)*rescues_lower/6
                assert pairs>=final*qp
                assert rescues_lower>=final*qp/16
                assert output_lower>=lengths[i+1]
                for exponent in (eps*eps*pairs/8,eps*eps*pairs/4,eps*eps*rescues_lower/12):
                    assert exponent>=final*qp/(1<<32)
                assert width-b>=2
                width-=b+1;stage_checks+=1
            assert width==1;parameter_cases+=1
    assert F(842,1215)>F(69,100)
    assert F(842,1215)+F(1,6804)<F(347,500)
    x=F(2,9)*F(69,100)
    assert 1+x+x*x/2>F(64,55)
    x=F(109,500)*F(347,500)
    upper=1+x+x*x/(2*(1-x/3))
    assert upper<F(64,55)
    assert 849**2*25>18*1000**2
    assert F(1391,500)*F(849,1000)==F(1180959,500000)
    out=dict(scope='Exact finite pooling/conditional-output and quota diagnostics; not a universal proof or quantum execution.',
             pooled_middle_width=4,pooled_primary_pairs=3,conditional_flag_patterns=patterns,
             conditional_uniform_output_records=records,exact_mean_pooled_outputs=mean,
             sum_flag_pairing_cases=flags_checked,triangular_kernel_counts=kernel_checks,
             parameter_cases=parameter_cases,exact_three_event_stage_checks=stage_checks,
             exact_exponential_coefficient='1180959/500000')
    Path(__file__).with_name('pooled_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
