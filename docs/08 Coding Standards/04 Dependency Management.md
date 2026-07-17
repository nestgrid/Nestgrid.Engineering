# Dependency Management

> Part of the **[Coding Standards](README.md)**.

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

### Review Dependency Changes

Adding, removing or upgrading dependencies can affect security, behaviour and supportability.

Dependency changes should be reviewed with appropriate care.

## Key Takeaways

- Dependencies should be intentional.
- Dependency direction should respect architecture.
- External packages require justification.
- Hidden coupling should be avoided.
- Shared abstractions should solve real problems.
- Dependency changes should be reviewed carefully.

## Related Reading

- [Solution Structure](../07%20Solution%20Structure/README.md)
- [05 Code Review](05%20Code%20Review.md)

---

## Navigation

**Previous**

- [03 Error Handling](03%20Error%20Handling.md)

**Next**

- [05 Code Review](05%20Code%20Review.md)

**Book**

- [Coding Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
