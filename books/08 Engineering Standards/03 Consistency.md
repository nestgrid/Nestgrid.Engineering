# Consistency

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Consistency reduces unnecessary variation across the codebase.

It helps engineers move between areas of a solution without relearning avoidable differences in style, structure or behaviour.

## Guidance

Consistency should make code easier to understand and maintain.

Standards should be followed where they exist. Deviations should be intentional and justified by context.

### Follow Local Patterns

Existing patterns should be respected when they are clear and appropriate.

Introducing a different style without reason increases cognitive load.

### Standardise Formatting

Formatting should be automated where possible.

Engineers should not spend review time debating formatting that tooling can enforce.

### Use Consistent Naming

Similar concepts should be named consistently.

Naming should align with the language of the domain and the conventions of the platform.

### Keep Similar Code Similar

Repeated workflows, error handling, validation and integration patterns should be recognisable.

Unnecessary variation makes code harder to compare and maintain.

### Avoid Unnecessary Abstractions

Interfaces and abstractions should be introduced because the design needs them.

They should not be introduced only to satisfy dependency injection, mocking or layering habits.

### Deviation Requires Reason

Sometimes consistency should be broken to improve design.

When that happens, the reason should be clear from the context or documented where significant.

## Key Takeaways

- Consistency reduces cognitive load.
- Existing appropriate patterns should be followed.
- Formatting should be automated where possible.
- Similar concepts should be named consistently.
- Abstractions should exist for a clear design reason.
- Deviations should be intentional.

## Related Reading

- [02 Readability](02%20Readability.md)
- [05 Dependency Management](05%20Dependency%20Management.md)

---

## Navigation

**Previous**

- [02 Readability](02%20Readability.md)

**Next**

- [04 Error Handling](04%20Error%20Handling.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
