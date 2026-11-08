"""Bounded checks of the actual PE filter, exact constants and source laws."""
from collections import Counter
from fractions import Fraction as F
import cmath
import hashlib
import itertools
import json
import math
from pathlib import Path
import resource
import time
from phase_filter import grover_filter, spectral_error, estimation_probability

resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(45,)*2)
START=time.process_time()


def norm_error(v,target):
    return sum(abs(z-(target[i] if j==0 else 0))**2
               for i,row in enumerate(v) for j,z in enumerate(row))


def phase_filter_checks():
    cases=0;max_identity=0.;max_norm=0.
    for K in (4,8,16,32,64):
        for eta in range(1,K+1):
            a=(math.sqrt(eta/K),math.sqrt(1-eta/K))
            for M in (8,32,128):
                prepared=grover_filter(eta,K,M,a)
                erased=grover_filter(eta,K,M,(1,0),inverse=True)
                error=norm_error(prepared,(1,0));inverse_error=norm_error(erased,a)
                expected=spectral_error(eta,K,M)
                max_identity=max(max_identity,abs(error-expected),abs(error-inverse_error))
                max_norm=max(max_norm,abs(sum(abs(z)**2 for row in prepared for z in row)-1))
                assert abs(error-expected)<2e-10 and abs(error-inverse_error)<2e-10
                cases+=1
    good=grover_filter(2,4,4,(math.sqrt(.5),math.sqrt(.5)))
    bad=grover_filter(2,4,4,(math.sqrt(.5),math.sqrt(.5)),wrong_sign=True)
    assert norm_error(good,(1,0))<1e-25 and norm_error(bad,(0,1))<1e-25
    return {'cases':cases,'max_squared_error_identity_discrepancy':max_identity,
            'max_norm_discrepancy':max_norm,'wrong_sign_maps_to_complement':True,
            'scope':'Floating-point circuit simulation on small grids. Production guard constants are checked separately by exact inequalities.'}


def source_and_rounding_checks():
    entries=rounding_cases=0;worst_mass=0.
    for N in range(2,18):
        for s in range(N):
            rho=Counter()
            for x in range(N):
                pair=(N+x,(x+s)%N)  # X on the first source register.
                for a,b in itertools.product(pair,repeat=2):rho[a,b]+=1
            for a,b in itertools.product(range(2*N),repeat=2):
                bit,u=divmod(a,N);other,v=divmod(b,N)
                latent=int((u-v+(bit-other)*s)%N==0)
                assert rho[a,b]==latent
                entries+=1
        n=(N-1).bit_length()
        for guard in (2,3,4):
            M=1<<(n+guard)
            bound=min(F(1),F(1,M//(2*N)-1))
            for k in range(N):
                mass=wrong=0.
                for j in range(M):
                    numerator=k*M-j*N
                    distance=abs(numerator)%(N*M)
                    distance=min(distance,N*M-distance)
                    if distance==0:prob=1.
                    elif numerator%N==0:prob=0.
                    else:
                        prob=(math.sin(math.pi*(numerator%N)/N)
                              /(M*math.sin(math.pi*distance/(N*M))))**2
                    guess=((2*N*j+M)//(2*M))%N
                    mass+=prob
                    if guess!=k:wrong+=prob
                worst_mass=max(worst_mass,abs(mass-1))
                assert abs(mass-1)<3e-11 and wrong<=float(bound)+3e-11
                rounding_cases+=1
    return {'exact_source_matrix_entries':entries,'rounding_eigenstate_cases':rounding_cases,
            'max_probability_mass_error':worst_mass}


def population_checks():
    rows=[]
    for N in range(2,9):
        n=(N-1).bit_length();m=n+2;K=1<<m
        profiles=Counter();total=N**m;z_sum=0
        for labels in itertools.product(range(N),repeat=m):
            sums=[0]
            for a in labels:sums += [(v+a)%N for v in sums]
            counts=Counter(sums)
            profile=tuple(sorted(counts.values()));profiles[profile]+=1
            z_sum+=sum(v*v for v in profile)
        assert F(z_sum,total)==K+F(K*(K-1),N)
        scale=1<<32;lower_numerator=0
        for profile,frequency in profiles.items():
            root_sum=sum(math.isqrt(v*scale*scale) for v in profile)
            lower_numerator+=frequency*root_sum*root_sum
        lower=F(lower_numerator,total*N*K*scale*scale)
        assert lower>=F(4,5)
        rows.append({'N':N,'m':m,'label_lists':total,'distinct_profiles':len(profiles),
                     'exact_collision_mean':str(F(z_sum,total)),
                     'certified_PGM_success_lower_bound':str(lower)})
    return rows


def finite_readout_checks():
    fixtures=[((0,0,0,0),3),((1,1,1,1),4),((0,1,1,2),3),((1,2,3,4,1),5),((1,1,1,1,1),8)]
    rows=[]
    for labels,N in fixtures:
        K=1<<len(labels);M=64;sums=[0]
        for a in labels:sums += [(v+a)%N for v in sums]
        fibers={t:[x for x,v in enumerate(sums) if v==t] for t in range(N)}
        targets={}
        for t,indices in fibers.items():
            if not indices:continue
            eta=len(indices);filtered=grover_filter(eta,K,M,(1,0),inverse=True)
            good=set(indices);weight=math.sqrt(eta/K)
            targets[t]=[[weight*(filtered[0][j]/math.sqrt(eta) if x in good
                         else filtered[1][j]/math.sqrt(K-eta)) for j in range(M)] for x in range(K)]
        probabilities=[]
        for secret in range(N):
            distribution=[]
            for guess in range(N):
                phases={t:cmath.exp(2j*math.pi*(secret-guess)*t/N)/math.sqrt(N) for t in targets}
                mass=sum(abs(sum(phases[t]*targets[t][x][j] for t in targets))**2
                         for x in range(K) for j in range(M))
                distribution.append(mass)
            assert abs(sum(distribution)-1)<3e-10
            probabilities.append(distribution[secret])
        assert max(probabilities)-min(probabilities)<3e-10
        rows.append({'labels':labels,'N':N,'toy_phase_grid':M,'true_secret_probabilities':probabilities,
                     'scope':'Full coherent target readout using a deliberately small grid, not the production guard.'})
    return rows


def exact_constants():
    filter_square=F(1,2**15)+F(4,2**13-1)
    assert filter_square<F(1,1024)
    for n in range(2,1025):
        m=n+2;q=(m-1).bit_length()+n+10;M=1<<q
        for N in (1<<n,(1<<(n-1))+1):
            assert M>=1024*m*N
            assert F(1,M//(2*N)-1)<=F(1,256*m)
        G=1<<((m+1)//2+15)
        assert G*G>=(1<<30)*(1<<m)
    success=F(4,5)-F(1,256)-F(1,256)-F(1,32)-F(1,128)
    assert success==F(241,320) and success>F(3,4)
    return {'filter_squared_error_upper':str(filter_square),'success_lower':str(success),
            'bit_lengths_checked':1023}


def main():
    out={'status':'pass','phase_filter':phase_filter_checks(),'source':source_and_rounding_checks(),
         'population_ensembles':population_checks(),'finite_readout':finite_readout_checks(),
         'exact_constants':exact_constants()}
    out['cpu_seconds']=time.process_time()-START
    out['process_memory']=[s.strip() for s in Path('/proc/self/status').read_text().splitlines() if s.startswith(('VmPeak:','VmHWM:'))]
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
