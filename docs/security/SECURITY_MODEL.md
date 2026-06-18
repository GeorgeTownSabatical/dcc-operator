# Security Model

Mathematical Authority: See ../../MATH.md.

DCCO security preserves evidence, provenance, policy validation, secret isolation, least privilege, audit logs, rollback paths, and blast-radius control.

Governed readiness depends on the machine-readable policy gates in ../../data/policy_gates.json. The validator at ../../scripts/validate_policy_gates.py requires every operational domain to be covered by hard approval gates with rollback and dissolution controls before a domain may claim `L4` or higher.
