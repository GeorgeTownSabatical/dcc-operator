# DCCO Operational Readiness Report

Mathematical Authority: See ../MATH.md.

## Summary

- `required_domain_count`: `15`
- `standard_count`: `12`
- `adapter_count`: `7`
- `covered_domain_count`: `15`
- `domains_at_target`: `15`
- `domains_below_target`: `0`
- `readiness_claim`: `target_achieved`

## Domain Readiness

| Domain | Current | Target | Gap | Mean Evidence Score | Evidence |
| --- | --- | --- | ---: | ---: | --- |
| `ai_high_density` | `L5` | `L5` | 0 | 86.091 | otel-core, qso-readiness |
| `compliance` | `L4` | `L4` | 0 | 81.667 | terraform-plan |
| `compute` | `L5` | `L5` | 0 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `cooling` | `L5` | `L5` | 0 | 98.572 | facility-bms, redfish-hardware |
| `disaster_recovery` | `L5` | `L5` | 0 | 39.781 | market-exchange, qso-readiness |
| `energy` | `L4` | `L4` | 0 | 67.183 | facility-bms, sustainability-xue |
| `facility` | `L5` | `L5` | 0 | 73.572 | facility-bms, terraform-plan |
| `finance` | `L4` | `L4` | 0 | 65.278 | market-exchange, sustainability-xue |
| `market` | `L4` | `L4` | 0 | 61.667 | market-exchange |
| `network` | `L5` | `L5` | 0 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `power` | `L5` | `L5` | 0 | 98.572 | facility-bms, redfish-hardware |
| `qso` | `L4` | `L4` | 0 | 17.895 | qso-readiness |
| `security` | `L5` | `L5` | 0 | 117.977 | otel-core, terraform-plan |
| `storage` | `L5` | `L5` | 0 | 122.54 | otel-core, redfish-hardware, terraform-plan |
| `sustainability` | `L4` | `L4` | 0 | 65.278 | market-exchange, sustainability-xue |

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
- none
