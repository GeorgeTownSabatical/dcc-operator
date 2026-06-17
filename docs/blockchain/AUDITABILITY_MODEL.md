# Auditability Model

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Evidence

Every settlement event must preserve:

- timestamp
- actor
- asset id
- quantity
- verifier
- evidence hash
- source event reference
- retirement state
