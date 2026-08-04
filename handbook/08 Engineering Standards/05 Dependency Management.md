# Dependency Management

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Dependency management defines how code should depend on internal modules, external packages and infrastructure concerns.

Responsible dependency management protects maintainability, security and architectural integrity.

## Guidance

Dependencies should be introduced deliberately.

Every dependency adds capability, but it may also add risk, coupling, maintenance cost and operational complexity.

### Respect Architecture

Dependencies should follow the intended architecture.

Code should not bypass boundaries or introduce shortcuts that weaken the structure of the solution.

### Keep External Dependencies Justified

External packages should solve real problems.

Teams should consider maturity, maintenance, licensing, security, compatibility and replacement cost before adoption.

### Avoid Hidden Coupling

Dependencies should be visible and understandable.

Hidden coupling makes code harder to test, change and reason about.

### Limit Shared Abstractions

Shared abstractions should exist because they reduce real duplication or clarify design.

They should not be introduced only to make code appear more generic.

### Prefer Concrete Domain Services by Default

Domain services should be implemented as concrete classes by default.

Do not introduce interfaces solely to satisfy dependency injection, mocking or layering conventions.

Introduce abstractions only when multiple implementations are required, the service represents an architectural boundary or genuine substitutability exists.

Domain tests should exercise real Domain behaviour directly.

Application tests may substitute external ports and infrastructure dependencies.

### Consume Published Nestgrid Libraries

Internal Nestgrid products should consume published Nestgrid libraries through NuGet packages rather than project references.

Project references are acceptable during concurrent development of a library and its consumer.

Before completion, the consuming product should migrate back to the published package.

### Review Dependency Changes

Adding, removing or upgrading dependencies can affect security, behaviour and supportability.

Dependency changes should be reviewed with appropriate care.

## Key Takeaways

- Dependencies should be intentional.
- Dependency direction should respect architecture.
- External packages require justification.
- Hidden coupling should be avoided.
- Shared abstractions should solve real problems.
- Domain services should be concrete by default.
- Published Nestgrid libraries should be consumed through packages.
- Dependency changes should be reviewed carefully.

## Related Reading

- [Solution Structure](../07%20Solution%20Structure/README.md)
- [06 Code Review](06%20Code%20Review.md)

---

## Navigation

**Previous**

- [04 Error Handling](04%20Error%20Handling.md)

**Next**

- [06 Code Review](06%20Code%20Review.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
