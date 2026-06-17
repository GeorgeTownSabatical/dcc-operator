# Settlement Engine

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Responsibilities

- reserve assets
- settle payments
- retire credits
- record audit evidence
- expose reconciliation events

## Default Mode

Use append-only event stores unless `BC > 1`.
