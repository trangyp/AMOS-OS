#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

FORBIDDEN = {"prompt","completion","raw_input","raw_output","input_value","output_value","tool_output","chain_of_thought","reasoning","authorization","api_key","token","password","secret","credential"}

class ContractError(RuntimeError): pass

def walk(x, path="$"):
    if isinstance(x, dict):
        for k,v in x.items():
            if str(k).lower() in FORBIDDEN: raise ContractError(f"forbidden field {path}.{k}")
            walk(v, f"{path}.{k}")
    elif isinstance(x, list):
        for i,v in enumerate(x): walk(v, f"{path}[{i}]")

def require(x, keys):
    missing=[k for k in keys if k not in x]
    if missing: raise ContractError("missing fields: "+",".join(missing))

def validate(x):
    walk(x)
    schema=x.get("schema")
    if schema=="amos.evaluator-calibration.report.v1":
        require(x,["session_id","phase","evaluator_id","evaluator_version","cohort_hash","observed_count","observed_coverage","reference_semantics","calibration_semantics","authority_semantics","deployment_semantics","receipt_hash"])
        if x["phase"] not in {"CALIBRATION","VALIDATION"}: raise ContractError("invalid phase")
        if x.get("score_semantics")!="PROBABILITY_PASS" and (x.get("brier_score") is not None or x.get("ece") is not None): raise ContractError("probability metrics require PROBABILITY_PASS")
    elif schema=="amos.evaluator-calibration.gate.v1":
        require(x,["session_id","verdict","checks","policy_hash","authority_semantics","deployment_semantics","receipt_hash"])
        if x["verdict"] not in {"PASS","FAIL","INCONCLUSIVE"}: raise ContractError("invalid verdict")
        if x["deployment_semantics"]!="RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY": raise ContractError("invalid deployment semantics")
    elif schema=="amos.evaluator-calibration.drift.v1":
        require(x,["baseline_session_id","candidate_session_id","state","reasons","causal_semantics","authority_semantics","receipt_hash"])
        if x["state"] not in {"COMPARABLE","NOT_COMPARABLE"}: raise ContractError("invalid drift state")
        if x["state"]=="NOT_COMPARABLE" and not x["reasons"]: raise ContractError("NOT_COMPARABLE requires reasons")
        if x["causal_semantics"]!="EVALUATOR_DRIFT_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION": raise ContractError("invalid causal semantics")
    else:
        raise ContractError("unknown schema")
    return True

def self_test():
    good={"schema":"amos.evaluator-calibration.gate.v1","session_id":"s","verdict":"PASS","checks":[],"policy_hash":"a"*64,"authority_semantics":"CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY","deployment_semantics":"RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY","receipt_hash":"b"*64}
    validate(good)
    try: validate({**good,"prompt":"x"})
    except ContractError: pass
    else: raise AssertionError("raw field not rejected")
    print("calibration_contract_check self-test: PASS")

if __name__=="__main__":
    if len(sys.argv)==2 and sys.argv[1]=="--self-test": self_test(); raise SystemExit(0)
    if len(sys.argv)!=2: raise SystemExit("usage: calibration_contract_check.py RECEIPT.json | --self-test")
    obj=json.loads(Path(sys.argv[1]).read_text())
    validate(obj)
    print("PASS")
