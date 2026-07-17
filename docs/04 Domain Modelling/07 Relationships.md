# Relationships

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Relationships describe how domain concepts depend on, refer to or interact with one another.

They help teams understand coupling, ownership, lifecycle and boundaries within the model.

## Guidance

Relationships should express meaningful domain connections, not only structural associations.

Understanding why concepts relate is more important than simply drawing lines between them.

### Understand Relationship Meaning

Teams should describe what a relationship means in business terms.

The model should make clear whether one concept owns, references, creates, changes, depends on or observes another.

### Consider Lifecycle

Some concepts are created, changed or removed together. Others have independent lifecycles.

Lifecycle differences can reveal aggregate boundaries and context boundaries.

### Avoid Accidental Coupling

Models should avoid unnecessary direct relationships.

If two concepts only need to know each other's identity or published events, a full object relationship may create avoidable coupling.

### Respect Context Boundaries

Relationships across bounded contexts should be treated carefully.

Concepts in different contexts may not share the same model, even when they appear related.

### Prefer Intentional Navigation

The ability to navigate from one concept to another should exist for a reason.

Convenient navigation can make models harder to maintain if it hides coupling or bypasses boundaries.

## Key Takeaways

- Relationships should express meaningful domain connections.
- Lifecycle differences help reveal boundaries.
- Not every association should become a direct object relationship.
- Cross-context relationships require care.
- Navigation should be intentional, not accidental.

## Related Reading

- [02 Bounded Contexts](02%20Bounded%20Contexts.md)
- [05 Aggregates](05%20Aggregates.md)

---

## Navigation

**Previous**

- [06 Invariants](06%20Invariants.md)

**Next**

- [08 Domain Services](08%20Domain%20Services.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
