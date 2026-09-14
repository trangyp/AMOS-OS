import importlib.util
from pathlib import Path

P = Path(__file__).with_name('ulk_fragment_execution_registry.py')
spec = importlib.util.spec_from_file_location('ulkreg_v207', P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

assert m.validate_execution_registry() == ()
assert len(tuple(m.Fragment)) == 8
assert [f.value for f in m.Fragment] == [
    'ClassicalPropositional','FirstOrderUnification','TemporalLTL','EpistemicModal',
    'NonMonotonicDung','DependentType','QuantumLogic','CategoricalTopos'
]
assert all(not m.execution_binding(f).canon_promoted for f in m.Fragment)

alu03 = m.validate_fragment_observation(
    m.Fragment.ALU03_TEMPORAL_LTL,
    '797c881ad2e3c8aa746740025445efcba48e2e76eaa1efe64bc1ac3e4fd1aa69',
    'NEWER_REVISION_FOR_TEST',
)
assert alu03['success'] is True
assert alu03['revision_state'] == 'REVISION_CHANGED_FRAGMENT_STABLE'
assert alu03['authority_granted'] is False

alu07 = m.validate_fragment_observation(
    m.Fragment.ALU07_QUANTUM_LOGIC,
    'f645bedd808bba01d512ec139a4b9e5d7d00043abf532672490eca9b7d0ab664',
    'NEWER_REVISION_FOR_TEST',
)
assert alu07['success'] is True
assert alu07['revision_state'] == 'REVISION_CHANGED_FRAGMENT_STABLE'
assert alu07['canon_promoted'] is False

bad = m.validate_fragment_observation(
    m.Fragment.ALU07_QUANTUM_LOGIC,
    '0' * 64,
    'NEWER_REVISION_FOR_TEST',
)
assert bad['success'] is False
assert bad['status'] == 'STALE_REVALIDATE'

for fragment in m.Fragment:
    binding = m.execution_binding(fragment)
    assert binding.canon_promoted is False
    assert 'confidence' not in binding.scope.lower()

print({'suite':'ulk_repair_contract_v207','checks':26,'status':'PASS'})
