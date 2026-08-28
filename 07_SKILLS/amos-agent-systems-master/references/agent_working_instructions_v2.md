---
title: agent working instructions v2
type: reference
source: 07_SKILLS/amos-agent-systems-master/references
tags: [reference, amos-agent-systems-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Agent Working Instructions V2

> Source: `_00_Cosmo brain/agents/AGENT_WORKING_INSTRUCTIONS_V2.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [agents]
---
# AGENT WORKING INSTRUCTIONS - MANDATORY READING

## PRE-WORK REQUIREMENTS

### **BEFORE STARTING ANY WORK**
1. **READ SYSTEM ARCHITECTURE REPORT**: `AMOS_SYSTEM_ARCHITECTURE_REPORT_V2.md`
2. **UNDERSTAND PACK ARCHITECTURE**: Review kernel pack registry system
3. **VALIDATE SYSTEM STATUS**: Check all components are operational
4. **REVIEW SECURITY GUIDELINES**: Understand threat detection and validation
5. **CHECK PERFORMANCE METRICS**: Verify optimization components

---

## WORKING GUIDELINES

### **REQUIRED PATTERNS**

#### **1. Singleton Brain Master**
```python
# ALWAYS use singleton pattern
from master import AMOSBrainMaster

master = AMOSBrainMaster.get_instance()
# NEVER instantiate directly: master = AMOSBrainMaster()
```

#### **2. Pack Registration**
```python
# ALWAYS register through canonical registry
from kernel import create_pack_registry, PackInterface

class MyPack(PackInterface):
    def _get_capabilities(self):
        return ['my_capability']

registry = create_pack_registry(kernel)
registry.register_pack('my_pack', MyPack, dependencies=[])
```

#### **3. Security Validation**
```python
# ALWAYS validate inputs
from core.advanced_security_enhancer import advanced_security_enhancer

user_input = request.get('data', '')
if not advanced_security_enhancer.validate_input(user_input, 'general'):
    raise SecurityError("Invalid input detected")
```

#### **4. Performance Optimization**
```python
# ALWAYS use caching and optimization
from core.memory_optimizer import memory_optimizer

# Use cached objects
obj = memory_optimizer.get_cached_object('key', factory_function)
```

---

## STRICT RESTRICTIONS

### **FILE OPERATIONS**
```python
# FORBIDDEN: Direct file operations
with open('file.txt', 'w') as f:
    f.write('data')

# REQUIRED: Use kernel file operations
from master import AMOSBrainMaster
master = AMOSBrainMaster.get_instance()
file_op = FileOperation('write', 'file.txt', 'data')
master.persist(file_op)
```

### **CONFIGURATION**
```python
# FORBIDDEN: Direct config loading
import json
with open('config.json') as f:
    config = json.load(f)

# REQUIRED: Use BrainContext
from kernel import BrainContext
context = BrainContext(kernel, {})
config = context.get_shared_state('config', {})
```

### **BRAIN OPERATIONS**
```python
# FORBIDDEN: Direct brain usage
from brain import AMOSBrain
brain = AMOSBrain()

# REQUIRED: Use kernel routing
kernel.get_brain_service('process_data')
```

### **PACK CREATION**
```python
# FORBIDDEN: Unauthorized pack creation
class MyPack:
    def __init__(self):
        self.initialize()

# REQUIRED: Use PackInterface and registry
from kernel import PackInterface
class MyPack(PackInterface):
    def _get_capabilities(self):
        return ['my_capability']
```

---

## TESTING REQUIREMENTS

### **Integration Tests**
```python
# ALWAYS run integration tests before deployment
from tests.simple_integration_tests import simple_integration_test_suite

test_report = simple_integration_test_suite.run_all_tests()
if test_report['summary']['success_rate'] < 80:
    raise DeploymentError("Integration tests failed")
```

### **Performance Tests**
```python
# ALWAYS validate performance
from core.performance_hardener import performance_hardener

status = performance_hardener.get_status()
if not status['monitoring']:
    raise PerformanceError("Performance monitoring not active")
```

### **Security Tests**
```python
# ALWAYS validate security
from core.advanced_security_enhancer import advanced_security_enhancer

metrics = advanced_security_enhancer.get_security_metrics()
if not metrics['monitoring_active']:
    raise SecurityError("Security monitoring not active")
```

---

## QUALITY STANDARDS

### **PERFORMANCE REQUIREMENTS**
- Operations must complete in **sub-millisecond** time
- Cache hit rate must be **≥ 50%**
- Memory usage must be **optimized** with bounded collections
- Network requests must use **caching and poo

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-agent-systems-master-agent-working-instructions-v2
node_type: reference
path: 07_SKILLS/amos-agent-systems-master/references/agent_working_instructions_v2.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
