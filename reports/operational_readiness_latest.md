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
| `ai_high_density` | `L3` | `L5` | 2 | 86.091 | otel-core, qso-readiness |
| `compliance` | `L3` | `L4` | 1 | 81.667 | terraform-plan |
| `compute` | `L3` | `L5` | 2 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `cooling` | `L3` | `L5` | 2 | 98.572 | facility-bms, redfish-hardware |
| `disaster_recovery` | `L3` | `L5` | 2 | 39.781 | market-exchange, qso-readiness |
| `energy` | `L3` | `L4` | 1 | 67.183 | facility-bms, sustainability-xue |
| `facility` | `L3` | `L5` | 2 | 73.572 | facility-bms, terraform-plan |
| `finance` | `L3` | `L4` | 1 | 65.278 | market-exchange, sustainability-xue |
| `market` | `L3` | `L4` | 1 | 61.667 | market-exchange |
| `network` | `L3` | `L5` | 2 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `power` | `L3` | `L5` | 2 | 98.572 | facility-bms, redfish-hardware |
| `qso` | `L3` | `L4` | 1 | 17.895 | qso-readiness |
| `security` | `L3` | `L5` | 2 | 117.977 | otel-core, terraform-plan |
| `storage` | `L3` | `L5` | 2 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `sustainability` | `L3` | `L4` | 1 | 65.278 | market-exchange, sustainability-xue |

## Adapter Scores

| Adapter | Level | Authority | Mean Risk-Adjusted Score | Domains |
| --- | --- | --- | ---: | --- |
| `facility-bms` | `L2` | `observe` | 65.476 | cooling, energy, facility, power |
| `market-exchange` | `L3` | `simulate` | 61.667 | disaster_recovery, finance, market, sustainability |
| `otel-core` | `L2` | `observe` | 154.286 | ai_high_density, compute, network, security, storage |
| `qso-readiness` | `L3` | `simulate` | 17.895 | ai_high_density, disaster_recovery, qso |
| `redfish-hardware` | `L2` | `observe` | 131.667 | compute, cooling, network, power, storage |
| `sustainability-xue` | `L2` | `observe` | 68.889 | energy, finance, sustainability |
| `terraform-plan` | `L3` | `simulate` | 81.667 | compliance, compute, facility, network, security, storage |

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
