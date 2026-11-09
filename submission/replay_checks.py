"""Capped replay of packaged exact diagnostics in temporary copies."""
from pathlib import Path
import json,os,resource,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(45,45))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))

def main():
    start=time.monotonic();checks=[]
    with tempfile.TemporaryDirectory(prefix='.replay-',dir=ROOT)as name:
        tmp=Path(name)
        for script,output,record,ignore in [
            ('check_constants.py','constant-results.json','constant-results-recorded.json',{'cpu_seconds'}),
            ('check_structure.py','results.json','structure-results-recorded.json',set())]:
            shutil.copyfile(ROOT/'checks'/script,tmp/script)
            r=subprocess.run([sys.executable,'-B',str(tmp/script)],cwd=tmp,
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),preexec_fn=limits,
                capture_output=True,text=True,timeout=60)
            assert r.returncode==0,(script,r.stderr[-1000:])
            a=json.loads((tmp/output).read_text());b=json.loads((ROOT/'checks'/record).read_text())
            assert {k:v for k,v in a.items()if k not in ignore}=={k:v for k,v in b.items()if k not in ignore}
            checks.append(dict(script=script,mathematical_results_match=True))
    result=dict(all_passed=True,checks=checks,python=sys.version,wall_seconds=time.monotonic()-start)
    (ROOT/'replay-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
