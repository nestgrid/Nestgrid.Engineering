# Domain Services

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Domain services model domain behaviour that does not naturally belong to a single entity, value object or aggregate.

They help keep domain logic explicit without forcing behaviour into the wrong concept.

## Guidance

Domain services should represent meaningful domain operations, not general application coordination or infrastructure work.

They are useful when behaviour involves multiple domain concepts or expresses a domain decision that has no natural owner.

### Use for Domain Behaviour

A domain service should contain behaviour that belongs to the domain model.

It should not become a place for application workflow, persistence, messaging or technical orchestration.

### Avoid Anemic Models

Domain services should not take behaviour away from entities or aggregates that naturally own it.

If behaviour clearly belongs to a domain object, it should usually stay there.

### Name by Domain Meaning

Domain services should be named after the domain operation or responsibility they represent.

Technical names can hide business meaning and make the model harder to discuss with domain experts.

### Keep Services Focused

A domain service should have a clear and narrow responsibility.

Broad services can become procedural containers that weaken the domain model.

### Validate with Domain Experts

If a domain service represents important business behaviour, domain experts should recognise the operation it performs.

If they cannot explain it, the model may need refinement.

## Key Takeaways

- Domain services represent domain behaviour without a natural object owner.
- They should not be used for technical orchestration.
- Behaviour should stay inside entities or aggregates when it naturally belongs there.
- Domain services should be focused and named by domain meaning.
- Important services should be understandable to domain experts.

## Related Reading

- [03 Domain Concepts](03%20Domain%20Concepts.md)
- [05 Aggregates](05%20Aggregates.md)

---

## Navigation

**Previous**

- [07 Relationships](07%20Relationships.md)

**Next**

- [09 Domain Events](09%20Domain%20Events.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
