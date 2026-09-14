#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime
from pathlib import Path
from typing import Any

STATES = {
    'SUBMITTED','WORKING','INPUT_REQUIRED','AUTH_REQUIRED','WAITING_DEPENDENCY',
    'COMPLETED','CANCELED','REJECTED','FAILED'
}
TERMINAL = {'COMPLETED','CANCELED','REJECTED','FAILED'}
ALLOWED = {
    'SUBMITTED': {'WORKING','CANCELED','REJECTED'},
    'WORKING': {'INPUT_REQUIRED','AUTH_REQUIRED','WAITING_DEPENDENCY','COMPLETED','CANCELED','FAILED'},
    'INPUT_REQUIRED': {'WORKING','CANCELED','FAILED'},
    'AUTH_REQUIRED': {'WORKING','CANCELED','FAILED'},
    'WAITING_DEPENDENCY': {'WORKING','CANCELED','FAILED'},
    'COMPLETED': set(), 'CANCELED': set(), 'REJECTED': set(), 'FAILED': set(),
}


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        return None


def string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {x for x in value if isinstance(x, str) and x}


def validate(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ('task_id','context_id','attempt_id','owner_agent','state'):
        if not isinstance(doc.get(key), str) or not doc[key]:
            errors.append(f'{key} missing')
    state = doc.get('state')
    if state not in STATES:
        errors.append('invalid state')
        return errors
    epoch = doc.get('state_epoch')
    if not isinstance(epoch, int) or epoch < 0:
        errors.append('state_epoch must be a non-negative integer')
    attempt = doc.get('attempt', 1)
    if not isinstance(attempt, int) or attempt < 1:
        errors.append('attempt must be a positive integer')
    retry_of = doc.get('retry_of_task_id')
    if retry_of is not None:
        if not isinstance(retry_of, str) or not retry_of or retry_of == doc.get('task_id'):
            errors.append('retry_of_task_id must reference a different task')
        if isinstance(attempt, int) and attempt < 2:
            errors.append('retry tasks require attempt >= 2')

    transition = doc.get('transition')
    if transition is None:
        return errors
    if not isinstance(transition, dict):
        errors.append('transition must be an object')
        return errors
    if state in TERMINAL:
        errors.append('terminal task cannot transition in place')
        return errors

    target = transition.get('to')
    if target not in STATES:
        errors.append('transition target invalid')
    elif target not in ALLOWED[state]:
        errors.append(f'illegal transition {state}->{target}')

    if transition.get('expected_state_epoch') != epoch:
        errors.append('expected_state_epoch does not match current state_epoch')
    if isinstance(epoch, int) and transition.get('next_state_epoch') != epoch + 1:
        errors.append('next_state_epoch must equal state_epoch + 1')

    cancel_epoch = doc.get('cancellation_epoch')
    if isinstance(cancel_epoch, int) and isinstance(epoch, int) and cancel_epoch <= epoch and target != 'CANCELED':
        errors.append('cancellation fence permits only transition to CANCELED')

    if state == 'SUBMITTED' and target == 'WORKING':
        new_lease = transition.get('new_lease')
        if not isinstance(new_lease, dict):
            errors.append('SUBMITTED->WORKING requires new_lease')
        else:
            if new_lease.get('owner_agent') != transition.get('actor_agent'):
                errors.append('new lease owner must equal actor_agent')
            if not isinstance(new_lease.get('fencing_token'), int) or new_lease['fencing_token'] < 1:
                errors.append('new lease requires positive fencing_token')
            expires = parse_time(new_lease.get('expires_at'))
            verify = parse_time(transition.get('verification_time'))
            if expires is None or verify is None:
                errors.append('new lease and transition require valid timestamps')
            elif verify > expires:
                errors.append('new lease is expired at verification_time')
    elif state != 'SUBMITTED':
        lease = doc.get('lease')
        if not isinstance(lease, dict):
            errors.append('active/interrupted task requires lease')
        else:
            if transition.get('actor_agent') != lease.get('owner_agent'):
                errors.append('actor_agent is not current lease owner')
            if transition.get('fencing_token') != lease.get('fencing_token'):
                errors.append('stale or mismatched fencing_token')
            expires = parse_time(lease.get('expires_at'))
            verify = parse_time(transition.get('verification_time'))
            if expires is None or verify is None:
                errors.append('lease and transition require valid timestamps')
            elif verify > expires:
                errors.append('lease expired before transition verification')

    artifacts = doc.get('artifacts') if isinstance(doc.get('artifacts'), list) else []
    artifact_ids = {
        a.get('artifact_id') for a in artifacts
        if isinstance(a, dict) and isinstance(a.get('artifact_id'), str) and a.get('artifact_id')
    }
    result_ids = string_set(transition.get('result_artifact_ids'))
    if target == 'COMPLETED':
        if not result_ids:
            errors.append('COMPLETED requires result_artifact_ids')
        if not result_ids.issubset(artifact_ids):
            errors.append('COMPLETED references missing result artifacts')

    if state == 'INPUT_REQUIRED' and target == 'WORKING' and not string_set(transition.get('input_artifact_ids')):
        errors.append('INPUT_REQUIRED->WORKING requires input_artifact_ids')
    if state == 'AUTH_REQUIRED' and target == 'WORKING' and not transition.get('authority_witness_id'):
        errors.append('AUTH_REQUIRED->WORKING requires authority_witness_id')
    if state == 'WAITING_DEPENDENCY' and target == 'WORKING' and not string_set(transition.get('dependency_artifact_ids')):
        errors.append('WAITING_DEPENDENCY->WORKING requires dependency_artifact_ids')

    child = transition.get('spawn_child')
    if child is not None:
        if not isinstance(child, dict):
            errors.append('spawn_child must be an object')
        else:
            parent_caps = string_set(doc.get('capability_grant'))
            child_caps = string_set(child.get('capability_grant'))
            if not child_caps.issubset(parent_caps):
                errors.append('child capability grant exceeds parent task grant')
            parent_auth = string_set(doc.get('authority_scope'))
            child_auth = string_set(child.get('authority_scope'))
            if not child_auth.issubset(parent_auth):
                errors.append('child authority scope exceeds parent task authority scope')
            depth = doc.get('delegation_depth', 0)
            max_depth = doc.get('max_delegation_depth', 2)
            child_depth = child.get('delegation_depth')
            if not isinstance(depth, int) or not isinstance(max_depth, int) or not isinstance(child_depth, int):
                errors.append('delegation depth values must be integers')
            elif child_depth != depth + 1 or child_depth > max_depth:
                errors.append('child delegation depth invalid')
    return errors


def self_test() -> None:
    valid = {
        'task_id':'t1','context_id':'c1','attempt_id':'a1','attempt':1,
        'owner_agent':'worker','state':'WORKING','state_epoch':3,
        'capability_grant':['read','analyze'],'authority_scope':['repo:read'],
        'delegation_depth':0,'max_delegation_depth':2,
        'lease':{'owner_agent':'worker','fencing_token':9,'expires_at':'2026-09-14T07:00:00+00:00'},
        'artifacts':[{'artifact_id':'r1','provenance':'run:1'}],
        'transition':{'to':'COMPLETED','actor_agent':'worker','expected_state_epoch':3,
                      'next_state_epoch':4,'fencing_token':9,
                      'verification_time':'2026-09-14T06:30:00+00:00',
                      'result_artifact_ids':['r1']}
    }
    assert validate(valid) == [], validate(valid)
    bad = json.loads(json.dumps(valid)); bad['transition']['fencing_token'] = 8
    assert 'stale or mismatched fencing_token' in validate(bad)
    terminal = dict(valid); terminal['state']='COMPLETED'; terminal['transition']={'to':'WORKING'}
    assert 'terminal task cannot transition in place' in validate(terminal)
    child = json.loads(json.dumps(valid)); child['transition']['to']='WAITING_DEPENDENCY'; child['transition'].pop('result_artifact_ids',None)
    child['transition']['spawn_child']={'capability_grant':['write'],'authority_scope':['repo:write'],'delegation_depth':1}
    errs=validate(child)
    assert 'child capability grant exceeds parent task grant' in errs
    assert 'child authority scope exceeds parent task authority scope' in errs
    print('validate_agent_task_lifecycle self-test: PASS')


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('path',nargs='?'); ap.add_argument('--self-test',action='store_true')
    a=ap.parse_args()
    if a.self_test:
        self_test(); return 0
    if not a.path:
        ap.error('provide a task contract JSON path or --self-test')
    doc=json.loads(Path(a.path).read_text(encoding='utf-8-sig'))
    errs=validate(doc)
    print(json.dumps({'valid':not errs,'errors':errs,'commit_authority':'NOT_EVALUATED'},indent=2))
    return 1 if errs else 0

if __name__=='__main__': raise SystemExit(main())
