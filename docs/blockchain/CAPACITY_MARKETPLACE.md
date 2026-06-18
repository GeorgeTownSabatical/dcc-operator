# Capacity Marketplace

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Tradable Capacity

- compute
- accelerator
- energy
- cooling
- network
- storage
- disaster recovery

## Rule

Marketplace settlement must increase `Xi` and preserve positive `DeltaDCCO`.

## Reservation Flow

```text
publish capacity -> verify availability -> reserve -> meter utilization -> settle -> release or renew -> audit
```

Capacity marketplaces are intended for inter-organization exchange, emergency overflow, AI accelerator availability, storage locality, network corridors, cooling headroom, and disaster-recovery rights.
