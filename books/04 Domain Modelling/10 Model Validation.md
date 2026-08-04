# Model Validation

> Part of the **[Domain Modelling](README.md)**.

## Purpose

Model validation checks whether the domain model accurately reflects the business understanding it is intended to represent.

It helps teams discover gaps, incorrect assumptions and unclear boundaries before architecture and implementation begin.

## Guidance

A domain model should be validated through conversation, examples and scenarios.

The model is successful when it helps domain experts and engineers reason about the same problem using shared language.

### Review with Domain Experts

Domain experts should be able to recognise the concepts, language and rules in the model.

If the model cannot be discussed with domain experts, it may be too technical or misaligned.

### Test with Scenarios

Scenarios help reveal whether the model handles real business situations.

Teams should walk through common, important and exceptional cases to test the model's behaviour.

### Challenge Boundaries

Boundaries should be reviewed against language, ownership, invariants, relationships and lifecycle.

If a boundary creates confusion or repeated exceptions, it may need to be refined.

### Look for Missing Rules

Unclear or missing rules often appear when scenarios reach edge cases.

These discoveries should feed back into requirements, glossary, decisions and model updates.

### Keep the Model Useful

The model should support decision-making and implementation.

If the model becomes too abstract, too detailed or disconnected from the work, it should be simplified or refocused.

## Key Takeaways

- Domain models should be validated before architecture begins.
- Domain experts should recognise the model.
- Scenarios reveal gaps and incorrect assumptions.
- Boundaries should be challenged and refined.
- Missing rules should update related documentation and decisions.
- A useful model supports both understanding and implementation.

## Related Reading

- [06 Invariants](06%20Invariants.md)
- [Architecture](../05%20Architecture/README.md)

---

## Navigation

**Previous**

- [09 Domain Events](09%20Domain%20Events.md)

**Next**

- [Architecture](../05%20Architecture/README.md)

**Book**

- [Domain Modelling](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
