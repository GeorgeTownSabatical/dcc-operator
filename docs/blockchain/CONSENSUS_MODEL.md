# Consensus Model

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Recommended Consensus

Use permissioned BFT or proof-of-authority consensus among identified institutions.

## Constraint

Consensus overhead must not reduce `BC` below 1.
