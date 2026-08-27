# Source Structure

> Part of the **[Solution Structure](README.md)**.

## Purpose

Source structure defines how implementation projects, modules and packages are organised.

It should make architectural boundaries, responsibilities and dependencies visible.

## Guidance

Source structure should follow the architecture rather than fight it.

A reader should be able to inspect the source layout and understand the major parts of the system.

### Align with Architecture

The source layout should reflect architectural decisions and boundaries.

Layers, modules, contexts, applications or services should be organised consistently with the selected architectural style.

Clean Architecture responsibilities are logical responsibilities. They remain relevant whether the approved physical organisation is layer-oriented, capability-first, service-oriented or another justified form.

The approved Architecture determines how those responsibilities map to projects, assemblies, packages, modules and folders. Engineering must follow that mapping and should raise Engineering Feedback when it is incomplete or impractical.

### Keep Responsibilities Clear

Projects and modules should have clear responsibilities.

Mixed responsibilities make dependency management, testing and maintenance harder.

Where Architecture selects capability-first modules, each module should represent a qualified enduring business capability or concept. Do not create modules for individual operations, workflows, entities or generic management groupings without an architectural rationale.

### Control Dependencies

The structure should make invalid dependencies difficult or obvious.

Core domain logic should not accidentally depend on infrastructure or presentation concerns unless the architecture deliberately allows it.

### Group by Meaning

Files should be grouped in ways that support understanding and change.

The best grouping depends on the architecture, but it should avoid scattering closely related behaviour unnecessarily.

### Organise Within Projects Deliberately

Projects should introduce folders where they clarify responsibility.

Do not copy the same folder pattern into every project when the project does not need it.

Folder names should describe meaningful areas such as capabilities, responsibilities, adapters, commands, persistence or views.

Avoid generic folders such as `Common`, `Shared`, `Misc` or `Utils` unless the responsibility is genuinely shared and clearly bounded.

### Avoid Premature Fragmentation

Too many projects or modules can create unnecessary overhead.

Structure should introduce boundaries when they improve clarity, ownership or maintainability.

## Key Takeaways

- Source structure should reflect architecture.
- Logical responsibilities do not prescribe physical projects or assemblies.
- The approved Architecture determines the physical source organisation.
- Responsibilities should be clear.
- Dependency direction should be intentional.
- Grouping should support understanding and change.
- Folder structure should clarify responsibility rather than mirror a generic template.
- Fragmentation should be justified.

## Related Reading

- [01 Repository Structure](01%20Repository%20Structure.md)
- [03 Test Structure](03%20Test%20Structure.md)

---

## Navigation

**Previous**

- [01 Repository Structure](01%20Repository%20Structure.md)

**Next**

- [03 Test Structure](03%20Test%20Structure.md)

**Book**

- [Solution Structure](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
