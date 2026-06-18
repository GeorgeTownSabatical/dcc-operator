# Data Center Coherence Operator

Data Center Coherence Operator (DCCO) is a coherence-first operator for data center planning, scoring, simulation, orchestration, and agentic decision support.

The objective is not maximum utilization. The objective is to maximize coherent useful work while minimizing distortion, obstruction, noise, uncertainty, and operational cost.

## Root Contracts

- [MATH.md](MATH.md) is the mathematical authority for all scoring, optimization, simulation, planning, and agent decisions.
- [AGENTS.md](AGENTS.md) is the agent behavior and output contract.
- [OPERATOR_CHARTER.md](OPERATOR_CHARTER.md) is the mission, boundary, and safety contract.
- [DESIGN_DOC.md](DESIGN_DOC.md) describes the operator architecture.

## Optional Extensions

- Blockchain settlement is optional and justified only when the blockchain score `BC > 1`; see [docs/blockchain/README.md](docs/blockchain/README.md).
- QSO Fabric compatibility is a future-facing extension requirement: programs, plans, agents, and infrastructure states may be treated as temporary coherent sections; see [docs/qso/README.md](docs/qso/README.md).

## Validation

```bash
make validate
```

The validation suite checks root contracts, math references, blockchain optionality, QSO safety gates, and agent output requirements.
