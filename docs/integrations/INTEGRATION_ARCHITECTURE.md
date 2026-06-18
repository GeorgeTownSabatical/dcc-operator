# Integration Architecture

Mathematical Authority: See ../../MATH.md.

## Purpose

DCCO integration is broad-spectrum by design. The operator must ingest, normalize, score, simulate, and act across IT, facilities, energy, sustainability, security, finance, and emerging infrastructure systems without making any single vendor or protocol the root of truth.

## Integration Planes

| Plane | Systems | Primary Signals | Control Mode |
| --- | --- | --- | --- |
| IT hardware | Redfish, SNMP, IPMI, vendor APIs | health, power, thermal, firmware, inventory | observe first; controlled action by approval |
| Compute platform | Kubernetes, VM managers, schedulers, batch systems | workload, utilization, placement, failure, cost | simulated plan before production |
| Network | switches, routers, SDN controllers, flow telemetry | traffic, hops, loss, latency, congestion | policy-gated change |
| Storage | arrays, object stores, file systems, backup systems | locality, IOPS, latency, durability, capacity | policy-gated change |
| Facilities | BMS, DCIM, BACnet, Modbus, OPC UA, SCADA gateways | cooling, power, environment, alarms, setpoints | guarded by facility authority |
| Energy | meters, UPS, generators, batteries, microgrids, utility feeds | power, quality, source, reserve, emissions | human approval for actuation |
| Sustainability | carbon registries, RECs, water meters, heat-reuse systems | PUE, WUE, CUE, renewable share, credits | settlement only when verified |
| Security | IAM, SIEM, vulnerability systems, physical access logs | identity, access, findings, events, exposure | hard gates and least privilege |
| Finance and market | billing, procurement, carbon and capacity exchanges | cost, contract, settlement, reservation | optional exchange layer if `BC > 1` |
| QSO future layer | QSO Fabric, QSO Field, hybrid bridges | coherent need, repair history, temporal continuity | sandbox and approval before materialization |

## Canonical Integration Envelope

Every adapter emits:

```json
{
  "adapter_id": "string",
  "domain": "compute|network|storage|facility|energy|security|market|qso",
  "source_system": "string",
  "standard_refs": ["string"],
  "observed_at": "ISO-8601",
  "state": {},
  "evidence_refs": [],
  "provenance": {},
  "coherence_terms": {
    "Gamma": 0.0,
    "Pi": 0.0,
    "R_nabla": 0.0,
    "B": 0.0,
    "epsilon": 0.0,
    "C": 0.0
  },
  "risk": 0.0,
  "control_authority": "observe|recommend|simulate|stage|approve_required",
  "rollback_path": [],
  "dissolution_path": []
}
```

## Adapter Requirements

Adapters must:

- preserve raw evidence references without storing secrets in logs
- normalize timestamps and units
- expose confidence and freshness
- declare read and write permissions separately
- degrade safely when telemetry is missing
- map local metrics into DCCO terms from ../../MATH.md
- produce replayable events for simulation

## Integration Priority

1. Observability and evidence: OpenTelemetry, Prometheus, syslog, event APIs.
2. Hardware and facility telemetry: Redfish, SNMP, BACnet, Modbus, DCIM/BMS.
3. Planning and orchestration: Terraform/OpenTofu, Kubernetes, GitOps, OpenAPI.
4. Energy and sustainability: meters, PUE/WUE/CUE, RECs, carbon registries.
5. Security and compliance: IAM, SIEM, policy-as-code, audit evidence.
6. Exchange layer: carbon, energy, capacity, and disaster-recovery settlement when `BC > 1`.
7. QSO-compatible execution: sandboxed materialization, repair, and dissolution.

## Control Boundary

DCCO may observe broadly, recommend carefully, simulate aggressively, and act conservatively.

Production-affecting writes require:

- human approval
- policy validation
- sandbox or staged evidence
- rollback path
- dissolution path
- audit log
- secret isolation
- blast-radius control
