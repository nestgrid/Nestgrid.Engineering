# End-to-End Testing

> Part of the **[Testing](README.md)**.

## Purpose

End-to-end testing validates important user or business flows across the system.

It provides confidence that major workflows function when the system is assembled.

## Guidance

End-to-end tests should be used selectively because they are often slower, more fragile and more expensive than lower-level tests.

They are most valuable for critical workflows that cannot be validated adequately through smaller tests.

### Focus on Critical Flows

End-to-end tests should cover high-value or high-risk journeys.

They should not attempt to test every possible variation.

### Keep Scenarios Clear

Each test should describe a meaningful user or business scenario.

Unclear end-to-end tests are difficult to diagnose when they fail.

### Avoid Duplicating Lower-Level Tests

End-to-end tests should not replace unit or integration tests.

They should validate assembly and workflow, while lower-level tests protect detailed behaviour.

### Manage Test Reliability

End-to-end tests must be reliable enough to trust.

Flaky tests should be fixed, quarantined or removed if they no longer provide useful confidence.

### Use Production-Like Behaviour

End-to-end tests should exercise realistic paths where practical.

They should avoid bypassing the behaviour they are intended to validate.

## Key Takeaways

- End-to-end tests validate important full-system flows.
- They should focus on critical scenarios.
- They should not duplicate lower-level testing.
- Reliability is essential for trust.
- Realistic behaviour improves confidence.

## Related Reading

- [03 Integration Testing](03%20Integration%20Testing.md)
- [05 Test Maintainability](05%20Test%20Maintainability.md)

---

## Navigation

**Previous**

- [03 Integration Testing](03%20Integration%20Testing.md)

**Next**

- [05 Test Maintainability](05%20Test%20Maintainability.md)

**Book**

- [Testing](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
