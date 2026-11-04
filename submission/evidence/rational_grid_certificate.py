"""Generate the fixed phase table with exact rationals and certified remainders."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib,json

def atan_bounds(q,terms=20):
    x=Q(1,q)
    low=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    return low,low+x**(2*terms+1)/Q(2*terms+1)

def series(x,sine):
    term=x if sine else Q(1); total=term
    for k in range(1,60):
        term*= -x*x/Q((2*k)*(2*k+1) if sine else (2*k-1)*(2*k))
        total+=term
    return total

def rounded_scaled(x,scale=1<<16):
    z=x*scale
    return (2*z.numerator+z.denominator)//(2*z.denominator)

def main():
    alo,ahi=atan_bounds(5); blo,bhi=atan_bounds(239)
    plo,phi=16*alo-4*bhi,16*ahi-4*blo
    width=phi-plo
    assert Q(3)<plo<phi<Q(22,7)
    assert width<Q(1,1<<90)
    tail=max(Q(7**120,factorial(120)),Q(7**121,factorial(121)))
    assert tail<Q(1,1<<200)
    error=2*width+tail+Q(1,1<<17)
    assert error<Q(1,1<<16)
    chord_bound=phi/64+Q(3,32)+Q(3,1<<16)
    assert chord_bound<Q(1,4)
    midpoint=(plo+phi)/2
    grid=[]
    for r in range(64):
        x=2*r*midpoint/64
        assert abs(x)<7
        grid.append({'index':r,'cosine_numerator':rounded_scaled(series(x,False)),
                     'sine_numerator':rounded_scaled(series(x,True))})
    table={'denominator':1<<16,'points':grid}
    path=Path(__file__).with_name('phase_grid.json')
    path.write_text(json.dumps(table,indent=2)+'\n')
    certificate={'scope':'Exact rational finite certificate for fixed constants only.',
                 'arctangent_terms':20,'sine_and_cosine_terms':60,
                 'pi_interval_width_less_than':'2^-90','Taylor_remainders_less_than':'2^-200',
                 'coordinate_error_less_than':'2^-16','decoder_chord_bound_less_than':'1/4',
                 'phase_error_less_than':'1/16','grid_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                 'points':len(grid)}
    Path(__file__).with_name('grid_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps(certificate,indent=2))
if __name__=='__main__':main()
