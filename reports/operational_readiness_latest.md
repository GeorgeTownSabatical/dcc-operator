# DCCO Operational Readiness Report

Mathematical Authority: See ../MATH.md.

## Summary

- `required_domain_count`: `15`
- `standard_count`: `12`
- `adapter_count`: `7`
- `covered_domain_count`: `15`
- `domains_at_target`: `0`
- `domains_below_target`: `15`
- `readiness_claim`: `in_progress`

## Domain Readiness

| Domain | Current | Target | Gap | Mean Evidence Score | Evidence |
| --- | --- | --- | ---: | ---: | --- |
| `ai_high_density` | `L1` | `L5` | 4 | 86.091 | otel-core, qso-readiness |
| `compliance` | `L1` | `L4` | 3 | 81.667 | terraform-plan |
| `compute` | `L1` | `L5` | 4 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `cooling` | `L1` | `L5` | 4 | 98.572 | facility-bms, redfish-hardware |
| `disaster_recovery` | `L1` | `L5` | 4 | 39.781 | market-exchange, qso-readiness |
| `energy` | `L1` | `L4` | 3 | 67.183 | facility-bms, sustainability-xue |
| `facility` | `L1` | `L5` | 4 | 73.572 | facility-bms, terraform-plan |
| `finance` | `L1` | `L4` | 3 | 65.278 | market-exchange, sustainability-xue |
| `market` | `L1` | `L4` | 3 | 61.667 | market-exchange |
| `network` | `L1` | `L5` | 4 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `power` | `L1` | `L5` | 4 | 98.572 | facility-bms, redfish-hardware |
| `qso` | `L1` | `L4` | 3 | 17.895 | qso-readiness |
| `security` | `L1` | `L5` | 4 | 117.977 | otel-core, terraform-plan |
| `storage` | `L1` | `L5` | 4 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `sustainability` | `L1` | `L4` | 3 | 65.278 | market-exchange, sustainability-xue |

## Adapter Scores

| Adapter | Level | Authority | Mean Risk-Adjusted Score | Domains |
| --- | --- | --- | ---: | --- |
| `facility-bms` | `L1` | `observe` | 65.476 | cooling, energy, facility, power |
| `market-exchange` | `L1` | `simulate` | 61.667 | disaster_recovery, finance, market, sustainability |
| `otel-core` | `L1` | `observe` | 154.286 | ai_high_density, compute, network, security, storage |
| `qso-readiness` | `L1` | `simulate` | 17.895 | ai_high_density, disaster_recovery, qso |
| `redfish-hardware` | `L1` | `observe` | 131.667 | compute, cooling, network, power, storage |
| `sustainability-xue` | `L1` | `observe` | 68.889 | energy, finance, sustainability |
| `terraform-plan` | `L2` | `simulate` | 81.667 | compliance, compute, facility, network, security, storage |

## Remaining Target Gaps

- `ai_high_density`
- `compliance`
- `compute`
- `cooling`
- `disaster_recovery`
- `energy`
- `facility`
- `finance`
- `market`
- `network`
- `power`
- `qso`
- `security`
- `storage`
- `sustainability`
