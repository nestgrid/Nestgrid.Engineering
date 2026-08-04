# Quality Attributes

> Part of the **[Architecture](README.md)**.

## Purpose

Quality attributes describe how well a solution must behave beyond its functional requirements.

They shape architecture by defining expectations for reliability, security, performance, maintainability, scalability, usability and operability.

## Guidance

Quality attributes should be considered early because they often determine architectural trade-offs.

A system can meet its functional requirements and still fail if it is unreliable, insecure, slow, difficult to operate or impossible to maintain.

### Make Attributes Explicit

Quality expectations should be written down and discussed.

Terms such as fast, secure, scalable or reliable are too vague unless they are clarified in context.

Common quality attributes include:

- Availability
- Recoverability
- Survivability
- Security
- Maintainability
- Portability
- Observability
- Performance

### Connect Attributes to Outcomes

Quality attributes should support business and user outcomes.

For example, availability may matter because downtime affects revenue, trust, safety, compliance or operational continuity.

### Prioritise Attributes

Quality attributes can conflict with one another.

A solution optimised for maximum consistency may make different trade-offs from one optimised for availability or low latency.

### Design for Testability

Quality attributes should be verifiable where practical.

Teams should consider how reliability, performance, security and operability will be tested or observed.

### Revisit During Delivery

Quality needs may change as understanding improves.

Architecture should be reviewed when new constraints, risks or usage expectations emerge.

## Key Takeaways

- Quality attributes define how well the system must behave.
- Vague quality terms should be clarified.
- Quality attributes should support business and user outcomes.
- Attributes may conflict and require trade-offs.
- Important quality attributes should be testable or observable.

## Related Reading

- [01 Architectural Drivers](01%20Architectural%20Drivers.md)
- [08 Operational Architecture](08%20Operational%20Architecture.md)

---

## Navigation

**Previous**

- [01 Architectural Drivers](01%20Architectural%20Drivers.md)

**Next**

- [03 Architectural Style](03%20Architectural%20Style.md)

**Book**

- [Architecture](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
