#!/usr/bin/env python3
"""Generate deterministic DCCO simulation reports from scenario fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DENOMINATOR_FLOOR = 0.000001
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


def load_json(path: str) -> Any:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def q_score(terms: dict[str, float]) -> float:
    denominator = max(
        terms["R_nabla"] + terms["B"] + terms["epsilon"] + terms["C"],
        DENOMINATOR_FLOOR,
    )
    return (terms["Gamma"] + terms["Pi"]) / denominator


def evaluate_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    before_q = q_score(scenario["before"])
    after_q = q_score(scenario["after"])
    delta = after_q - before_q
    plan_score = delta - scenario["risk"] - scenario["migration_cost"]
    return {
        "scenario_id": scenario["scenario_id"],
        "name": scenario["name"],
        "domains": sorted(scenario["domains"]),
        "before_Q": round(before_q, 6),
        "after_Q": round(after_q, 6),
        "DeltaDCCO": round(delta, 6),
        "risk": scenario["risk"],
        "migration_cost": scenario["migration_cost"],
        "PlanScore": round(plan_score, 6),
        "favorable": plan_score > 0,
        "approval_required": scenario["approval_required"],
        "rollback_path": scenario["rollback_path"],
        "dissolution_path": scenario["dissolution_path"],
        "evidence_refs": scenario["evidence_refs"],
    }


def validate_scenarios(doc: dict[str, Any]) -> None:
    if doc.get("mathematical_authority") != "MATH.md":
        raise SystemExit("simulation scenarios must cite MATH.md")
    covered: set[str] = set()
    seen: set[str] = set()
    for scenario in doc["scenarios"]:
        sid = scenario["scenario_id"]
        if sid in seen:
            raise SystemExit(f"duplicate scenario id: {sid}")
        seen.add(sid)
        if not set(scenario["domains"]).issubset(DOMAINS):
            raise SystemExit(f"{sid} has unknown domain")
        covered.update(scenario["domains"])
        for key in ("before", "after"):
            terms = scenario[key]
            for term in ("Gamma", "Pi", "R_nabla", "B", "epsilon", "C"):
                if term not in terms or not isinstance(terms[term], (int, float)) or terms[term] < 0:
                    raise SystemExit(f"{sid} invalid {key}.{term}")
        if scenario["risk"] < 0 or scenario["migration_cost"] < 0:
            raise SystemExit(f"{sid} risk and migration_cost must be non-negative")
        if not scenario["approval_required"]:
            raise SystemExit(f"{sid} must require approval")
        for evidence_ref in scenario["evidence_refs"]:
            if not (ROOT / evidence_ref).exists():
                raise SystemExit(f"{sid} missing evidence ref: {evidence_ref}")
        if not scenario["rollback_path"] or not scenario["dissolution_path"]:
            raise SystemExit(f"{sid} must include rollback and dissolution paths")
    missing = DOMAINS - covered
    if missing:
        raise SystemExit(f"simulation scenarios miss domains: {sorted(missing)}")


def build_report() -> dict[str, Any]:
    doc = load_json("data/simulation_scenarios.json")
    validate_scenarios(doc)
    evaluations = [evaluate_scenario(scenario) for scenario in doc["scenarios"]]
    covered_domains = sorted({domain for item in evaluations for domain in item["domains"]})
    favorable_count = sum(1 for item in evaluations if item["favorable"])
    return {
        "version": "0.1",
        "mathematical_authority": "MATH.md",
        "generated_from": ["data/simulation_scenarios.json"],
        "summary": {
            "scenario_count": len(evaluations),
            "covered_domain_count": len(covered_domains),
            "favorable_scenario_count": favorable_count,
            "approval_required_count": sum(1 for item in evaluations if item["approval_required"]),
            "simulation_claim": "replayable_before_after_estimates",
        },
        "covered_domains": covered_domains,
        "scenarios": evaluations,
    }


def write_json(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# DCCO Simulation Report",
        "",
        "Mathematical Authority: See ../MATH.md.",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Scenarios", ""])
    lines.append("| Scenario | Domains | DeltaDCCO | Risk | Migration Cost | PlanScore | Favorable |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | --- |")
    for scenario in report["scenarios"]:
        domains = ", ".join(scenario["domains"])
        lines.append(
            f"| `{scenario['scenario_id']}` | {domains} | {scenario['DeltaDCCO']} | "
            f"{scenario['risk']} | {scenario['migration_cost']} | {scenario['PlanScore']} | "
            f"`{scenario['favorable']}` |"
        )
    lines.extend(["", "## Control Boundary", ""])
    lines.append("Every scenario requires human approval before production effect.")
    lines.append("Each scenario includes rollback and dissolution paths in the JSON report.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed reports differ")
    parser.add_argument("--json", default="reports/simulation_latest.json")
    parser.add_argument("--markdown", default="reports/simulation_latest.md")
    args = parser.parse_args()

    report = build_report()
    json_path = ROOT / args.json
    markdown_path = ROOT / args.markdown
    if args.check:
        expected_json = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if not json_path.exists() or json_path.read_text(encoding="utf-8") != expected_json:
            raise SystemExit(f"{args.json} is stale; run scripts/generate_simulation_report.py")
        temp_path = ROOT / ".tmp_simulation_check.md"
        write_markdown(report, temp_path)
        try:
            expected_markdown = temp_path.read_text(encoding="utf-8")
        finally:
            temp_path.unlink(missing_ok=True)
        if not markdown_path.exists() or markdown_path.read_text(encoding="utf-8") != expected_markdown:
            raise SystemExit(f"{args.markdown} is stale; run scripts/generate_simulation_report.py")
        print("simulation report: ok")
        return

    write_json(report, json_path)
    write_markdown(report, markdown_path)
    print(f"wrote {args.json}")
    print(f"wrote {args.markdown}")


if __name__ == "__main__":
    main()
