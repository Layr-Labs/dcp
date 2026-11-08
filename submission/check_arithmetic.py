"""Bounded exact gate checks for clean arithmetic and controlled diffusion."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time
from arithmetic import mod_add_circuit, run_boolean, controlled_grover_gates, layout
from exact import Exact

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (45,)*2)
START=time.process_time()


def run_state(gates, state):
    out=dict(state); h=Exact.sqrt(F(1,2))
    for gate in gates:
        op,*w=gate
        if op=='H':
            fresh={}
            for z,amp in out.items():
                zero=z&~(1<<w[0]); one=zero|(1<<w[0])
                fresh[zero]=fresh.get(zero,Exact())+h*amp
                fresh[one]=fresh.get(one,Exact())+h*amp*(-1 if z>>w[0]&1 else 1)
            out={z:a for z,a in fresh.items() if a}
        else:
            fresh={}
            for z,amp in out.items():
                target,sign=run_boolean([gate],z)
                fresh[target]=amp*sign
            out=fresh
    return out


def main():
    addition_cases=circuits=0
    for n in range(1,6):
        for N in range(max(2,(1<<(n-1))+1),(1<<n)+1):
            for c in range(N):
                gates,q=mod_add_circuit(n,N,c)
                assert len(gates)==153*n+112 and q==23*n+18
                circuits+=1
                for flag in (0,1):
                    for x in range(1<<n):
                        initial=x|(flag<<n)
                        got,phase=run_boolean(gates,initial)
                        expected=((x+c)%N if flag and x<N else x)|(flag<<n)
                        assert got==expected and phase==1
                        assert run_boolean(reversed(gates),got)==(initial,1)
                        addition_cases+=1
    columns=0; ledgers=[]
    fixtures=[((0,1,1),2),((1,1,2),3),((1,2,4),5),((1,2,3,5),7)]
    for labels,N in fixtures:
        loc=layout(labels,N); K=1<<loc.m
        gates=list(controlled_grover_gates(labels,N))
        assert loc.qubits==24*loc.n+2*loc.m+17
        ledger={'N':N,'labels':labels,'gates':len(gates),'qubits':loc.qubits}
        ledgers.append(ledger)
        for t in range(1<<loc.n):
            target=sum((t>>i&1)<<wire for i,wire in enumerate(loc.target))
            for control in (0,1):
                fixed=target|(control<<loc.control)
                for x in range(K):
                    got=run_state(gates,{fixed|x:Exact(1)})
                    if not control:expected={fixed|x:Exact(1)}
                    else:
                        marked=sum(a for i,a in enumerate(labels) if x>>i&1)%N==t
                        expected={fixed|y:Exact((F(2,K)-int(x==y))*(-1 if marked else 1)) for y in range(K)}
                        expected={z:a for z,a in expected.items() if a}
                    assert got==expected,(labels,N,t,control,x)
                    columns+=1
    labels,N=(1,2),3;loc=layout(labels,N); scale=Exact.sqrt(F(1,2))
    source={0:scale,1<<loc.control:scale}
    correct=run_state(controlled_grover_gates(labels,N),source)
    wrong=run_state(controlled_grover_gates(labels,N,correct_sign=False),source)
    overlap=sum((amp.conjugate()*wrong.get(z,Exact()) for z,amp in correct.items()),Exact())
    assert overlap==0
    result={'status':'pass','modular_circuits':circuits,'controlled_addition_basis_cases':addition_cases,
            'exact_controlled_Grover_columns':columns,'ledgers':ledgers,
            'wrong_diffusion_sign_control_overlap':overlap.data(),
            'scope':'Actual emitted X/CNOT/Toffoli/H/Z/CZ gates; coherent target and PE control signs are checked. The full phase-estimation loop is not emitted.'}
    result['cpu_seconds']=time.process_time()-START
    result['process_memory']=[s.strip() for s in Path('/proc/self/status').read_text().splitlines() if s.startswith(('VmPeak:','VmHWM:'))]
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':main()
