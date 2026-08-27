---
tags: [misc]
---
"""
Command-line interface for the Hierarchical AI Architecture Generator.

Usage:
    python -m hierarchical_ai_architecture_generator generate --limit 1000 --output arch.json
    python -m hierarchical_ai_architecture_generator query --layer safety_controller
    python -m hierarchical_ai_architecture_generator stats
    python -m hierarchical_ai_architecture_generator demo
"""

import argparse
import sys
import json
from typing import List, Optional

from hierarchical_ai_architecture_generator import (
    HierarchicalGenerator,
    AILayer,
    Scale,
    Constraint,
    Validation,
    EquationFamily,
    MetaEquationType,
    AMOSArchitectureBridge,
)


def cmd_generate(args: argparse.Namespace) -> int:
    """Generate architecture entries."""
    generator = HierarchicalGenerator()
    
    print(f"Generating up to {args.limit} architecture entries...")
    entries = generator.generate(limit=args.limit, validate=not args.no_validate)
    
    print(f"Generated {len(entries)} entries")
    
    if args.output:
        generator.export_to_json(entries, args.output)
        print(f"Exported to {args.output}")
    
    if args.verbose:
        for entry in entries[:5]:
            print(f"\n  {entry.id}: {entry.ai_layer.value} / {entry.scale.value}")
            print(f"    Formula: {entry.generated_formula[:60]}...")
    
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    """Query the architecture index."""
    generator = HierarchicalGenerator()
    
    # Build query parameters
    kwargs = {}
    
    if args.layer:
        try:
            kwargs['ai_layer'] = AILayer(args.layer)
        except ValueError:
            print(f"Error: Unknown layer '{args.layer}'")
            print(f"Available layers: {[l.value for l in AILayer]}")
            return 1
    
    if args.scale:
        try:
            kwargs['scale'] = Scale(args.scale)
        except ValueError:
            print(f"Error: Unknown scale '{args.scale}'")
            return 1
    
    if args.constraint:
        try:
            kwargs['constraint'] = Constraint(args.constraint)
        except ValueError:
            print(f"Error: Unknown constraint '{args.constraint}'")
            return 1
    
    if args.validation:
        try:
            kwargs['validation'] = Validation(args.validation)
        except ValueError:
            print(f"Error: Unknown validation '{args.validation}'")
            return 1
    
    if args.family:
        try:
            kwargs['equation_family'] = EquationFamily(args.family)
        except ValueError:
            print(f"Error: Unknown family '{args.family}'")
            return 1
    
    # Generate some entries first if index is empty
    if generator.index.count() == 0:
        print("Populating index with entries...")
        generator.generate(limit=1000)
    
    results = generator.query(**kwargs)
    
    print(f"Found {len(results)} matching entries")
    
    for entry in results[:args.limit]:
        print(f"\n  {entry.id}")
        print(f"    Layer: {entry.ai_layer.value}")
        print(f"    Scale: {entry.scale.value}")
        print(f"    Meta-eq: {entry.meta_equation.name}")
        print(f"    Signature: {entry.structural_signature}")
    
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    """Show generator statistics."""
    generator = HierarchicalGenerator()
    
    if generator.index.count() == 0:
        print("Populating index...")
        generator.generate(limit=500)
    
    stats = generator.get_stats()
    
    print("Generator Statistics:")
    print(f"  Total entries: {stats['total_entries']}")
    print(f"  Meta-equations: {stats['meta_equations']}")
    print(f"  Equation families: {stats['equation_families']}")
    print(f"  AI layers: {stats['ai_layers']}")
    print(f"  Scales: {stats['scales']}")
    print(f"  Constraints: {stats['constraints']}")
    print(f"  Validations: {stats['validations']}")
    
    if args.detailed:
        print("\nEntries by layer:")
        for layer, count in sorted(generator.by_layer.items()):
            print(f"  {layer}: {count}")
    
    return 0


def cmd_bridge(args: argparse.Namespace) -> int:
    """AMOS bridge commands."""
    bridge = AMOSArchitectureBridge()
    
    if args.command == "status":
        status = bridge.get_status()
        print("AMOS Bridge Status:")
        for key, value in status.items():
            print(f"  {key}: {value}")
    
    elif args.command == "safety":
        entries = bridge.get_safety_architecture()
        print(f"Safety architectures: {len(entries)}")
        for entry in entries[:10]:
            print(f"  {entry.id}: {entry.ai_layer.value}")
    
    elif args.command == "governance":
        entries = bridge.get_governance_architecture()
        print(f"Governance architectures: {len(entries)}")
        for entry in entries[:10]:
            print(f"  {entry.id}: {entry.ai_layer.value}")
    
    elif args.command == "export":
        if not args.output:
            print("Error: --output required for export")
            return 1
        
        bridge.generator.generate(limit=args.limit or 100)
        entries = bridge.get_safety_architecture()
        bridge.export_to_amos_config(entries, args.output)
        print(f"Exported {len(entries)} entries to {args.output}")
    
    return 0


def cmd_demo(args: argparse.Namespace) -> int:
    """Run demonstration."""
    from hierarchical_ai_architecture_generator.demo import run_all_demos
    run_all_demos()
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="hierarchical_ai_architecture_generator",
        description="Hierarchical AI Architecture Generator CLI"
    )
    
    subparsers = parser.add_subparsers(dest="cmd", required=True)
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate architecture entries")
    gen_parser.add_argument("--limit", type=int, default=100, help="Maximum entries to generate")
    gen_parser.add_argument("--output", "-o", type=str, help="Output JSON file")
    gen_parser.add_argument("--no-validate", action="store_true", help="Skip validation")
    gen_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    # Query command
    query_parser = subparsers.add_parser("query", help="Query architecture entries")
    query_parser.add_argument("--layer", type=str, help="Filter by AI layer")
    query_parser.add_argument("--scale", type=str, help="Filter by scale")
    query_parser.add_argument("--constraint", type=str, help="Filter by constraint")
    query_parser.add_argument("--validation", type=str, help="Filter by validation")
    query_parser.add_argument("--family", type=str, help="Filter by equation family")
    query_parser.add_argument("--limit", type=int, default=20, help="Maximum results")
    
    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument("--detailed", "-d", action="store_true", help="Show detailed stats")
    
    # Bridge command
    bridge_parser = subparsers.add_parser("bridge", help="AMOS bridge commands")
    bridge_sub = bridge_parser.add_subparsers(dest="command", required=True)
    bridge_sub.add_parser("status", help="Show bridge status")
    bridge_sub.add_parser("safety", help="Get safety architectures")
    bridge_sub.add_parser("governance", help="Get governance architectures")
    export_parser = bridge_sub.add_parser("export", help="Export to AMOS config")
    export_parser.add_argument("--output", "-o", type=str, required=True, help="Output file")
    export_parser.add_argument("--limit", type=int, default=100, help="Entries to generate")
    
    # Demo command
    subparsers.add_parser("demo", help="Run demonstration")
    
    args = parser.parse_args(argv)
    
    commands = {
        "generate": cmd_generate,
        "query": cmd_query,
        "stats": cmd_stats,
        "bridge": cmd_bridge,
        "demo": cmd_demo,
    }
    
    return commands[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
