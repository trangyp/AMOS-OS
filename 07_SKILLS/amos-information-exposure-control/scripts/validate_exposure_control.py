#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from exposure_control import sha

def validate_receipt(r):
    if not isinstance(r,dict):return ["receipt_not_object"]
    h=r.get("receipt_hash"); core=dict(r); core.pop("receipt_hash",None); errs=[]
    if h!=sha(core):errs.append("receipt_hash_mismatch")
    if r.get("authority_semantics")!="EXPOSURE_DECISION_DOES_NOT_GRANT_EFFECT_COMMIT_AUTHORITY":errs.append("authority_semantics_missing")
    if r.get("accountant_semantics")!="POLICY_UNIT_SUM_IS_NOT_DIFFERENTIAL_PRIVACY_EPSILON":errs.append("accountant_semantics_missing")
    return errs

def self_test():
    x={"release_id":"r","phase":"PREFLIGHT","state":"UNKNOWN_GAP","request_hash":"q","canonical_charges":{},"proof_join_hash":None,"reasons":[],"authority_semantics":"EXPOSURE_DECISION_DOES_NOT_GRANT_EFFECT_COMMIT_AUTHORITY","accountant_semantics":"POLICY_UNIT_SUM_IS_NOT_DIFFERENTIAL_PRIVACY_EPSILON"};x["receipt_hash"]=sha(x);assert validate_receipt(x)==[];print("validate_exposure_control self-test: PASS")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("input",nargs="?");ap.add_argument("--self-test",action="store_true");a=ap.parse_args()
    if a.self_test:return self_test()
    if not a.input:raise SystemExit("input required")
    with open(a.input,encoding="utf-8") as f:print(json.dumps(validate_receipt(json.load(f)),sort_keys=True))
if __name__=="__main__":main()
