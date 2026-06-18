#!/usr/bin/env bash
set -euo pipefail

required=(
  README.md
  MATH.md
  DESIGN_DOC.md
  AGENTS.md
  COHERENCE_SCORE_MODEL.md
  OPERATOR_CHARTER.md
  ROADMAP.md
  docs/standards/INDUSTRY_STANDARDS_MATRIX.md
  docs/integrations/INTEGRATION_ARCHITECTURE.md
  docs/operations/OPERATIONAL_STATUS_MODEL.md
  docs/facility/EMERGING_FACILITY_NEEDS.md
  schemas/integration_envelope.schema.json
  data/standards_coverage.json
  data/integration_adapters.json
  data/operational_readiness.json
  data/simulation_scenarios.json
  data/policy_gates.json
  data/staged_operations.json
  reports/operational_readiness_latest.json
  reports/operational_readiness_latest.md
  reports/simulation_latest.json
  reports/simulation_latest.md
  scripts/validate_operational_manifests.py
  scripts/validate_policy_gates.py
  scripts/validate_staged_operations.py
  scripts/generate_readiness_report.py
  scripts/generate_simulation_report.py
  docs/blockchain/BLOCKCHAIN_ARCHITECTURE.md
  docs/blockchain/TOKENOMICS.md
  docs/blockchain/SMART_CONTRACT_MODEL.md
  docs/blockchain/CARBON_CREDIT_MARKET.md
  docs/blockchain/CAPACITY_MARKETPLACE.md
  docs/blockchain/SETTLEMENT_ENGINE.md
  docs/blockchain/CONSENSUS_MODEL.md
  docs/blockchain/INTEROPERABILITY.md
  docs/blockchain/AUDITABILITY_MODEL.md
  docs/blockchain/REGULATORY_COMPLIANCE.md
  docs/qso/QSO_FABRIC_EXTENSION.md
  docs/qso/QSO_FIELD_MODEL.md
  docs/qso/QSO_CLASSICAL_QUANTUM_BRIDGE.md
  docs/qso/QSO_PROGRAM_MATERIALIZATION.md
  docs/qso/QSO_PROGRAM_DISSOLUTION.md
  docs/qso/QSO_AGENT_PROTOCOL.md
  docs/qso/QSO_MEMORY_AND_REPAIR.md
  docs/qso/QSO_SECURITY_BOUNDARIES.md
  docs/qso/QSO_TELEMETRY_SCHEMA.md
  docs/qso/QSO_ROADMAP.md
)

for path in "${required[@]}"; do
  test -f "$path" || {
    echo "missing required document: $path" >&2
    exit 1
  }
done

echo "docs: ok"
