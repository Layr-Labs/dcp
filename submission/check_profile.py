"""Finite arithmetic diagnostics; not a quantum execution or proof certificate."""
from decimal import Decimal, localcontext
from math import isqrt
from itertools import product
import json
from pathlib import Path


def parameters(n):
    v = isqrt(n)
    v += v*v < n
    ell = (n-1).bit_length()
    z = (ell-1).bit_length()
    b = (3*v*ell*(ell+4*z+32)+1)//2
    m = (n-2)//b+1
    return v, ell, z, b, m


def main():
    profile_cases = []
    # Includes nonpowers and both sides of integer-root/bit-length boundaries.
    cases = []
    for t in [16384, 16385, 20000, 32768, 65536]:
        p = 1 << t
        cases.extend([p-1, p, p+1, p+isqrt(p)+17])
    with localcontext() as ctx:
        ctx.prec = 100
        two = Decimal(2)
        ln2 = two.ln()
        for n in cases:
            v, ell, z, b, m = parameters(n)
            assert (v-1)**2 < n <= v*v
            assert (m-1)*b < n-1 <= m*b
            assert b+1 <= n and m*(b+1) <= 3*n
            # Audit exact top-down widths without enumerating astronomically many levels.
            for B in [1, 2, n//3, n-1]:
                full, rem = divmod(B,b)
                positive = full + bool(rem)
                assert positive <= m and full*b+rem == B
                assert full*b+rem+1 <= n+1  # retained phase-qubit bound
            nd = Decimal(n)
            y, L = nd.sqrt(), nd.ln()/ln2
            A = Decimal(2*(b+1)).ln()/ln2
            lg = Decimal(m)*A
            qlog_upper = lg + 2*L + 28
            target = y/(3*L)
            assert qlog_upper < target
            assert qlog_upper <= target-3*y/(L*L)
            assert lg <= target-(Decimal(10)/3)*y/(L*L)+L
            tlog_upper = 10*L+qlog_upper+Decimal((b+2)//2)
            explicit = Decimal(3)/4*y*L*L+3*y*L*(L.ln()/ln2)+64*y*L
            assert tlog_upper <= explicit
            assert explicit+18*L <= explicit+y*L
            profile_cases.append({
                'n_bits': n.bit_length(),
                'offset_bit_length': (n-(1<<(n.bit_length()-1))).bit_length(),
                'source_log_upper_over_declared_log': str(qlog_upper/target),
                'time_log_upper_over_explicit_log': str(tlog_upper/explicit),
                'all_integer_checks': True,
                'physical_interpreter_factor_within_yL': True,
                'tight_source_envelope': True,
            })
        # Verify the threshold used to absorb the logarithmic correction.
        L = two**80
        assert L**(Decimal(1)/8)/2 > 4*(L.ln()/ln2)+64
        # Physical ledger: (1/2)L^(1/8) >= 3log2 L+65 from L=2^80 on.
        assert L**(Decimal(1)/8)/2 == 512 and 3*(L.ln()/ln2)+65 < 306
        assert L**(Decimal(1)/8)/16 > 3/ln2

    # Exhaust the abstract fiber statistic for the three smallest widths.
    fibers = []
    for b in range(1,4):
        modulus, r = 1<<b, b+1
        total_good, count = 0, 0
        for labels in product(range(modulus), repeat=r):
            sums = [0]
            for label in labels:
                sums += [(s+label)%modulus for s in sums]
            hist = [0]*modulus
            for s in sums:
                hist[s] += 1
            total_good += sum(c>=2 for c in hist)
            count += 1
        # Pair projection before SEARCH failure is good_fibers / modulus.
        assert 36*total_good >= 19*count*modulus
        assert 2*299**2*total_good > 300**2*count*modulus
        fibers.append({'b':b,'label_vectors':count,
                       'pair_projection_mean':f'{total_good}/{count*modulus}',
                       'success_lower_bound_above_half':True})

    layout_cases=[]
    for n in [1,2,3,7,16,63,64,65,256,1024,1<<16,1<<128,1<<16384]:
        r=(n+1).bit_length()
        U=1<<(2*r)
        B=7*(1<<48)*U
        H=(1<<32)*(1<<r)
        maxspan=max(2,B,H+1)
        h=1<<(maxspan-1).bit_length()
        assert h<2*maxspan
        assert 2*(B-1)<2*h and 2*H+1<2*h
        assert 2*h <= (1<<64)*(n+1)**2
        assert U>=n*n
        layout_cases.append({'n_bit_length':n.bit_length(),'mapping_and_capacity':True})
    result = {'layout_cases':layout_cases,'kind':'finite arithmetic diagnostics, not mathematical certification',
              'profile_cases':profile_cases,'fiber_cases':fibers,
              'logarithm_absorption_threshold_verified':True}
    Path(__file__).with_name('checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(profile_cases)} width/cap cases, 3 exhaustive fiber cases, absorption threshold, {len(layout_cases)} physical layouts')

if __name__=='__main__':
    main()
