# Operational Status Model

Mathematical Authority: See ../../MATH.md.

## Purpose

Full-spectrum operational status means DCCO can observe, score, simulate, recommend, gate, deploy, verify, repair, and dissolve capabilities across the complete data-center and facility operating surface.

It is not a marketing label. It is an evidence-backed maturity state.

## Status Levels

| Level | Name | Meaning |
| --- | --- | --- |
| `L0` | Contracted | Root math, agent, charter, and safety contracts exist. |
| `L1` | Observable | Telemetry adapters emit canonical integration envelopes. |
| `L2` | Scored | DCCO terms are computed with confidence, freshness, and evidence. |
| `L3` | Simulated | Proposed changes produce replayable before/after DCCO estimates. |
| `L4` | Governed | Policy gates, approval, rollback, and dissolution are enforced. |
| `L5` | Operational | Approved plans can be staged, deployed, verified, repaired, and retired. |
| `L6` | Federated | Multi-organization exchange or QSO-compatible execution is available under gates. |

## Full-Spectrum Definition

DCCO reaches full-spectrum operational status when these domains are at least `L4` and core domains are `L5`:

- compute
- storage
- network
- facilities
- power
- cooling
- energy
- sustainability
- security
- compliance
- finance and cost
- market exchange where justified
- disaster recovery
- AI/high-density workloads
- QSO future compatibility

## Readiness Evidence

Every operational-status claim must include:

- adapter inventory
- standards matrix coverage
- telemetry freshness
- scoring coverage
- simulation fixtures
- policy gate status
- approval model
- rollback and dissolution evidence
- validation command output
- known gaps

## Status Functional

Define:

```text
OperationalReadiness =
(Coverage + EvidenceQuality + SimulationDepth + GovernanceStrength)
/
(IntegrationRisk + TelemetryStaleness + PolicyGaps + UnknownDependencies)
```

Readiness improves only when coverage is backed by evidence. Unsupported claims increase `epsilon` and `Risk`.

## Promotion Rule

A domain may advance one level only when:

```text
DeltaDCCO > 0
Risk <= approved_risk_budget
EvidenceQuality >= evidence_threshold
```

Promotion must not skip validation gates.

## Full-Spectrum Gate

The operator may call itself full-spectrum only when:

- all required domains have named owners or owner classes
- all adapter permissions are explicit
- all production writes are approval-gated
- all standards mappings are documented
- all score terms cite evidence
- all simulations are replayable
- all rollback and dissolution paths are present
- unresolved gaps are visible in the roadmap
