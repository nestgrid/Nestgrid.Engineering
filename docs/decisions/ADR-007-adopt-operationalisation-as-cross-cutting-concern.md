# ADR-007: Adopt Operationalisation as Cross-Cutting Concern

> Decision record for **Architecture**.

## Status

Accepted

## Type

Architecture

## Date

2026-08-06

## Owners

- Nestgrid Engineering

## Context

The Nestgrid Engineering Operating System already defines Product, Architecture, Engineering, Quality, Security and Platform responsibilities.

As real products began moving through the lifecycle, operational packaging became visibly important. A product may be technically implemented but still fail its purpose if it cannot be delivered, consumed, installed, configured, upgraded, supported and validated in its target environment.

This concern applies beyond deployed services. It also applies to libraries, APIs, web applications, command-line tools, workers, mobile applications and other product types.

## Decision

Operationalisation is adopted as a cross-cutting engineering concern.

Operational Requirements will be captured during Discovery, shaped into an operational model during Architecture, implemented during Engineering, validated by Quality, assessed by Security and realised by Platform.

Platform owns final operationalisation and operational readiness, but Platform should not discover the operational strategy for the first time at the end of the lifecycle.

## Rationale

Operationalisation is necessary for a product to fulfil its intended purpose.

Treating it as a late deployment concern creates avoidable risk because installation, consumption, configuration, upgrade, support and validation needs can materially affect product requirements, architecture, implementation and testing.

Making it cross-cutting keeps the lifecycle product-agnostic while ensuring each role carries the right responsibility.

## Alternatives Considered

### Treat Operationalisation as Platform-Only

This was rejected because Platform would inherit unresolved product and architecture questions too late in the lifecycle.

### Create a Separate Operationalisation Role

This was rejected because the existing roles already cover the concern when their responsibilities are made explicit.

### Treat Operationalisation as Deployment Documentation Only

This was rejected because documentation alone does not ensure the product can be published, installed, consumed, configured, upgraded or validated.

## Consequences

Product Briefs should capture Operational Requirements where relevant.

Architecture Packs should define the operational model where it affects design.

Implementation Plans should explain how Engineering will implement the approved operational model.

Quality, Security and Platform artefacts should validate, secure and realise operationalisation proportionately to product type and risk.

## Related Decisions

- [ADR-003: Adopt Books and Workflows Structure](ADR-003-adopt-books-and-workflows-structure.md)
- [ADR-004: Adopt Role-Based Methodology](ADR-004-adopt-role-based-methodology.md)

## Related Documentation

- [Operationalisation](../../books/10%20Deployment/07%20Operationalisation.md)
- [Requirements](../../books/03%20Discovery/04%20Requirements.md)
- [Lifecycle Flow](../../books/15%20Engineering%20Workflow/03%20Lifecycle%20Flow.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
