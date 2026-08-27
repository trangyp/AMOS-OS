---
title: UNIFIED GENERATOR
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


"""
Unified AI Architecture Generator

Combines hierarchical and goal-driven generation approaches into a single,
coherent interface for generating AI architectures.

Usage:
    from unified_generator import UnifiedGenerator
    
    # Hierarchical approach (rule-based)
    gen = UnifiedGenerator(mode="hierarchical")
    entries = gen.generate(limit=100)
    
    # Goal-driven approach (ontology-based)
    gen = UnifiedGenerator(mode="goal")
    entries = gen.generate(goal="Create a safe multi-agent system")
    
    # Hybrid approach
    gen = UnifiedGenerator(mode="hybrid")
    entries = gen.generate(goal="Build retrieval system", limit=50)
"""

from __future__ import annotations
from typing import Optional, List, Dict, Any, Union
from enum import Enum, auto

# Import both generators
try:
    from .core import HierarchicalGenerator, ArchitectureEntry, AILayer, Scale, Constraint, Validation
    from .goal_core import GoalDrivenGenerator, GoalArchitecture, GoalType, ScaleLevel, ConstraintType
except ImportError:
    # Fallback for standalone usage
    from core import HierarchicalGenerator, ArchitectureEntry, AILayer, Scale, Constraint, Validation
    from goal_core import GoalDrivenGenerator, GoalArchitecture, GoalType, ScaleLevel, ConstraintType


class GenerationMode(Enum):
    """Modes for the unified generator."""
    HIERARCHICAL = "hierarchical"  # Rule-based hierarchical generation
    GOAL = "goal"                   # Ontology-driven goal generation
    HYBRID = "hybrid"               # Combined approach


