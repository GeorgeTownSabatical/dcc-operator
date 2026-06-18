# QSO Program Materialization

Mathematical Authority: See ../../MATH.md.
Agent Compatibility: See ../../AGENTS.md.
QSO programs are temporary coherent sections, not permanent artifacts.

No self-materializing program may deploy into production without human approval, policy validation, sandbox test, rollback path, audit log, secret isolation, and blast-radius control.

## Rule

```text
Need * Coherence > Cost + Risk
```

When this inequality holds, DCCO may propose a temporary coherent program section. Production deployment still requires approval.

## Required Gate

Materialization must produce a simulation result, coherence score, risk score, Terraform/Kubernetes/runtime plan, rollback path, dissolution path, and evidence envelope before approval.
