#!/usr/bin/env python3
"""
skill_guardrail_checker.py — Scan skills for prompt injection, malicious code,
and credential theft patterns.

Inspired by SOTA repos:
  - dwarvesf/claude-guardrails: deny rules, pre-commit hooks, prompt injection defense
    (40 credential deny rules, 6 PreToolUse hooks, PostToolUse injection scanner)
  - mannanj/skillguard: multi-engine scanner + PreToolUse hook that blocks unscanned skills
  - mbay7/claude-code-security: 6-layer security framework, memory poisoning prevention
  - adityaarakeri/claude-on-a-leash: 6 deterministic guardrails (RCE, exfil, SSRF, injection)
  - lasso-security/claude-hooks: prompt injection defender, PostToolUse patterns.yaml

This checker provides:
  1. Prompt injection detection — scans for instruction override patterns
  2. Credential theft detection — scans for secret exfiltration patterns
  3. Malicious code detection — scans for reverse shells, RCE, data exfiltration
  4. Supply-chain detection — scans for suspicious imports, eval/exec patterns
  5. Hook integrity check — verifies hook files haven't been tampered with
  6. OWASP Agentic Skills Top 10 mapping

Usage:
  python3 scripts/skill_guardrail_checker.py [--skills-dir DIR] [--skill NAME]
  python3 scripts/skill_guardrail_checker.py --skills-dir DIR --owasp
  python3 scripts/skill_guardrail_checker.py --skills-dir DIR --report FILE
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


# ============================================================
# OWASP Agentic Skills Top 10 Mapping
# ============================================================

OWASP_AGENTIC_TOP_10 = {
    "AS01": "Prompt Injection",
    "AS02": "Sensitive Information Disclosure",
    "AS03": "Supply Chain Vulnerabilities",
    "AS04": "Excessive Agency",
    "AS05": "Insecure Output Handling",
    "AS06": "Insecure Skill Design",
    "AS07": "Insecure Communication",
    "AS08": "Insecure Authentication",
    "AS09": "Insecure Authorization",
    "AS10": "Insecure Integration",
}


# ============================================================
# Detection Patterns
# ============================================================

PROMPT_INJECTION_PATTERNS = [
    # Instruction override patterns — require "instructions" keyword to reduce false positives
    (r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions?", "Instruction override", "AS01", "CRITICAL"),
    (r"disregard\s+(all\s+)?(previous|prior|above)\s+(instructions?|rules?|guidelines?)", "Instruction override", "AS01", "CRITICAL"),
    (r"forget\s+(everything|all|previous|prior)\s+(instructions?|rules?|context)", "Memory wipe", "AS01", "CRITICAL"),
    # Role hijack — require "you are now" or "pretend you are" (stronger signal)
    (r"you\s+are\s+now\s+(a|an)\s+(dan|jailbreak|developer|admin|root|unrestricted)", "Role hijack", "AS01", "CRITICAL"),
    (r"pretend\s+you\s+are\s+(a|an)\s+(dan|jailbreak|developer|admin|root|unrestricted)", "Role hijack", "AS01", "CRITICAL"),
    # System prompt injection — only match at start of line or after newline (not in JSON)
    (r"(^|\n)\s*system\s*:\s*(ignore|forget|disregard|override|you\s+are|act\s+as|pretend|new\s+instructions)", "System prompt injection", "AS01", "CRITICAL"),
    # System tag injection — only match <system> when it contains instructions
    (r"<\s*system\s*>\s*(ignore|forget|disregard|override|you\s+are|act\s+as|pretend|new\s+instructions)", "System tag injection", "AS01", "CRITICAL"),
    (r"new\s+instructions?\s*:\s*(ignore|forget|disregard|override|you\s+are|act\s+as|pretend)", "Instruction override", "AS01", "HIGH"),
    (r"override\s+(all\s+)?(safety|security|guardrails?|rules?)", "Safety override", "AS01", "CRITICAL"),
    (r"do\s+not\s+follow\s+(your|the)\s+rules?", "Rule bypass", "AS01", "CRITICAL"),
    (r"jailbreak", "Jailbreak keyword", "AS01", "HIGH"),
    (r"DAN\s+mode", "DAN jailbreak", "AS01", "CRITICAL"),
    (r"developer\s+mode\s+(enabled|activated|on)", "Developer mode jailbreak", "AS01", "HIGH"),
    # Social engineering — require urgency + action
    (r"i\s+am\s+the\s+(admin|developer|owner|creator)\s+(and\s+I\s+command|so\s+you\s+must|bypass)", "Authority claim", "AS01", "MEDIUM"),
    (r"if\s+you\s+don'?t\s+(do|comply|help).*(secret|password|key|token|credential)", "Threat coercion", "AS01", "MEDIUM"),
]

CREDENTIAL_THEFT_PATTERNS = [
    # Secret patterns
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI API key", "AS02", "CRITICAL"),
    (r"sk-ant-[a-zA-Z0-9]{20,}", "Anthropic API key", "AS02", "CRITICAL"),
    (r"AKIA[A-Z0-9]{16}", "AWS access key", "AS02", "CRITICAL"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub personal access token", "AS02", "CRITICAL"),
    (r"gho_[a-zA-Z0-9]{36}", "GitHub OAuth token", "AS02", "CRITICAL"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "Private key", "AS02", "CRITICAL"),
    # Credential exfiltration
    (r"send\s+(.*?\s+)?to\s+(https?://|ftp://|ssh://)", "Data exfiltration URL", "AS02", "CRITICAL"),
    (r"upload\s+(.*?\s+)?to\s+(https?://|ftp://)", "Data exfiltration upload", "AS02", "CRITICAL"),
    (r"curl\s+.*\|\s*(sh|bash|zsh)", "Pipe to shell", "AS02", "CRITICAL"),
    (r"wget\s+.*\|\s*(sh|bash|zsh)", "Pipe to shell", "AS02", "CRITICAL"),
    (r"exfiltrate", "Exfiltration keyword", "AS02", "HIGH"),
    (r"read\s+.*\.env\s+and\s+(send|upload|post|transmit)", "Env file exfiltration", "AS02", "CRITICAL"),
    (r"cat\s+.*\.ssh/id_rsa", "SSH key read", "AS02", "CRITICAL"),
    (r"cat\s+.*\.aws/credentials", "AWS credentials read", "AS02", "CRITICAL"),
]

MALICIOUS_CODE_PATTERNS = [
    # Reverse shell
    (r"bash\s+-i\s+>&\s*/dev/tcp/", "Reverse shell", "AS04", "CRITICAL"),
    (r"nc\s+-e\s+/bin/(sh|bash)", "Netcat reverse shell", "AS04", "CRITICAL"),
    (r"python\s+-c\s+.*socket.*connect", "Python reverse shell", "AS04", "CRITICAL"),
    (r"perl\s+-e\s+.*Socket.*connect", "Perl reverse shell", "AS04", "CRITICAL"),
    # RCE
    (r"eval\s*\(\s*(input|raw_input|request)", "Eval of user input", "AS04", "CRITICAL"),
    (r"exec\s*\(\s*(input|raw_input|request)", "Exec of user input", "AS04", "CRITICAL"),
    (r"os\.system\s*\(\s*(input|request|user)", "OS system of user input", "AS04", "CRITICAL"),
    (r"subprocess\.call\s*\(\s*shell\s*=\s*True", "Shell=True subprocess", "AS04", "HIGH"),
    # Data exfiltration
    (r"requests\.post\s*\(.*(?:secrets?|keys?|tokens?|passwords?)", "Secret exfiltration via HTTP", "AS02", "CRITICAL"),
    (r"base64\.b64encode\s*\(.*(?:secrets?|keys?|tokens?|passwords?)", "Secret encoding", "AS02", "HIGH"),
    # Privilege escalation
    (r"sudo\s+su", "Sudo escalation", "AS04", "HIGH"),
    (r"chmod\s+777", "World-writable chmod", "AS06", "MEDIUM"),
    # Destructive commands
    (r"rm\s+-rf\s+/", "Recursive root delete", "AS04", "CRITICAL"),
    (r"mkfs\.", "Filesystem format", "AS04", "CRITICAL"),
    (r"dd\s+.*of=/dev/", "Disk overwrite", "AS04", "CRITICAL"),
]

SUPPLY_CHAIN_PATTERNS = [
    # Suspicious imports
    (r"import\s+(subprocess|os|shutil|ctypes)\s*$", "Suspicious import", "AS03", "LOW"),
    (r"from\s+(subprocess|os|shutil|ctypes)\s+import", "Suspicious import", "AS03", "LOW"),
    # Dynamic execution
    (r"__import__\s*\(", "Dynamic import", "AS03", "MEDIUM"),
    (r"importlib\.import_module\s*\(\s*(input|request|user)", "Dynamic import of user input", "AS03", "CRITICAL"),
    # Obfuscation — require 4+ consecutive hex escapes (not just Vietnamese text)
    (r"(?:\\x[0-9a-f]{2}){4,}", "Hex obfuscation", "AS03", "HIGH"),
    (r"(?:\\u[0-9a-f]{4}){4,}", "Unicode obfuscation", "AS03", "HIGH"),
    (r"eval\s*\(\s*base64", "Base64 eval obfuscation", "AS03", "CRITICAL"),
    (r"exec\s*\(\s*base64", "Base64 exec obfuscation", "AS03", "CRITICAL"),
    # Suspicious URLs in code
    (r"https?://(?:bit\.ly|tinyurl|t\.co|goo\.gl)", "Shortened URL in code", "AS03", "MEDIUM"),
    (r"https?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}", "IP URL in code", "AS03", "MEDIUM"),
]

INSECURE_DESIGN_PATTERNS = [
    # Missing safety boundaries
    (r"autonomously\s+(execute|run|delete|modify)\s+without", "Autonomous execution without guard", "AS04", "HIGH"),
    (r"no\s+human\s+(review|approval|oversight)\s+required", "No human oversight", "AS04", "HIGH"),
    (r"always\s+(execute|run|proceed)\s+regardless", "Always execute regardless", "AS04", "HIGH"),
    # Insecure output
    (r"output\s+directly\s+to\s+(terminal|shell|console)\s+without\s+validation", "Unvalidated output", "AS05", "MEDIUM"),
    # Insecure skill design
    (r"trust\s+all\s+(input|user|external)", "Trust all input", "AS06", "HIGH"),
    (r"no\s+validation\s+(needed|required|necessary)", "No validation", "AS06", "HIGH"),
]


ALL_PATTERN_GROUPS = {
    "prompt_injection": PROMPT_INJECTION_PATTERNS,
    "credential_theft": CREDENTIAL_THEFT_PATTERNS,
    "malicious_code": MALICIOUS_CODE_PATTERNS,
    "supply_chain": SUPPLY_CHAIN_PATTERNS,
    "insecure_design": INSECURE_DESIGN_PATTERNS,
}


# ============================================================
# Scanner
# ============================================================

def scan_content(content: str, file_path: str = "") -> List[dict]:
    """Scan content for all pattern groups. Returns list of findings."""
    findings = []

    for group_name, patterns in ALL_PATTERN_GROUPS.items():
        for pattern, description, owasp_id, severity in patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE if group_name == "prompt_injection" else 0):
                line_num = content[:match.start()].count('\n') + 1
                finding = {
                    "group": group_name,
                    "pattern": pattern,
                    "description": description,
                    "owasp_id": owasp_id,
                    "owasp_name": OWASP_AGENTIC_TOP_10.get(owasp_id, "Unknown"),
                    "severity": severity,
                    "file": file_path,
                    "line": line_num,
                    "match": match.group()[:80],
                }
                findings.append(finding)

    return findings


def scan_skill(skill_dir: Path, skip_references: bool = False) -> List[dict]:
    """Scan all files in a skill directory for security issues."""
    all_findings = []

    for f in sorted(skill_dir.rglob("*")):
        if not f.is_file():
            continue
        # Skip binary files, images, etc.
        if f.suffix in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.zip', '.gz', '.tar'):
            continue
        # Skip reference/documentation files if requested
        if skip_references and "references/" in str(f.relative_to(skill_dir)):
            continue

        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        rel_path = str(f.relative_to(skill_dir))
        findings = scan_content(content, rel_path)
        all_findings.extend(findings)

    return all_findings


def scan_all_skills(skills_dir: Path, skill_filter: Optional[str] = None, skip_references: bool = False) -> dict:
    """Scan all skills and return aggregated results."""
    results = {
        "total_skills": 0,
        "clean_skills": 0,
        "skills_with_findings": 0,
        "total_findings": 0,
        "by_severity": defaultdict(int),
        "by_owasp": defaultdict(int),
        "by_group": defaultdict(int),
        "skills": {},
    }

    for d in sorted(skills_dir.iterdir()):
        if not (d.is_dir() and (d / "SKILL.md").exists()):
            continue
        if skill_filter and skill_filter not in d.name:
            continue

        results["total_skills"] += 1
        findings = scan_skill(d, skip_references=skip_references)

        if findings:
            results["skills_with_findings"] += 1
            results["skills"][d.name] = findings
            results["total_findings"] += len(findings)

            for f in findings:
                results["by_severity"][f["severity"]] += 1
                results["by_owasp"][f["owasp_id"]] += 1
                results["by_group"][f["group"]] += 1
        else:
            results["clean_skills"] += 1

    return results


# ============================================================
# Hook Integrity Check
# ============================================================

def check_hook_integrity(hooks_dir: Path, manifest_path: Optional[Path] = None) -> dict:
    """Check hook file integrity against SHA-256 manifest."""
    result = {
        "hooks_dir": str(hooks_dir),
        "total_hooks": 0,
        "verified": 0,
        "missing_manifest": False,
        "mismatches": [],
        "new_hooks": [],
    }

    if not hooks_dir.exists():
        result["missing_manifest"] = True
        return result

    hook_files = list(hooks_dir.rglob("*.py")) + list(hooks_dir.rglob("*.sh"))
    result["total_hooks"] = len(hook_files)

    if manifest_path and manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for hook in hook_files:
            rel = str(hook.relative_to(hooks_dir))
            current_hash = hashlib.sha256(hook.read_bytes()).hexdigest()
            if rel in manifest:
                if manifest[rel] == current_hash:
                    result["verified"] += 1
                else:
                    result["mismatches"].append({
                        "hook": rel,
                        "expected": manifest[rel][:16],
                        "actual": current_hash[:16],
                    })
            else:
                result["new_hooks"].append(rel)
    else:
        result["missing_manifest"] = True

    return result


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Scan skills for security guardrail violations")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Filter to specific skill name")
    parser.add_argument("--owasp", action="store_true", help="Show OWASP Agentic Top 10 mapping")
    parser.add_argument("--hooks-dir", default=None, help="Hooks directory for integrity check")
    parser.add_argument("--report", default=None, help="Write JSON report to file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    parser.add_argument("--skip-references", action="store_true", help="Skip references/ documentation dirs")
    args = parser.parse_args()

    if args.owasp:
        print("=" * 70)
        print("  OWASP Agentic Skills Top 10")
        print("=" * 70)
        print()
        for owasp_id, name in sorted(OWASP_AGENTIC_TOP_10.items()):
            print(f"  {owasp_id}: {name}")
        print()
        print("  Pattern coverage:")
        all_patterns = {}
        for group, patterns in ALL_PATTERN_GROUPS.items():
            for _, _, owasp_id, _ in patterns:
                all_patterns.setdefault(owasp_id, []).append(group)
        for owasp_id in sorted(all_patterns):
            groups = ", ".join(sorted(set(all_patterns[owasp_id])))
            print(f"    {owasp_id} ({OWASP_AGENTIC_TOP_10[owasp_id]}): {groups}")
        return

    skills_dir = Path(args.skills_dir)
    results = scan_all_skills(skills_dir, args.skill, skip_references=args.skip_references)

    if args.summary:
        print(f"Skills scanned:       {results['total_skills']}")
        print(f"Clean skills:         {results['clean_skills']}")
        print(f"Skills with findings: {results['skills_with_findings']}")
        print(f"Total findings:       {results['total_findings']}")
        print(f"  CRITICAL: {results['by_severity'].get('CRITICAL', 0)}")
        print(f"  HIGH:     {results['by_severity'].get('HIGH', 0)}")
        print(f"  MEDIUM:   {results['by_severity'].get('MEDIUM', 0)}")
        print(f"  LOW:      {results['by_severity'].get('LOW', 0)}")
        return

    print("=" * 70)
    print("  AMOS Skill Guardrail Checker")
    print("  OWASP Agentic Skills Top 10 + Prompt Injection Defense")
    print("=" * 70)
    print()
    print(f"  Skills directory: {skills_dir}")
    print()
    print(f"  Skills scanned:       {results['total_skills']}")
    print(f"  Clean skills:         {results['clean_skills']}")
    print(f"  Skills with findings: {results['skills_with_findings']}")
    print(f"  Total findings:       {results['total_findings']}")
    print()
    print(f"  By Severity:")
    print(f"    CRITICAL: {results['by_severity'].get('CRITICAL', 0)}")
    print(f"    HIGH:     {results['by_severity'].get('HIGH', 0)}")
    print(f"    MEDIUM:   {results['by_severity'].get('MEDIUM', 0)}")
    print(f"    LOW:      {results['by_severity'].get('LOW', 0)}")
    print()
    print(f"  By OWASP Category:")
    for owasp_id in sorted(results["by_owasp"]):
        name = OWASP_AGENTIC_TOP_10.get(owasp_id, "Unknown")
        print(f"    {owasp_id} ({name}): {results['by_owasp'][owasp_id]}")
    print()
    print(f"  By Pattern Group:")
    for group in sorted(results["by_group"]):
        print(f"    {group}: {results['by_group'][group]}")
    print()

    # Show findings
    if results["skills"]:
        print("  Findings by skill:")
        for skill_name in sorted(results["skills"]):
            findings = results["skills"][skill_name]
            print(f"    {skill_name} ({len(findings)} findings):")
            for f in findings[:5]:
                print(f"      [{f['severity']}] {f['owasp_id']} {f['description']} at {f['file']}:{f['line']}")
                print(f"        Match: {f['match'][:60]}")
            if len(findings) > 5:
                print(f"      ... and {len(findings) - 5} more")
        print()

    # Hook integrity check
    if args.hooks_dir:
        hooks_dir = Path(args.hooks_dir)
        manifest = hooks_dir / ".integrity.sha256"
        hook_result = check_hook_integrity(hooks_dir, manifest if manifest.exists() else None)
        print("  Hook Integrity Check:")
        print(f"    Hooks directory: {hook_result['hooks_dir']}")
        print(f"    Total hooks:     {hook_result['total_hooks']}")
        print(f"    Verified:        {hook_result['verified']}")
        if hook_result["mismatches"]:
            print(f"    Mismatches:      {len(hook_result['mismatches'])}")
            for m in hook_result["mismatches"][:5]:
                print(f"      {m['hook']}: expected {m['expected']}..., got {m['actual']}...")
        if hook_result["new_hooks"]:
            print(f"    New (unmanifested): {len(hook_result['new_hooks'])}")
            for h in hook_result["new_hooks"][:5]:
                print(f"      {h}")
        print()

    if args.report:
        # Convert defaultdicts to regular dicts for JSON
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "results": {
                "total_skills": results["total_skills"],
                "clean_skills": results["clean_skills"],
                "skills_with_findings": results["skills_with_findings"],
                "total_findings": results["total_findings"],
                "by_severity": dict(results["by_severity"]),
                "by_owasp": dict(results["by_owasp"]),
                "by_group": dict(results["by_group"]),
                "skills": results["skills"],
            },
        }
        Path(args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Report written to: {args.report}")

    # Exit code: 0 if no critical/high, 1 if any
    if results["by_severity"].get("CRITICAL", 0) > 0 or results["by_severity"].get("HIGH", 0) > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
