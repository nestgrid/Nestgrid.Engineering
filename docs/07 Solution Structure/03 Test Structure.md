# Test Structure

> Part of the **[Solution Structure](README.md)**.

## Purpose

Test structure defines where tests live and how they relate to the source they validate.

It helps engineers find, run and maintain tests consistently.

## Guidance

Tests should be organised deliberately, not added wherever convenient.

A clear test structure supports confidence, automation and long-term maintainability.

### Separate Test Artefacts

Tests should be clearly separated from production source where the technology and repository style allow it.

This makes build, packaging and automation behaviour easier to reason about.

### Mirror Meaningful Boundaries

Test organisation should reflect meaningful source boundaries.

When tests map clearly to modules, components or behaviours, engineers can locate relevant validation quickly.

### Distinguish Test Types

Different kinds of tests may need different folders, projects or naming.

Unit, integration, contract, end-to-end and performance tests often have different dependencies and execution expectations.

### Keep Shared Test Support Clear

Shared fixtures, builders, factories and helpers should be organised carefully.

They should reduce duplication without becoming hidden frameworks that make tests hard to understand.

### Support Automation

Test structure should make it easy for automation to run the right tests at the right time.

Slow, environment-dependent or destructive tests should be identifiable.

## Key Takeaways

- Test structure should be deliberate and discoverable.
- Tests should map clearly to the behaviour they validate.
- Test types should be distinguishable.
- Shared test support should remain understandable.
- Structure should support automation.

## Related Reading

- [Testing](../09%20Testing/README.md)
- [02 Source Structure](02%20Source%20Structure.md)

---

## Navigation

**Previous**

- [02 Source Structure](02%20Source%20Structure.md)

**Next**

- [04 Naming and Organisation](04%20Naming%20and%20Organisation.md)

**Book**

- [Solution Structure](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
