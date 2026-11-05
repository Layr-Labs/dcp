"""Exact finite joint-law audit, including truncation and a negative control."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

def instrument_law(B,a,c,L,bad_sort=False):
    M=B//(1<<(a+c)); law=defaultdict(lambda:defaultdict(Q)); counts={}
    for inputs in product(range(B),repeat=L):
        layout=tuple((u%(1<<a),u//((1<<a)*M)) for u in inputs)
        buckets=defaultdict(list)
        for i,key in enumerate(layout):buckets[key].append(i)
        pairs=[]
        for key in sorted(buckets):
            indices=buckets[key]
            if bad_sort:indices=sorted(indices,key=lambda i:inputs[i])
            pairs.extend(zip(indices[::2],indices[1::2]))
        counts[layout]=len(pairs)
        ds=[abs(inputs[i]-inputs[j])//(1<<a) for i,j in pairs]
        ps=[Q(0) if d>=M//2 else Q(1,2) if d==0 else Q(M,4*(M-d)) for d in ds]
        for flags in product((0,1),repeat=len(pairs)):
            probability=Q(1,B**L)
            for flag,p in zip(flags,ps):probability*=p if flag else 1-p
            if probability:
                outputs=tuple(d for d,flag in zip(ds,flags) if flag)
                law[(layout,flags)][outputs]+=probability
    return M,law,counts

def main():
    scenarios=[(4,0,0,4),(8,1,0,4),(8,0,1,4),(8,0,0,4),(16,1,1,3)]
    records=prefixes=0
    for B,a,c,L in scenarios:
        M,law,counts=instrument_law(B,a,c,L)
        K=1<<(a+c); D=M//2
        for (layout,flags),hist in law.items():
            successes=sum(flags); pairs=counts[layout]
            expected_mass=Q(1,K**L)*Q(1,4)**successes*Q(3,4)**(pairs-successes)
            assert sum(hist.values())==expected_mass
            for labels in product(range(D),repeat=successes):
                assert hist.get(labels,Q(0))==expected_mass/Q(D**successes)
                records+=1
            for requested in range(1,successes+1):
                marginal=defaultdict(Q)
                for labels,p in hist.items():marginal[labels[:requested]]+=p
                assert all(p==expected_mass/Q(D**requested) for p in marginal.values())
                assert len(marginal)==D**requested
                prefixes+=1
    _,bad,_=instrument_law(4,0,0,4,True)
    counterexample=None
    for (layout,flags),hist in bad.items():
        if sum(flags)==1:
            mass=sum(hist.values())
            if hist.get((0,),Q(0))!=mass/2:
                counterexample={'flags':list(flags),'conditional_output_probabilities':
                                {str(k):str(v/mass) for k,v in hist.items()}}
                break
    assert counterexample is not None
    result={'scope':'Exact finite instrument-law evidence; not an asymptotic or official proof review.',
            'scenarios':scenarios,'conditional_joint_output_records':records,
            'truncated_prefix_checks':prefixes,
            'negative_control_sorting_by_middle_label_breaks_uniformity':counterexample}
    Path(__file__).with_name('batch_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
