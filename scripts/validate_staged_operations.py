#!/usr/bin/env python3
"""Validate L5 staged operation evidence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main() -> None:
    staged = load_json("data/staged_operations.json")
    readiness = load_json("data/operational_readiness.json")
    simulations = load_json("data/simulation_scenarios.json")
    gates = load_json("data/policy_gates.json")
    required_lifecycle = set(staged["required_lifecycle"])
    scenario_ids = {item["scenario_id"] for item in simulations["scenarios"]}
    gate_ids = {item["gate_id"] for item in gates["gates"]}

    if staged.get("mathematical_authority") != "MATH.md":
        raise SystemExit("staged operations must cite MATH.md")
    if required_lifecycle != {"stage", "deploy", "verify", "repair", "retire"}:
        raise SystemExit("staged operations lifecycle is incomplete")

    covered: set[str] = set()
    seen: set[str] = set()
    for operation in staged["operations"]:
        oid = operation["operation_id"]
        if oid in seen:
            raise SystemExit(f"duplicate operation id: {oid}")
        seen.add(oid)
        if operation["mode"] != "sandbox":
            raise SystemExit(f"{oid} must remain sandbox until live authority exists")
        if not operation["approved"]:
            raise SystemExit(f"{oid} must have explicit approval flag")
        if set(operation["lifecycle"]) != required_lifecycle:
            raise SystemExit(f"{oid} lifecycle does not cover stage/deploy/verify/repair/retire")
        if not set(operation["scenario_refs"]).issubset(scenario_ids):
            raise SystemExit(f"{oid} references unknown simulation scenario")
        if not set(operation["policy_gate_refs"]).issubset(gate_ids):
            raise SystemExit(f"{oid} references unknown policy gate")
        for evidence_ref in operation["evidence_refs"]:
            if not (ROOT / evidence_ref).exists():
                raise SystemExit(f"{oid} missing evidence ref: {evidence_ref}")
        if not operation["verification"] or not operation["repair_path"] or not operation["retirement_path"]:
            raise SystemExit(f"{oid} must include verification, repair, and retirement evidence")
        covered.update(operation["domains"])

    for domain, item in readiness["domains"].items():
        if item["current_level"] in {"L5", "L6"} and domain not in covered:
            raise SystemExit(f"{domain} claims L5 without staged operation evidence")

    print("staged operations: ok")


if __name__ == "__main__":
    main()
