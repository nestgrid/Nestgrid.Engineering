# Domain Concepts

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Domain concepts identify the meaningful things, behaviours and rules that exist within the business domain.

They provide the foundation for modelling entities, value objects, aggregates, events and services.

## Guidance

Domain concepts should come from discovery, language and stakeholder understanding. They should not be invented purely from database tables, screens or technical structures.

The goal is to understand what the business cares about and how those concepts behave.

### Identify Important Concepts

Teams should identify nouns, actions, rules and events that appear repeatedly in discovery conversations.

Important concepts usually affect decisions, workflows, responsibilities or outcomes.

### Understand Behaviour

A concept is more than data.

Teams should understand what a concept can do, what can happen to it and what rules govern its lifecycle.

### Avoid Data-Only Modelling

Domain modelling should not begin as a database design exercise.

Data matters, but the model should represent meaning and behaviour before persistence details.

### Use Shared Language

Concept names should align with the ubiquitous language of the relevant bounded context.

If the name of a concept is unclear, the underlying understanding is probably not stable enough yet.

### Refine Continuously

Initial concepts are often incomplete.

Teams should expect to merge, split, rename or remove concepts as domain understanding improves.

## Key Takeaways

- Domain concepts represent meaningful business ideas and behaviours.
- Concepts should come from discovery and shared language.
- A concept is more than stored data.
- Naming should align with the relevant bounded context.
- Concepts should be refined as understanding improves.

## Related Reading

- [04 Value Objects](04%20Value%20Objects.md)
- [05 Aggregates](05%20Aggregates.md)

---

## Navigation

**Previous**

- [02 Bounded Contexts](02%20Bounded%20Contexts.md)

**Next**

- [04 Value Objects](04%20Value%20Objects.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
