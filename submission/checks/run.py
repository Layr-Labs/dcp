#!/usr/bin/env python3
"""Run finite evidence in temporary storage; never mutate the submitted files."""
from pathlib import Path
from hashlib import sha256
import argparse,json,os,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path)
args=parser.parse_args()
scripts=['check_profiles.py','check_grid.py','check_complete.py','check_channel.py',
         'check_lower_bound.py','check_decoder.py']
inputs=['profile.py','protocol.json',*scripts,'replay/check_preparation.py','replay/score_schedules.py']
summary=dict(status='PASS',scope='Finite exact diagnostics only; no mathematical acceptance, physical quantum run or asymptotic inference.',
             input_sha256={p:sha256((HERE/p).read_bytes()).hexdigest() for p in inputs},checks=[])
with tempfile.TemporaryDirectory(prefix='dcp-ppc-checks-') as folder:
    work=Path(folder)
    (work/'results').mkdir()
    (work/'replay').mkdir()
    for name in inputs:shutil.copyfile(HERE/name,work/name)
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
    for script in scripts:
        run=subprocess.run([sys.executable,'-B',str(work/script)],env=env,
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=90)
        if run.returncode:
            print(run.stdout)
            raise SystemExit(run.returncode)
        summary['checks'].append(dict(script=script,exit_code=run.returncode))
        print(script+': PASS',flush=True)
    for name in ['profiles','grid','complete','channel','lower-bound','decoder']:
        result=json.loads((work/'results'/(name+'.json')).read_text())
        assert result['status']=='PASS'
        summary[name]={k:v for k,v in result.items() if k in
                      ['status','counts','fixed_fiber_lower_bounds','limits','scope']}
if args.out:
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(dict(status=summary['status'],checks=len(scripts))))
