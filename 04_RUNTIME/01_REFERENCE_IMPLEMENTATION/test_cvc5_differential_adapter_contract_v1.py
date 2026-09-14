import importlib.util
from pathlib import Path

p = Path(__file__).with_name('cvc5_differential_adapter_contract_v1.py')
spec = importlib.util.spec_from_file_location('cvc5c', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

state = m.binding_state('EXACT_TEST_VERSION')
assert state['status'] in {'UNAVAILABLE_HOLD', 'HOLD_VERSION_MISMATCH', 'BOUND_EXACT_VERSION', 'HOLD_VERSION_UNRESOLVED'}
assert state['authority_granted'] is False
for token in ('sat', 'unsat', 'unknown'):
    r = m.normalize_result(token, theory_scope='QF_LIA test', unknown_explanation='timeout' if token == 'unknown' else None)
    assert r['success'] and r['solver_result'] == token.upper()
    assert r['authority_granted'] is False and r['canon_promoted'] is False
agree = m.differential_verdict('sat', 'SAT', theory_scope='QF_LIA')
assert agree['success'] and agree['status'] == 'AGREE' and agree['agreement_is_truth'] is False
dis = m.differential_verdict('sat', 'unsat', theory_scope='QF_LIA')
assert not dis['success'] and dis['status'] == 'DISAGREE_REVIEW'
bad = m.normalize_result('unknown', theory_scope='QF_LIA', unknown_explanation=5)
assert not bad['success'] and bad['status'] == 'ILL_TYPED_UNKNOWN_EXPLANATION'
print({'suite': 'cvc5_differential_adapter_contract_v1', 'checks': 14, 'status': 'PASS'})
