# Smart Contract Model

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Contract Families

- Carbon credit contract
- Capacity lease contract
- Energy contract
- SLA contract
- Disaster recovery reservation contract
- Renewable certificate contract
- Audit hash anchoring contract

## Required Fields

- asset id
- owner
- issuer
- verifier
- quantity
- expiration
- settlement terms
- audit evidence hash
- retirement status

## Settlement Guard

Contracts may execute only when the exchange layer is justified by `BC > 1`, the relevant asset has verifiable provenance, and the transaction improves or preserves global DCCO.
