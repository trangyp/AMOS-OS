#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HEX64 = re.compile(r'^[0-9a-f]{64}$')
FORBIDDEN_KEYS = {
    'authorization', 'api_key', 'token', 'password', 'secret', 'raw_prompt', 'raw_output',
    'raw_input', 'completion', 'chain_of_thought', 'reasoning',
}


def _hex64(value: Any) -> bool:
    return isinstance(value, str) and bool(HEX64.fullmatch(value))


def _forbidden_paths(value: Any, path: str = '$') -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            p = f'{path}.{key}'
            if str(key).lower() in FORBIDDEN_KEYS:
                found.append(p)
            found.extend(_forbidden_paths(child, p))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            found.extend(_forbidden_paths(child, f'{path}[{i}]'))
    return found


def validate_manifest_receipt(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        'manifest_id', 'schema_valid', 'root_present', 'hashes_valid', 'lineage_closed',
        'attestation_subject_bound', 'signature_claims_supported', 'vulnerability_attribution_valid',
        'manifest_hash_valid', 'structural_integrity', 'policy_complete', 'policy_checks', 'component_count',
        'attestation_count', 'vulnerability_count', 'output_binding_count', 'sealed', 'manifest_hash',
        'expected_manifest_hash', 'authority_semantics', 'trust_semantics', 'completeness_semantics', 'receipt_hash',
    }
    for key in sorted(required - set(obj)):
        errors.append(f'missing {key}')
    if obj.get('authority_semantics') != 'AIBOM_EVIDENCE_DOES_NOT_GRANT_AUTHORITY':
        errors.append('AIBOM receipt cannot grant authority')
    if obj.get('trust_semantics') != 'DIGEST_OR_SIGNATURE_EVIDENCE_DOES_NOT_PROVE_SEMANTIC_CORRECTNESS':
        errors.append('signature/digest evidence cannot imply semantic correctness')
    if obj.get('completeness_semantics') != 'BOM_PRESENT_DOES_NOT_PROVE_COMPLETE_INVENTORY':
        errors.append('BOM presence cannot imply inventory completeness')
    if obj.get('sealed') is True:
        if not _hex64(obj.get('manifest_hash')):
            errors.append('sealed receipt requires manifest_hash')
    elif obj.get('manifest_hash') is not None:
        errors.append('unsealed receipt cannot assert manifest_hash')
    if not _hex64(obj.get('expected_manifest_hash')):
        errors.append('expected_manifest_hash must be sha256')
    if not _hex64(obj.get('receipt_hash')):
        errors.append('receipt_hash must be sha256')
    checks = obj.get('policy_checks')
    if not isinstance(checks, dict):
        errors.append('policy_checks must be object')
    else:
        needed = {'attestation', 'verified_signature', 'vulnerability_evidence', 'environment_identity', 'output_binding', 'replay_evidence'}
        if set(checks) != needed:
            errors.append('policy_checks must contain exact policy dimensions')
        if obj.get('policy_complete') is True and not all(checks.get(k) is True for k in needed):
            errors.append('policy_complete=true requires every policy check true')
    integrity_parts = (
        'schema_valid', 'root_present', 'hashes_valid', 'lineage_closed', 'attestation_subject_bound',
        'signature_claims_supported', 'vulnerability_attribution_valid', 'manifest_hash_valid',
    )
    if obj.get('structural_integrity') is True and not all(obj.get(k) is True for k in integrity_parts):
        errors.append('structural_integrity=true conflicts with failed structural invariant')
    for name in ('component_count', 'attestation_count', 'vulnerability_count', 'output_binding_count'):
        if not isinstance(obj.get(name), int) or obj.get(name, -1) < 0:
            errors.append(f'{name} must be non-negative integer')
    return errors


