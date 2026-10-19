"""Exact finite certificate for the fine-decoder constant generator."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

def clog(x):return (x-1).bit_length()

def pi_interval(p):
    T=2*(p+10)
    def atan(q):
        low=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(T)),F(0))
        return low,low+F(1,(2*T+1)*q**(2*T+1))
    a,b=atan(5);c,d=atan(239)
    return 16*a-4*d,16*b-4*c

def coordinate(index,G,p,sine):
    lo,hi=pi_interval(p)
    pi_scale=1<<(p+40);mid=(lo+hi)/2*pi_scale
    rounded_pi=(2*mid.numerator+mid.denominator)//(2*mid.denominator)
    x=F(2*index,G)*F(rounded_pi,pi_scale)
    L=p+100
    term=x if sine else F(1);value=term
    for k in range(1,L):
        term*= -x*x/F(2*k*(2*k+1) if sine else (2*k-1)*(2*k))
        value+=term
    scale=1<<(p+4);z=value*scale
    rounded=(2*z.numerator+z.denominator)//(2*z.denominator)
    return F(rounded,scale)

def main():
    cases=0;coordinates=0
    moduli=list(range(2,34))+[64,128,1024,1<<32,1<<128]
    for K in moduli:
        p=clog((1<<20)*K);L=p+100
        lo,hi=pi_interval(p)
        width=hi-lo
        assert 3<lo<hi<F(22,7)
        assert width<F(1,1<<(p+30))
        tail=max(F(7**(2*L),factorial(2*L)),F(7**(2*L+1),factorial(2*L+1)))
        assert tail<F(1,1<<(p+90))
        assert width+F(1,1<<(p+40))+tail+F(1,1<<(p+5))<F(1,1<<p)
        G=1<<clog(64*K)
        assert hi/G+F(3,32*K)+F(3,(1<<20)*K)<F(1,4*K)
        if K in (2,3,5):
            for index in (0,G//4,G//2,3*G//4,G-1):
                for sine in (False,True):
                    value=coordinate(index,G,p,sine)
                    assert abs(value)<=F(1)+F(1,1<<p)
                    coordinates+=1
        cases+=1
    result={'scope':'Finite exact constant-generator certificate; not an asymptotic or official review.',
            'fine_decoder_moduli':cases,'generated_coordinate_samples':coordinates,
            'largest_tested_modulus':'2^128','coordinate_error_proof_bound':'2^-p',
            'phase_error_proof_bound':'1/(16K)'}
    Path(__file__).with_name('fine_grid_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
