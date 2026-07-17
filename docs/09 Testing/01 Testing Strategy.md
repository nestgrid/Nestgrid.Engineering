# Testing Strategy

> Part of the **[Testing](README.md)**.

## Purpose

Testing strategy defines what should be tested, why it should be tested and which test types provide the right confidence.

It helps teams focus validation effort on meaningful risk.

## Guidance

A testing strategy should be shaped by domain rules, architecture, quality attributes, delivery risk and operational needs.

The goal is balanced confidence, not maximum test volume.

### Test Important Behaviour

Tests should protect behaviours that matter to users, stakeholders and the domain.

Important rules, workflows and failure cases deserve more attention than incidental implementation details.

### Match Test Type to Risk

Different risks require different tests.

Unit, integration, contract, end-to-end, performance and security tests each provide different kinds of confidence.

### Prefer Fast Feedback

Tests should provide feedback quickly where possible.

Fast tests support frequent change, while slower tests should be reserved for risks that cannot be validated cheaply.

### Automate Critical Checks

Critical behaviours should be validated through automation where practical.

Manual testing may still be useful, but it should not be the only protection for important behaviour.

### Review the Strategy

The testing strategy should evolve as the system grows.

New risks, incidents, defects and architectural changes should influence testing priorities.

## Key Takeaways

- Testing strategy should focus on meaningful risk.
- Important behaviour deserves explicit validation.
- Different test types provide different confidence.
- Fast feedback supports safe change.
- Critical checks should be automated where practical.
- Testing strategy should evolve with the system.

## Related Reading

- [02 Unit Testing](02%20Unit%20Testing.md)
- [05 Test Maintainability](05%20Test%20Maintainability.md)

---

## Navigation

**Previous**

- [Testing](README.md)

**Next**

- [02 Unit Testing](02%20Unit%20Testing.md)

**Book**

- [Testing](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
