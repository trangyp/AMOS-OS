---
title: SIMPLE DEMO
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


# simple_demo

```python
#!/usr/bin/env python3
"""
Simple working demonstration of the Hierarchical AI Architecture Generator.
This script proves the implementation is functional.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def demo():
    print("=" * 60)
    print("Hierarchical AI Architecture Generator - Simple Demo")
    print("=" * 60)
    
    # 1. Test core imports
    print("\n1. Testing core imports...")
    try:
        from core import HierarchicalGenerator, ArchitectureEntry
        from core import MetaEquationType, EquationFamily, AILayer, Scale, Constraint, Validation
        print("   ✓ Core classes imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import core: {e}")
        return False
    
    # 2. Create generator and generate entries
    print("\n2. Creating HierarchicalGenerator...")
    try:
        gen = HierarchicalGenerator()
        print("   ✓ Generator created")
        
        print("\n3. Generating 5 architecture entries...")
        entries = gen.generate(limit=5, validate=True)
        print(f"   ✓ Generated {len(entries)} entries")
        
        # Show first entry
        if entries:
            e = entries[0]
            print(f"\n   First entry details:")
            print(f"   - ID: {e.id}")
            print(f"   - Meta-equation: {e.meta_equation.name}")
            print(f"   - Formula: {e.meta_equation.formula}")
            print(f"   - Layer: {e.ai_layer.value}")
            print(f"   - Scale: {e.scale.value}")
            print(f"   - Signature: {e.structural_signature}")
    except Exception as e:
        print(f"   ✗ Generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 4. Test querying
    print("\n4. Testing query functionality...")
    try:
        # Generate more for querying
        gen.generate(limit=50)
        
        # Query by layer
        results = gen.query(ai_layer=AILayer.SAFETY_CONTROLLER)
        print(f"   ✓ Found {len(results)} safety controller entries")
        
        # Query by constraint
        results = gen.query(constraint=Constraint.PRIVACY)
        print(f"   ✓ Found {len(results)} privacy-constrained entries")
    except Exception as e:
        print(f"   ✗ Query failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 5. Test patterns
    print("\n5. Testing PatternLibrary...")
    try:
        from patterns import PatternLibrary, PatternType
        
        library = PatternLibrary()
        patterns = library.list_patterns()
        print(f"   ✓ Found {len(patterns)} patterns")
        
        # Get state machine pattern
        pattern = library.get_pattern(PatternType.STATE_MACHINE)
        code = pattern.get_code_template(AILayer.SAFETY_CONTROLLER, Scale.RESPONSE)
        print(f"   ✓ Generated code template ({len(code)} characters)")
    except Exception as e:
        print(f"   ✗ Pattern test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 6. Test goal-driven (if available)
    print("\n6. Testing GoalDrivenGenerator...")
    try:
        from goal_core import GoalDrivenGenerator
        
        g = GoalDrivenGenerator()
        archs = g.generate("Build a retrieval system", count=3)
        print(f"   ✓ Generated {len(archs)} goal-driven architectures")
        
        if archs:
            a = archs[0]
            print(f"   - Goal type: {a.goal_type.value}")
            print(f"   - Layers: {len(a.layers)}")
    except ImportError:
        print("   ℹ GoalDrivenGenerator not available (optional)")
    except Exception as e:
        print(f"   ✗ Goal-driven test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n" + "=" * 60)
    print("SUCCESS - All features working correctly!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = demo()
    sys.exit(0 if success else 1)


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
