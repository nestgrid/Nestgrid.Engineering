# Invariants

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Invariants define business rules that must remain true for the domain model to be valid.

They help teams identify consistency boundaries, validation rules and behaviours that must be protected.

## Guidance

Invariants are central to domain modelling because they reveal what the business cannot allow to become inconsistent.

They should be discovered from business rules, workflows, policies, constraints and failure scenarios.

### Identify Rules That Must Always Hold

An invariant describes something that must remain true after every valid change.

If a rule can be temporarily inconsistent without harming the domain, it may not need to be protected within the same boundary.

### Connect Invariants to Aggregates

Aggregate boundaries should be influenced by invariants.

Objects that must change together to preserve a rule may belong inside the same aggregate.

### Make Rules Explicit

Important rules should be named, documented and tested.

Hidden rules are easily bypassed or duplicated inconsistently.

### Distinguish Validation from Invariants

Not all validation is an invariant.

Some validation checks input format or completeness. Invariants protect business correctness within the model.

### Revisit as Understanding Improves

Invariants may change when domain knowledge becomes clearer.

Teams should review them when business rules, priorities or boundaries change.

## Key Takeaways

- Invariants are rules that must remain true.
- They help reveal aggregate and consistency boundaries.
- Important rules should be explicit and testable.
- Input validation and domain invariants are related but not identical.
- Invariants should evolve with domain understanding.

## Related Reading

- [05 Aggregates](05%20Aggregates.md)
- [10 Model Validation](10%20Model%20Validation.md)

---

## Navigation

**Previous**

- [05 Aggregates](05%20Aggregates.md)

**Next**

- [07 Relationships](07%20Relationships.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
