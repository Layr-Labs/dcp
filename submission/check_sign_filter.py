"""Coherent PE/sign/inverse and complete readout on bounded numerical grids."""
import cmath,itertools,json,math,resource
from fractions import Fraction as F
from sign_filter import apply_filter,squared_error,estimation_probability,sign_at,walk_matrix,multiply,adjoint
from walk import decoded_source_label,decoded_secret


def main():
    resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20));resource.setrlimit(resource.RLIMIT_CPU,(45,45))
    tests=0;max_error=0.;max_norm=0.
    for K in (4,8,16,32):
        for eta in range(1,K+1):
            alpha=math.sqrt(eta/K);beta=math.sqrt(1-eta/K)
            for M in (8,32,128):
                out=apply_filter(eta,K,M,(1,0,0,0))
                mass=sum(abs(z)**2 for row in out for z in row)
                max_norm=max(max_norm,abs(mass-1));assert abs(mass-1)<2e-10
                if eta==K:assert squared_error(out,(1,0,0,0))<1e-20
                else:
                    for sigma in (1,-1):
                        if sigma==1:v=(math.sqrt((1+alpha)/2),math.sqrt((1-alpha)/2),0,0)
                        else:v=(math.sqrt((1-alpha)/2),-math.sqrt((1+alpha)/2),0,0)
                        got=apply_filter(eta,K,M,v);error=squared_error(got,tuple(sigma*x for x in v))
                        phase=math.acos(sigma*alpha)/(2*math.pi)
                        expected=sum(2*estimation_probability(a,M,j)*(sign_at(j,M)-sigma)**2/4
                                     for a in (phase,(-phase)%1) for j in range(M))
                        # Each of the two walk eigenphases has weight one half.
                        max_error=max(max_error,abs(error-expected));assert abs(error-expected)<2e-9
                tests+=1
        empty=apply_filter(0,K,32,(0,1,0,0))
        assert abs(sum(abs(z)**2 for row in empty for z in row)-1)<2e-10
    fixtures=[((1,0),2),((0,1,2),3),((1,1,2),4),((1,2,3,4),5),((0,1,3,4),6),((1,2,3,5),7),((0,1,2,4),8)]
    rows=[];secrets=0
    for labels,N in fixtures:
        K=1<<len(labels);M=128;sums=[0]
        for a in labels:sums += [(x+a)%N for x in sums]
        fibers={t:[x for x,y in enumerate(sums) if y==t] for t in range(N)}
        eta={t:len(xs) for t,xs in fibers.items()};targets={};error2=0.
        for t,xs in fibers.items():
            if not xs:continue
            output=apply_filter(len(xs),K,M,(1,0,0,0));good=set(xs);weight=math.sqrt(len(xs)/K)
            error2+=len(xs)/K*squared_error(output,(math.sqrt(len(xs)/K),math.sqrt(1-len(xs)/K),0,0))
            targets[t]=[[[weight*(output[2*b][j]/math.sqrt(len(xs)) if x in good else output[2*b+1][j]/math.sqrt(K-len(xs)))
                           for j in range(M)] for x in range(K)] for b in (0,1)]
        ideal=sum(math.sqrt(v) for v in eta.values())**2/(N*K)
        actual=[]
        for secret in range(N):
            distribution=[]
            for guess in range(N):
                phases={t:cmath.exp(2j*math.pi*(secret-guess)*t/N)/math.sqrt(N) for t in targets}
                prob=sum(abs(sum(phases[t]*targets[t][b][x][j] for t in targets))**2
                         for b in (0,1) for x in range(K) for j in range(M))
                distribution.append(prob)
            assert abs(sum(distribution)-1)<2e-9
            assert abs(distribution[secret]-ideal)<=math.sqrt(error2)+2e-9
            actual.append(distribution[secret]);secrets+=1
        assert max(actual)-min(actual)<2e-9
        rows.append({'N':N,'labels':labels,'grid':M,'ideal_success':ideal,'actual_success':actual,
                     'whole_vector_error_bound':math.sqrt(error2)})
    # A target-dependent phase changes the ideal readout, so coherence is tested.
    counts=(3,3,2);good=sum(math.sqrt(x) for x in counts)**2/24
    bad=(-math.sqrt(counts[0])+sum(math.sqrt(x) for x in counts[1:]))**2/24
    assert good-bad>.5
    source_entries=rounding=0
    for N in range(2,18):
        for s in range(N):
            direct={}
            for x in range(N):
                pair=(x,N+(x+s)%N)
                for a,b in itertools.product(pair,repeat=2):direct[a,b]=direct.get((a,b),0)+1
            for i,j in itertools.product(range(2*N),repeat=2):
                bit,u=divmod(i,N);other,v=divmod(j,N)
                assert direct.get((i,j),0)==int((u-v-(bit-other)*s)%N==0)
                source_entries+=1
        n=(N-1).bit_length()
        for guard in (3,4):
            M=1<<(n+guard);bound=F(1,M//(2*N)-1)
            for a in range(N):
                wrong_source=wrong_final=mass=0.
                for j in range(M):
                    p=estimation_probability(a/N,M,j);mass+=p
                    wrong_source+=p*(decoded_source_label(j,M,N)!=a)
                    p_final=estimation_probability((-a)%N/N,M,j)
                    wrong_final+=p_final*(decoded_secret(j,M,N)!=a)
                assert abs(mass-1)<1e-9 and max(wrong_source,wrong_final)<=float(bound)+1e-9
                rounding+=1
    print(json.dumps({'passed':True,'filter_cases':tests,'max_spectral_identity_error':max_error,'max_norm_error':max_norm,
                      'complete_secret_fixture_cases':secrets,'fixtures':rows,
                      'target_relative_phase_negative_control':True,'exact_source_entries':source_entries,
                      'source_and_final_sign_rounding_cases':rounding,
                      'scope':'Numerical toy grids check the sequence; the production error budget is analytic and separately rational-certified.'},indent=2))


if __name__=='__main__':main()
