"""Exact emitted controlled-W columns, inverse cleanup, signs and stream counts."""
import itertools,json,resource
from fractions import Fraction as F
from exact import Exact
from arithmetic import mod_add_circuit
from circuit_reference import apply,compile_parts
from walk import layout,controlled_walk_gates,parameters,power_schedule,sign_phase_gates


def encoded(x,t,control,block,pos):
    out=x|(control<<pos.outer_control)|(block<<pos.block)
    for i,w in enumerate(pos.arithmetic.target):out|=((t>>i)&1)<<w
    return out


def expected_column(labels,N,x,t,control,block,pos,inverse=False):
    if not control:return {encoded(x,t,control,block,pos):Exact(1)}
    K=1<<len(labels);sign=1 if sum(a for i,a in enumerate(labels) if x>>i&1)%N==t else -1
    out={}
    for y,ob in itertools.product(range(K),(0,1)):
        plus=F(2,K)-int(x==y);target=sign*int(x==y)
        value=(plus+(1 if ob==block else -1)*target)/2
        value*=(-1)**(block if inverse else ob)
        if value:out[encoded(y,t,control,ob,pos)]=Exact(value)
    return out


def main():
    resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20));resource.setrlimit(resource.RLIMIT_CPU,(45,45))
    columns=inverses=0;bad_detected=False;rows=[]
    for labels,N in [((1,2),3),((1,1,2),4),((1,3),5),((0,0),2)]:
        pos=layout(labels,N);gates=list(controlled_walk_gates(labels,N));reverse=list(controlled_walk_gates(labels,N,inverse=True))
        forward,back=compile_parts(gates),compile_parts(reverse)
        for x,t,control,block in itertools.product(range(1<<len(labels)),range(1<<pos.arithmetic.n),(0,1),(0,1)):
            initial=encoded(x,t,control,block,pos)
            got=apply({initial:Exact(1)},forward)
            assert got==expected_column(labels,N,x,t,control,block,pos)
            assert apply(got,back)=={initial:Exact(1)}
            assert apply({initial:Exact(1)},back)==expected_column(labels,N,x,t,control,block,pos,True)
            columns+=1;inverses+=1
        bad=compile_parts(list(controlled_walk_gates(labels,N,wrong_target_phase=True)))
        initial=encoded(0,0,1,0,pos)
        bad_detected |= apply({initial:Exact(1)},bad)!=apply({initial:Exact(1)},forward)
        rows.append({'N':N,'m':len(labels),'qubits':pos.qubits,'logical_gates':len(gates)})
    assert bad_detected
    streams=0
    for n in range(1,13):
        for N in (1<<n,(1<<(n-1))+1):
            m=n+1;labels=tuple((3*i+1)%N for i in range(m));pos=layout(labels,N)
            gate_count=sum(1 for _ in controlled_walk_gates(labels,N))
            expected=2*m*(153*n+112)+6*n+6*m+11
            assert gate_count==expected
            assert pos.qubits==2*m+24*n+19
            config=parameters(N);p=config['p']
            assert sum(count for _,count,_ in power_schedule(p))==(1<<p)-1
            assert sum(count for _,count,_ in power_schedule(p,True))==(1<<p)-1
            assert list(sign_phase_gates(range(p)))==[('Z',p-1),('Z',p-2)]
            streams+=1
    print(json.dumps({'passed':True,'exact_controlled_walk_columns':columns,'inverse_cleanup_columns':inverses,
                      'missing_controlled_phase_negative_control':bad_detected,'fixtures':rows,
                      'stream_parameter_cases':streams,'source_calls_in_walk':0,
                      'scope':'Actual emitted logical gates; Toffoli and CZ have exact constant-size Clifford+T expansions.'},indent=2))


if __name__=='__main__':main()
