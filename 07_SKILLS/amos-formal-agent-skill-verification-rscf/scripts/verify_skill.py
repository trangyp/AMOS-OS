#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path
from typing import Any

EFFECTS={"FS_READ","FS_WRITE","PROCESS_EXEC","NETWORK","ENV_READ","DYNAMIC_CODE","DYNAMIC_IMPORT","SERIALIZATION_UNSAFE"}
CALL_EFFECTS={
 "open":None,"eval":"DYNAMIC_CODE","exec":"DYNAMIC_CODE","__import__":"DYNAMIC_IMPORT",
 "os.getenv":"ENV_READ","os.environ.get":"ENV_READ","subprocess.run":"PROCESS_EXEC","subprocess.Popen":"PROCESS_EXEC",
 "subprocess.call":"PROCESS_EXEC","subprocess.check_call":"PROCESS_EXEC","subprocess.check_output":"PROCESS_EXEC",
 "os.system":"PROCESS_EXEC","pickle.load":"SERIALIZATION_UNSAFE","pickle.loads":"SERIALIZATION_UNSAFE",
}
WRITE_METHODS={"write_text","write_bytes","unlink","rename","replace","mkdir","rmdir","touch"}
READ_METHODS={"read_text","read_bytes","exists","is_file","is_dir","glob","rglob","iterdir"}

NETWORK_PREFIXES=("requests.","httpx.","urllib.","socket.","aiohttp.","http.","ftplib.")

class VError(RuntimeError): pass

def call_effect(name:str)->str|None:
    direct=CALL_EFFECTS.get(name)
    if direct: return direct
    if any(name.startswith(prefix) for prefix in NETWORK_PREFIXES): return "NETWORK"
    return None

def sha256_bytes(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def dotted(n:ast.AST)->str:
    if isinstance(n,ast.Name): return n.id
    if isinstance(n,ast.Attribute):
        p=dotted(n.value); return f"{p}.{n.attr}" if p else n.attr
    return ""

def effect_scan(path:Path)->dict[str,Any]:
    src=path.read_text(encoding="utf-8")
    try: tree=ast.parse(src,filename=str(path))
    except SyntaxError as e: return {"path":str(path),"parse_error":str(e),"effects":[],"findings":[],"unknown_dynamic":True}
    effects=set(); findings=[]; unknown=False
    for node in ast.walk(tree):
        if isinstance(node,(ast.Import,ast.ImportFrom)):
            mods=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module or ""]
            for m in mods:
                if m.split('.')[0] in {"subprocess"}: effects.add("PROCESS_EXEC")
                if m.split('.')[0] in {"socket","requests","urllib","http","ftplib"}: effects.add("NETWORK")
                if m.split('.')[0] in {"pickle","marshal"}: effects.add("SERIALIZATION_UNSAFE")
        if isinstance(node,ast.Call):
            name=dotted(node.func)
            eff=call_effect(name)
            if eff: effects.add(eff); findings.append({"line":getattr(node,"lineno",0),"call":name,"effect":eff})
            if name=="open":
                mode="r"
                if len(node.args)>1 and isinstance(node.args[1],ast.Constant) and isinstance(node.args[1].value,str): mode=node.args[1].value
                for kw in node.keywords:
                    if kw.arg=="mode" and isinstance(kw.value,ast.Constant) and isinstance(kw.value.value,str): mode=kw.value.value
                eff2="FS_WRITE" if any(c in mode for c in "wax+") else "FS_READ"
                effects.add(eff2); findings.append({"line":getattr(node,"lineno",0),"call":"open","effect":eff2})
            if isinstance(node.func,ast.Attribute):
                if node.func.attr in WRITE_METHODS: effects.add("FS_WRITE"); findings.append({"line":getattr(node,"lineno",0),"call":name,"effect":"FS_WRITE"})
                if node.func.attr in READ_METHODS: effects.add("FS_READ"); findings.append({"line":getattr(node,"lineno",0),"call":name,"effect":"FS_READ"})
            if name in {"getattr","setattr"} and any(not isinstance(a,ast.Constant) for a in node.args[1:2]): unknown=True
    return {"path":str(path),"sha256":sha256_bytes(src.encode()),"effects":sorted(effects),"findings":findings,"unknown_dynamic":unknown,"parse_error":None}

def verify(skill_dir:str|Path, manifest_path:str|Path)->dict[str,Any]:
    root=Path(skill_dir).resolve(); mp=Path(manifest_path)
    manifest=json.loads(mp.read_text(encoding="utf-8"))
    allowed=set(manifest.get("allowed_effects",[])); unknown_decl=allowed-EFFECTS
    if unknown_decl: raise VError("unknown allowed effects: "+",".join(sorted(unknown_decl)))
    scripts=sorted((root/"scripts").rglob("*.py")) if (root/"scripts").exists() else []
    scans=[effect_scan(p) for p in scripts]
    observed=set().union(*(set(s["effects"]) for s in scans)) if scans else set()
    violations=sorted(observed-allowed)
    parse_errors=[s for s in scans if s["parse_error"]]
    dynamic=any(s["unknown_dynamic"] for s in scans)
    if violations or parse_errors: verdict="VIOLATION"
    elif dynamic: verdict="UNKNOWN"
    else: verdict="CONTAINED"
    receipt={"schema":"amos.skill-capability-containment.v1","skill":root.name,"allowed_effects":sorted(allowed),"observed_effects":sorted(observed),"violations":violations,"dynamic_unknown":dynamic,"parse_error_count":len(parse_errors),"scanned_scripts":len(scans),"verdict":verdict,"scope":"PYTHON_AST_OVERAPPROXIMATION_ONLY","authority_semantics":"CONTAINMENT_EVIDENCE_DOES_NOT_GRANT_EXECUTION_AUTHORITY","formal_semantics":"CONTAINED_DOES_NOT_MEAN_SEMANTICALLY_SAFE_OR_FORMALLY_VERIFIED","files":[{"path":str(Path(s['path']).relative_to(root)),"sha256":s.get("sha256"),"effects":s["effects"],"unknown_dynamic":s["unknown_dynamic"],"parse_error":s["parse_error"]} for s in scans]}
    x=dict(receipt); receipt["receipt_hash"]=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest(); return receipt

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("skill_dir"); ap.add_argument("manifest"); ap.add_argument("--json",action="store_true"); a=ap.parse_args(); r=verify(a.skill_dir,a.manifest); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r["verdict"]=="CONTAINED" else 2)
if __name__=="__main__": main()
