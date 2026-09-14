#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any

ABI='AMOS_AGENT_INTEROP_ABI_v1'
A2A_DISCOVERY='/.well-known/agent-card.json'
MCP_REVISION='2026-07-28'
LEGACY=re.compile(r'^A2A-v([0-9]+(?:\.[0-9]+)*)$')


def as_list(v: Any) -> list[Any]:
    return v if isinstance(v, list) else []


def normalize(agent: dict[str, Any]) -> dict[str, Any]:
    card = agent.get('agent_card') if isinstance(agent.get('agent_card'), dict) else {}
    a2a = {
        'discovery_path': A2A_DISCOVERY,
        'binding_status': 'UNBOUND',
        'supported_interfaces': [],
        'default_input_modes': as_list(card.get('default_input_modes')),
        'default_output_modes': as_list(card.get('default_output_modes')),
        'skill_refs': as_list(card.get('skill_refs')),
    }
    interfaces = card.get('supported_interfaces') or card.get('supportedInterfaces')
    if isinstance(interfaces, list) and interfaces:
        for item in interfaces:
            if not isinstance(item, dict):
                continue
            binding = item.get('protocol_binding') or item.get('protocolBinding')
            version = item.get('protocol_version') or item.get('protocolVersion')
            if binding and version:
                x = {'protocol_binding': binding, 'protocol_version': str(version)}
                if item.get('url'):
                    x['url'] = item['url']
                a2a['supported_interfaces'].append(x)
        if a2a['supported_interfaces']:
            a2a['binding_status'] = 'DECLARED'
            a2a['source_format'] = 'a2a_interface_list'
    else:
        m = LEGACY.fullmatch(str(card.get('protocol') or ''))
        if m:
            a2a['supported_interfaces'] = [{'protocol_binding':'JSONRPC','protocol_version':m.group(1)}]
            a2a['binding_status'] = 'LEGACY_DECLARATION_REQUIRES_ENDPOINT_BINDING'
            a2a['source_format'] = 'legacy_amos_agent_card'
    return {
        'schema': ABI,
        'agent_id': str(agent.get('name') or agent.get('id') or ''),
        'identity': {
            'name': card.get('name') or agent.get('display_name') or agent.get('name') or '',
            'description': card.get('description') or agent.get('description') or '',
            'version': str(card.get('version') or agent.get('version') or '0.0.0'),
        },
        'external_protocols': {
            'a2a': a2a,
            'mcp': {'compatibility_target_revision': MCP_REVISION, 'binding_status':'UNBOUND', 'roles':[]},
        },
        'amos_extensions': {
            'epistemic_class': agent.get('epistemic_class','UNKNOWN/GAP'),
            'rscf_state': agent.get('rscf_state','UNKNOWN/GAP'),
            'capability_is_not_authority': True,
            'commit_authority_external_to_protocol': True,
        },
    }


def validate(obj: dict[str, Any]) -> list[str]:
    e=[]
    if obj.get('schema') != ABI: e.append('schema mismatch')
    if not obj.get('agent_id'): e.append('agent_id missing')
    ident=obj.get('identity',{})
    if not ident.get('name') or not ident.get('description'): e.append('identity incomplete')
    a2a=obj.get('external_protocols',{}).get('a2a',{})
    if a2a.get('discovery_path') != A2A_DISCOVERY: e.append('A2A discovery path mismatch')
    for i,x in enumerate(as_list(a2a.get('supported_interfaces'))):
        if not isinstance(x,dict) or not x.get('protocol_binding') or not x.get('protocol_version'):
            e.append(f'A2A interface {i} incomplete')
    mcp=obj.get('external_protocols',{}).get('mcp',{})
    if mcp.get('compatibility_target_revision') != MCP_REVISION: e.append('MCP revision mismatch')
    ext=obj.get('amos_extensions',{})
    if ext.get('capability_is_not_authority') is not True: e.append('authority firewall missing')
    if ext.get('commit_authority_external_to_protocol') is not True: e.append('commit firewall missing')
    return e


def scan(root: Path) -> int:
    total=bad=legacy=0
    for f in sorted(root.rglob('*.json')):
        total += 1
        try: agent=json.loads(f.read_text(encoding='utf-8-sig'))
        except Exception as exc:
            print(f'ERROR {f}: {exc}'); bad += 1; continue
        obj=normalize(agent); errs=validate(obj)
        if obj['external_protocols']['a2a'].get('source_format') == 'legacy_amos_agent_card': legacy += 1
        if errs:
            print(f"ERROR {f}: {'; '.join(errs)}"); bad += 1
    print(f'AMOS agent protocol ABI: total={total} invalid={bad} legacy_a2a={legacy}')
    return 1 if bad else 0


def self_test() -> None:
    a={'name':'demo','description':'demo','agent_card':{'protocol':'A2A-v1.0','name':'Demo','description':'Demo'}}
    n=normalize(a); assert validate(n)==[]
    assert n['external_protocols']['a2a']['binding_status']=='LEGACY_DECLARATION_REQUIRES_ENDPOINT_BINDING'
    assert n['external_protocols']['a2a']['supported_interfaces'][0]['protocol_version']=='1.0'
    print('agent_protocol_abi self-test: PASS')


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('path',nargs='?'); ap.add_argument('--scan-dir'); ap.add_argument('--self-test',action='store_true')
    a=ap.parse_args()
    if a.self_test: self_test(); raise SystemExit(0)
    if a.scan_dir: raise SystemExit(scan(Path(a.scan_dir)))
    if not a.path: ap.error('provide path or --scan-dir')
    obj=normalize(json.loads(Path(a.path).read_text(encoding='utf-8-sig')))
    print(json.dumps(obj,indent=2,ensure_ascii=False)); raise SystemExit(1 if validate(obj) else 0)
