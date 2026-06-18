# Operations Model

Mathematical Authority: See ../../MATH.md.

Operations follow staged modes: observe, simulate, approve, deploy, verify, repair, and dissolve.

Operational readiness levels are defined in [OPERATIONAL_STATUS_MODEL.md](OPERATIONAL_STATUS_MODEL.md). No domain should be called operational without evidence for telemetry freshness, score coverage, simulation, policy gates, rollback, and dissolution.

Sandbox staged-operation evidence is tracked in ../../data/staged_operations.json. Staged operations must cover stage, deploy, verify, repair, and retire before a domain can claim `L5`.
