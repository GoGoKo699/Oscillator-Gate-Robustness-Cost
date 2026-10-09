#!/usr/bin/env python3
"""Run all scoped scientific suites without changing their sources or references.

Use a new output directory outside this package. Scientific assertion failures and
canonical-report differences are separate receipt fields. Any difference yields
nonzero exit status for explicit inspection, without adjusting tolerances.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def inventory() -> dict[str,str]:
    return {str(p.relative_to(ROOT)):sha(p) for p in sorted(ROOT.rglob('*')) if p.is_file()}

def diffs(a,b,path=''):
    result=[]
    if isinstance(a,dict) and isinstance(b,dict):
        if a.keys()!=b.keys():result.append({'path':path,'kind':'keys','reference':list(a),'run':list(b)})
        for k in sorted(a.keys() & b.keys()):result.extend(diffs(a[k],b[k],path+'/'+str(k)))
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b):result.append({'path':path,'kind':'length','reference':len(a),'run':len(b)})
        for i,(x,y) in enumerate(zip(a,b)):result.extend(diffs(x,y,path+'/'+str(i)))
    elif a!=b or type(a) is not type(b):
        entry={'path':path,'reference':a,'run':b,'kind':'value'}
        if isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):
            entry.update(kind='numeric',absolute_difference=abs(a-b))
        result.append(entry)
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args()
    out=args.output_dir.expanduser().resolve()
    if out==ROOT or ROOT in out.parents:ap.error('Output must lie outside the package')
    if out.exists():ap.error('Output directory must not already exist')
    before=inventory()
    manifests=[]
    for m in sorted((ROOT/'prior').rglob('MANIFEST.json')):
        data=json.loads(m.read_text())
        for name,expected in data.items():
            f=(m.parent/name).resolve()
            if not f.is_relative_to(ROOT/'prior'):raise ValueError('Manifest traversal')
            if sha(f)!=expected['sha256'] or f.stat().st_size!=expected['bytes']:
                raise ValueError('Source integrity mismatch: '+str(f))
        manifests.append({'manifest':str(m.relative_to(ROOT)),'members':len(data)})
    source=json.loads((ROOT/'notes/incoming_hashes.json').read_text())
    for name,digest in source.items():
        if sha(ROOT/'prior'/name)!=digest:raise ValueError('Changed incoming file: '+name)
    out.mkdir(parents=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    suites=[('consolidation','check_consolidation.py','evidence/final.json'),
            ('cost_audit','prior/check_audit.py','prior/evidence/final.json'),
            ('resource_review','prior/prior/check_review.py','prior/prior/evidence/first.json'),
            ('pilot','prior/prior/prior/check_pilot.py','prior/prior/prior/evidence/final.json')]
    records=[]
    for name,script,reference in suites:
        report=out/(name+'.json');log=out/(name+'.log')
        with log.open('xb') as f:
            proc=subprocess.run([sys.executable,str(ROOT/script),'--output',str(report)],
                                cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=120)
        item={'suite':name,'script':script,'reference':reference,'report':report.name,'log':log.name,
              'returncode':proc.returncode,'report_exists':report.exists()}
        if report.exists():
            data=json.loads(report.read_text());ref=json.loads((ROOT/reference).read_text())
            item.update(status=data.get('status'),groups=data.get('test_groups'),
                        byte_identical=report.read_bytes()==(ROOT/reference).read_bytes(),
                        differences=diffs(ref,data))
        records.append(item)
    after=inventory()
    passed=all(r['returncode']==0 and r.get('status')=='PASS' for r in records)
    identical=all(r.get('byte_identical',False) for r in records)
    receipt={'scientific_assertions_pass':passed,'all_canonical_reports_byte_identical':identical,
             'source_unchanged':before==after,'source_sha256':before,'incoming_files':len(source),
             'manifests':manifests,'total_groups':sum(r.get('groups',0) for r in records),'runs':records,
             'environment_overrides':{k:env[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONDONTWRITEBYTECODE')}}
    with (out/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('source_sha256','runs')},indent=2))
    raise SystemExit(0 if passed and identical and before==after else 1)
if __name__=='__main__':main()
