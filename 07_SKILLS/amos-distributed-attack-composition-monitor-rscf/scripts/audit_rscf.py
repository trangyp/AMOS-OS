#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':'))
def sha(v):return hashlib.sha256(canon(v).encode()).hexdigest()
def validate(r):
    if r.get('schema')!='amos.distributed-composition.v1' or r.get('status')!='BLOCK_COMPOSITION':return False
    x=dict(r); h=x.pop('receipt_hash',None); return bool(h) and h==sha(x) and r.get('authority_semantics')=='COMPOSITION_MATCH_DOES_NOT_PROVE_ADVERSARIAL_INTENT_OR_GRANT_RESPONSE_AUTHORITY'
def selftest():
    x={'schema':'amos.distributed-composition.v1','status':'BLOCK_COMPOSITION','rule_id':'r','severity':'H','policy_epoch':1,'as_of_ns':1,'minimal_event_ids':['a'],'distinct_principals':1,'distinct_sessions':1,'authority_semantics':'COMPOSITION_MATCH_DOES_NOT_PROVE_ADVERSARIAL_INTENT_OR_GRANT_RESPONSE_AUTHORITY'}; x['receipt_hash']=sha(x); assert validate(x); print('self-test: PASS')
def main():
    a=argparse.ArgumentParser();a.add_argument('path',nargs='?');a.add_argument('--self-test',action='store_true');x=a.parse_args()
    if x.self_test:return selftest()
    if not x.path:raise SystemExit('path required')
    print(json.dumps({'valid':validate(json.loads(Path(x.path).read_text()))}))
if __name__=='__main__':main()
