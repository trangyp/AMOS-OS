import importlib.util
from pathlib import Path

p = Path(__file__).with_name('z3_muz_adapter_contract_v1.py')
spec = importlib.util.spec_from_file_location('z3c', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

state = m.binding_state('EXACT_TEST_VERSION')
assert state['status'] in {'UNAVAILABLE_HOLD', 'HOLD_VERSION_MISMATCH', 'BOUND_EXACT_VERSION', 'HOLD_VERSION_UNRESOLVED'}
assert state['authority_granted'] is False
for token in ('sat', 'unsat', 'unknown'):
    r = m.normalize_fixedpoint_result(token, query_scope='bounded Horn test')
    assert r['success'] and r['solver_result'] == token.upper()
    assert r['authority_granted'] is False and r['canon_promoted'] is False
bad = m.normalize_fixedpoint_result('maybe', query_scope='x')
assert bad['success'] is False and bad['status'] == 'ILL_TYPED_SOLVER_RESULT'
bad = m.normalize_fixedpoint_result('sat', query_scope='')
assert bad['success'] is False and bad['status'] == 'ILL_TYPED_SCOPE'
print({'suite': 'z3_muz_adapter_contract_v1', 'checks': 11, 'status': 'PASS'})
