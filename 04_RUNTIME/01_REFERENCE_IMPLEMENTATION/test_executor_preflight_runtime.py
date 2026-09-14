import hashlib
import pytest

import executor_preflight_runtime as e

H=lambda s: hashlib.sha256(s.encode()).hexdigest()


def proposal(**kw):
    base=dict(
        proposal_id='p1',principal='alice',objective='send approved payload',
        action_type='message.send',target='recipient:bob',payload_hash=H('payload'),
        expected_effect='one provider message',risk_class='medium',
        reversibility=e.Reversibility.COMPENSATABLE,authority_reference='auth1',
        created_at=100,expires_at=200,evidence_ids=('ev1',),
    )
    base.update(kw)
    return e.ActionProposal(**base)


def writes():
    return (e.IntendedWrite('provider:mail','message','create',H('value'),H('before')),)


def policy(**kw):
    base=dict(policy_id='pol1',policy_epoch='7',allowed_action_types=frozenset({'message.send'}),allowed_targets=frozenset({'recipient:bob'}),policy_hash=H('policy'))
    base.update(kw)
    return e.PolicyBinding(**base)


def authority(p, ws, **kw):
    base=dict(witness_id='auth1',principal='alice',policy_id='pol1',policy_epoch='7',effect_digest=e.effect_digest(p,ws),transaction_id='tx1',idempotency_key='idem-1',allowed_action_types=frozenset({'message.send'}),allowed_targets=frozenset({'recipient:bob'}),valid_from=90,expires_at=190,revoked=False)
    base.update(kw)
    return e.AuthorityBinding(**base)


def request(**kw):
    p=kw.pop('proposal',proposal()); ws=kw.pop('intended_write_set',writes()); a=kw.pop('authority',authority(p,ws)); pol=kw.pop('policy',policy())
    base=dict(request_id='r1',tx_id='tx1',principal='alice',proposal=p,authority=a,policy=pol,expected_state_epoch='state-9',observed_read_set=(e.ObservedRead('provider:mail','quota','3',H('quota')),),intended_write_set=ws,idempotency_key='idem-1',rollback_policy='compensate:delete-provider-message',durable_effect=True,created_at=110,expires_at=180)
    base.update(kw)
    return e.ExecutionRequest(**base)


def test_valid_request_prepares_but_never_authorizes_commit():
    out=e.prepare_execution(request(),now=120)
    assert out.status is e.PreflightStatus.PREPARED_FOR_CONTROL_PLANE
    assert out.prepared is not None and out.prepared.commit_authorized is False


def test_missing_authority_holds():
    assert e.prepare_execution(request(authority=None),now=120).status is e.PreflightStatus.HOLD_AUTHORITY


def test_expired_request_holds_stale():
    assert e.prepare_execution(request(),now=181).status is e.PreflightStatus.HOLD_STALE


def test_revoked_authority_holds():
    r=request(); a=authority(r.proposal,r.intended_write_set,revoked=True)
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.HOLD_AUTHORITY


def test_principal_mismatch_blocks_effect_binding():
    assert e.prepare_execution(request(principal='mallory'),now=120).status is e.PreflightStatus.BLOCK_EFFECT_BINDING


def test_effect_digest_mismatch_blocks():
    r=request(); a=authority(r.proposal,r.intended_write_set,effect_digest=H('wrong'))
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.BLOCK_EFFECT_BINDING


def test_authority_scope_is_exact():
    r=request(); a=authority(r.proposal,r.intended_write_set,allowed_targets=frozenset({'recipient:eve'}))
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.HOLD_AUTHORITY


def test_policy_binding_mismatch_holds():
    r=request(); a=authority(r.proposal,r.intended_write_set,policy_epoch='8')
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.HOLD_POLICY


def test_policy_scope_blocks():
    assert e.prepare_execution(request(policy=policy(allowed_targets=frozenset({'recipient:eve'}))),now=120).status is e.PreflightStatus.HOLD_POLICY


def test_duplicate_read_coordinate_blocks():
    x=e.ObservedRead('r','f','1',H('a')); y=e.ObservedRead('r','f','2',H('b'))
    assert e.prepare_execution(request(observed_read_set=(x,y)),now=120).status is e.PreflightStatus.BLOCK_READ_SET


def test_duplicate_write_coordinate_blocks_before_authority_use():
    x=e.IntendedWrite('r','f','set',H('a')); y=e.IntendedWrite('r','f','set',H('b'))
    p=proposal(); ws=(x,y); a=authority(p,ws)
    assert e.prepare_execution(request(proposal=p,intended_write_set=ws,authority=a),now=120).status is e.PreflightStatus.BLOCK_WRITE_SET