def validate_drift_receipt(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if obj.get('state') not in {'COMPARABLE', 'NOT_COMPARABLE'}:
        errors.append('invalid drift state')
    if obj.get('authority_semantics') != 'DRIFT_RESULT_DOES_NOT_GRANT_AUTHORITY':
        errors.append('drift result cannot grant authority')
    if obj.get('state') == 'NOT_COMPARABLE':
        if not isinstance(obj.get('reasons'), list) or not obj.get('reasons'):
            errors.append('NOT_COMPARABLE requires reasons')
        return errors
    required_lists = {
        'added_component_ids', 'removed_component_ids', 'digest_changed_component_ids',
        'version_changed_component_ids', 'kind_changed_component_ids', 'material_changed_component_ids',
    }
    for key in required_lists:
        if not isinstance(obj.get(key), list):
            errors.append(f'{key} must be list')
    for key in ('old_hash', 'new_hash', 'receipt_hash'):
        if not _hex64(obj.get(key)):
            errors.append(f'{key} must be sha256')
    if obj.get('causal_semantics') != 'AIBOM_DRIFT_DOES_NOT_IDENTIFY_CAUSE':
        errors.append('drift receipt cannot claim causal identification')
    return errors


def validate_output_binding(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {'binding_id', 'manifest_id', 'execution_id', 'artifact_hash', 'aibom_hash', 'evidence_ref'}
    for key in sorted(required - set(obj)):
        errors.append(f'missing {key}')
    for key in ('artifact_hash', 'aibom_hash'):
        if not _hex64(obj.get(key)):
            errors.append(f'{key} must be sha256')
    erh = obj.get('evaluation_receipt_hash')
    if erh is not None and not _hex64(erh):
        errors.append('evaluation_receipt_hash must be null or sha256')
    return errors


def validate(obj: dict[str, Any]) -> list[str]:
    errors = [f'forbidden persisted field: {p}' for p in _forbidden_paths(obj)]
    if 'structural_integrity' in obj and 'policy_checks' in obj:
        errors.extend(validate_manifest_receipt(obj))
    elif 'state' in obj and ('old_manifest_id' in obj or 'reasons' in obj):
        errors.extend(validate_drift_receipt(obj))
    elif 'binding_id' in obj and 'execution_id' in obj:
        errors.extend(validate_output_binding(obj))
    else:
        errors.append('unknown AIBOM receipt type')
    return errors


def self_test() -> int:
    good = {
        'manifest_id': 'm', 'schema_valid': True, 'root_present': True, 'hashes_valid': True,
        'lineage_closed': True, 'attestation_subject_bound': True, 'signature_claims_supported': True,
        'vulnerability_attribution_valid': True, 'manifest_hash_valid': True, 'structural_integrity': True,
        'policy_complete': False,
        'policy_checks': {'attestation': True, 'verified_signature': False, 'vulnerability_evidence': True,
                          'environment_identity': True, 'output_binding': True, 'replay_evidence': True},
        'component_count': 1, 'attestation_count': 1, 'vulnerability_count': 1, 'output_binding_count': 0,
        'sealed': True, 'manifest_hash': 'a' * 64, 'expected_manifest_hash': 'a' * 64,
        'authority_semantics': 'AIBOM_EVIDENCE_DOES_NOT_GRANT_AUTHORITY',
        'trust_semantics': 'DIGEST_OR_SIGNATURE_EVIDENCE_DOES_NOT_PROVE_SEMANTIC_CORRECTNESS',
        'completeness_semantics': 'BOM_PRESENT_DOES_NOT_PROVE_COMPLETE_INVENTORY', 'receipt_hash': 'b' * 64,
    }
    if validate(good):
        print('positive manifest fixture failed', file=sys.stderr)
        return 1
    bad = dict(good); bad['authority_semantics'] = 'AUTHORIZED'
    if not validate(bad):
        print('authority negative fixture failed', file=sys.stderr)
        return 1
    bad2 = dict(good); bad2['raw_prompt'] = 'secret'
    if not validate(bad2):
        print('raw-content negative fixture failed', file=sys.stderr)
        return 1
    drift = {
        'state': 'COMPARABLE', 'old_manifest_id': 'a', 'new_manifest_id': 'b', 'old_hash': 'a' * 64,
        'new_hash': 'b' * 64, 'added_component_ids': [], 'removed_component_ids': [],
        'digest_changed_component_ids': [], 'version_changed_component_ids': [], 'kind_changed_component_ids': [],
        'material_changed_component_ids': [], 'source_ref_changed': True, 'build_id_changed': True,
        'environment_id_changed': False, 'causal_semantics': 'AIBOM_DRIFT_DOES_NOT_IDENTIFY_CAUSE',
        'authority_semantics': 'DRIFT_RESULT_DOES_NOT_GRANT_AUTHORITY', 'receipt_hash': 'c' * 64,
    }
    if validate(drift):
        print('positive drift fixture failed', file=sys.stderr)
        return 1
    print('SELF_TEST_PASS')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description='Validate AMOS AIBOM receipts')
    ap.add_argument('path', nargs='?')
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.path:
        ap.error('receipt path required unless --self-test')
    try:
        obj = json.loads(Path(args.path).read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'invalid receipt JSON: {exc}', file=sys.stderr)
        return 2
    errors = validate(obj)
    for error in errors:
        print('ERROR', error)
    print(f'AIBOM_CONTRACT errors={len(errors)}')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
