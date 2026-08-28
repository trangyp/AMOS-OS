#!/usr/bin/env python3
"""
AMOS Skill Observability Hook — Telemetry, audit trail, and metrics for skill
activations, tool calls, and session lifecycle.

Inspired by SOTA repos:
  - PackmindHub/skillsight: Self-hosted OTLP dashboard, skill activation events,
    status cascade (marketplace→plugin→skill), audit log with CSV export
  - JuanjoFuchs/claudefana: Grafana dashboard, 26 panels (cost, tokens, tools,
    cache, latency), OTLP ingestion
  - anhermon/claude-public/setup-telemetry: Hook events (SessionStart,
    PreToolUse, PostToolUse, SessionEnd), fail-silent hooks
  - xops-labs/claude-observability: LGTM stack (Loki/Grafana/Tempo/Mimir)
  - linxuhao/SkillFlow: Immutable audit trace, never deleted, keyed by step_id

Generates:
  1. JSONL audit trail — every skill activation, tool call, session event
  2. Metrics summary — activation counts, tool usage, duration, errors
  3. Status tracking — to_review/approved/removed/denied per skill
  4. CSV export for compliance and reporting

Usage:
  python3 scripts/skill_observability_hook.py --event session_start --skill amos-foo
  python3 scripts/skill_observability_hook.py --event pre_tool_use --skill amos-foo --tool Read
  python3 scripts/skill_observability_hook.py --event post_tool_use --skill amos-foo --tool Read --duration 1.2
  python3 scripts/skill_observability_hook.py --event session_end --skill amos-foo --duration 45.3
  python3 scripts/skill_observability_hook.py --metrics
  python3 scripts/skill_observability_hook.py --csv
  python3 scripts/skill_observability_hook.py --status amos-foo --set approved
"""

import argparse
import csv
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from collections import defaultdict


# ── Configuration ────────────────────────────────────────────────────────────

AUDIT_DIR = Path(os.environ.get("AMOS_AUDIT_DIR", ".amos-observability"))
AUDIT_TRAIL = AUDIT_DIR / "audit-trail.jsonl"
METRICS_FILE = AUDIT_DIR / "metrics.json"
STATUS_FILE = AUDIT_DIR / "skill-status.json"

# Status cascade: marketplace → plugin → skill (per skillsight pattern)
STATUS_FLOW = ["to_review", "approved", "removed", "denied"]


def ensure_audit_dir():
    """Ensure audit directory exists. Fail-silent (per setup-telemetry pattern)."""
    try:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass


# ── Audit Trail (per SkillFlow immutable trace pattern) ──────────────────────

def generate_step_id(event: str, skill: str, timestamp: float) -> str:
    """Generate deterministic step ID (per SkillFlow step_instance_id pattern)."""
    h = hashlib.sha256(f"{event}:{skill}:{timestamp}".encode()).hexdigest()[:16]
    return f"step_{h}"


def write_audit_event(event: dict) -> bool:
    """Append event to immutable audit trail. Fail-silent."""
    ensure_audit_dir()
    try:
        with open(AUDIT_TRAIL, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, sort_keys=True) + "\n")
        return True
    except Exception:
        return False


def record_event(event_type: str, skill: str, **kwargs) -> dict:
    """Record a telemetry event."""
    timestamp = time.time()
    event = {
        "step_id": generate_step_id(event_type, skill, timestamp),
        "event": event_type,
        "skill": skill,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(timestamp)),
        "epoch": timestamp,
        **kwargs,
    }
    write_audit_event(event)
    return event


# ── Metrics Aggregation (per claudefana dashboard pattern) ───────────────────

def aggregate_metrics() -> dict:
    """Aggregate metrics from audit trail."""
    if not AUDIT_TRAIL.exists():
        return {"total_events": 0, "skills": {}, "tools": {}, "events": {}}

    metrics = {
        "total_events": 0,
        "skills": defaultdict(lambda: {
            "activations": 0, "tool_calls": 0, "errors": 0,
            "total_duration": 0.0, "last_used": None,
        }),
        "tools": defaultdict(lambda: {"calls": 0, "errors": 0, "total_duration": 0.0}),
        "events": defaultdict(int),
        "session_count": 0,
        "error_count": 0,
    }

    with open(AUDIT_TRAIL, "r", encoding="utf-8") as f:
        for line in f:
            try:
                ev = json.loads(line.strip())
            except json.JSONDecodeError:
                continue

            metrics["total_events"] += 1
            metrics["events"][ev["event"]] += 1
            skill = ev.get("skill", "unknown")

            if ev["event"] == "session_start":
                metrics["skills"][skill]["activations"] += 1
                metrics["session_count"] += 1
            elif ev["event"] == "pre_tool_use":
                metrics["skills"][skill]["tool_calls"] += 1
                tool = ev.get("tool", "unknown")
                metrics["tools"][tool]["calls"] += 1
            elif ev["event"] == "post_tool_use":
                tool = ev.get("tool", "unknown")
                duration = ev.get("duration", 0)
                metrics["tools"][tool]["total_duration"] += duration
                if ev.get("error"):
                    metrics["tools"][tool]["errors"] += 1
                    metrics["skills"][skill]["errors"] += 1
                    metrics["error_count"] += 1
            elif ev["event"] == "session_end":
                duration = ev.get("duration", 0)
                metrics["skills"][skill]["total_duration"] += duration
                metrics["skills"][skill]["last_used"] = ev["timestamp"]

    # Convert defaultdicts to regular dicts
    metrics["skills"] = dict(metrics["skills"])
    metrics["tools"] = dict(metrics["tools"])
    metrics["events"] = dict(metrics["events"])
    return metrics


