# Data Center Coherence Operator

Data Center Coherence Operator (DCCO) is a coherence-first operator for data center planning, scoring, simulation, orchestration, and agentic decision support.

The objective is not maximum utilization. The objective is to maximize coherent useful work while minimizing distortion, obstruction, noise, uncertainty, and operational cost.

## Root Contracts

- [MATH.md](MATH.md) is the mathematical authority for all scoring, optimization, simulation, planning, and agent decisions.
- [AGENTS.md](AGENTS.md) is the agent behavior and output contract.
- [OPERATOR_CHARTER.md](OPERATOR_CHARTER.md) is the mission, boundary, and safety contract.
- [DESIGN_DOC.md](DESIGN_DOC.md) describes the operator architecture.

## Operational Scope

- [docs/standards/INDUSTRY_STANDARDS_MATRIX.md](docs/standards/INDUSTRY_STANDARDS_MATRIX.md) maps data-center and facility domains to standards, evidence, and DCCO obligations.
- [docs/integrations/INTEGRATION_ARCHITECTURE.md](docs/integrations/INTEGRATION_ARCHITECTURE.md) defines the broad-spectrum adapter envelope for IT, facilities, energy, sustainability, security, market, and QSO systems.
- [docs/operations/OPERATIONAL_STATUS_MODEL.md](docs/operations/OPERATIONAL_STATUS_MODEL.md) defines what full-spectrum operational status means.
- [docs/facility/EMERGING_FACILITY_NEEDS.md](docs/facility/EMERGING_FACILITY_NEEDS.md) covers high-density, liquid-cooled, microgrid, heat-reuse, edge, and future hybrid facilities.

## Machine-Readable Evidence

- [data/standards_coverage.json](data/standards_coverage.json) maps required domains to external standards and DCCO extension contracts.
- [data/integration_adapters.json](data/integration_adapters.json) defines planned adapter coverage, permissions, fixtures, and readiness levels.
- [data/operational_readiness.json](data/operational_readiness.json) records current and target readiness by domain with explicit gaps.
- [schemas/integration_envelope.schema.json](schemas/integration_envelope.schema.json) defines the canonical adapter envelope.
- [fixtures/integration_envelopes](fixtures/integration_envelopes) contains replayable contract fixtures for representative integrations.
- [scripts/validate_operational_manifests.py](scripts/validate_operational_manifests.py) validates coverage, references, fixture envelopes, and readiness claims.
- [reports/operational_readiness_latest.md](reports/operational_readiness_latest.md) is the generated readiness report; `make validate` fails if it drifts from the manifests and fixtures.
- [data/simulation_scenarios.json](data/simulation_scenarios.json) defines replayable before/after DCCO simulations.
- [reports/simulation_latest.md](reports/simulation_latest.md) is the generated simulation report; `make validate` fails if it drifts from the scenario fixtures.

## Optional Extensions

- Blockchain settlement is optional and justified only when the blockchain score `BC > 1`; see [docs/blockchain/README.md](docs/blockchain/README.md).
- QSO Fabric compatibility is a future-facing extension requirement: programs, plans, agents, and infrastructure states may be treated as temporary coherent sections; see [docs/qso/README.md](docs/qso/README.md).

## Validation

```bash
make validate
```

The validation suite checks root contracts, math references, blockchain optionality, QSO safety gates, and agent output requirements.

Regenerate deterministic reports with:

```bash
make reports
```
