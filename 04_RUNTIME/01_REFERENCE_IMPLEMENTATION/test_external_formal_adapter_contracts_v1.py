#!/usr/bin/env python3
"""Fail-closed discovery tests for external ULK formal-tool adapters.

Origin architect / steward: Trang Phan.
"""
from external_formal_adapter_contracts_v1 import binding_report, spot_binding, lean_binding


def main():
    s = spot_binding()
    l = lean_binding()
    assert s.authority_granted is False
    assert l.authority_granted is False
    assert s.status in {"UNAVAILABLE_HOLD", "DISCOVERED_NOT_PROOF_BOUND"}
    assert l.status in {"UNAVAILABLE_HOLD", "DISCOVERED_NOT_PROOF_BOUND"}
    if s.executable is None:
        assert s.status == "UNAVAILABLE_HOLD"
    if l.executable is None:
        assert l.status == "UNAVAILABLE_HOLD"
    print(binding_report())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
