# Unit Testing

> Part of the **[Testing](README.md)**.

## Purpose

Unit testing validates small units of behaviour in isolation.

It provides fast feedback about domain rules, calculations, decisions and logic.

## Guidance

Unit tests should focus on behaviour rather than implementation mechanics.

Good unit tests help engineers change code confidently without over-specifying private details.

### Test Behaviour

Tests should describe expected behaviour clearly.

They should make it obvious what scenario is being validated and why it matters.

### Keep Tests Fast

Unit tests should usually be fast and deterministic.

They should avoid unnecessary dependence on networks, databases, file systems or external services.

### Protect Domain Rules

Domain rules and invariants should have strong unit test coverage.

These tests provide confidence that core business behaviour remains correct.

### Avoid Brittle Tests

Tests should not fail because harmless implementation details changed.

Brittle tests slow delivery and reduce trust in the test suite.

### Use Clear Test Data

Test data should make the scenario easy to understand.

Builders, factories or fixtures should clarify setup rather than hide important meaning.

## Key Takeaways

- Unit tests validate focused behaviour.
- They should be fast and deterministic.
- Domain rules deserve strong unit test coverage.
- Tests should avoid private implementation coupling.
- Test data should make scenarios clear.

## Related Reading

- [01 Testing Strategy](01%20Testing%20Strategy.md)
- [03 Integration Testing](03%20Integration%20Testing.md)

---

## Navigation

**Previous**

- [01 Testing Strategy](01%20Testing%20Strategy.md)

**Next**

- [03 Integration Testing](03%20Integration%20Testing.md)

**Book**

- [Testing](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
