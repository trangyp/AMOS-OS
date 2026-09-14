#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCHEMA = "amos.agent-protocol-gateway-policy.v1"
ALLOWED_PROTOCOLS = {"mcp", "a2a", "llm"}
ALLOWED_TRANSPORTS = {"stdio", "http", "streamable-http", "sse", "a2a-http", "provider-native"}


def require_bool(obj: dict[str, Any], key: str, expected: bool, errors: list[str], prefix: str) -> None:
    value = obj.get(key)
    if value is not expected:
        errors.append(f"{prefix}.{key} must be {str(expected).lower()}")


def require_object(root: dict[str, Any], key: str, errors: list[str]) -> dict[str, Any]:
    value = root.get(key)
    if not isinstance(value, dict):
        errors.append(f"{key} must be an object")
        return {}
    return value


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema") != SCHEMA:
        errors.append(f"schema must equal {SCHEMA}")
    for field in ("gateway_id", "version", "status"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"{field} must be a non-empty string")

    protocols = data.get("protocols")
    if not isinstance(protocols, list) or not protocols:
        errors.append("protocols must be a non-empty list")
    elif not set(protocols).issubset(ALLOWED_PROTOCOLS):
        errors.append(f"protocols contain unsupported values: {sorted(set(protocols) - ALLOWED_PROTOCOLS)}")

    transports = data.get("transports")
    if not isinstance(transports, list) or not transports:
        errors.append("transports must be a non-empty list")
    elif not set(transports).issubset(ALLOWED_TRANSPORTS):
        errors.append(f"transports contain unsupported values: {sorted(set(transports) - ALLOWED_TRANSPORTS)}")

    discovery = require_object(data, "discovery", errors)
    require_bool(discovery, "static_first", True, errors, "discovery")
    require_bool(discovery, "stdio_launch_requires_explicit_authority", True, errors, "discovery")
    require_bool(discovery, "untrusted_stdio_requires_sandbox", True, errors, "discovery")
    require_bool(discovery, "auto_execute_untrusted_config", False, errors, "discovery")

    taint = require_object(data, "instruction_taint", errors)
    require_bool(taint, "tool_descriptions_untrusted", True, errors, "instruction_taint")
    require_bool(taint, "tool_outputs_untrusted", True, errors, "instruction_taint")
    require_bool(taint, "allow_instruction_override", False, errors, "instruction_taint")

    authority = require_object(data, "authority", errors)
    require_bool(authority, "gateway_is_commit_authority", False, errors, "authority")
    require_bool(authority, "consequential_calls_require_control_plane", True, errors, "authority")
    require_bool(authority, "capability_implies_authority", False, errors, "authority")

    observability = require_object(data, "observability", errors)
    require_bool(observability, "correlation_identity", True, errors, "observability")
    require_bool(observability, "redact_credentials", True, errors, "observability")
    require_bool(observability, "telemetry_is_authority", False, errors, "observability")

    if data.get("unknown_behavior") != "fail_closed":
        errors.append("unknown_behavior must equal fail_closed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AMOS agent protocol gateway policy")
    parser.add_argument("policy")
    args = parser.parse_args()
    path = Path(args.policy)
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR invalid policy JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(raw, dict):
        print("ERROR policy root must be an object", file=sys.stderr)
        return 2
    errors = validate(raw)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"GATEWAY_POLICY_FAIL errors={len(errors)}")
        return 1
    print("GATEWAY_POLICY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
