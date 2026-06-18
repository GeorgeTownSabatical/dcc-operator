#!/usr/bin/env python3
"""Validate DCCO policy gates for L4 governed readiness."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    "compute",
    "storage",
    "network",
    "facility",
    "power",
    "cooling",
    "energy",
    "sustainability",
    "security",
    "compliance",
    "finance",
    "market",
    "disaster_recovery",
    "ai_high_density",
    "qso",
}


def load_json(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main() -> None:
    gates = load_json("data/policy_gates.json")
    readiness = load_json("data/operational_readiness.json")
    required_controls = set(gates["required_controls"])
    if gates.get("mathematical_authority") != "MATH.md":
        raise SystemExit("policy gates must cite MATH.md")
    if not required_controls:
        raise SystemExit("policy gates must define required controls")

    covered: set[str] = set()
    seen: set[str] = set()
    for gate in gates["gates"]:
        gate_id = gate["gate_id"]
        if gate_id in seen:
            raise SystemExit(f"duplicate gate id: {gate_id}")
        seen.add(gate_id)
        domains = set(gate["domains"])
        if not domains or not domains.issubset(DOMAINS):
            raise SystemExit(f"{gate_id} has invalid domains")
        if gate["control_authority"] != "approve_required":
            raise SystemExit(f"{gate_id} must require approval")
        if not gate["hard_gate"]:
            raise SystemExit(f"{gate_id} must be a hard gate")
        if set(gate["required_controls"]) != required_controls:
            raise SystemExit(f"{gate_id} must include every required control")
        if not gate["failure_mode"].startswith("block "):
            raise SystemExit(f"{gate_id} failure mode must block unsafe action")
        for evidence_ref in gate["evidence_refs"]:
            if not (ROOT / evidence_ref).exists():
                raise SystemExit(f"{gate_id} missing evidence ref: {evidence_ref}")
        covered.update(domains)

    missing = DOMAINS - covered
    if missing:
        raise SystemExit(f"policy gates miss domains: {sorted(missing)}")

    for domain, item in readiness["domains"].items():
        if item["current_level"] in {"L4", "L5", "L6"} and domain not in covered:
            raise SystemExit(f"{domain} claims governed readiness without policy gate")

    print("policy gates: ok")


if __name__ == "__main__":
    main()
