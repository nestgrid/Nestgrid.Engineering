# Architectural Style

> Part of the **[Architecture](README.md)**.

## Purpose

Architectural style defines the overall structural approach used to organise the solution.

It provides guidance for how responsibilities, dependencies, boundaries and runtime behaviour should be arranged.

## Guidance

Architectural styles should be chosen intentionally based on drivers, quality attributes and constraints.

No style is universally correct. A style is useful when it supports the needs of the solution better than the alternatives.

### Choose for the Context

The chosen style should fit the domain, team, delivery model, operational needs and expected change.

Teams should avoid adopting a style only because it is popular or familiar.

### Understand Trade-offs

Every architectural style has costs.

Layered, modular monolith, microservice, event-driven, serverless and distributed styles each create different trade-offs in complexity, deployment, testing and operations.

### Keep the Style Coherent

Once a style is chosen, the solution should follow it consistently where practical.

Inconsistent structure makes systems harder to understand and maintain.

### Avoid Premature Distribution

Distributed architecture introduces operational and coordination complexity.

Teams should choose distribution when the benefits justify the cost, not merely to mirror domain boundaries.

### Document the Rationale

The reason for choosing an architectural style should be recorded.

Future engineers should understand why the style was selected and which trade-offs were accepted.

## Key Takeaways

- Architectural style should be chosen intentionally.
- There is no universally correct style.
- Every style has trade-offs.
- Consistency improves maintainability.
- Distribution should be justified by clear needs.
- The rationale should be recorded for future readers.

## Related Reading

- [01 Architectural Drivers](01%20Architectural%20Drivers.md)
- [04 Boundaries and Responsibilities](04%20Boundaries%20and%20Responsibilities.md)

---

## Navigation

**Previous**

- [02 Quality Attributes](02%20Quality%20Attributes.md)

**Next**

- [04 Boundaries and Responsibilities](04%20Boundaries%20and%20Responsibilities.md)

**Book**

- [Architecture](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
