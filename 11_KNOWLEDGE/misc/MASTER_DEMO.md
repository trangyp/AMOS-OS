---
title: MASTER DEMO
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


# master_demo

```python
#!/usr/bin/env python3
"""
Master Demonstration of Hierarchical AI Architecture Generator

This demo showcases all implemented features:
- Hierarchical generation (rule-based)
- Goal-driven generation (ontology-based)
- Unified generation (hybrid)
- Pattern library with code templates
- AMOS integration bridge
- Query and validation

Run: python master_demo.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hierarchical_ai_architecture_generator import (
    HierarchicalGenerator,
    GoalDrivenGenerator,
    AILayer, Scale, Constraint, Validation,
    PatternLibrary, PatternType,
    AMOSArchitectureBridge,
)
from unified_generator import UnifiedGenerator, GenerationMode


def section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")


def demo_1_hierarchical_basic():
    """Demo 1: Basic hierarchical generation"""
    section("1. HIERARCHICAL GENERATION - Basic")
    
    gen = HierarchicalGenerator()
    
    # Generate 20 entries
    print("\nGenerating 20 architecture entries...")
    entries = gen.generate(limit=20, validate=True)
    print(f"✓ Generated {len(entries)} entries")
    
    # Show first entry details
    e = entries[0]
    print(f"\nFirst entry: {e.id}")
    print(f"  Meta-equation: {e.meta_equation.name}")
    print(f"  Formula: {e.meta_equation.formula}")
    print(f"  Layer: {e.ai_layer.value}")
    print(f"  Scale: {e.scale.value}")
    print(f"  Constraint: {e.constraint.value}")
    print(f"  Signature: {e.structural_signature}")
    
    # Show architecture structure
    print(f"\n  Architecture:")
    for key, value in e.architecture.items():
        print(f"    {key}: {value}")
    
    return gen, entries


def demo_2_hierarchical_query(gen, entries):
    """Demo 2: Querying architectures"""
    section("2. HIERARCHICAL - Query & Filter")
    
    # Generate more entries for querying
    if gen.index.count() < 100:
        print("\nPopulating index with more entries...")
        gen.generate(limit=100)
    
    # Query by layer
    print("\nQuery: Safety Controller layer")
    safety = gen.query(ai_layer=AILayer.SAFETY_CONTROLLER)
    print(f"✓ Found {len(safety)} safety architectures")
    
    # Query by constraint
    print("\nQuery: Privacy constraint")
    privacy = gen.query(constraint=Constraint.PRIVACY)
    print(f"✓ Found {len(privacy)} privacy-constrained architectures")
    
    # Complex query
    print("\nQuery: Planning + Safety + Risk Score validation")
    complex_results = gen.query(
        ai_layer=AILayer.PLANNING_ENGINE,
        constraint=Constraint.SAFETY,
        validation=Validation.RISK_SCORE
    )
    print(f"✓ Found {len(complex_results)} matching architectures")
    
    # Show stats
    print("\nGenerator Statistics:")
    stats = gen.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")


def demo_3_goal_driven():
    """Demo 3: Goal-driven generation"""
    section("3. GOAL-DRIVEN GENERATION")
    
    gen = GoalDrivenGenerator()
    
    # Test goals
    goals = [
        "Create a system to search and cite academic papers",
        "Build a tool that generates safe Python code",
        "Design a multi-agent debate system for fact checking",
    ]
    
    for goal in goals:
        print(f"\nGoal: {goal}")
        
        # Explain classification
        explanation = gen.explain_goal(goal)
        print(f"  Classified as: {explanation['classified_as']}")
        print(f"  Confidence: {explanation['confidence']:.0%}")
        
        # Generate architectures
        archs = gen.generate(goal, count=5)
        print(f"  Generated {len(archs)} architectures")
        
        if archs:
            a = archs[0]
            print(f"  Example: {a.id}")
            print(f"    Layers: {', '.join(l.name for l in a.layers[:3])}")
            print(f"    Scale: {a.scale.value}")
            print(f"    Constraint: {a.constraint.value}")
    
    return gen


def demo_4_patterns():
    """Demo 4: Pattern library"""
    section("4. PATTERN LIBRARY")
    
    library = PatternLibrary()
    
    print(f"\nAvailable patterns: {len(library.list_patterns())}")
    for pt in library.list_patterns():
        print(f"  - {pt.value}")
    
    # Get specific pattern
    pattern = library.get_pattern(PatternType.STATE_MACHINE)
    print(f"\nStateMachinePattern code templates:")
    
    # Generate code for different layers
    layers = [AILayer.SAFETY_CONTROLLER, AILayer.TOOL_EXECUTOR, AILayer.INPUT_PERCEPTION]
    for layer in layers:
        code = pattern.get_code_template(layer, Scale.RESPONSE)
        preview = code[:150].replace('\n', ' ')
        print(f"\n  {layer.value}:")
        print(f"    {preview}...")
    
    # Generate pattern instance
    print("\n\nGenerating pattern instance...")
    instance = pattern.generate_instance(
        AILayer.SAFETY_CONTROLLER,
        Scale.RESPONSE,
        Constraint.SAFETY,
        Validation.UNIT_TEST
    )
    print(f"  Configuration keys: {list(instance.configuration.keys())}")
    print(f"  Test cases: {len(instance.test_cases)}")


def demo_5_amos_bridge(gen=None):
    """Demo 5: AMOS integration"""
    section("5. AMOS INTEGRATION BRIDGE")
    
    bridge = AMOSArchitectureBridge(gen)
    
    # Status
    print("\nBridge Status:")
    status = bridge.get_status()
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    # Get architecture for specific layer
    print("\nGetting Safety Controller architecture...")
    arch = bridge.get_architecture_for_layer("safety_controller", "response")
    if arch:
        print(f"  Found: {arch.id}")
        print(f"  AMOS Engine mapping: {bridge.map_to_amos_engine(arch)}")
    
    # Get safety architectures
    print("\nGetting all safety architectures...")
    if gen:
        gen.generate(limit=200)
    safety_archs = bridge.get_safety_architecture()
    print(f"  Found {len(safety_archs)} safety architectures")
    
    # Get validation suite
    if safety_archs:
        print("\nValidation suite for first safety entry:")
        suite = bridge.get_validation_suite(safety_archs[0])
        print(f"  Type: {suite['validation_type']}")
        print(f"  Tests: {len(suite['tests'])}")


def demo_6_unified():
    """Demo 6: Unified generator (hybrid mode)"""
    section("6. UNIFIED GENERATOR (Hybrid Mode)")
    
    # Test all three modes
    modes = [
        (GenerationMode.HIERARCHICAL, "Hierarchical only"),
        (GenerationMode.GOAL, "Goal-driven only"),
        (GenerationMode.HYBRID, "Hybrid (combined)"),
    ]
    
    goal = "Create a safe multi-agent retrieval system"
    
    for mode, desc in modes:
        print(f"\n{desc}:")
        gen = UnifiedGenerator(mode=mode)
        
        if mode == GenerationMode.HIERARCHICAL:
            entries = gen.generate(limit=10)
        else:
            entries = gen.generate(goal=goal, limit=10)
        
        print(f"  Generated {len(entries)} entries")
        
        # Show breakdown for hybrid
        if mode == GenerationMode.HYBRID and entries:
            types = {}
            for e in entries:
                t = e.get("type", "unknown")
                types[t] = types.get(t, 0) + 1
            print(f"  Breakdown: {types}")
    
    # Goal classification
    print("\n\nGoal Classification Examples:")
    gen = UnifiedGenerator(mode=GenerationMode.GOAL)
    
    test_goals = [
        "Search and cite papers",
        "Generate Python code",
        "Multi-agent consensus",
        "Privacy-preserving recommendations",
    ]
    
    for g in test_goals:
        result = gen.classify_goal(g)
        print(f"  {g[:30]:30} → {result['classified_as']}")


def demo_7_export_import(gen):
    """Demo 7: Export and import"""
    section("7. EXPORT & IMPORT")
    
    import tempfile
    import json
    
    # Generate some entries
    entries = gen.generate(limit=10)
    
    # Export to JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    print(f"\nExporting {len(entries)} entries to JSON...")
    gen.export_to_json(entries, temp_path)
    
    # Verify file exists and is valid JSON
    with open(temp_path, 'r') as f:
        data = json.load(f)
    
    print(f"✓ Exported successfully")
    print(f"  Metadata: {data['metadata']['title']}")
    print(f"  Entry count: {data['metadata']['entry_count']}")
    
    # Import back
    print(f"\nImporting from JSON...")
    new_gen = HierarchicalGenerator()
    imported = new_gen.import_from_json(temp_path)
    print(f"✓ Imported {len(imported)} entries")
    
    # Cleanup
    os.unlink(temp_path)
    print(f"\n(temporary file cleaned up)")


def run_all_demos():
    """Run all demonstrations"""
    print("\n" + "="*70)
    print("  HIERARCHICAL AI ARCHITECTURE GENERATOR")
    print("  Master Demonstration - All Features")
    print("="*70)
    
    # Demo 1 & 2: Hierarchical
    gen, entries = demo_1_hierarchical_basic()
    demo_2_hierarchical_query(gen, entries)
    
    # Demo 3: Goal-driven
    goal_gen = demo_3_goal_driven()
    
    # Demo 4: Patterns
    demo_4_patterns()
    
    # Demo 5: AMOS Bridge
    demo_5_amos_bridge(gen)
    
    # Demo 6: Unified
    demo_6_unified()
    
    # Demo 7: Export/Import
    demo_7_export_import(gen)
    
    # Summary
    section("SUMMARY")
    print("\n✓ All features demonstrated successfully:")
    print("  1. Hierarchical generation with 7-level hierarchy")
    print("  2. Multi-index querying with filters")
    print("  3. Goal-driven generation with natural language parsing")
    print("  4. Pattern library with 5 pattern types and code templates")
    print("  5. AMOS integration bridge")
    print("  6. Unified generator with 3 modes")
    print("  7. Export/Import functionality")
    print("\n" + "="*70)
    print("  Master Demo Complete!")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_demos()


```

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
