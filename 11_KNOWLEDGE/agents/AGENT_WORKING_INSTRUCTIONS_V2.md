---
tags: [agents]
---
# 🚨 AGENT WORKING INSTRUCTIONS - MANDATORY READING

## 📋 PRE-WORK REQUIREMENTS

### **🔧 BEFORE STARTING ANY WORK**
1. **READ SYSTEM ARCHITECTURE REPORT**: `AMOS_SYSTEM_ARCHITECTURE_REPORT_V2.md`
2. **UNDERSTAND PACK ARCHITECTURE**: Review kernel pack registry system
3. **VALIDATE SYSTEM STATUS**: Check all components are operational
4. **REVIEW SECURITY GUIDELINES**: Understand threat detection and validation
5. **CHECK PERFORMANCE METRICS**: Verify optimization components

---

## 🎯 WORKING GUIDELINES

### **✅ REQUIRED PATTERNS**

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

## 🚫 STRICT RESTRICTIONS

### **📝 FILE OPERATIONS**
```python
# ❌ FORBIDDEN: Direct file operations
with open('file.txt', 'w') as f:
    f.write('data')

# ✅ REQUIRED: Use kernel file operations
from master import AMOSBrainMaster
master = AMOSBrainMaster.get_instance()
file_op = FileOperation('write', 'file.txt', 'data')
master.persist(file_op)
```

### **🔧 CONFIGURATION**
```python
# ❌ FORBIDDEN: Direct config loading
import json
with open('config.json') as f:
    config = json.load(f)

# ✅ REQUIRED: Use BrainContext
from kernel import BrainContext
context = BrainContext(kernel, {})
config = context.get_shared_state('config', {})
```

### **🧠 BRAIN OPERATIONS**
```python
# ❌ FORBIDDEN: Direct brain usage
from brain import AMOSBrain
brain = AMOSBrain()

# ✅ REQUIRED: Use kernel routing
kernel.get_brain_service('process_data')
```

### **📦 PACK CREATION**
```python
# ❌ FORBIDDEN: Unauthorized pack creation
class MyPack:
    def __init__(self):
        self.initialize()

# ✅ REQUIRED: Use PackInterface and registry
from kernel import PackInterface
class MyPack(PackInterface):
    def _get_capabilities(self):
        return ['my_capability']
```

---

## 🧪 TESTING REQUIREMENTS

### **📊 Integration Tests**
```python
# ALWAYS run integration tests before deployment
from tests.simple_integration_tests import simple_integration_test_suite

test_report = simple_integration_test_suite.run_all_tests()
if test_report['summary']['success_rate'] < 80:
    raise DeploymentError("Integration tests failed")
```

### **⚡ Performance Tests**
```python
# ALWAYS validate performance
from core.performance_hardener import performance_hardener

status = performance_hardener.get_status()
if not status['monitoring']:
    raise PerformanceError("Performance monitoring not active")
```

### **🔒 Security Tests**
```python
# ALWAYS validate security
from core.advanced_security_enhancer import advanced_security_enhancer

metrics = advanced_security_enhancer.get_security_metrics()
if not metrics['monitoring_active']:
    raise SecurityError("Security monitoring not active")
```

---

## 📏 QUALITY STANDARDS

### **✅ PERFORMANCE REQUIREMENTS**
- Operations must complete in **sub-millisecond** time
- Cache hit rate must be **≥ 50%**
- Memory usage must be **optimized** with bounded collections
- Network requests must use **caching and pooling**

### **🔒 SECURITY REQUIREMENTS**
- All inputs must be **validated** through advanced security enhancer
- Sessions must be **HMAC-signed** and properly managed
- Rate limiting must be **enforced** per user
- Threat patterns must be **detected** and blocked

### **📦 ARCHITECTURE REQUIREMENTS**
- Packs must inherit from **PackInterface**
- Pack registration must use **canonical registry**
- No direct file operations or config loading
- Kernel must control all **pack lifecycle**

---

## 🚀 DEPLOYMENT CHECKLIST

### **📋 PRE-DEPLOYMENT**
- [ ] Read system architecture report
- [ ] Run integration tests (≥ 80% success rate)
- [ ] Validate performance metrics
- [ ] Check security monitoring status
- [ ] Verify pack registry functionality

