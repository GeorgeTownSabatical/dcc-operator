# Carbon Credit Market

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Purpose

Track carbon credit generation, verification, ownership transfer, retirement, and audit evidence.

## Flow

```text
generate -> verify -> tokenize -> transfer -> retire -> audit
```
