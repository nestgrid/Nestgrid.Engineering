# Logging

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Logging standards define what should be recorded so software can be understood, supported and operated in production.

## Guidance

Logging should provide operational insight without leaking sensitive data or creating noise.

Logs should help engineers understand important workflows, failures and integration behaviour.

### Log Operational Boundaries

Important orchestration boundaries should log meaningful failures.

Examples include:

- Application use case failures.
- Integration failures.
- Persistence failures.
- Domain event publishing failures.
- Unexpected exceptions.

### Use Structured Context

Logs should include structured context where useful.

Examples include correlation identifiers, tenant identifiers, workspace identifiers, operation names and relevant non-sensitive business identifiers.

### Protect Sensitive Data

Logs must not expose secrets, credentials, tokens, personal data or sensitive financial values unless explicitly approved and protected.

### Avoid Log Noise

Expected validation failures should usually be returned as application results rather than logged as unexpected errors.

Repeated low-value logs make operational signals harder to find.

## Key Takeaways

- Logs should support production understanding.
- Important orchestration and integration failures should be logged.
- Logs should include useful structured context.
- Sensitive data must not be logged.
- Expected validation failures should not become noisy error logs.

## Related Reading

- [04 Error Handling](04%20Error%20Handling.md)
- [Observability](../11%20Operations/02%20Observability.md)

---

## Navigation

**Previous**

- [07 Application Response Model](07%20Application%20Response%20Model.md)

**Next**

- [09 Domain Events](09%20Domain%20Events.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
