# API Contracts

> Part of the **[Engineering Standards](README.md)**.

## Purpose

API contract standards define how external and internal consumers interact with application capabilities.

## Guidance

API contracts should be explicit, stable and testable.

They should not leak accidental implementation details.

### Use Explicit Request Models

API endpoints should use explicit request models for non-trivial operations.

Query parameters may be appropriate for simple reads, but commands and complex assessments should use request contracts.

### Map Application Results Deliberately

API layers should map `Result` and `Result<T>` responses to clear transport outcomes.

Validation, conflict, not found and unexpected failures should be distinguishable.

### Test Contract Behaviour

API tests should cover:

- Successful requests.
- Validation failures.
- Invalid payloads.
- Response shapes.
- Failure mapping.
- Authorisation posture.

### Separate Stable API Enums When Needed

If an API is intended to be a stable external contract, API enum values may need to be separated from Domain enum values.

This prevents internal domain evolution from accidentally breaking consumers.

## Key Takeaways

- API contracts should be explicit and stable.
- Non-trivial operations should use request models.
- Application results should be mapped deliberately.
- API tests should cover success, validation and response shape.
- Stable external contracts may need API-specific enums.

## Related Reading

- [Integration Architecture](../05%20Architecture/06%20Integration%20Architecture.md)
- [End-to-End Testing](../09%20Testing/04%20End-to-End%20Testing.md)

---

## Navigation

**Previous**

- [10 Strong Identifiers](10%20Strong%20Identifiers.md)

**Next**

- [12 Database Migrations](12%20Database%20Migrations.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