def save_metrics(metrics: dict):
    """Save metrics to file."""
    ensure_audit_dir()
    try:
        METRICS_FILE.write_text(json.dumps(metrics, indent=2, sort_keys=True), encoding="utf-8")
    except Exception:
        pass


# ── Status Tracking (per skillsight cascade pattern) ─────────────────────────

def load_status() -> dict:
    """Load skill status tracking."""
    if STATUS_FILE.exists():
        try:
            return json.loads(STATUS_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"skills": {}}


def save_status(status: dict):
    """Save skill status."""
    ensure_audit_dir()
    try:
        STATUS_FILE.write_text(json.dumps(status, indent=2, sort_keys=True), encoding="utf-8")
    except Exception:
        pass


def set_skill_status(skill: str, status: str) -> dict:
    """Set status for a skill."""
    if status not in STATUS_FLOW:
        raise ValueError(f"Invalid status: {status}. Must be one of {STATUS_FLOW}")
    st = load_status()
    st["skills"][skill] = {
        "status": status,
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    save_status(st)
    record_event("status_change", skill, status=status)
    return st["skills"][skill]


# ── CSV Export (per skillsight audit log pattern) ────────────────────────────

def export_csv(output_file: Path = None):
    """Export audit trail to CSV."""
    if not AUDIT_TRAIL.exists():
        print("No audit trail to export", file=sys.stderr)
        return

    out = output_file or (AUDIT_DIR / "audit-export.csv")
    fields = ["step_id", "timestamp", "event", "skill", "tool", "duration", "error", "status"]

    with open(AUDIT_TRAIL, "r", encoding="utf-8") as inf, \
         open(out, "w", encoding="utf-8", newline="") as outf:
        writer = csv.DictWriter(outf, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for line in inf:
            try:
                ev = json.loads(line.strip())
                writer.writerow(ev)
            except json.JSONDecodeError:
                continue
    print(f"Exported to {out}")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Observability Hook")
    parser.add_argument("--event", default=None,
                        choices=["session_start", "pre_tool_use", "post_tool_use", "session_end", "status_change"],
                        help="Record a telemetry event")
    parser.add_argument("--skill", default=None, help="Skill name")
    parser.add_argument("--tool", default=None, help="Tool name (for tool events)")
    parser.add_argument("--duration", type=float, default=None, help="Duration in seconds")
    parser.add_argument("--error", default=None, help="Error message if failed")
    parser.add_argument("--metrics", action="store_true", help="Show metrics summary")
    parser.add_argument("--csv", action="store_true", help="Export audit trail to CSV")
    parser.add_argument("--status", default=None, help="Show/set skill status")
    parser.add_argument("--set", default=None, choices=STATUS_FLOW, help="Set status value")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if args.metrics:
        m = aggregate_metrics()
        save_metrics(m)
        if args.json:
            json.dump(m, sys.stdout, indent=2, sort_keys=True)
            print()
        else:
            print(f"=== Skill Observability Metrics ===")
            print(f"  Total events:     {m['total_events']}")
            print(f"  Sessions:         {m['session_count']}")
            print(f"  Errors:           {m['error_count']}")
            print()
            print(f"  Event types:")
            for ev, count in sorted(m["events"].items(), key=lambda x: -x[1]):
                print(f"    {ev:20s}: {count}")
            print()
            if m["skills"]:
                print(f"  Top skills by activations:")
                sorted_skills = sorted(m["skills"].items(), key=lambda x: -x[1]["activations"])
                for name, data in sorted_skills[:10]:
                    print(f"    {name:40s}: {data['activations']} activations, {data['tool_calls']} tools, {data['errors']} errors")
            print()
            if m["tools"]:
                print(f"  Top tools by calls:")
                sorted_tools = sorted(m["tools"].items(), key=lambda x: -x[1]["calls"])
                for name, data in sorted_tools[:10]:
                    print(f"    {name:20s}: {data['calls']} calls, {data['errors']} errors, {data['total_duration']:.1f}s total")
        return

    if args.csv:
        export_csv()
        return

    if args.status and args.set:
        result = set_skill_status(args.status, args.set)
        if args.json:
            json.dump(result, sys.stdout, indent=2)
            print()
        else:
            print(f"Set {args.status} status to: {args.set}")
        return

    if args.status:
        st = load_status()
        skill_status = st["skills"].get(args.status, {"status": "to_review", "note": "not yet tracked"})
        if args.json:
            json.dump(skill_status, sys.stdout, indent=2)
            print()
        else:
            print(f"Status for {args.status}: {skill_status.get('status', 'unknown')}")
        return

    if args.event:
        kwargs = {}
        if args.tool:
            kwargs["tool"] = args.tool
        if args.duration is not None:
            kwargs["duration"] = args.duration
        if args.error:
            kwargs["error"] = args.error
        event = record_event(args.event, args.skill or "unknown", **kwargs)
        if args.json:
            json.dump(event, sys.stdout, indent=2)
            print()
        else:
            print(f"[{event['event']}] {event['skill']} — {event['step_id']}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
