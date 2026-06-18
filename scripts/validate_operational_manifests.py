#!/usr/bin/env python3
"""Validate DCCO operational integration manifests using only stdlib."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEVELS = ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]
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
CONTROL_AUTHORITIES = {"observe", "recommend", "simulate", "stage", "approve_required"}
COHERENCE_TERMS = {"Gamma", "Pi", "R_nabla", "B", "epsilon", "C"}


def load_json(path: str) -> object:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def fail(message: str) -> None:
    print(f"operational manifests: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def parse_datetime(value: str, context: str) -> None:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail(f"{context} has invalid ISO-8601 datetime: {value}")


def validate_envelope(path: Path, adapter_id: str, standard_ids: set[str]) -> dict:
    envelope = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "adapter_id",
        "domain",
        "source_system",
        "standard_refs",
        "observed_at",
        "state",
        "evidence_refs",
        "provenance",
        "coherence_terms",
        "risk",
        "control_authority",
        "rollback_path",
        "dissolution_path",
    }
    missing = required - set(envelope)
    require(not missing, f"{path} missing required keys: {sorted(missing)}")
    require(envelope["adapter_id"] == adapter_id, f"{path} adapter_id does not match {adapter_id}")
    require(envelope["domain"] in DOMAINS, f"{path} has unknown domain {envelope['domain']}")
    require(envelope["standard_refs"], f"{path} must cite at least one standard reference")
    require(set(envelope["standard_refs"]).issubset(standard_ids), f"{path} cites unknown standard refs")
    parse_datetime(envelope["observed_at"], str(path))
    require(envelope["evidence_refs"], f"{path} must include evidence refs")
    for evidence_ref in envelope["evidence_refs"]:
        require((ROOT / evidence_ref).exists(), f"{path} evidence ref does not exist: {evidence_ref}")
    terms = envelope["coherence_terms"]
    require(COHERENCE_TERMS.issubset(terms), f"{path} missing DCCO coherence terms")
    for term in COHERENCE_TERMS:
        require(isinstance(terms[term], (int, float)), f"{path} term {term} must be numeric")
        require(terms[term] >= 0, f"{path} term {term} must be non-negative")
    require(isinstance(envelope["risk"], (int, float)), f"{path} risk must be numeric")
    require(envelope["risk"] >= 0, f"{path} risk must be non-negative")
    require(envelope["control_authority"] in CONTROL_AUTHORITIES, f"{path} invalid control authority")
    require(envelope["rollback_path"], f"{path} must include rollback path")
    require(envelope["dissolution_path"], f"{path} must include dissolution path")
    return envelope


def validate() -> None:
    standards = load_json("data/standards_coverage.json")
    adapters = load_json("data/integration_adapters.json")
    readiness = load_json("data/operational_readiness.json")

    for doc in (standards, adapters, readiness):
        require(isinstance(doc, dict), "manifest root must be an object")
        require(doc.get("mathematical_authority") == "MATH.md", "manifest must cite MATH.md")

    required_domains = set(standards["required_domains"])
    require(required_domains == DOMAINS, "required domains must match operational domain set")

    standard_ids = {item["id"] for item in standards["standards"]}
    require(len(standard_ids) == len(standards["standards"]), "standard ids must be unique")
    covered_by_standards: set[str] = set()
    for item in standards["standards"]:
        require(item["domains"], f"standard {item['id']} must cover domains")
        require(set(item["domains"]).issubset(DOMAINS), f"standard {item['id']} has unknown domain")
        require(item["url"], f"standard {item['id']} must include a source URL or repo path")
        require(item["dcc_terms"], f"standard {item['id']} must map to DCCO terms")
        require(item["evidence_required"], f"standard {item['id']} must name required evidence")
        covered_by_standards.update(item["domains"])
    require(required_domains.issubset(covered_by_standards), "standards coverage misses required domains")

    adapter_ids = {item["adapter_id"] for item in adapters["adapters"]}
    require(len(adapter_ids) == len(adapters["adapters"]), "adapter ids must be unique")
    covered_by_adapters: set[str] = set()
    fixture_adapter_ids: set[str] = set()
    for adapter in adapters["adapters"]:
        aid = adapter["adapter_id"]
        require(set(adapter["domains"]).issubset(DOMAINS), f"adapter {aid} has unknown domain")
        require(set(adapter["standard_refs"]).issubset(standard_ids), f"adapter {aid} cites unknown standard")
        require(adapter["control_authority"] in CONTROL_AUTHORITIES, f"adapter {aid} invalid control authority")
        require(adapter["status_level"] in LEVELS, f"adapter {aid} invalid status level")
        require(adapter["fixtures"], f"adapter {aid} must include fixtures")
        for fixture in adapter["fixtures"]:
            path = ROOT / fixture
            require(path.exists(), f"adapter {aid} fixture missing: {fixture}")
            envelope = validate_envelope(path, aid, standard_ids)
            require(envelope["domain"] in adapter["domains"], f"{fixture} domain not declared by adapter {aid}")
            fixture_adapter_ids.add(envelope["adapter_id"])
        covered_by_adapters.update(adapter["domains"])
    require(required_domains.issubset(covered_by_adapters), "adapter coverage misses required domains")
    require(adapter_ids == fixture_adapter_ids, "every adapter must have at least one valid fixture envelope")

    readiness_levels = readiness["status_levels"]
    require(readiness_levels == LEVELS, "readiness status levels must be canonical")
    domain_targets = readiness["domain_targets"]
    require(set(domain_targets) == required_domains, "readiness targets must cover every required domain")
    readiness_domains = readiness["domains"]
    require(set(readiness_domains) == required_domains, "readiness domains must cover every required domain")
    for domain, target_level in domain_targets.items():
        require(target_level in LEVELS, f"{domain} target level invalid")
        item = readiness_domains[domain]
        current_level = item["current_level"]
        require(current_level in LEVELS, f"{domain} current level invalid")
        require(LEVELS.index(current_level) <= LEVELS.index(target_level), f"{domain} current exceeds target")
        require(item["evidence"], f"{domain} must include evidence adapters")
        require(set(item["evidence"]).issubset(adapter_ids), f"{domain} cites unknown evidence adapter")
        require(item["gaps"], f"{domain} must list known gaps until target is reached")

    print("operational manifests: ok")


if __name__ == "__main__":
    validate()
