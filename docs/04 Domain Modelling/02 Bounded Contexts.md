# Bounded Contexts

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Bounded contexts define where a particular domain model and language apply.

They help teams manage complexity by preventing one model from being stretched across areas where concepts mean different things.

## Guidance

A bounded context is a boundary of meaning. Inside the boundary, terms, rules and models should be consistent. Outside the boundary, the same words may have different meanings.

Bounded contexts should be discovered from the domain before they are mapped to software boundaries.

### Define Model Boundaries

Teams should identify where a model is valid and where it stops being accurate.

This prevents concepts from being reused in contexts where their meaning changes.

### Respect Language Differences

Different bounded contexts may use different language for similar ideas.

These differences should be captured clearly instead of forcing artificial consistency across the entire domain.

### Avoid Premature System Design

Bounded contexts are not automatically services, projects or databases.

They inform architecture, but architecture should consider additional concerns such as deployment, ownership, scale and operational complexity.

### Clarify Integration Points

Where bounded contexts interact, teams should understand what information is exchanged and what meaning must be preserved.

Integration should respect the language and rules of each context.

### Keep Boundaries Reviewable

Bounded context boundaries may change as understanding improves.

Teams should revisit boundaries when language, ownership, rules or dependencies become clearer.

## Key Takeaways

- Bounded contexts define where a model and language apply.
- The same term may mean different things in different contexts.
- Bounded contexts inform architecture but are not automatically technical boundaries.
- Integration points should preserve meaning across contexts.
- Boundaries should evolve with understanding.

## Related Reading

- [01 Context Mapping](01%20Context%20Mapping.md)
- [07 Relationships](07%20Relationships.md)

---

## Navigation

**Previous**

- [01 Context Mapping](01%20Context%20Mapping.md)

**Next**

- [03 Domain Concepts](03%20Domain%20Concepts.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
