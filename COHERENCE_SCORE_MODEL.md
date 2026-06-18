# Coherence Score Model

Mathematical Authority: See [MATH.md](MATH.md).

All local score models must preserve the DCCO objective: maximize coherent useful work while minimizing distortion, obstruction, noise, and cost.

## Score Inputs

- `Gamma`: global coherence
- `Pi`: productive output
- `R_nabla`: operational curvature
- `B`: topological obstruction
- `epsilon`: noise
- `C`: cost
- `Risk`: deployment risk

## Primary Score

```text
Q = (Gamma + Pi) / (R_nabla + B + epsilon + C)
```

Implementations must apply the denominator floor defined in [MATH.md](MATH.md). The generated readiness report computes `Q`, `EnterpriseScore`, and a risk-adjusted score for each fixture envelope.

## Change Score

```text
DeltaDCCO = DCCO_new - DCCO_current
```

## Plan Score

```text
PlanScore = DeltaDCCO - Risk - MigrationCost
```

## Extension Policy

Subsystems may specialize this score but may not redefine it. Specialized metrics must cite [MATH.md](MATH.md).

## Generated Evidence

The deterministic report generator at [scripts/generate_readiness_report.py](scripts/generate_readiness_report.py) reads the machine-readable manifests and fixture envelopes, then writes:

- [reports/operational_readiness_latest.json](reports/operational_readiness_latest.json)
- [reports/operational_readiness_latest.md](reports/operational_readiness_latest.md)

`make validate` checks that these reports are current.
