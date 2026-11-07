#!/usr/bin/env python3
"""Run F4 finite evidence in temporary storage without changing the package."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path)
args=parser.parse_args()
scripts=['check_local.py','check_profiles.py','check_decoder.py']
inputs=['common.py',*scripts]
summary=dict(status='PASS',scope='Finite diagnostics only; no full quantum run, asymptotic inference or hosted acceptance.',
    input_sha256={name:sha256((HERE/name).read_bytes()).hexdigest() for name in inputs},checks=[])
with tempfile.TemporaryDirectory(prefix='dcp-f4-checks-') as folder:
    work=Path(folder); (work/'checks').mkdir()
    for name in inputs: shutil.copyfile(HERE/name,work/'checks'/name)
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
    for script in scripts:
        run=subprocess.run([sys.executable,'-B',str(work/'checks'/script)],env=env,
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=60)
        if run.returncode:
            print(run.stdout)
            raise SystemExit(run.returncode)
        summary['checks'].append(dict(script=script,exit_code=0))
        print(script+': PASS',flush=True)
    for name in ('local','profile','decoder'):
        result=json.loads((work/(name+'-results.json')).read_text())
        assert result['status']=='PASS'
        summary[name]=result
if args.out:
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(dict(status='PASS',checks=len(scripts))))
