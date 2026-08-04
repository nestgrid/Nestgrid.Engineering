# Architectural Drivers

> Part of the **[Architecture](README.md)**.

## Purpose

Architectural drivers are the forces that shape the architecture of a solution.

They help engineers understand which requirements, constraints, risks and goals matter most when making architectural decisions.

## Guidance

Architecture should be driven by the problem, not by preference. Architectural drivers make the reasons behind design choices explicit.

Drivers usually come from discovery, domain modelling, constraints, quality expectations, stakeholder needs and operational realities.

### Identify Business Drivers

Business drivers explain why the solution matters.

They may include growth, cost reduction, risk reduction, compliance, user experience, operational efficiency or strategic flexibility.

### Identify Domain Drivers

Domain drivers come from the structure and complexity of the domain model.

Bounded contexts, aggregates, invariants, workflows and relationships can all influence architectural boundaries.

### Identify Technical Drivers

Technical drivers include platform expectations, existing systems, integration needs, data requirements, performance needs and delivery constraints.

These drivers should be captured clearly rather than assumed.

### Identify Operational Drivers

Operational drivers describe what the system needs in production.

Monitoring, supportability, deployment, resilience, recovery, observability and maintainability should influence the architecture early.

### Prioritise Drivers

Not all drivers have equal importance.

Teams should identify which drivers are most important so trade-offs can be made deliberately.

## Key Takeaways

- Architecture should be driven by explicit needs and constraints.
- Drivers may be business, domain, technical or operational.
- Domain modelling should influence architectural boundaries.
- Operational needs should be considered early.
- Prioritised drivers make trade-offs easier to explain.

## Related Reading

- [02 Quality Attributes](02%20Quality%20Attributes.md)
- [09 Architecture Validation](09%20Architecture%20Validation.md)

---

## Navigation

**Previous**

- [Architecture](README.md)

**Next**

- [02 Quality Attributes](02%20Quality%20Attributes.md)

**Book**

- [Architecture](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
