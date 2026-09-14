#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

SCHEMA = "amos.interop.agent-manifest.v1"


def load_agents(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    agents_dir = root / "06_AGENTS"
    items: list[tuple[Path, dict[str, Any]]] = []
    if not agents_dir.exists():
        raise FileNotFoundError(f"missing agent directory: {agents_dir}")
    for path in sorted(agents_dir.rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError(f"invalid JSON: {path}: {exc}") from exc
        if isinstance(data, dict) and data.get("name"):
            items.append((path, data))
    return items


def validate_agent(path: Path, agent: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("name", "description", "version"):
        if not isinstance(agent.get(field), str) or not agent[field].strip():
            errors.append(f"{path}: missing/invalid {field}")
    capabilities = agent.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        errors.append(f"{path}: capabilities must be a non-empty list")
    else:
        seen: set[str] = set()
        for idx, cap in enumerate(capabilities):
            if not isinstance(cap, dict):
                errors.append(f"{path}: capability[{idx}] is not an object")
                continue
            name = cap.get("name")
            effect = cap.get("side_effect")
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{path}: capability[{idx}] missing stable name")
            elif name in seen:
                errors.append(f"{path}: duplicate capability name {name}")
            else:
                seen.add(name)
            if not isinstance(effect, str) or not effect.strip():
                errors.append(f"{path}: capability[{idx}] missing side_effect")
    return errors


def normalize(path: Path, root: Path, agent: dict[str, Any]) -> dict[str, Any]:
    caps = []
    for cap in agent.get("capabilities", []):
        if not isinstance(cap, dict):
            continue
        caps.append({
            "id": cap.get("name"),
            "description": cap.get("description", ""),
            "effect": cap.get("side_effect"),
        })
    governance = agent.get("governance") if isinstance(agent.get("governance"), dict) else {}
    lifecycle = agent.get("lifecycle") if isinstance(agent.get("lifecycle"), dict) else {}
    return {
        "schema": SCHEMA,
        "source": {
            "path": str(path.relative_to(root)),
            "content_hash": agent.get("content_hash"),
        },
        "identity": {
            "name": agent.get("name"),
            "display_name": agent.get("display_name", agent.get("name")),
            "description": agent.get("description"),
            "version": agent.get("version"),
            "origin_architect": agent.get("origin_architect", agent.get("author")),
        },
        "capabilities": caps,
        "bindings": {
            "skills": agent.get("depends_on_skills", []),
            "workflows": agent.get("depends_on_workflows", []),
        },
        "governance": {
            "risk_tier": governance.get("risk_tier"),
            "approval_mode": governance.get("approval_mode"),
            "promotion_state": governance.get("promotion_state"),
            "lifecycle_status": lifecycle.get("status"),
        },
    }


def project_a2a(manifest: dict[str, Any]) -> dict[str, Any]:
    ident = manifest["identity"]
    return {
        "projection": "A2A_CANDIDATE_NOT_CONFORMANT",
        "name": ident["display_name"],
        "description": ident["description"],
        "version": ident["version"],
        "skills": [
            {
                "id": cap["id"],
                "name": cap["id"],
                "description": cap["description"],
                "tags": [f"effect:{cap['effect']}"] if cap.get("effect") else [],
            }
            for cap in manifest["capabilities"]
        ],
        "amos": {
            "source": manifest["source"],
            "governance": manifest["governance"],
            "missing_for_conformance": [
                "service_endpoint",
                "transport_binding",
                "authentication_policy",
                "runtime_handler",
                "protocol_schema_validation",
            ],
        },
    }


def project_mcp(manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "projection": "MCP_CANDIDATE_NOT_CALLABLE",
        "server": manifest["identity"]["name"],
        "tools": [
            {
                "name": cap["id"],
                "description": cap["description"],
                "effect": cap["effect"],
                "inputSchema": None,
                "outputSchema": None,
                "executable_binding": None,
            }
            for cap in manifest["capabilities"]
        ],
        "amos": {
            "source": manifest["source"],
            "governance": manifest["governance"],
            "missing_for_activation": [
                "typed_input_schema",
                "typed_output_schema",
                "executable_handler",
                "authority_gate",
                "transport_validation",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--format",
        choices=("manifest", "a2a-candidate", "mcp-candidate"),
        default="manifest",
    )
    parser.add_argument("--output")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    try:
        agents = load_agents(root)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 2

    all_errors: list[str] = []
    names: set[str] = set()
    manifests: list[dict[str, Any]] = []
    for path, agent in agents:
        errors = validate_agent(path, agent)
        name = agent.get("name")
        if isinstance(name, str):
            if name in names:
                errors.append(f"{path}: duplicate agent identity {name}")
            names.add(name)
        all_errors.extend(errors)
        if not errors:
            manifests.append(normalize(path, root, agent))

    if all_errors:
        for error in all_errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1

    if args.check:
        print(f"PASS agents={len(manifests)} schema={SCHEMA}")
        return 0

    if args.format == "a2a-candidate":
        payload: Any = [project_a2a(item) for item in manifests]
    elif args.format == "mcp-candidate":
        payload = [project_mcp(item) for item in manifests]
    else:
        payload = manifests

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
