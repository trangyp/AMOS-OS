#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sqlite3, time, uuid
from pathlib import Path
from typing import Any

KINDS={'SOURCE_REPO','CODE','SKILL','AGENT','WORKFLOW','TOOL','MODEL','DATASET','DEPENDENCY','RUNTIME','CONFIG','CONTAINER','BUILD_ARTIFACT','OUTPUT','OTHER'}
RELATIONS={'DEPENDS_ON','BUILT_FROM','TRAINED_ON','CONFIGURED_BY','EXECUTES_ON','PACKAGED_IN','PRODUCES','USES_TOOL','EVALUATED_BY','DERIVED_FROM','DESCRIBES','CONTAINS'}
SIG_STATES={'NOT_PRESENT','UNVERIFIED','VERIFIED_EXTERNAL'}
VULN_STATES={'APPLICABLE','NOT_APPLICABLE','UNKNOWN'}
FORBIDDEN={'authorization','api_key','token','password','secret','raw_prompt','raw_output','raw_input','completion','chain_of_thought','reasoning'}
POLICY_KEYS=('require_attestation','require_verified_signature','require_vulnerability_evidence','require_environment_identity','require_output_binding','require_replay_evidence')

class AIBOMError(ValueError): pass

def canon(x:Any)->str: return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def hjson(x:Any)->str: return hashlib.sha256(canon(x).encode()).hexdigest()
def hex64(x:Any)->bool: return isinstance(x,str) and len(x)==64 and all(c in '0123456789abcdef' for c in x)
def nonempty(name:str,x:Any)->str:
    if not isinstance(x,str) or not x.strip(): raise AIBOMError(f'{name} must be a non-empty string')
    return x.strip()
def safe(x:Any,path='$')->None:
    if isinstance(x,dict):
        for k,v in x.items():
            if str(k).lower() in FORBIDDEN: raise AIBOMError(f'forbidden persistent field at {path}.{k}')
            safe(v,f'{path}.{k}')
    elif isinstance(x,list):
        for i,v in enumerate(x): safe(v,f'{path}[{i}]')
def vulnerability_applicable(version_match:bool|None,configuration_match:bool|None,component_present:bool|None)->str:
    xs=(version_match,configuration_match,component_present)
    return 'UNKNOWN' if any(v is None for v in xs) else ('APPLICABLE' if all(xs) else 'NOT_APPLICABLE')
def closure_vector(**dims:bool)->dict[str,Any]:
    out={k:bool(v) for k,v in dims.items()}; out['closed']=all(out.values()); return out

class ManifestPolicy:
    def __init__(self,**kw:bool):
        bad=set(kw)-set(POLICY_KEYS)
        if bad: raise AIBOMError(f'unknown policy keys: {sorted(bad)}')
        for k in POLICY_KEYS: setattr(self,k,bool(kw.get(k,False)))
    def to_dict(self)->dict[str,bool]: return {k:getattr(self,k) for k in POLICY_KEYS}

