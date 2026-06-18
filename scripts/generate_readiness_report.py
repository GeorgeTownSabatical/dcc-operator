#!/usr/bin/env python3
"""Generate deterministic DCCO readiness reports from fixture envelopes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEVELS = ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]
DENOMINATOR_FLOOR = 0.000001


def load_json(path: str) -> Any:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def score_envelope(envelope: dict[str, Any]) -> dict[str, float]:
    terms = envelope["coherence_terms"]
    denominator = max(
        terms["R_nabla"] + terms["B"] + terms["epsilon"] + terms["C"],
        DENOMINATOR_FLOOR,
    )
    q = (terms["Gamma"] + terms["Pi"]) / denominator
    enterprise_score = 100 * q
    risk_adjusted_score = max(enterprise_score - (100 * envelope["risk"]), 0)
    return {
        "Q": round(q, 6),
        "EnterpriseScore": round(enterprise_score, 3),
        "RiskAdjustedScore": round(risk_adjusted_score, 3),
    }


def level_gap(current: str, target: str) -> int:
    return LEVELS.index(target) - LEVELS.index(current)


def build_report() -> dict[str, Any]:
    standards = load_json("data/standards_coverage.json")
    adapters = load_json("data/integration_adapters.json")
    readiness = load_json("data/operational_readiness.json")

    adapter_by_id = {adapter["adapter_id"]: adapter for adapter in adapters["adapters"]}
    adapter_scores: dict[str, dict[str, Any]] = {}
    for adapter_id in sorted(adapter_by_id):
        adapter = adapter_by_id[adapter_id]
        scored_fixtures = []
        for fixture in sorted(adapter["fixtures"]):
            envelope = load_json(fixture)
            scored_fixtures.append(
                {
                    "fixture": fixture,
                    "domain": envelope["domain"],
                    "control_authority": envelope["control_authority"],
                    "score": score_envelope(envelope),
                }
            )
        risk_adjusted_scores = [item["score"]["RiskAdjustedScore"] for item in scored_fixtures]
        adapter_scores[adapter_id] = {
            "domains": sorted(adapter["domains"]),
            "status_level": adapter["status_level"],
            "control_authority": adapter["control_authority"],
            "fixtures": scored_fixtures,
            "mean_risk_adjusted_score": round(sum(risk_adjusted_scores) / len(risk_adjusted_scores), 3),
        }

    domains: dict[str, Any] = {}
    for domain in sorted(readiness["domains"]):
        item = readiness["domains"][domain]
        target = readiness["domain_targets"][domain]
        evidence = sorted(item["evidence"])
        evidence_scores = [adapter_scores[adapter]["mean_risk_adjusted_score"] for adapter in evidence]
        domains[domain] = {
            "current_level": item["current_level"],
            "target_level": target,
            "level_gap": level_gap(item["current_level"], target),
            "evidence_adapters": evidence,
            "mean_evidence_score": round(sum(evidence_scores) / len(evidence_scores), 3),
            "gaps": sorted(item["gaps"]),
        }

    required_domains = set(standards["required_domains"])
    standard_domain_coverage = {
        standard["id"]: sorted(standard["domains"])
        for standard in sorted(standards["standards"], key=lambda item: item["id"])
    }
    covered_domains = sorted(
        {
            domain
            for standard in standards["standards"]
            for domain in standard["domains"]
        }
    )
    target_gaps = [domain for domain, item in domains.items() if item["level_gap"] > 0]

    return {
        "version": "0.1",
        "mathematical_authority": "MATH.md",
        "generated_from": [
            "data/standards_coverage.json",
            "data/integration_adapters.json",
            "data/operational_readiness.json",
            "fixtures/integration_envelopes/*.json",
        ],
        "summary": {
            "required_domain_count": len(required_domains),
            "standard_count": len(standards["standards"]),
            "adapter_count": len(adapters["adapters"]),
            "covered_domain_count": len(covered_domains),
            "domains_at_target": len(domains) - len(target_gaps),
            "domains_below_target": len(target_gaps),
            "readiness_claim": "in_progress",
        },
        "standard_domain_coverage": standard_domain_coverage,
        "adapter_scores": adapter_scores,
        "domain_readiness": domains,
        "next_gaps": target_gaps,
    }


def write_json(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# DCCO Operational Readiness Report",
        "",
        "Mathematical Authority: See ../MATH.md.",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Domain Readiness", ""])
    lines.append("| Domain | Current | Target | Gap | Mean Evidence Score | Evidence |")
    lines.append("| --- | --- | --- | ---: | ---: | --- |")
    for domain, item in report["domain_readiness"].items():
        evidence = ", ".join(item["evidence_adapters"])
        lines.append(
            f"| `{domain}` | `{item['current_level']}` | `{item['target_level']}` | "
            f"{item['level_gap']} | {item['mean_evidence_score']} | {evidence} |"
        )
    lines.extend(["", "## Adapter Scores", ""])
    lines.append("| Adapter | Level | Authority | Mean Risk-Adjusted Score | Domains |")
    lines.append("| --- | --- | --- | ---: | --- |")
    for adapter_id, item in report["adapter_scores"].items():
        domains = ", ".join(item["domains"])
        lines.append(
            f"| `{adapter_id}` | `{item['status_level']}` | `{item['control_authority']}` | "
            f"{item['mean_risk_adjusted_score']} | {domains} |"
        )
    lines.extend(["", "## Remaining Target Gaps", ""])
    for domain in report["next_gaps"]:
        lines.append(f"- `{domain}`")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed reports differ")
    parser.add_argument("--json", default="reports/operational_readiness_latest.json")
    parser.add_argument("--markdown", default="reports/operational_readiness_latest.md")
    args = parser.parse_args()

    report = build_report()
    json_path = ROOT / args.json
    markdown_path = ROOT / args.markdown

    if args.check:
        expected_json = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if not json_path.exists() or json_path.read_text(encoding="utf-8") != expected_json:
            raise SystemExit(f"{args.json} is stale; run scripts/generate_readiness_report.py")
        temp_path = ROOT / ".tmp_operational_readiness_check.md"
        write_markdown(report, temp_path)
        try:
            expected_markdown = temp_path.read_text(encoding="utf-8")
        finally:
            temp_path.unlink(missing_ok=True)
        if not markdown_path.exists() or markdown_path.read_text(encoding="utf-8") != expected_markdown:
            raise SystemExit(f"{args.markdown} is stale; run scripts/generate_readiness_report.py")
        print("readiness report: ok")
        return

    write_json(report, json_path)
    write_markdown(report, markdown_path)
    print(f"wrote {args.json}")
    print(f"wrote {args.markdown}")


if __name__ == "__main__":
    main()
