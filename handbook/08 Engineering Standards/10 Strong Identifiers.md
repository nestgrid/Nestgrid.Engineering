# Strong Identifiers

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Strong identifier standards define how typed identifiers should protect domain integrity.

## Guidance

Strongly typed identifiers should prevent invalid identity values from entering the model.

Identifier wrappers should not simply expose primitive values without enforcing basic validity.

### Reject Empty Identifiers

Identifier types backed by `Guid` should reject `Guid.Empty` unless there is a deliberate and documented reason to allow it.

This applies consistently to domain entities, aggregate identifiers, member identifiers and workspace or tenant-scoped identifiers.

### Keep Identity Semantics Explicit

Composite identity, tenant identity and workspace-scoped identity should be represented clearly.

Do not rely on arbitrary query delegates or repository behaviour to preserve identity semantics silently.

### Validate at Boundaries

Invalid identifiers should be rejected early at API and Application boundaries.

Domain models should still protect themselves from invalid construction.

## Key Takeaways

- Strong identifiers should enforce validity.
- `Guid.Empty` should be rejected by default.
- Tenant and workspace identity semantics should be explicit.
- Boundary validation does not replace domain protection.

## Related Reading

- [Domain Concepts](../04%20Domain%20Modelling/03%20Domain%20Concepts.md)
- [Aggregates](../04%20Domain%20Modelling/05%20Aggregates.md)

---

## Navigation

**Previous**

- [09 Domain Events](09%20Domain%20Events.md)

**Next**

- [11 API Contracts](11%20API%20Contracts.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