class AIBOMStore:
    def __init__(self,path:str|Path=':memory:'):
        self.db=sqlite3.connect(str(path)); self.db.row_factory=sqlite3.Row; self.db.execute('PRAGMA foreign_keys=ON'); self._schema()
    def close(self): self.db.close()
    def _schema(self):
        self.db.executescript('''
CREATE TABLE IF NOT EXISTS manifests(id TEXT PRIMARY KEY,root TEXT NOT NULL,repo TEXT NOT NULL,ref TEXT NOT NULL,build TEXT NOT NULL,env TEXT,supersedes TEXT,policy TEXT NOT NULL,created INTEGER NOT NULL,sealed INTEGER,mhash TEXT,status TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS components(mid TEXT NOT NULL,cid TEXT NOT NULL,kind TEXT NOT NULL,name TEXT NOT NULL,version TEXT,uri TEXT,digest TEXT,format TEXT NOT NULL,source_ref TEXT NOT NULL,metadata TEXT NOT NULL,PRIMARY KEY(mid,cid));
CREATE TABLE IF NOT EXISTS relations(mid TEXT NOT NULL,src TEXT NOT NULL,rel TEXT NOT NULL,tgt TEXT NOT NULL,evidence TEXT NOT NULL,PRIMARY KEY(mid,src,rel,tgt,evidence));
CREATE TABLE IF NOT EXISTS attestations(aid TEXT PRIMARY KEY,mid TEXT NOT NULL,cid TEXT NOT NULL,stype TEXT NOT NULL,ptype TEXT NOT NULL,digest TEXT NOT NULL,issuer TEXT,sig_state TEXT NOT NULL,verifier TEXT,verifier_version TEXT,evidence TEXT NOT NULL,ahash TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS vulns(fid TEXT PRIMARY KEY,mid TEXT NOT NULL,cid TEXT NOT NULL,vid TEXT NOT NULL,scanner TEXT NOT NULL,scanner_version TEXT NOT NULL,db_snapshot TEXT NOT NULL,version_match INTEGER,config_match INTEGER,present INTEGER,applicability TEXT NOT NULL,evidence TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS flags(mid TEXT NOT NULL,name TEXT NOT NULL,present INTEGER NOT NULL,evidence TEXT NOT NULL,PRIMARY KEY(mid,name));
CREATE TABLE IF NOT EXISTS bindings(bid TEXT PRIMARY KEY,mid TEXT NOT NULL,execution TEXT NOT NULL,artifact_hash TEXT NOT NULL,aibom_hash TEXT NOT NULL,trace TEXT,eval_hash TEXT,evidence TEXT NOT NULL,created INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS ledger(seq INTEGER PRIMARY KEY AUTOINCREMENT,mid TEXT NOT NULL,event TEXT NOT NULL,payload_hash TEXT NOT NULL,prev TEXT NOT NULL,ehash TEXT NOT NULL,ts INTEGER NOT NULL);
'''); self.db.commit()
    def _m(self,mid):
        r=self.db.execute('SELECT * FROM manifests WHERE id=?',(mid,)).fetchone()
        if not r: raise AIBOMError(f'unknown manifest_id: {mid}')
        return r
    def _open(self,mid):
        r=self._m(mid)
        if r['sealed'] is not None: raise AIBOMError('manifest is sealed and immutable')
        return r
    def _c(self,mid,cid):
        r=self.db.execute('SELECT * FROM components WHERE mid=? AND cid=?',(mid,cid)).fetchone()
        if not r: raise AIBOMError(f'unknown component_id: {cid}')
        return r
    def _event(self,mid,event,payload):
        safe(payload); ph=hjson(payload); prior=self.db.execute('SELECT ehash FROM ledger ORDER BY seq DESC LIMIT 1').fetchone(); prev=prior['ehash'] if prior else '0'*64; ts=time.time_ns(); eh=hjson({'mid':mid,'event':event,'payload_hash':ph,'prev':prev,'ts':ts})
        self.db.execute('INSERT INTO ledger(mid,event,payload_hash,prev,ehash,ts) VALUES(?,?,?,?,?,?)',(mid,event,ph,prev,eh,ts)); self.db.commit(); return eh
    def create_manifest(self,*,root_component_id,source_repo,source_ref,build_id,environment_id=None,supersedes_manifest_id=None,policy=None,manifest_id=None):
        if supersedes_manifest_id and self._m(supersedes_manifest_id)['sealed'] is None: raise AIBOMError('superseded manifest must be sealed')
        if policy is None: p=ManifestPolicy().to_dict()
        elif isinstance(policy,ManifestPolicy): p=policy.to_dict()
        elif isinstance(policy,dict): p=ManifestPolicy(**policy).to_dict()
        else: raise AIBOMError('policy must be ManifestPolicy, dict, or None')
        mid=manifest_id or uuid.uuid4().hex
        vals=(mid,nonempty('root_component_id',root_component_id),nonempty('source_repo',source_repo),nonempty('source_ref',source_ref),nonempty('build_id',build_id),environment_id,supersedes_manifest_id,canon(p),time.time_ns(),'DRAFT')
        self.db.execute('INSERT INTO manifests(id,root,repo,ref,build,env,supersedes,policy,created,status) VALUES(?,?,?,?,?,?,?,?,?,?)',vals); self.db.commit(); self._event(mid,'MANIFEST_CREATED',{'root':root_component_id,'repo':source_repo,'ref':source_ref,'build':build_id,'env':environment_id,'supersedes':supersedes_manifest_id,'policy':p}); return mid
    def add_component(self,manifest_id,*,component_id,kind,name,version=None,uri=None,digest_sha256=None,source_format='AMOS',source_ref='local',metadata=None):
        self._open(manifest_id); component_id=nonempty('component_id',component_id); name=nonempty('name',name)
        if kind not in KINDS: raise AIBOMError(f'invalid component kind: {kind}')
        if digest_sha256 is not None and not hex64(digest_sha256): raise AIBOMError('digest_sha256 must be 64 lowercase hex chars')
        metadata=metadata or {}; safe(metadata)
        self.db.execute('INSERT INTO components VALUES(?,?,?,?,?,?,?,?,?,?)',(manifest_id,component_id,kind,name,version,uri,digest_sha256,nonempty('source_format',source_format),nonempty('source_ref',source_ref),canon(metadata))); self.db.commit(); self._event(manifest_id,'COMPONENT_ADDED',{'cid':component_id,'kind':kind,'name':name,'version':version,'uri':uri,'digest':digest_sha256,'format':source_format,'source_ref':source_ref,'metadata_hash':hjson(metadata)})
    def add_relationship(self,manifest_id,*,source_component_id,relation,target_component_id,evidence_ref):
        self._open(manifest_id)
        if relation not in RELATIONS: raise AIBOMError(f'invalid relation: {relation}')
        self._c(manifest_id,source_component_id); self._c(manifest_id,target_component_id); evidence_ref=nonempty('evidence_ref',evidence_ref)
        self.db.execute('INSERT INTO relations VALUES(?,?,?,?,?)',(manifest_id,source_component_id,relation,target_component_id,evidence_ref)); self.db.commit(); self._event(manifest_id,'RELATIONSHIP_ADDED',{'src':source_component_id,'rel':relation,'tgt':target_component_id,'evidence':evidence_ref})
    def mark_evidence(self,manifest_id,flag_name,present,evidence_ref):
        self._open(manifest_id); flag_name=nonempty('flag_name',flag_name); evidence_ref=nonempty('evidence_ref',evidence_ref)
        self.db.execute('INSERT OR REPLACE INTO flags VALUES(?,?,?,?)',(manifest_id,flag_name,int(bool(present)),evidence_ref)); self.db.commit(); self._event(manifest_id,'EVIDENCE_FLAG_SET',{'name':flag_name,'present':bool(present),'evidence':evidence_ref})
    def add_in_toto_attestation(self,manifest_id,*,subject_component_id,statement,evidence_ref,signature_state='UNVERIFIED',issuer=None,verifier_id=None,verifier_version=None,attestation_id=None):
        self._open(manifest_id); c=self._c(manifest_id,subject_component_id); safe(statement)
        if statement.get('_type')!='https://in-toto.io/Statement/v1': raise AIBOMError('only in-toto Statement/v1 is accepted')
        ptype=nonempty('predicateType',statement.get('predicateType')); subjects=statement.get('subject')
        if not isinstance(subjects,list) or not subjects: raise AIBOMError('subject must be a non-empty list')
        if not c['digest']: raise AIBOMError('attested component requires digest_sha256')
        if not any(isinstance(s,dict) and isinstance(s.get('digest'),dict) and s['digest'].get('sha256')==c['digest'] for s in subjects): raise AIBOMError('attestation subject digest does not bind to component digest')
        if signature_state not in SIG_STATES: raise AIBOMError('invalid signature_state')
        if signature_state=='VERIFIED_EXTERNAL': nonempty('verifier_id',verifier_id); nonempty('verifier_version',verifier_version); nonempty('evidence_ref',evidence_ref)
        aid=attestation_id or uuid.uuid4().hex; ah=hjson(statement)
        self.db.execute('INSERT INTO attestations VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(aid,manifest_id,subject_component_id,statement['_type'],ptype,c['digest'],issuer,signature_state,verifier_id,verifier_version,nonempty('evidence_ref',evidence_ref),ah)); self.db.commit(); self._event(manifest_id,'ATTESTATION_ADDED',{'aid':aid,'cid':subject_component_id,'stype':statement['_type'],'ptype':ptype,'digest':c['digest'],'issuer':issuer,'sig_state':signature_state,'verifier':verifier_id,'verifier_version':verifier_version,'evidence':evidence_ref,'ahash':ah}); return aid
    def add_vulnerability(self,manifest_id,*,component_id,vulnerability_id,scanner_id,scanner_version,database_snapshot,version_match,configuration_match,evidence_ref,finding_id=None):
        self._open(manifest_id); self._c(manifest_id,component_id); app=vulnerability_applicable(version_match,configuration_match,True); fid=finding_id or uuid.uuid4().hex
        vals=(fid,manifest_id,component_id,nonempty('vulnerability_id',vulnerability_id),nonempty('scanner_id',scanner_id),nonempty('scanner_version',scanner_version),nonempty('database_snapshot',database_snapshot),None if version_match is None else int(version_match),None if configuration_match is None else int(configuration_match),1,app,nonempty('evidence_ref',evidence_ref))
        self.db.execute('INSERT INTO vulns VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',vals); self.db.commit(); self._event(manifest_id,'VULNERABILITY_RECORDED',{'fid':fid,'cid':component_id,'vid':vulnerability_id,'scanner':scanner_id,'scanner_version':scanner_version,'db_snapshot':database_snapshot,'version_match':version_match,'config_match':configuration_match,'present':True,'applicability':app,'evidence':evidence_ref}); return fid
    def import_cyclonedx_json(self,manifest_id,document,*,source_ref):
        self._open(manifest_id); safe(document); xs=document.get('components')
        if not isinstance(xs,list): raise AIBOMError('CycloneDX document requires components list')
        tm={'machine-learning-model':'MODEL','container':'CONTAINER','application':'BUILD_ARTIFACT','library':'DEPENDENCY','framework':'DEPENDENCY','operating-system':'RUNTIME','device':'RUNTIME','file':'CODE'}; ids={}; out=[]
        for i,x in enumerate(xs):
            if not isinstance(x,dict): raise AIBOMError('CycloneDX component must be object')
            sid=str(x.get('bom-ref') or f'cyclonedx:{i}'); cid='cdx:'+sid; dg=None
            for q in x.get('hashes') or []:
                if isinstance(q,dict) and str(q.get('alg','')).replace('-','').upper()=='SHA256' and hex64(q.get('content')): dg=q['content']; break
            md={}
            if 'modelCard' in x: md['model_card_hash']=hjson(x['modelCard'])
            self.add_component(manifest_id,component_id=cid,kind=tm.get(x.get('type'),'OTHER'),name=str(x.get('name') or sid),version=x.get('version'),uri=x.get('purl'),digest_sha256=dg,source_format=f'CycloneDX-{document.get("specVersion","unknown")}',source_ref=source_ref,metadata=md); ids[sid]=cid; out.append(cid)
        for d in document.get('dependencies') or []:
            if isinstance(d,dict) and ids.get(str(d.get('ref'))):
                for tgt in d.get('dependsOn') or []:
                    if ids.get(str(tgt)): self.add_relationship(manifest_id,source_component_id=ids[str(d['ref'])],relation='DEPENDS_ON',target_component_id=ids[str(tgt)],evidence_ref=source_ref)
        return out
    def import_spdx_json(self,manifest_id,document,*,source_ref):
        self._open(manifest_id); safe(document); xs=document.get('packages')
        if not isinstance(xs,list): raise AIBOMError('SPDX JSON requires packages list')
        ids={}; out=[]
        for i,x in enumerate(xs):
            if not isinstance(x,dict): raise AIBOMError('SPDX package must be object')
            sid=str(x.get('SPDXID') or f'SPDXRef-{i}'); cid='spdx:'+sid; dg=None
            for q in x.get('checksums') or []:
                if isinstance(q,dict) and str(q.get('algorithm','')).replace('-','').upper()=='SHA256' and hex64(q.get('checksumValue')): dg=q['checksumValue']; break
            self.add_component(manifest_id,component_id=cid,kind='DEPENDENCY',name=str(x.get('name') or sid),version=x.get('versionInfo'),uri=x.get('downloadLocation'),digest_sha256=dg,source_format=str(document.get('spdxVersion') or 'SPDX'),source_ref=source_ref,metadata={'supplier':x.get('supplier')} if x.get('supplier') else {}); ids[sid]=cid; out.append(cid)
        rm={'DEPENDS_ON':'DEPENDS_ON','DEPENDENCY_OF':'DEPENDS_ON','DESCRIBES':'DESCRIBES','CONTAINS':'CONTAINS','GENERATED_FROM':'DERIVED_FROM'}
        for r in document.get('relationships') or []:
            if not isinstance(r,dict) or r.get('relationshipType') not in rm: continue
            typ=r['relationshipType']; a=ids.get(str(r.get('spdxElementId'))); b=ids.get(str(r.get('relatedSpdxElement')))
            if typ=='DEPENDENCY_OF': a,b=b,a
            if a and b: self.add_relationship(manifest_id,source_component_id=a,relation=rm[typ],target_component_id=b,evidence_ref=source_ref)
        return out
    def _payload(self,mid):
        m=self._m(mid); comps=[]
        for r in self.db.execute('SELECT cid,kind,name,version,uri,digest,format,source_ref,metadata FROM components WHERE mid=? ORDER BY cid',(mid,)):
            d=dict(r); d['metadata']=json.loads(d['metadata']); comps.append(d)
        def rows(sql): return [dict(r) for r in self.db.execute(sql,(mid,))]
        return {'schema':'amos.aibom.v1','manifest_id':mid,'root_component_id':m['root'],'source_repo':m['repo'],'source_ref':m['ref'],'build_id':m['build'],'environment_id':m['env'],'supersedes_manifest_id':m['supersedes'],'policy':json.loads(m['policy']),'components':comps,'relationships':rows('SELECT src,rel,tgt,evidence FROM relations WHERE mid=? ORDER BY src,rel,tgt,evidence'),'attestations':rows('SELECT aid,cid,stype,ptype,digest,issuer,sig_state,verifier,verifier_version,evidence,ahash FROM attestations WHERE mid=? ORDER BY aid'),'vulnerabilities':rows('SELECT fid,cid,vid,scanner,scanner_version,db_snapshot,version_match,config_match,present,applicability,evidence FROM vulns WHERE mid=? ORDER BY fid'),'evidence_flags':rows('SELECT name,present,evidence FROM flags WHERE mid=? ORDER BY name')}
    def _verify(self,mid,check_hash=True):
        m=self._m(mid); cs=list(self.db.execute('SELECT * FROM components WHERE mid=?',(mid,))); ids={x['cid'] for x in cs}; root=m['root'] in ids; hashes=all(x['digest'] is None or hex64(x['digest']) for x in cs); lineage=root and all(x['src'] in ids and x['tgt'] in ids for x in self.db.execute('SELECT * FROM relations WHERE mid=?',(mid,))); ats=list(self.db.execute('SELECT * FROM attestations WHERE mid=?',(mid,))); bound=True; sig=True
        for a in ats:
            bound &= self._c(mid,a['cid'])['digest']==a['digest']
            if a['sig_state']=='VERIFIED_EXTERNAL': sig &= bool(a['verifier'] and a['verifier_version'] and a['evidence'])
        vs=list(self.db.execute('SELECT * FROM vulns WHERE mid=?',(mid,))); vvalid=all(v['cid'] in ids and v['applicability'] in VULN_STATES for v in vs); flags={x['name']:bool(x['present']) for x in self.db.execute('SELECT * FROM flags WHERE mid=?',(mid,))}; p=json.loads(m['policy']); binds=list(self.db.execute('SELECT * FROM bindings WHERE mid=?',(mid,));); checks={'attestation':not p['require_attestation'] or bool(ats),'verified_signature':not p['require_verified_signature'] or any(a['sig_state']=='VERIFIED_EXTERNAL' for a in ats),'vulnerability_evidence':not p['require_vulnerability_evidence'] or bool(vs),'environment_identity':not p['require_environment_identity'] or bool(m['env']),'output_binding':not p['require_output_binding'] or bool(binds),'replay_evidence':not p['require_replay_evidence'] or flags.get('replay_evidence',False)}; expected=hjson(self._payload(mid)); mh_ok=not(check_hash and m['mhash'] is not None) or m['mhash']==expected; structural=all((bool(cs),root,hashes,lineage,bound,sig,vvalid,mh_ok))
        return {'manifest_id':mid,'schema_valid':True,'root_present':root,'hashes_valid':hashes,'lineage_closed':lineage,'attestation_subject_bound':bound,'signature_claims_supported':sig,'vulnerability_attribution_valid':vvalid,'manifest_hash_valid':mh_ok,'structural_integrity':structural,'policy_complete':all(checks.values()),'policy_checks':checks,'component_count':len(cs),'attestation_count':len(ats),'vulnerability_count':len(vs),'output_binding_count':len(binds),'sealed':m['sealed'] is not None,'manifest_hash':m['mhash'],'expected_manifest_hash':expected,'authority_semantics':'AIBOM_EVIDENCE_DOES_NOT_GRANT_AUTHORITY','trust_semantics':'DIGEST_OR_SIGNATURE_EVIDENCE_DOES_NOT_PROVE_SEMANTIC_CORRECTNESS','completeness_semantics':'BOM_PRESENT_DOES_NOT_PROVE_COMPLETE_INVENTORY'}
    def seal_manifest(self,manifest_id):
        self._open(manifest_id); r=self._verify(manifest_id,False)
        if not r['structural_integrity']: raise AIBOMError('cannot seal structurally invalid manifest')
        mh=hjson(self._payload(manifest_id)); ts=time.time_ns(); self.db.execute("UPDATE manifests SET sealed=?,mhash=?,status='SEALED' WHERE id=?",(ts,mh,manifest_id)); self.db.commit(); self._event(manifest_id,'MANIFEST_SEALED',{'manifest_hash':mh,'sealed_at_ns':ts,'policy_complete':r['policy_complete']}); return self.verify_manifest(manifest_id)
    def bind_output(self,manifest_id,*,execution_id,artifact_hash,aibom_hash,evidence_ref,trace_id=None,evaluation_receipt_hash=None,binding_id=None):
        m=self._m(manifest_id)
        if m['sealed'] is None: raise AIBOMError('output binding requires sealed manifest')
        if not hex64(artifact_hash) or not hex64(aibom_hash): raise AIBOMError('artifact_hash and aibom_hash must be sha256 hex')
        if m['mhash']!=aibom_hash: raise AIBOMError('aibom_hash must equal sealed manifest hash')
        if evaluation_receipt_hash is not None and not hex64(evaluation_receipt_hash): raise AIBOMError('evaluation_receipt_hash must be sha256 hex or null')
        bid=binding_id or uuid.uuid4().hex; vals=(bid,manifest_id,nonempty('execution_id',execution_id),artifact_hash,aibom_hash,trace_id,evaluation_receipt_hash,nonempty('evidence_ref',evidence_ref),time.time_ns()); self.db.execute('INSERT INTO bindings VALUES(?,?,?,?,?,?,?,?,?)',vals); self.db.commit(); self._event(manifest_id,'OUTPUT_BOUND',{'bid':bid,'execution':execution_id,'artifact_hash':artifact_hash,'aibom_hash':aibom_hash,'trace':trace_id,'eval_hash':evaluation_receipt_hash,'evidence':evidence_ref}); return bid
    def verify_manifest(self,manifest_id):
        r=self._verify(manifest_id,True); r['receipt_hash']=hjson(r); return r
    def output_bindings(self,manifest_id): self._m(manifest_id); return [dict(r) for r in self.db.execute('SELECT * FROM bindings WHERE mid=? ORDER BY created,bid',(manifest_id,))]
    def closure(self,manifest_id):
        m=self._m(manifest_id); kinds={r['kind'] for r in self.db.execute('SELECT kind FROM components WHERE mid=?',(manifest_id,))}; f={r['name']:bool(r['present']) for r in self.db.execute('SELECT * FROM flags WHERE mid=?',(manifest_id,))}; return closure_vector(component_inventory=bool(kinds),environment_identity=bool(m['env']),model_lineage=('MODEL' not in kinds) or f.get('model_lineage',False),runtime_capture=('RUNTIME' not in kinds) or f.get('runtime_capture',False),output_binding=bool(self.output_bindings(manifest_id)),replay_evidence=f.get('replay_evidence',False))
    def compare_manifests(self,old_manifest_id,new_manifest_id):
        a=self._m(old_manifest_id); b=self._m(new_manifest_id)
        if a['sealed'] is None or b['sealed'] is None: raise AIBOMError('both manifests must be sealed for comparison')
        if a['repo']!=b['repo']: return {'state':'NOT_COMPARABLE','reasons':['source_repo mismatch'],'authority_semantics':'DRIFT_RESULT_DOES_NOT_GRANT_AUTHORITY'}
        def items(mid): return {r['cid']:r for r in self.db.execute('SELECT * FROM components WHERE mid=?',(mid,))}
        x,y=items(old_manifest_id),items(new_manifest_id); added=sorted(set(y)-set(x)); removed=sorted(set(x)-set(y)); dg=[]; ver=[]; kind=[]
        for cid in sorted(set(x)&set(y)):
            if x[cid]['digest']!=y[cid]['digest']: dg.append(cid)
            if x[cid]['version']!=y[cid]['version']: ver.append(cid)
            if x[cid]['kind']!=y[cid]['kind']: kind.append(cid)
        material={'MODEL','DATASET','RUNTIME','CONFIG','CONTAINER','BUILD_ARTIFACT'}; changed=sorted({cid for cid in added+removed+dg+ver+kind if (x.get(cid) or y.get(cid))['kind'] in material}); r={'state':'COMPARABLE','old_manifest_id':old_manifest_id,'new_manifest_id':new_manifest_id,'old_hash':a['mhash'],'new_hash':b['mhash'],'added_component_ids':added,'removed_component_ids':removed,'digest_changed_component_ids':dg,'version_changed_component_ids':ver,'kind_changed_component_ids':kind,'material_changed_component_ids':changed,'source_ref_changed':a['ref']!=b['ref'],'build_id_changed':a['build']!=b['build'],'environment_id_changed':a['env']!=b['env'],'causal_semantics':'AIBOM_DRIFT_DOES_NOT_IDENTIFY_CAUSE','authority_semantics':'DRIFT_RESULT_DOES_NOT_GRANT_AUTHORITY'}; r['receipt_hash']=hjson(r); return r
    def verify_ledger(self):
        prev='0'*64; n=0
        for r in self.db.execute('SELECT * FROM ledger ORDER BY seq'):
            if r['prev']!=prev: return {'valid':False,'failed_seq':r['seq'],'reason':'prev_hash mismatch'}
            expected=hjson({'mid':r['mid'],'event':r['event'],'payload_hash':r['payload_hash'],'prev':r['prev'],'ts':r['ts']})
            if r['ehash']!=expected: return {'valid':False,'failed_seq':r['seq'],'reason':'event_hash mismatch'}
            prev=r['ehash']; n+=1
        return {'valid':True,'event_count':n,'head_hash':prev}

def self_test():
    s=AIBOMStore(); m=s.create_manifest(root_component_id='root',source_repo='example/repo',source_ref='abc',build_id='b',environment_id='e',policy=ManifestPolicy(require_environment_identity=True)); s.add_component(m,component_id='root',kind='BUILD_ARTIFACT',name='app',digest_sha256='a'*64); r=s.seal_manifest(m); ok=r['structural_integrity'] and s.verify_ledger()['valid']; s.close(); print('SELF_TEST_PASS' if ok else 'SELF_TEST_FAIL'); return 0 if ok else 1

def main():
    p=argparse.ArgumentParser(); p.add_argument('--self-test',action='store_true'); p.add_argument('--db',default=':memory:'); p.add_argument('--verify-manifest'); p.add_argument('--verify-ledger',action='store_true'); p.add_argument('--diff',nargs=2); a=p.parse_args()
    if a.self_test: return self_test()
    s=AIBOMStore(a.db)
    try:
        if a.verify_manifest: print(json.dumps(s.verify_manifest(a.verify_manifest),indent=2,sort_keys=True)); return 0
        if a.verify_ledger: r=s.verify_ledger(); print(json.dumps(r,indent=2,sort_keys=True)); return 0 if r['valid'] else 1
        if a.diff: print(json.dumps(s.compare_manifests(*a.diff),indent=2,sort_keys=True)); return 0
        p.error('choose --self-test, --verify-manifest, --verify-ledger, or --diff')
    finally: s.close()
if __name__=='__main__': raise SystemExit(main())
