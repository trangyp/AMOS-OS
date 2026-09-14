from canon_promotion_gate_v2 import *
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding,PublicFormat
import hashlib, random
checks=0

def req(n,c,d=None):
 global checks; checks+=1
 if not c: raise AssertionError((n,d))

priv=Ed25519PrivateKey.generate(); pub=priv.public_key().public_bytes(Encoding.Raw,PublicFormat.Raw).hex()
payload={'claim':'finite theorem','scope':'test'}
payload_sha=hashlib.sha256(canonical_json_bytes(payload)).hexdigest()
def request(conf=.2):
 epoch=7; msg=authority_message('C1',payload_sha,epoch); sig=priv.sign(msg).hex()
 return {
  'claim_id':'C1','payload':payload,'epistemic_class':'DERIVED','conclusion_class':'VERIFIED',
  'scope':'test','regime':'finite','freshness_status':'FRESH','proof_status':'PASS',
  'proof_capsule_sha256':'1'*64,'contradictions':[],
  'evidence_roots':[
    {'evidence_id':'e1','root_id':'r1','ancestry':['a1']},
    {'evidence_id':'e2','root_id':'r2','ancestry':['a2']},
  ],
  'validators':[{'validator_id':'v1','status':'PASS'},{'validator_id':'v2','status':'PASS'}],
  'authority_witness':{'principal':'council','claim_id':'C1','action':'promote_to_canon','epoch':epoch,'issued_at':900,'expires_at':1100,'public_key_hex':pub,'signature_hex':sig},
  'expected_canon_epoch':epoch,'current_canon_epoch':epoch,'confidence':conf,
  'prior_canon_leaf_payloads':[{'old':1},{'old':2}],
 }

r=evaluate_canon_promotion(request(.01),now=1000)
req('eligible-low-confidence',r['eligible'],r); req('confidence-not-rule',r['confidence_used_as_promotion_rule'] is False,r)
r2=evaluate_canon_promotion(request(.99),now=1000)
req('eligible-high-confidence',r2['eligible'],r2); req('same-root-confidence-independent',r['prospective_merkle_root_sha256']==r2['prospective_merkle_root_sha256'])

for mutate,reason in [
 (lambda x:x.update(conclusion_class='CONDITIONAL'),'CONCLUSION_NOT_VERIFIED'),
 (lambda x:x.update(freshness_status='STALE'),'STALE_OR_UNKNOWN_FRESHNESS'),
 (lambda x:x.update(proof_status='UNKNOWN'),'PROOF_NOT_PASSED'),
 (lambda x:x.update(contradictions=['c']),'ACTIVE_CONTRADICTION'),
 (lambda x:x.update(expected_canon_epoch=6),'CANON_EPOCH_CAS_MISMATCH'),
]:
 q=request(); mutate(q); z=evaluate_canon_promotion(q,now=1000); req(reason,not z['eligible'] and z['reason']==reason,z)
q=request(); q['evidence_roots'][1]['root_id']='r1'; z=evaluate_canon_promotion(q,now=1000); req('correlated-roots',z['reason']=='RULE_OF_2_INDEPENDENCE_NOT_MET',z)
q=request(); q['evidence_roots'][1]['ancestry']=['shared']; q['evidence_roots'][0]['ancestry']=['shared']; z=evaluate_canon_promotion(q,now=1000); req('shared-ancestry',z['reason']=='RULE_OF_2_INDEPENDENCE_NOT_MET',z)
q=request(); q['authority_witness']['signature_hex']='00'*64; z=evaluate_canon_promotion(q,now=1000); req('bad-signature',z['reason']=='AUTHORITY_SIGNATURE_INVALID',z)
q=request(); q['authority_witness']['expires_at']=999; z=evaluate_canon_promotion(q,now=1000); req('expired',z['reason']=='AUTHORITY_NOT_FRESH',z)

a=merkle_tree_hash([b'a',b'b',b'c']); b=merkle_tree_hash([b'a',b'b',b'c'])
req('merkle-deterministic',a==b); req('merkle-order-sensitive',a!=merkle_tree_hash([b'c',b'b',b'a']))
req('leaf-node-domain-separation',leaf_hash(b'ab')!=node_hash(hashlib.sha256(b'a').digest(),hashlib.sha256(b'b').digest()))

rng=random.Random(211)
for _ in range(1000):
 c=rng.random(); q=request(c); z=evaluate_canon_promotion(q,now=1000)
 req('confidence-invariant',z['eligible'] is True,(c,z))

print({'suite':'canon_promotion_gate_v2','checks':checks,'status':'PASS'})
