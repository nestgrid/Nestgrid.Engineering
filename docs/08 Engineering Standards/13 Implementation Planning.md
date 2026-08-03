# Implementation Planning

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Implementation planning defines what Engineering should make explicit before significant implementation begins.

It helps Engineering translate approved Architecture into source code, tests, tooling and handover artefacts without relying on hidden assumptions.

## Guidance

Engineering should not move from approval directly into code.

Before execution, Engineering should produce or update an Implementation Plan that explains how the approved Architecture will be realised.

### Align With the Technology Baseline

Engineering should confirm how the implementation aligns with the Nestgrid technology baseline.

Where the product follows the baseline, the plan should reference that baseline rather than re-justify standard choices from external release schedules or general platform preference.

Where the product deviates from the baseline, the reason should be recorded through the appropriate decision record.

### Define Implementation Principles

Engineering should record a short set of implementation principles for the product or initiative.

These principles should guide consistency during implementation.

Examples include:

- Keep the first release host-native.
- Prefer inspectable local storage.
- Preserve clear project responsibilities.
- Keep collectors isolated from persistence details.
- Fail safely and capture useful evidence.

Implementation principles should not replace Architecture principles. They translate approved Architecture into practical engineering constraints.

### Clarify Solution Structure Responsibilities

The Implementation Plan should explain the responsibility of each project, module or major folder.

This prevents names such as `Core`, `Host`, `Application`, `Infrastructure` or `Cli` from becoming ambiguous containers.

Each structure decision should make ownership, dependencies and change boundaries easier to understand.

### Plan Source and Test Organisation

Engineering should organise source and tests around meaningful responsibilities.

Avoid copying the same folder pattern into every project when it does not clarify responsibility.

Avoid broad buckets such as `Common`, `Shared`, `Misc` or `Utils`.

Tests should mirror meaningful source boundaries where practical, and shared test helpers should live in clearly named support areas such as `TestSupport`.

### Record Implementation Decisions

Engineering decisions that materially affect future implementation, operations, testing or maintenance should be recorded.

Small local decisions may be captured in the Implementation Plan.

Durable technical choices should be captured as decision records, usually `TDR`s.

Examples include:

- Selecting a persistence format.
- Choosing a runtime packaging approach.
- Introducing a significant dependency.
- Deviating from the standard technology baseline.
- Choosing a solution structure that future work must follow.

### Keep Repository Tooling Navigable

Where the project tooling supports it, Engineering should make important repository content visible to maintainers.

For .NET solutions, this may include adding root documentation, decision records and lifecycle artefacts to the solution as solution items when that improves IDE navigation.

The solution view should preserve meaningful filesystem structure where practical.

Do not distort the filesystem only to satisfy an IDE view.

## Key Takeaways

- Engineering should plan implementation before significant coding begins.
- Implementation Plans should align with the technology baseline.
- Implementation principles help preserve consistency during delivery.
- Solution structure responsibilities should be explicit.
- Source and tests should be organised around meaningful responsibilities.
- Durable implementation decisions should be recorded.
- Tooling and IDE visibility should support maintainability without distorting the repository.

## Related Reading

- [01 Technology Baseline](01%20Technology%20Baseline.md)
- [Source Structure](../07%20Solution%20Structure/02%20Source%20Structure.md)
- [Test Structure](../07%20Solution%20Structure/03%20Test%20Structure.md)
- [Naming and Organisation](../07%20Solution%20Structure/04%20Naming%20and%20Organisation.md)
- [Decisions](../06%20Decisions/README.md)
- [Implementation Plan Template](../../templates/artefacts/Implementation%20Plan.Template.md)

---

## Navigation

**Previous**

- [12 Database Migrations](12%20Database%20Migrations.md)

**Next**

- [Testing](../09%20Testing/README.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
