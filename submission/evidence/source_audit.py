"""Exact finite circuit/parameter diagnostics; universal proofs in source-labels.md."""
from fractions import Fraction as F
from pathlib import Path
import json
from recycle_audit import parameters

def monomial(power,order):
    power%=order
    return {power if power<order//2 else power-order//2:1 if power<order//2 else -1}

def polyadd(a,b,sign=1):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+sign*v
    return {k:v for k,v in out.items() if v}

def mulphase(poly,power,order):
    out={}
    for k,v in poly.items():
        for kk,sgn in monomial(k+power,order).items():out[kk]=out.get(kk,0)+sgn*v
    return {k:v for k,v in out.items() if v}

def transform(t,x,inverse=False):
    size=1<<t;state=[{} for _ in range(size)];state[x]={0:1}
    gates=[]
    for j in range(t-1,-1,-1):
        gates.append(('h',j,0))
        for k in range(j-1,-1,-1):gates.append(('p',j,k))
    gates.extend(('s',j,t-1-j) for j in range(t//2))
    if inverse:gates.reverse()
    for tag,j,k in gates:
        if tag=='h':
            for z in range(size):
                if z>>j&1:continue
                one=z|(1<<j);a,b=state[z],state[one]
                state[z]=polyadd(a,b);state[one]=polyadd(a,b,-1)
        elif tag=='p':
            power=(size//(1<<(j-k+1)))*(-1 if inverse else 1)
            for z in range(size):
                if z>>j&1 and z>>k&1:state[z]=mulphase(state[z],power,size)
        else:
            new=[{} for _ in range(size)]
            for z,a in enumerate(state):
                zz=z^((1<<j)|(1<<k)) if ((z>>j)^(z>>k))&1 else z
                new[zz]=a
            state=new
    # Every path has exactly t Hadamards; omitted common normalization is 2^(-t/2).
    return state

def main():
    circuit=0
    for t in range(1,7):
        for x in range(1<<t):
            for inv in (False,True):
                actual=transform(t,x,inv)
                for z,a in enumerate(actual):
                    assert a==monomial((-1 if inv else 1)*x*z,1<<t)
                    circuit+=1
    kickback=0
    for B in range(1,9):
        modulus=1<<B
        for r in range(1,B+1):
            for sign in (-1,1):
                d=sign*(1<<(B-r))
                for control in (0,1):
                    for z in range(modulus):
                        previous=(z-control*d)%modulus
                        assert (-previous)%modulus==(-z+control*d)%modulus
                        kickback+=1
    schedules=0
    for n in list(range(17,2049))+[4096,16384,100000,1000000]:
        for m in (n-1,n):
            ell,final,lengths,widths=parameters(n,m)
            R=4*(m-ell)*lengths[0]
            a=((1<<20)*R-1).bit_length();t=n+a+4
            B=min(t,((1<<30)*R*(t+1)-1).bit_length())
            assert 1<=B<=t and 1<<(t-n-1)>=(1<<23)*R
            if B<t:assert F(8*R*t,1<<B)<F(1,1<<27)
            retained=sum(min(j,B-1) for j in range(t))
            assert retained<=t*B
            schedules+=1
    assert F(4*40,1<<60)+F(8,1<<40)<F(1,1<<36)
    assert F(7,8)**8<F(1,2)
    assert 40*F(7,8)**1024<F(1,1<<122)
    assert F(1,1<<23)+F(1,1<<27)+F(1,1<<36)+F(1,1<<122)<F(1,1024)
    out=dict(scope='Exact finite circuit and parameter diagnostics; no device run or asymptotic certification.',cyclotomic_transform_amplitudes=circuit,gradient_translation_exponent_checks=kickback,source_schedule_checks=schedules,source_budget='2^-23+2^-27+2^-36+2^-122<1/1024')
    Path(__file__).with_name('source_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