class UnifiedGenerator:
    """
    Unified interface for AI architecture generation.
    
    Combines hierarchical (rule-based) and goal-driven (ontology-based)
    approaches into a single coherent interface.
    """
    
    def __init__(self, mode: Union[str, GenerationMode] = GenerationMode.HYBRID):
        self.mode = GenerationMode(mode) if isinstance(mode, str) else mode
        
        # Initialize sub-generators
        self._hierarchical: Optional[HierarchicalGenerator] = None
        self._goal: Optional[GoalDrivenGenerator] = None
        
        if self.mode in (GenerationMode.HIERARCHICAL, GenerationMode.HYBRID):
            self._hierarchical = HierarchicalGenerator()
        
        if self.mode in (GenerationMode.GOAL, GenerationMode.HYBRID):
            self._goal = GoalDrivenGenerator()
    
    def generate(self, 
                 goal: Optional[str] = None,
                 limit: int = 100,
                 **kwargs) -> List[Any]:
        """
        Generate architectures based on mode and parameters.
        
        Args:
            goal: Natural language goal (for goal/hybrid modes)
            limit: Maximum number of architectures to generate
            **kwargs: Additional parameters passed to specific generators
        
        Returns:
            List of architecture entries (type depends on mode)
        """
        if self.mode == GenerationMode.HIERARCHICAL:
            return self._generate_hierarchical(limit, **kwargs)
        elif self.mode == GenerationMode.GOAL:
            if not goal:
                raise ValueError("Goal mode requires a 'goal' parameter")
            return self._generate_goal(goal, limit)
        elif self.mode == GenerationMode.HYBRID:
            return self._generate_hybrid(goal, limit, **kwargs)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")
    
    def _generate_hierarchical(self, limit: int, **kwargs) -> List[ArchitectureEntry]:
        """Generate using hierarchical approach."""
        if not self._hierarchical:
            raise RuntimeError("Hierarchical generator not initialized")
        return self._hierarchical.generate(limit=limit, **kwargs)
    
    def _generate_goal(self, goal: str, limit: int) -> List[GoalArchitecture]:
        """Generate using goal-driven approach."""
        if not self._goal:
            raise RuntimeError("Goal generator not initialized")
        return self._goal.generate(goal, count=limit)
    
    def _generate_hybrid(self, goal: Optional[str], limit: int, **kwargs) -> List[Dict[str, Any]]:
        """
        Generate using hybrid approach.
        
        Uses goal-driven generator to determine goal type and required layers,
        then uses hierarchical generator to fill in detailed configurations.
        """
        results = []
        
        if goal and self._goal:
            # Get goal type and taxonomy
            goal_type = self._goal.parser.parse(goal)
            taxonomy = self._goal.ontology.get_goal_taxonomy(goal_type)
            
            # Generate goal-driven architectures
            goal_archs = self._goal.generate(goal, count=min(limit // 2, 50))
            
            # Convert to unified format
            for arch in goal_archs:
                results.append({
                    "type": "goal_driven",
                    "goal": goal,
                    "goal_type": arch.goal_type.value,
                    "architecture": arch.to_dict()
                })
        
        # Fill remaining with hierarchical entries
        remaining = limit - len(results)
        if remaining > 0 and self._hierarchical:
            # If we have goal info, use it to guide hierarchical generation
            if goal:
                # Map goal type to appropriate AI layers
                layer_mapping = {
                    GoalType.REASONING: AILayer.RECURSIVE_REASONING,
                    GoalType.GENERATION: AILayer.LANGUAGE_GENERATOR,
                    GoalType.RETRIEVAL: AILayer.RETRIEVAL_ENGINE,
                    GoalType.AGENTIC_EXECUTION: AILayer.TOOL_EXECUTOR,
                    GoalType.SAFETY_GOVERNANCE: AILayer.SAFETY_CONTROLLER,
                    GoalType.MEMORY_PERSONALIZATION: AILayer.LONG_TERM_MEMORY,
                    GoalType.MULTI_AGENT: AILayer.MULTI_AGENT_LAYER,
                    GoalType.FRACTAL_SCALING: AILayer.ECOSYSTEM_MONITOR,
                }
                
                if 'goal_type' in locals():
                    target_layer = layer_mapping.get(goal_type)
                    if target_layer:
                        hier_archs = self._hierarchical.query(ai_layer=target_layer)
                        for arch in hier_archs[:remaining]:
                            results.append({
                                "type": "hierarchical",
                                "goal_informed": True,
                                "architecture": arch.to_dict()
                            })
            
            # If still need more, generate generic
            remaining = limit - len(results)
            if remaining > 0:
                hier_archs = self._hierarchical.generate(limit=remaining)
                for arch in hier_archs:
                    results.append({
                        "type": "hierarchical",
                        "goal_informed": False,
                        "architecture": arch.to_dict()
                    })
        
        return results
    
    def query(self, **kwargs) -> List[Any]:
        """
        Query generated architectures.
        
        Args depend on the current mode.
        """
        if self.mode == GenerationMode.HIERARCHICAL and self._hierarchical:
            return self._hierarchical.query(**kwargs)
        elif self.mode == GenerationMode.GOAL and self._goal:
            return self._goal.query(**kwargs)
        else:
            # Hybrid mode - query both
            results = []
            if self._hierarchical:
                results.extend([{"type": "hierarchical", "data": a} for a in self._hierarchical.query(**kwargs)])
            if self._goal:
                results.extend([{"type": "goal", "data": a} for a in self._goal.query(**kwargs)])
            return results
    
    def classify_goal(self, goal: str) -> Dict[str, Any]:
        """
        Classify a natural language goal.
        
        Returns detailed classification information.
        """
        if not self._goal:
            raise RuntimeError("Goal generator not initialized")
        
        return self._goal.explain_goal(goal)
    
    def export(self, entries: List[Any], filepath: str, format: str = "json") -> None:
        """
        Export architectures to file.
        
        Args:
            entries: Architecture entries to export
            filepath: Output file path
            format: Export format (json)
        """
        import json
        
        data = {
            "metadata": {
                "generator": "UnifiedGenerator",
                "mode": self.mode.value,
                "entry_count": len(entries)
            },
            "entries": entries
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get combined statistics from all sub-generators."""
        stats = {
            "mode": self.mode.value,
            "hierarchical": None,
            "goal": None
        }
        
        if self._hierarchical:
            stats["hierarchical"] = self._hierarchical.get_stats()
        
        if self._goal:
            stats["goal"] = self._goal.get_stats()
        
        return stats
    
    def switch_mode(self, mode: Union[str, GenerationMode]) -> None:
        """Switch to a different generation mode."""
        new_mode = GenerationMode(mode) if isinstance(mode, str) else mode
        
        if new_mode == self.mode:
            return
        
        self.mode = new_mode
        
        # Initialize generators as needed
        if new_mode in (GenerationMode.HIERARCHICAL, GenerationMode.HYBRID) and not self._hierarchical:
            self._hierarchical = HierarchicalGenerator()
        
        if new_mode in (GenerationMode.GOAL, GenerationMode.HYBRID) and not self._goal:
            self._goal = GoalDrivenGenerator()


def demo_unified():
    """Demonstrate the unified generator."""
    print("=" * 60)
    print("UNIFIED AI ARCHITECTURE GENERATOR - DEMO")
    print("=" * 60)
    
    # Hierarchical mode
    print("\n1. HIERARCHICAL MODE")
    print("-" * 60)
    gen = UnifiedGenerator(mode="hierarchical")
    entries = gen.generate(limit=10)
    print(f"Generated {len(entries)} hierarchical entries")
    print(f"First entry: {entries[0].id} - {entries[0].ai_layer.value}")
    
    # Goal mode
    print("\n2. GOAL MODE")
    print("-" * 60)
    gen = UnifiedGenerator(mode="goal")
    entries = gen.generate(goal="Build a safe retrieval system", limit=10)
    print(f"Generated {len(entries)} goal-driven entries")
    print(f"First entry: {entries[0].id} - {entries[0].goal_type.value}")
    
    # Hybrid mode
    print("\n3. HYBRID MODE")
    print("-" * 60)
    gen = UnifiedGenerator(mode="hybrid")
    entries = gen.generate(goal="Create multi-agent consensus system", limit=20)
    print(f"Generated {len(entries)} hybrid entries")
    
    goal_types = {}
    for e in entries:
        t = e.get("type", "unknown")
        goal_types[t] = goal_types.get(t, 0) + 1
    print(f"Breakdown: {goal_types}")
    
    # Goal classification
    print("\n4. GOAL CLASSIFICATION")
    print("-" * 60)
    gen = UnifiedGenerator(mode="goal")
    
    test_goals = [
        "Search and cite academic papers",
        "Generate Python code safely",
        "Multi-agent debate system",
        "Privacy-preserving recommendations"
    ]
    
    for goal in test_goals:
        classification = gen.classify_goal(goal)
        print(f"  {goal[:40]:40} → {classification['classified_as']}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demo_unified()

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
