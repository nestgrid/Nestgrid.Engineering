# Aggregates

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Aggregates group related domain objects that must be kept consistent together.

They define transactional consistency boundaries and protect important business rules.

## Guidance

An aggregate should represent a meaningful consistency boundary, not simply a convenient object graph.

Good aggregate design helps teams manage complexity by deciding what must change together and what can remain eventually consistent.

### Identify the Aggregate Root

An aggregate root is the entry point for accessing and changing the aggregate.

External code should interact with the aggregate through the root so that rules and invariants can be protected.

### Protect Consistency

Aggregates should enforce rules that must always be true within their boundary.

If a rule must be guaranteed immediately, it may belong inside the aggregate.

### Keep Aggregates Focused

Aggregates should be as small as the domain allows.

Large aggregates can become difficult to load, change, test and reason about.

### Reference Other Aggregates Carefully

Aggregates should usually reference other aggregates by identity rather than holding large object graphs.

This keeps boundaries clear and reduces accidental coupling.

### Let Boundaries Emerge

Aggregate boundaries should be discovered from invariants, behaviours and lifecycle rules.

They should not be chosen only from database relationships or screen layouts.

## Key Takeaways

- Aggregates define consistency boundaries.
- The aggregate root protects access and behaviour.
- Aggregates should enforce rules that must always hold inside the boundary.
- Smaller focused aggregates are usually easier to maintain.
- Aggregate boundaries should emerge from domain rules and behaviour.

## Related Reading

- [06 Invariants](06%20Invariants.md)
- [07 Relationships](07%20Relationships.md)

---

## Navigation

**Previous**

- [04 Value Objects](04%20Value%20Objects.md)

**Next**

- [06 Invariants](06%20Invariants.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
