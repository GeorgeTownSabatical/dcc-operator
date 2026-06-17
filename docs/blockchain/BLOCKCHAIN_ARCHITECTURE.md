# Blockchain Architecture

Mathematical Authority: See ../../MATH.md.
Optionality Rule: Blockchain is enabled only when BC > 1.

Blockchain is an optional settlement subsystem, not a core DCCO dependency.
It is justified only when the blockchain score BC > 1 as defined in MATH.md.
Otherwise, DCCO must use conventional databases, event stores, and audit logs.

## Purpose

Provide auditable settlement for multi-organization exchanges where participants do not fully trust each other.

## Recommended Form

- Permissioned consortium chain
- Participants: data centers, utilities, carbon registries, cloud providers, customers, auditors
- Candidate stacks: Hyperledger Besu, Hyperledger Fabric, Tendermint-based chain, Substrate-based chain

## Non-Goals

- Internal scheduling
- Telemetry ingestion
- Terraform execution
- Low-latency optimization loops
