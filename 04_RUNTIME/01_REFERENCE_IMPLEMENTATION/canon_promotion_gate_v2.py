"""K_CANON repair candidate: deterministic Canon promotion eligibility gate.

Origin architect / steward: Trang Phan.

This module does not mutate Canon. It decides whether a proposed immutable
Canon append is eligible for a separately authorized durable commit. Confidence
is metadata only and is deliberately excluded from the eligibility conjunction.

Cryptographic conventions:
- Ed25519 signature verification uses RFC 8032-compatible primitives.
- Merkle leaf/internal-node domain separation follows the Certificate
  Transparency Merkle Tree Hash construction (0x00 leaf, 0x01 node).
"""
from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

EPISTEMIC_CLASSES = frozenset({"SOURCE_CLAIM","OBSERVATION","DERIVED","MODEL","DECISION","UNKNOWN"})
CONCLUSION_CLASSES = frozenset({"VERIFIED","DERIVED","MODEL","CONDITIONAL","COMPETING","UNKNOWN/GAP"})


def _is_sha256(x: Any) -> bool:
    return isinstance(x,str) and len(x)==64 and all(c in '0123456789abcdef' for c in x.lower())


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def leaf_hash(data: bytes) -> bytes:
    return hashlib.sha256(b'\x00' + data).digest()


def node_hash(left: bytes, right: bytes) -> bytes:
    if len(left)!=32 or len(right)!=32:
        raise ValueError('Merkle children must be SHA-256 digests')
    return hashlib.sha256(b'\x01' + left + right).digest()


def merkle_tree_hash(leaves: Sequence[bytes]) -> bytes:
    """RFC-9162-style Merkle Tree Hash over raw leaf payloads."""
    n=len(leaves)
    if n==0:
        return hashlib.sha256(b'').digest()
    if n==1:
        return leaf_hash(leaves[0])
    k=1 << ((n-1).bit_length()-1)
    return node_hash(merkle_tree_hash(leaves[:k]), merkle_tree_hash(leaves[k:]))


def authority_message(claim_id: str, payload_sha256: str, epoch: int) -> bytes:
    if not isinstance(claim_id,str) or not claim_id:
        raise ValueError('claim_id required')
    if not _is_sha256(payload_sha256):
        raise ValueError('payload_sha256 must be 64 hex characters')
    if isinstance(epoch,bool) or not isinstance(epoch,int) or epoch<0:
        raise ValueError('epoch must be a nonnegative integer')
    return b'AMOS_CANON_PROMOTE_V2\x00' + claim_id.encode() + b'\x00' + payload_sha256.lower().encode() + b'\x00' + str(epoch).encode()


def verify_ed25519(public_key_hex: str, signature_hex: str, message: bytes) -> bool:
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        key=Ed25519PublicKey.from_public_bytes(bytes.fromhex(public_key_hex))
        key.verify(bytes.fromhex(signature_hex), message)
        return True
    except Exception:
        return False


def _origin_record(x: Any) -> Optional[Tuple[str,str,frozenset]]:
    if not isinstance(x,Mapping): return None
    eid=x.get('evidence_id'); root=x.get('root_id'); ancestry=x.get('ancestry',[])
    if not isinstance(eid,str) or not eid or not isinstance(root,str) or not root:
        return None
    if not isinstance(ancestry,list) or any(not isinstance(a,str) or not a for a in ancestry):
        return None
    return eid,root,frozenset(ancestry)


def independent_evidence_pairs(evidence: Sequence[Any], trusted_common_roots: Iterable[str]=()) -> List[Tuple[str,str]]:
    """Return provenance-independent pairs under a conservative ancestry rule."""
    trusted=frozenset(trusted_common_roots)
    rows=[r for r in (_origin_record(x) for x in evidence) if r is not None]
    out=[]
    for i,(ei,ri,ai) in enumerate(rows):
        for ej,rj,aj in rows[i+1:]:
            if ri==rj: continue
            if (ai & aj) - trusted: continue
            if ri in aj or rj in ai: continue
            out.append((ei,ej))
    return out