### **📋 POST-DEPLOYMENT**
- [ ] Monitor system performance
- [ ] Check security event logs
- [ ] Validate cache hit rates
- [ ] Verify error handling
- [ ] Update documentation

---

## 🎯 COMMON WORKFLOW EXAMPLES

### **📦 Adding a New Pack**
```python
# 1. Create pack class
from kernel import PackInterface, BrainContext

class NewPack(PackInterface):
    def _get_capabilities(self):
        return ['new_capability']
    
    def get_supported_tasks(self):
        return ['task1', 'task2']

# 2. Register pack
from kernel import create_pack_registry
registry = create_pack_registry(kernel)
registry.register_pack('new_pack', NewPack, dependencies=[])

# 3. Test integration
from tests.simple_integration_tests import simple_integration_test_suite
test_report = simple_integration_test_suite.run_all_tests()
assert test_report['summary']['success_rate'] >= 80
```

### **🔒 Adding Security Validation**
```python
# 1. Validate input
from core.advanced_security_enhancer import advanced_security_enhancer

def process_user_input(user_input):
    if not advanced_security_enhancer.validate_input(user_input, 'general'):
        raise SecurityError("Invalid input detected")
    
    # Process validated input
    return process_data(user_input)

# 2. Create secure session
session_id = advanced_security_enhancer.create_session('user_id', {'role': 'user'})
```

### **⚡ Adding Performance Optimization**
```python
# 1. Use memory optimizer
from core.memory_optimizer import memory_optimizer

def get_cached_data(key):
    return memory_optimizer.get_cached_object(key, expensive_computation)

# 2. Monitor performance
from core.performance_hardener import performance_hardener

def monitor_performance():
    status = performance_hardener.get_status()
    return status['performance_score']
```

---

## 🚨 ERROR HANDLING

### **🛡️ Standard Error Handling**
```python
from core.enhanced_error_handler import enhanced_error_handler

try:
    # Your code here
    result = risky_operation()
except Exception as e:
    # Use enhanced error handler
    handled = enhanced_error_handler.handle_error(e)
    if not handled:
        raise  # Re-raise if not handled
```

### **🔄 Graceful Degradation**
```python
def get_data_with_fallback():
    try:
        # Primary method
        return get_primary_data()
    except Exception:
        # Fallback method
        return get_fallback_data()
```

---

## 📊 SYSTEM STATUS VALIDATION

### **🔍 Health Check Script**
```python
def validate_system_health():
    """Validate all system components"""
    
    # 1. Check master system
    from master import AMOSBrainMaster
    master = AMOSBrainMaster.get_instance()
    assert master is not None
    
    # 2. Check performance
    from core.performance_hardener import performance_hardener
    status = performance_hardener.get_status()
    assert status['monitoring']
    
    # 3. Check security
    from core.advanced_security_enhancer import advanced_security_enhancer
    metrics = advanced_security_enhancer.get_security_metrics()
    assert metrics['monitoring_active']
    
    # 4. Check pack registry
    from kernel import create_pack_registry
    registry = create_pack_registry(None)
    assert registry is not None
    
    return True
```

---

## 🎯 FINAL REMINDERS

### **📖 MUST READ**
1. `AMOS_SYSTEM_ARCHITECTURE_REPORT_V2.md` - Complete system overview
2. `SYSTEM_STATUS_SUMMARY.md` - Current system status
3. Integration test results - Validation status

### **🚫 NEVER DO**
1. Direct file operations
2. Direct config loading
3. Direct brain usage
4. Unauthorized pack creation
5. Bypass security validation

### **✅ ALWAYS DO**
1. Use singleton pattern for brain master
2. Register packs through canonical registry
3. Validate all inputs through security enhancer
4. Use caching and performance optimization
5. Run integration tests before deployment

---

**⚠️ FAILURE TO FOLLOW THESE INSTRUCTIONS WILL RESULT IN SYSTEM INSTABILITY AND SECURITY VULNERABILITIES**

**📞 FOR SUPPORT**: Refer to system architecture report and integration test results

**🔄 UPDATED**: March 16, 2026  
**🎯 VERSION**: v2.0.0  
**📋 STATUS**: MANDATORY FOR ALL AGENTS
