#!/usr/bin/env python3
import json,sys
REQ={"schema","skill","allowed_effects","observed_effects","violations","verdict","scope","receipt_hash"}
def validate(d):
 m=REQ-set(d); return [] if not m else ["missing:"+",".join(sorted(m))]
if __name__=='__main__':
 if '--self-test' in sys.argv:
  assert not validate({k:"x" for k in REQ}); print('formal_skill audit self-test: PASS'); raise SystemExit(0)
 d=json.load(open(sys.argv[1],encoding='utf-8')); e=validate(d); print(json.dumps({"valid":not e,"errors":e})); raise SystemExit(0 if not e else 2)
