# AGENTS.md

Mathematical Authority: See [MATH.md](MATH.md).
Mission Authority: See [OPERATOR_CHARTER.md](OPERATOR_CHARTER.md).

## Agent Authority

Agents implement the DCCO objective. No agent may define a competing score, risk functional, or deployment boundary without referencing [MATH.md](MATH.md).

## Core Agent Loop

```text
Sense -> Interpret -> Decide -> Act -> Observe -> Adapt
```

Every action must close the loop with validation evidence.

## DCCO Objective Compliance

Agents maximize:

```text
AgentUtility = DeltaDCCO - Risk - CostOfChange
```

Agents must never optimize a local metric at the expense of global coherence.

## QSO Compatibility Requirement

All agents must be designed so future QSO Fabric integration is possible.

Agents should treat workloads, services, plans, policies, simulations, and infrastructure states as coherent sections that may be instantiated, transformed, repaired, or dissolved.

No agent may assume that a program is permanent.

No agent may assume that execution is only classical.

All agent outputs must preserve:

- state
- evidence
- provenance
- coherence score
- risk score
- repair path
- rollback path
- dissolution path

## Agent Output Contract

Every agent recommendation must include:

- objective
- current score
- proposed score
- `DeltaDCCO`
- risk score
- cost of change
- validation evidence
- rollback path
- dissolution path

## Approval and Policy Gates

Production changes require approval, policy validation, sandbox test, rollback path, audit log, secret isolation, and blast-radius control.

## Rollback and Dissolution Requirements

Agents must plan both rollback and dissolution. Rollback restores a prior state. Dissolution retires a temporary coherent section while preserving evidence and continuity.

## Forbidden Assumptions

- Programs are permanent.
- Execution is only classical.
- Local optimization is sufficient.
- Blockchain is mandatory.
- A high utilization score implies high DCCO.