def evaluate_canon_promotion(request: Mapping[str,Any], *, now: Optional[float]=None) -> Dict[str,Any]:
    """Evaluate eligibility; never performs Canon mutation."""
    def hold(reason: str, **extra: Any) -> Dict[str,Any]:
        return {
            'success': False,'status':'HOLD_CANON_PROMOTION','eligible':False,
            'commit_eligible':False,'canon_promoted':False,'mutation_performed':False,
            'authority_granted':False,'reason':reason,**extra,
        }
    if not isinstance(request,Mapping): return hold('ILL_TYPED_REQUEST')
    required={
        'claim_id','payload','epistemic_class','conclusion_class','scope','regime',
        'freshness_status','proof_status','proof_capsule_sha256','contradictions',
        'evidence_roots','validators','authority_witness','expected_canon_epoch','current_canon_epoch'
    }
    miss=sorted(required-set(request))
    if miss: return hold('MISSING_FIELDS',missing_fields=miss)

    claim_id=request['claim_id']; payload=request['payload']
    if not isinstance(claim_id,str) or not claim_id.strip(): return hold('INVALID_CLAIM_ID')
    if not isinstance(payload,Mapping): return hold('INVALID_PAYLOAD')
    payload_sha=hashlib.sha256(canonical_json_bytes(payload)).hexdigest()

    ep=str(request['epistemic_class']).upper(); cc=str(request['conclusion_class']).upper()
    if ep not in EPISTEMIC_CLASSES: return hold('INVALID_EPISTEMIC_CLASS')
    if cc not in CONCLUSION_CLASSES: return hold('INVALID_CONCLUSION_CLASS')
    if cc!='VERIFIED': return hold('CONCLUSION_NOT_VERIFIED')
    if request['scope'] in (None,'',{},[]): return hold('SCOPE_REQUIRED')
    if request['regime'] in (None,'',{},[]): return hold('REGIME_REQUIRED')
    if str(request['freshness_status']).upper()!='FRESH': return hold('STALE_OR_UNKNOWN_FRESHNESS')
    if str(request['proof_status']).upper()!='PASS': return hold('PROOF_NOT_PASSED')
    if not _is_sha256(str(request['proof_capsule_sha256']).lower()): return hold('INVALID_PROOF_CAPSULE_HASH')

    contradictions=request['contradictions']
    if not isinstance(contradictions,list): return hold('CONTRADICTIONS_MUST_BE_LIST')
    if contradictions: return hold('ACTIVE_CONTRADICTION',contradiction_count=len(contradictions))

    evidence=request['evidence_roots']
    if not isinstance(evidence,list): return hold('EVIDENCE_ROOTS_MUST_BE_LIST')
    if any(_origin_record(x) is None for x in evidence): return hold('MALFORMED_EVIDENCE_ROOT')
    trusted=request.get('trusted_common_roots',[])
    if not isinstance(trusted,list) or any(not isinstance(x,str) for x in trusted): return hold('MALFORMED_TRUST_ROOTS')
    independent=independent_evidence_pairs(evidence,trusted)
    if not independent: return hold('RULE_OF_2_INDEPENDENCE_NOT_MET')

    validators=request['validators']
    if not isinstance(validators,list) or len(validators)<2: return hold('TWO_VALIDATORS_REQUIRED')
    vids=[]
    for v in validators:
        if not isinstance(v,Mapping) or not isinstance(v.get('validator_id'),str) or not v.get('validator_id'):
            return hold('MALFORMED_VALIDATOR')
        if str(v.get('status','')).upper()!='PASS': return hold('VALIDATOR_NOT_PASSED')
        vids.append(v['validator_id'])
    if len(set(vids))<2: return hold('VALIDATORS_NOT_INDEPENDENT_BY_ID')

    expected=request['expected_canon_epoch']; current=request['current_canon_epoch']
    if any(isinstance(x,bool) or not isinstance(x,int) or x<0 for x in (expected,current)):
        return hold('ILL_TYPED_CANON_EPOCH')
    if expected!=current: return hold('CANON_EPOCH_CAS_MISMATCH')

    aw=request['authority_witness']
    if not isinstance(aw,Mapping): return hold('MALFORMED_AUTHORITY_WITNESS')
    awreq={'principal','claim_id','action','epoch','issued_at','expires_at','public_key_hex','signature_hex'}
    if awreq-set(aw): return hold('MALFORMED_AUTHORITY_WITNESS',missing_authority_fields=sorted(awreq-set(aw)))
    if aw['claim_id']!=claim_id or aw['action']!='promote_to_canon' or aw['epoch']!=current:
        return hold('AUTHORITY_BINDING_MISMATCH')
    nowv=time.time() if now is None else now
    if not isinstance(nowv,(int,float)) or isinstance(nowv,bool): return hold('ILL_TYPED_NOW')
    issued=aw['issued_at']; expires=aw['expires_at']
    if any(not isinstance(x,(int,float)) or isinstance(x,bool) for x in (issued,expires)):
        return hold('ILL_TYPED_AUTHORITY_TIME')
    if issued>nowv or expires<nowv or expires<issued: return hold('AUTHORITY_NOT_FRESH')
    msg=authority_message(claim_id,payload_sha,current)
    if not verify_ed25519(str(aw['public_key_hex']),str(aw['signature_hex']),msg):
        return hold('AUTHORITY_SIGNATURE_INVALID')

    conf=request.get('confidence')
    if conf is not None and (isinstance(conf,bool) or not isinstance(conf,(int,float)) or not 0<=float(conf)<=1):
        return hold('ILL_TYPED_CONFIDENCE_METADATA')

    prior=request.get('prior_canon_leaf_payloads',[])
    if not isinstance(prior,list) or any(not isinstance(x,(bytes,bytearray,str,Mapping,list,int,float,bool,type(None))) for x in prior):
        return hold('MALFORMED_PRIOR_CANON_LEAVES')
    prior_bytes=[x if isinstance(x,(bytes,bytearray)) else canonical_json_bytes(x) for x in prior]
    leaf_payload=canonical_json_bytes({
        'claim_id':claim_id,'payload_sha256':payload_sha,'proof_capsule_sha256':str(request['proof_capsule_sha256']).lower(),
        'canon_epoch':current+1,'authority_principal':aw['principal']
    })
    prospective_root=merkle_tree_hash(prior_bytes+[leaf_payload]).hex()

    return {
        'success':True,'status':'ELIGIBLE_FOR_AUTHORIZED_COMMIT','eligible':True,
        'commit_eligible':True,'canon_promoted':False,'mutation_performed':False,
        'authority_granted':False,'authority_witness_validated':True,
        'claim_id':claim_id,'payload_sha256':payload_sha,'proof_capsule_sha256':str(request['proof_capsule_sha256']).lower(),
        'independent_evidence_pair':list(independent[0]),'validator_ids':sorted(set(vids)),
        'current_canon_epoch':current,'prospective_canon_epoch':current+1,
        'prospective_merkle_root_sha256':prospective_root,
        'confidence_metadata':conf,'confidence_used_as_promotion_rule':False,
        'boundary':'ELIGIBILITY_DOES_NOT_EQUAL_DURABLE_CANON_COMMIT_OR_EMPIRICAL_TRUTH'
    }
