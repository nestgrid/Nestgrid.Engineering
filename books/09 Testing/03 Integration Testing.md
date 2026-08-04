# Integration Testing

> Part of the **[Testing](README.md)**.

## Purpose

Integration testing validates how parts of the system work together.

It provides confidence in boundaries, persistence, messaging, APIs, infrastructure and external interactions.

## Guidance

Integration tests should focus on risks that unit tests cannot cover.

They are often slower or more complex, so they should be used where integration behaviour matters.

### Test Real Boundaries

Integration tests should validate important boundaries between components, modules, services or infrastructure.

The boundary being tested should be clear.

### Use Realistic Dependencies

Where practical, integration tests should use realistic versions of dependencies.

Mocks may be useful, but they can hide issues caused by real infrastructure behaviour.

### Validate Persistence

Data access, transactions, migrations and consistency expectations should be tested where they carry risk.

Persistence behaviour often differs from in-memory assumptions.

In-memory persistence tests may be useful for repository smoke tests, but they do not validate provider mappings, relational constraints, migrations, precision, indexes or generated schema.

Where those concerns matter, use provider-backed integration tests.

### Validate Contracts

APIs and messages should be tested against expected contracts.

Contract changes can break consumers even when internal tests pass.

### Manage Test Cost

Integration tests should be reliable and purposeful.

Slow or unstable integration tests should be reviewed because they reduce trust in the pipeline.

## Key Takeaways

- Integration tests validate behaviour across boundaries.
- They should cover risks unit tests cannot.
- Realistic dependencies improve confidence.
- Persistence and contracts deserve attention.
- In-memory persistence tests do not prove database provider behaviour.
- Integration test cost should be managed.

## Related Reading

- [02 Unit Testing](02%20Unit%20Testing.md)
- [04 End-to-End Testing](04%20End-to-End%20Testing.md)

---

## Navigation

**Previous**

- [02 Unit Testing](02%20Unit%20Testing.md)

**Next**

- [04 End-to-End Testing](04%20End-to-End%20Testing.md)

**Book**

- [Testing](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
