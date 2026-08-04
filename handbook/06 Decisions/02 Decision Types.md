# Decision Types

> Part of the **[Decisions](README.md)**.

## Purpose

Decision types classify decisions by the area they primarily affect.

They help teams organise records and avoid treating every important choice as an architectural decision.

## Guidance

Different decisions affect different parts of the lifecycle. Classifying them improves clarity and helps the right people participate in review.

The type should describe the primary nature of the decision, even when a decision has secondary effects elsewhere.

### Business Decisions

Business decisions affect commercial direction, operating model, policy, governance, risk appetite or organisational constraints.

They explain why the business chooses one direction over another.

### Product Decisions

Product decisions affect user experience, capability, scope, prioritisation, workflows or product behaviour.

They explain what the product should do and why that outcome matters.

### Technical Decisions

Technical decisions affect implementation approach, tooling, libraries, frameworks, code organisation or engineering practices.

They explain how engineers intend to build or maintain the solution.

### Architectural Decisions

Architectural decisions affect major structural choices, boundaries, quality attributes, data ownership, integrations, security or operations.

They explain how the solution is shaped at a system level.

### Use Clear Prefixes

Decision identifiers should make the type visible.

Recommended prefixes are `BDR` for business, `PDR` for product, `TDR` for technical and `ADR` for architecture.

## Key Takeaways

- Decision types improve organisation and review.
- Not every significant decision is architectural.
- Business, product, technical and architectural decisions should all be supported.
- The decision type should reflect the primary impact.
- Consistent prefixes make records easier to find.

## Related Reading

- [01 Decision Records](01%20Decision%20Records.md)
- [03 Decision Criteria](03%20Decision%20Criteria.md)

---

## Navigation

**Previous**

- [01 Decision Records](01%20Decision%20Records.md)

**Next**

- [03 Decision Criteria](03%20Decision%20Criteria.md)

**Book**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