def test_durable_effect_requires_idempotency_key():
    assert e.prepare_execution(request(idempotency_key=None),now=120).status is e.PreflightStatus.BLOCK_IDEMPOTENCY


def test_read_hash_order_invariant():
    a=e.ObservedRead('a','x','1',H('1')); b=e.ObservedRead('b','y','2',H('2'))
    assert e.read_set_hash((a,b))==e.read_set_hash((b,a))


def test_write_hash_and_effect_digest_order_invariant():
    a=e.IntendedWrite('a','x','set',H('1')); b=e.IntendedWrite('b','y','set',H('2'))
    p=proposal()
    assert e.write_set_hash((a,b))==e.write_set_hash((b,a))
    assert e.effect_digest(p,(a,b))==e.effect_digest(p,(b,a))


def test_payload_change_changes_effect_digest():
    assert e.effect_digest(proposal(payload_hash=H('a')),writes()) != e.effect_digest(proposal(payload_hash=H('b')),writes())


def test_evidence_ids_do_not_mint_different_effect_identity():
    assert e.effect_digest(proposal(evidence_ids=('a',)),writes()) == e.effect_digest(proposal(evidence_ids=('a','b')),writes())


def test_invalid_digest_rejected_at_type_boundary():
    with pytest.raises(ValueError): proposal(payload_hash='not-a-digest')


def test_prepared_capsule_binds_policy_authority_state_and_sets():
    out=e.prepare_execution(request(),now=120).prepared
    assert out is not None
    assert out.authority_witness_id=='auth1' and out.policy_id=='pol1' and out.policy_epoch=='7'
    assert len(out.declared_read_set_hash)==64 and len(out.write_set_hash)==64 and out.expected_state_epoch=='state-9'


def test_durable_authority_must_bind_transaction():
    r=request(); a=authority(r.proposal,r.intended_write_set,transaction_id='other')
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.HOLD_AUTHORITY


def test_durable_authority_must_bind_idempotency_key():
    r=request(); a=authority(r.proposal,r.intended_write_set,idempotency_key='other')
    assert e.prepare_execution(request(authority=a),now=120).status is e.PreflightStatus.HOLD_AUTHORITY


def test_randomized_effect_digest_is_order_invariant_and_value_sensitive():
    import random
    rng=random.Random(20260914)
    for trial in range(2000):
        ws=tuple(e.IntendedWrite(f'r{j}',f'f{j}',rng.choice(('set','create','delete')),H(f'v-{trial}-{j}')) for j in range(rng.randrange(0,7)))
        p=proposal(payload_hash=H(f'payload-{trial}'))
        d=e.effect_digest(p,ws)
        shuffled=list(ws); rng.shuffle(shuffled)
        assert d==e.effect_digest(p,tuple(shuffled))
        if ws:
            changed=list(ws); w=changed[0]
            changed[0]=e.IntendedWrite(w.resource,w.field,w.operation,H(f'changed-{trial}'),w.expected_precondition_hash)
            assert d!=e.effect_digest(p,tuple(changed))


def test_randomized_gate_matches_exact_conjunction_oracle():
    import random
    rng=random.Random(731)
    for _ in range(5000):
        p=proposal(action_type='act',target='target',authority_reference='auth',created_at=10,expires_at=100)
        ws=(e.IntendedWrite('r','f','set',H('v')),)
        exact_principal=rng.choice((True,False)); exact_effect=rng.choice((True,False)); auth_scope=rng.choice((True,False)); policy_scope=rng.choice((True,False)); fresh=rng.choice((True,False)); revoked=rng.choice((True,False)); idem=rng.choice((True,False))
        a=e.AuthorityBinding('auth','alice' if exact_principal else 'mallory','pol','1',e.effect_digest(p,ws) if exact_effect else H('wrong'),'tx','idem' if idem else None,frozenset({'act'} if auth_scope else {'other'}),frozenset({'target'} if auth_scope else {'other'}),0,90 if fresh else 15,revoked)
        pol=e.PolicyBinding('pol','1',frozenset({'act'} if policy_scope else {'other'}),frozenset({'target'} if policy_scope else {'other'}),H('pol'))
        req=e.ExecutionRequest('req','tx','alice',p,a,pol,'s',(),ws,'idem' if idem else None,'rb',True,20,80)
        out=e.prepare_execution(req,now=30)
        should=(exact_principal and exact_effect and auth_scope and policy_scope and fresh and not revoked and idem)
        assert (out.status is e.PreflightStatus.PREPARED_FOR_CONTROL_PLANE)==should
