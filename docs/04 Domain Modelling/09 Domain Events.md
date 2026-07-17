# Domain Events

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Domain events represent meaningful things that have happened within the domain.

They help teams model business change, communicate between parts of the model and capture facts that other processes may react to.

## Guidance

Domain events should describe completed facts in business language.

They are useful for understanding workflows, side effects, state changes, integration needs and eventual consistency.

### Name Events as Past Facts

Events should describe something that has already happened.

Names should use domain language and make the business meaning clear.

### Capture Meaningful Change

Not every state change requires a domain event.

Events should represent changes that matter to the domain, other processes or future decisions.

### Support Decoupling

Domain events can reduce direct coupling between behaviours.

One part of the model can record that something happened without knowing every reaction that may follow.

### Respect Boundaries

Events crossing bounded contexts should be designed carefully.

The receiving context may need a translated or integration-specific representation rather than the internal event of another context.

### Keep Events Focused

Events should contain enough information to describe the fact, but not become large data transfer objects for unrelated needs.

The event should remain understandable and stable.

## Key Takeaways

- Domain events describe meaningful things that have happened.
- Event names should use past-tense business language.
- Events should represent changes that matter.
- Events can reduce coupling between behaviours.
- Cross-context events may require translation.
- Events should remain focused and understandable.

## Related Reading

- [02 Bounded Contexts](02%20Bounded%20Contexts.md)
- [08 Domain Services](08%20Domain%20Services.md)

---

## Navigation

**Previous**

- [08 Domain Services](08%20Domain%20Services.md)

**Next**

- [10 Model Validation](10%20Model%20Validation.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
