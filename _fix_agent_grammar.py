#!/usr/bin/env python3
"""Fix remaining grammar issues: missing verb after 'Agent that' and double 'executes Executes'."""
import json, re
from pathlib import Path

AGENTS_DIR = Path("/Users/mac/Documents/AMOS_OS/.devin/agents")

fixed = 0
for af in sorted(AGENTS_DIR.glob("*.json")):
    try:
        data = json.loads(af.read_text())
        desc = data.get('description', '')
        original = desc
        
        # Fix 1: "Agent that executes Executes, ..." -> "Agent that executes, ..."
        desc = re.sub(r'^Agent that executes (Executes|Orchestrates|Runs|Validates|Analyzes|Traces|Assesses|Generates|Builds|Transforms|Coordinates|Govern|Operates|Implements|Computes|Evaluates|Monitors|Detects|Classifies|Maps|Routes|Resolves|Compiles|Manages|Performs|Applies|Processes|Derives|Extracts|Constructs|Maintains|Queries|Assumes|Integrates|Bridges|Balances|Preserves|Enforces|Controls|Schedules|Dispatches|Allocates|Optimizes|Calibrates|Adjusts|Adapts|Evolves|Learns|Reasons|Infers|Deduces|Induces|Abstracts|Decomposes|Synthesizes|Composes|Combines|Merges|Splits|Forks|Clones|Replicates|Mirrors|Reflects|Projects|Extends|Expands|Contracts|Shrinks|Grows|Develops|Matures|Ages|Decays|Degrades|Recovers|Restores|Repairs|Heals|Regenerates|Renews|Refreshes|Reloads|Reboots|Restarts|Resumes|Continues|Pauses|Suspends|Halts|Stops|Starts|Begins|Initiates|Launches|Triggers|Fires|Activates|Deactivates|Disables|Enables|Toggles|Switches|Transitions|Migrates|Moves|Shifts|Transfers|Conveys|Carries|Delivers|Sends|Receives|Accepts|Rejects|Filters|Purges|Cleans|Wipes|Clears|Resets|Reinitializes),\s*', 'Agent that ', desc)
        
        # Fix 2: "Agent that <non-verb>..." -> "Agent that executes <non-verb>..."
        # These are cases where the verb was stripped but the next word is not a verb
        # Pattern: "Agent that " followed by a non-verb word (lowercase noun/adjective)
        # We need to add "executes" back for these
        non_verb_starts = [
            '32-layer', 'Quantum Logic', 'Unified Biological', 'multi-dimensional',
            'arXiv/scientific', 'governs', 'govern',  # 'governs' is actually a verb, keep
        ]
        for nv in non_verb_starts:
            if desc.startswith(f'Agent that {nv}') and not desc.startswith(f'Agent that executes {nv}'):
                desc = desc.replace(f'Agent that {nv}', f'Agent that executes {nv}', 1)
        
        # Fix 3: "Agent that executes governs ..." -> "Agent that governs ..."
        # (governs is already a verb, no need for "executes")
        desc = re.sub(r'^Agent that executes (governs|govern)\s+', r'Agent that \1 ', desc)
        
        if desc != original:
            data['description'] = desc
            af.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
            fixed += 1
            print(f"  FIXED {af.stem}: {original[:80]}... -> {desc[:80]}...")
    except Exception as e:
        print(f"  ERROR {af.stem}: {e}")

print(f"\nFixed: {fixed}")
