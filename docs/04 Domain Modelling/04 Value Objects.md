# Value Objects

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Value objects model descriptive domain concepts that are defined by their values rather than by identity.

They help express meaning, protect invariants and reduce primitive or ambiguous representations in the model.

## Guidance

Value objects are useful when a concept has business meaning but does not need a unique identity.

They should make the domain model more expressive and safer by keeping related values and rules together.

### Model Meaningful Values

A value object should represent a meaningful concept, not just a technical wrapper.

Examples may include quantities, ranges, names, codes, periods, addresses or measurements when those concepts carry domain rules.

### Prefer Immutability

Value objects should usually be immutable.

If a value changes, it is normally clearer to replace the value object with a new value rather than mutate the existing one.

### Keep Rules Close

Validation and behaviour related to a value should live with the value object where practical.

This prevents the same rule from being repeated inconsistently across the system.

### Compare by Value

Two value objects are considered equal when their relevant values are equal.

They do not need separate identity when the domain does not care which instance was created.

### Avoid Overuse

Not every value needs its own object.

Value objects should be introduced when they improve clarity, correctness or maintainability.

## Key Takeaways

- Value objects are defined by their values, not identity.
- They should represent meaningful domain concepts.
- Immutability usually makes value objects safer.
- Related rules should stay close to the value.
- Value objects should improve clarity rather than add ceremony.

## Related Reading

- [03 Domain Concepts](03%20Domain%20Concepts.md)
- [06 Invariants](06%20Invariants.md)

---

## Navigation

**Previous**

- [03 Domain Concepts](03%20Domain%20Concepts.md)

**Next**

- [05 Aggregates](05%20Aggregates.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
