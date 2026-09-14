#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from exposure_control import validate_proof_join

def self_test():
    base={"proof_id":"1","skill_id":"a","decision":"PASS","effect_hash":"e","semantic_transaction_hash":"t","policy_id":"p","policy_version":"1","policy_epoch":1,"authority_hash":"au","environment_hash":"env","capability_contract_hash":"cap","proof_epoch":1}; b=dict(base,proof_id="2",skill_id="b")
    assert validate_proof_join({"required_skills":["a","b"],"proofs":[base,b]})["state"]=="JOINT_PROOF_PASS"; print("validate_multi_skill_join self-test: PASS")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("input",nargs="?");ap.add_argument("--self-test",action="store_true");a=ap.parse_args()
    if a.self_test:return self_test()
    if not a.input:raise SystemExit("input required")
    with open(a.input,encoding="utf-8") as f:print(json.dumps(validate_proof_join(json.load(f)),sort_keys=True))
if __name__=="__main__":main()
