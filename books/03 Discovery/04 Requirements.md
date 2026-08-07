# Requirements

> Part of the **[Discovery](README.md)**.

## Purpose

Requirements capture what the solution must support, satisfy or respect in order to address the problem and achieve the desired outcomes.

They provide the bridge between discovery and later modelling, architecture, testing and delivery.

## Guidance

Requirements should express needs clearly without prematurely dictating implementation details.

Good requirements help teams reason about behaviour, rules, constraints and quality expectations while still leaving room for effective design.

### Capture Functional Needs

Functional requirements describe behaviours, workflows, rules and capabilities the solution must support.

They should be tied to stakeholder needs and domain understanding rather than isolated feature requests.

### Capture Quality Expectations

Quality requirements describe how well the solution must operate.

These may include reliability, performance, security, accessibility, usability, maintainability, auditability, availability and operability.

### Capture Operational Requirements

Operational requirements describe what must be true for the product to be delivered, consumed, installed, configured, upgraded, supported and validated in its target environment.

They are product requirements, not late deployment details.

Operational requirements should be proportionate to the product type.

Examples:

- A NuGet library may need package publication, semantic versioning, consumer guidance and package-consumption validation.
- A service may need installation, service registration, configuration, upgrade, uninstall and smoke-test expectations.
- A web or API application may need hosting, deployment, configuration, health checks, observability and rollback expectations.
- A mobile application may need signing, app-store distribution, platform compatibility, update and support expectations.

Capture operational requirements early so Architecture can design the operational model and Platform does not inherit surprises at the end of the lifecycle.

### Identify Business Rules

Business rules define required behaviour within the domain.

Rules should be made explicit because they often become central to domain models, validation, tests and decision records.

### Keep Requirements Testable

Requirements should be written so they can be validated.

If nobody can determine whether a requirement has been satisfied, it is likely too vague and needs refinement.

### Avoid Premature Design

Requirements should describe what is needed and why.

They should avoid prescribing technical implementation unless the technology itself is a genuine constraint or decision.

## Key Takeaways

- Requirements bridge discovery and delivery.
- Functional needs should be connected to stakeholder and domain understanding.
- Quality expectations should be captured early.
- Operational requirements should be captured early and treated as product requirements.
- Business rules should be explicit.
- Requirements should be testable.
- Requirements should avoid unnecessary implementation detail.

## Related Reading

- [02 Stakeholders](02%20Stakeholders.md)
- [05 Constraints and Risks](05%20Constraints%20and%20Risks.md)

---

## Navigation

**Previous**

- [03 Goals and Outcomes](03%20Goals%20and%20Outcomes.md)

**Next**

- [05 Constraints and Risks](05%20Constraints%20and%20Risks.md)

**Book**

- [Discovery](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
