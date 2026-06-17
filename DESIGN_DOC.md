# Design Document

Mathematical Authority: See [MATH.md](MATH.md).
Agent Authority: See [AGENTS.md](AGENTS.md).

## System Overview

DCCO is a coherence-first operator for observing, scoring, simulating, planning, deploying, repairing, and retiring data center capabilities.

## Control Plane

The control plane coordinates agents, policy gates, orchestration requests, Terraform plans, simulation jobs, and approval workflows.

## Data Plane

The data plane ingests telemetry, topology, inventory, performance counters, thermal state, cost signals, event logs, and operator evidence.

## Coherence Engine

The coherence engine computes `Gamma`, `Pi`, `R_nabla`, `B`, `epsilon`, `C`, `Q`, `DeltaDCCO`, and `Risk` according to [MATH.md](MATH.md).

## Telemetry Pipeline

Telemetry is normalized into append-only events and projected into regional sections for sheaf-level agreement checks.

## Simulation Engine

The simulation engine estimates the DCCO impact of proposed plans before production deployment.

## Terraform Planner

Terraform plans are ranked by:

```text
PlanScore = DeltaDCCO - Risk - MigrationCost
```

## Agent Runtime

Agents observe need, propose changes, simulate impact, produce evidence, and request approval for production-affecting actions.

## Policy Gates

Policy gates enforce human approval, sandbox validation, rollback paths, audit logging, secret isolation, and blast-radius control.

## Event Store

DCCO uses a conventional append-only event store by default. Blockchain settlement is optional and justified only when `BC > 1`.

## Optional Exchange Layer

The exchange layer supports carbon credits, energy credits, compute capacity, storage capacity, network capacity, disaster recovery reservations, and settlement.

## QSO Compatibility Layer

The QSO compatibility layer treats programs as temporary coherent sections that can materialize, repair, and dissolve.

## Security Model

Security boundaries include secret isolation, least privilege, policy-as-code, signed artifacts, audit trails, and blast-radius controls.

## Deployment Model

DCCO must support dry-run, sandbox, staged, and approved production deployment modes.

## Failure Modes

- incoherent telemetry
- high curvature
- topological obstruction
- unbounded risk
- unsafe agent proposal
- blockchain overhead exceeding benefit
- QSO materialization without policy gate
