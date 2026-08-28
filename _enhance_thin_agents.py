#!/usr/bin/env python3
"""Enhance thin agent descriptions (<100 chars) using vault-sourced skill descriptions."""
import json, re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not available, using manual frontmatter parser")
    yaml = None

BASE = Path("/Users/mac/Documents/AMOS_OS")
AGENTS_DIR = BASE / ".devin/agents"
SKILLS_DIR = BASE / ".devin/skills"

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    fm_end = content.find("---", 3)
    if fm_end < 0:
        return {}
    fm_text = content[3:fm_end]
    if yaml:
        try:
            return yaml.safe_load(fm_text) or {}
        except:
            pass
    # Manual fallback: extract description field
    result = {}
    for line in fm_text.split('\n'):
        m = re.match(r'^description:\s*[>"\']?(.+?)[<"\'\']*\s*$', line)
        if m:
            result['description'] = m.group(1).strip()
    return result

def make_agent_description(skill_desc, agent_name, agent_data):
    """Transform a skill description into an agent-appropriate description."""
    if not skill_desc:
        return None
    
    # Get the display name for cleaner reference
    display = agent_data.get('display_name', agent_name)
    
    # The skill description typically starts with "Name — domain capability. Use when..."
    # We want to transform it to: "Agent that executes <capability>. Use when..."
    
    # Extract the core capability part (before "Use when")
    parts = re.split(r'\.\s*Use when\b', skill_desc, maxsplit=1)
    core = parts[0].strip()
    
    # Clean up the core - remove the "Name —" prefix if present
    core = re.sub(r'^[A-Z][\w\s\-/]+\s*—\s*', '', core)
    
    # Build the agent description
    if len(parts) > 1:
        use_when = "Use when " + parts[1].strip()
        # Trim the "Do not use..." part if it makes it too long
        use_when = re.sub(r'\.\s*Do not use.*$', '.', use_when, flags=re.DOTALL)
        # Trim routing instructions
        use_when = re.sub(r'\.\s*Use when\s+amos-.*$', '.', use_when, flags=re.DOTALL)
        
        agent_desc = f"Agent that executes {core}. {use_when}"
    else:
        agent_desc = f"Agent that executes {core}."
    
    # Clean up
    agent_desc = re.sub(r'\s+', ' ', agent_desc).strip()
    
    # Ensure reasonable length (150-400 chars)
    if len(agent_desc) > 400:
        # Truncate at last sentence boundary
        agent_desc = agent_desc[:400]
        last_period = agent_desc.rfind('.')
        if last_period > 150:
            agent_desc = agent_desc[:last_period+1]
    
    return agent_desc

# Collect thin agents
thin_agents = []
for af in sorted(AGENTS_DIR.glob("*.json")):
    try:
        data = json.loads(af.read_text())
        desc = data.get('description', '')
        if len(desc) < 100:
            thin_agents.append((len(desc), af, data))
    except:
        pass

thin_agents.sort()
print(f"Found {len(thin_agents)} thin agents to enhance")

# Enhance each one
enhanced = 0
skipped = 0
errors = 0

for orig_len, af, data in thin_agents:
    agent_name = data.get('name', af.stem)
    skill_binding = data.get('skill_binding', {})
    skill_name = skill_binding.get('primary_skill', '')
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    
    if not skill_path.exists():
        print(f"  SKIP {agent_name}: skill not found at {skill_path}")
        skipped += 1
        continue
    
    content = skill_path.read_text(encoding='utf-8', errors='replace')
    fm = parse_frontmatter(content)
    skill_desc = fm.get('description', '')
    
    if not skill_desc or len(skill_desc) < 50:
        print(f"  SKIP {agent_name}: skill description too thin ({len(skill_desc)}c)")
        skipped += 1
        continue
    
    new_desc = make_agent_description(skill_desc, agent_name, data)
    
    if not new_desc or len(new_desc) < 100:
        print(f"  SKIP {agent_name}: generated desc too short ({len(new_desc) if new_desc else 0}c)")
        skipped += 1
        continue
    
    old_desc = data.get('description', '')
    data['description'] = new_desc
    
    # Also enhance the role field if it's thin
    role = data.get('role', '')
    if len(role) < 100:
        display = data.get('display_name', agent_name)
        data['role'] = f"{display} — {new_desc}"
    
    # Write back
    af.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    enhanced += 1
    print(f"  OK   {agent_name}: {orig_len}c -> {len(new_desc)}c")

print(f"\n=== SUMMARY ===")
print(f"Enhanced: {enhanced}")
print(f"Skipped:  {skipped}")
print(f"Errors:   {errors}")
