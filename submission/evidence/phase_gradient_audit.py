"""PG2 finite diagnostics: not a proof, quantum execution or official judgment."""
import cmath
from fractions import Fraction as F
import json
import math
from pathlib import Path


def fourier_circuit_column(t, x):
    size=1<<t
    v=[0j]*size;v[x]=1
    for j in reversed(range(t)):
        w=v[:]
        for z in range(size):
            if not z>>j&1:
                other=z|(1<<j)
                w[z]=(v[z]+v[other])/math.sqrt(2)
                w[other]=(v[z]-v[other])/math.sqrt(2)
        v=w
        for z in range(size):
            if z>>j&1:
                low=z&((1<<j)-1)
                v[z]*=cmath.exp(2j*math.pi*low/(1<<(j+1)))
    out=[0j]*size
    for z in range(size):
        reverse=int(f'{z:0{t}b}'[::-1],2)
        out[reverse]=v[z]
    return out


def main():
    qft_columns=gradient_shifts=preparation_cases=tail_cases=0
    maximum_qft_error=maximum_shift_error=0.0
    for t in range(1,7):
        size=1<<t
        gradient=[cmath.exp(-2j*math.pi*z/size)/math.sqrt(size) for z in range(size)]
        for x in range(size):
            v=fourier_circuit_column(t,x)
            for z in range(size):
                exact=cmath.exp(2j*math.pi*x*z/size)/math.sqrt(size)
                error=abs(v[z]-exact)
                maximum_qft_error=max(maximum_qft_error,error)
                assert error<1e-12
            qft_columns+=1
        for d in range(size):
            for z in range(size):
                got=gradient[(z-d)%size]
                expected=cmath.exp(2j*math.pi*d/size)*gradient[z]
                error=abs(got-expected)
                maximum_shift_error=max(maximum_shift_error,error)
                assert error<1e-12
            gradient_shifts+=1
    # Exact successful preparation amplitudes; omit the common 1/(2 sqrt 2).
    for p in range(1,6):
        den=1<<p
        weights=sorted({-den,-den+1,-1,0,1,den-1,den})
        for a in weights:
            for b in weights:
                amplitudes=[]
                for target in (0,1):
                    re=im=0
                    for selector in (0,1):
                        w=((den,0),(a,b))[target][selector]
                        for r in range(den):
                            if r<abs(w):
                                if selector:im+=(-1 if w<0 else 1)
                                else:re+=(-1 if w<0 else 1)
                    amplitudes.append((F(re,den),F(im,den)))
                assert amplitudes==[(F(1),F(0)),(F(a,den),F(b,den))]
                success=(1+F(a*a+b*b,den*den))/8
                assert success>=F(1,8)
                preparation_cases+=1
    # Tail sums on finite binary phase estimation instances, including wraparound.
    for t in range(4,10):
        size=1<<t
        for modulus in range(2,min(24,size//8)+1):
            d0=F(size,2*modulus)
            floor_d0=d0.numerator//d0.denominator
            bound=F(1,2*(floor_d0-1))
            assert d0>=4
            for y in range(modulus):
                theta=F(y,modulus)
                fail=0.0;total=0.0
                for z in range(size):
                    offset=theta-F(z,size)
                    offset-=math.floor(offset+F(1,2))
                    if offset==0:probability=1.0
                    elif (size*offset).denominator==1:probability=0.0
                    else:
                        u=float(offset)
                        probability=(math.sin(math.pi*size*u)/(size*math.sin(math.pi*u)))**2
                    total+=probability
                    if abs(offset)>=F(1,2*modulus):fail+=probability
                assert abs(total-1)<1e-10
                assert fail<=float(bound)+1e-12
                tail_cases+=1
    assert F(7,8)**8<F(1,2)
    assert 40*F(7,8)**1024<F(1,2**122)
    assert 160*F(1,2**60)+8*F(1,2**40)<F(1,2**36)
    assert F(1,2**23)+F(1,4096)<F(1,1024)
    out=dict(scope='Finite diagnostics only; no asymptotic proof, device execution or official judgment.',
             binary_qft_columns=qft_columns,gradient_translation_cases=gradient_shifts,
             maximum_numeric_qft_amplitude_error=maximum_qft_error,
             maximum_numeric_gradient_amplitude_error=maximum_shift_error,
             exact_postselected_amplitude_cases=preparation_cases,
             numerical_qpe_tail_cases=tail_cases,
             exact_preparation_cap_and_norm_budget_checks=True)
    Path(__file__).with_name('phase_gradient_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
