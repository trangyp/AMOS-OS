import importlib.util
from pathlib import Path
P=Path(__file__).with_name('ulk_fragment_execution_registry.py')
spec=importlib.util.spec_from_file_location('ulkreg_v211',P)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
checks=0

def req(n,c,d=None):
 global checks; checks+=1
 if not c: raise AssertionError((n,d))

req('registry',m.validate_execution_registry()==(),m.validate_execution_registry())
req('eight',len(tuple(m.Fragment))==8)
req('alu02-scope-euf','ground-EUF' in m.execution_binding(m.Fragment.ALU02_FIRST_ORDER_UNIFICATION).scope)
for f in m.Fragment: req('not-canon',m.execution_binding(f).canon_promoted is False,f)
for name,h in m.ALU02_SUBPROFILE_HASHES.items():
 r=m.validate_alu02_subprofile_observation(name,h,m.UNIFIED_BRAIN_REVALIDATED_REVISION)
 req('subprofile-match',r['success'] and r['revision_state']=='SAME_REVALIDATED_REVISION',(name,r))
 r2=m.validate_alu02_subprofile_observation(name,h,'NEW_REV')
 req('subprofile-revision-stable',r2['success'] and r2['revision_state']=='REVISION_CHANGED_FRAGMENT_STABLE',(name,r2))
bad=m.validate_alu02_subprofile_observation('GROUND_EUF_CONGRUENCE_CLOSURE','0'*64,'NEW')
req('euf-stale',not bad['success'] and bad['status']=='STALE_REVALIDATE',bad)
for frag,h in [(m.Fragment.ALU03_TEMPORAL_LTL,m.ALU03_SOURCE_METHOD_AST_SHA256),(m.Fragment.ALU07_QUANTUM_LOGIC,m.ALU07_SOURCE_METHOD_AST_SHA256)]:
 r=m.validate_fragment_observation(frag,h,'NEWER')
 req('stable-frag',r['success'] and r['revision_state']=='REVISION_CHANGED_FRAGMENT_STABLE',r)
print({'suite':'ulk_repair_contract_v211','checks':checks,'status':'PASS'})
