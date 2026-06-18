# DCCO Simulation Report

Mathematical Authority: See ../MATH.md.

## Summary

- `scenario_count`: `7`
- `covered_domain_count`: `15`
- `favorable_scenario_count`: `6`
- `approval_required_count`: `7`
- `simulation_claim`: `replayable_before_after_estimates`

## Scenarios

| Scenario | Domains | DeltaDCCO | Risk | Migration Cost | PlanScore | Favorable |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `ai-density-placement-001` | ai_high_density, compute, network, storage | 0.506709 | 0.18 | 0.08 | 0.246709 | `True` |
| `storage-locality-001` | compute, network, storage | 0.457357 | 0.16 | 0.07 | 0.227357 | `True` |
| `thermal-coherence-001` | cooling, energy, facility, power | 0.331417 | 0.22 | 0.05 | 0.061417 | `True` |
| `microgrid-energy-001` | energy, finance, power, sustainability | 0.295875 | 0.2 | 0.06 | 0.035875 | `True` |
| `security-compliance-gate-001` | compliance, compute, network, security, storage | 0.327108 | 0.14 | 0.04 | 0.147108 | `True` |
| `capacity-market-dr-001` | disaster_recovery, finance, market, sustainability | 0.314624 | 0.24 | 0.05 | 0.024624 | `True` |
| `qso-sandbox-materialization-001` | ai_high_density, disaster_recovery, qso | 0.258242 | 0.32 | 0.04 | -0.101758 | `False` |

## Control Boundary

Every scenario requires human approval before production effect.
Each scenario includes rollback and dissolution paths in the JSON report.
