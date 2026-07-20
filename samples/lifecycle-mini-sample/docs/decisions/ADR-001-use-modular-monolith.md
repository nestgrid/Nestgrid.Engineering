# ADR-001: Use Modular Monolith

> Decision record for **Architecture**.

## Status

Accepted

## Type

Architecture

## Date

2026-07-19

## Owners

- Sample maintainers

## Context

The sample product is a small internal task coordination tool.

Discovery identified a need for simple task visibility, clear ownership and low operational overhead. Domain modelling identified one initial bounded context: task coordination.

The architecture should preserve internal boundaries without introducing unnecessary runtime complexity.

## Decision

Use a modular monolith as the initial architectural style.

The solution should be deployed as one unit while keeping domain, application, infrastructure and interface concerns separated internally.

## Rationale

A modular monolith satisfies the sample's current needs with lower operational cost than a distributed architecture.

It supports clear internal boundaries, simple deployment, easier local development and a reasonable path to future separation if the domain grows.

## Alternatives Considered

### Single Unstructured Project

This would be simple to start but would not demonstrate architectural boundaries clearly.

It risks mixing domain logic, application flow and infrastructure concerns.

### Microservices

This would make runtime boundaries explicit but introduces deployment, monitoring, integration and operational complexity that the sample does not justify.

The domain is not yet complex enough to require independent deployable services.

## Consequences

The sample remains easy to understand and operate.

Internal boundaries must still be maintained deliberately because the runtime will not enforce service-level separation.

If future requirements introduce independent scale, ownership or deployment needs, the architecture may be revisited.

## Related Decisions

- None

## Related Documentation

- [Architecture](../handbooks/05%20Architecture.md)
- [Domain Modelling](../handbooks/04%20Domain%20Modelling.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../../../README.md)
