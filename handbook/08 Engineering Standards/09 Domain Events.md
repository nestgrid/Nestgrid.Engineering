# Domain Events

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Domain event standards define how important domain facts are recorded and published safely.

## Guidance

Domain events should describe meaningful business facts that have occurred.

They should not imply operational reliability that the implementation does not provide.

### Distinguish Evidence from Integration

In-process domain events may be useful as evidence of domain behaviour.

If events are used for operational integration, the system must provide appropriate reliability such as an outbox, retry behaviour or durable messaging.

### Do Not Discard Integration Events Silently

If a write commits successfully but event publication fails, the system must not pretend the whole operation failed without considering the committed state.

Systems should either make event publication reliable or explicitly document that events are not yet operational integration behaviour.

### Publish After Durable State Carefully

Publishing after commit is acceptable only when the consequences are understood.

Where downstream processing matters, publication should be made durable.

## Key Takeaways

- Domain events should describe meaningful business facts.
- In-process evidence and operational integration are different responsibilities.
- Integration events require reliability when downstream work matters.
- Event publication failure after commit must be handled deliberately.

## Related Reading

- [08 Logging](08%20Logging.md)
- [Operational Architecture](../05%20Architecture/08%20Operational%20Architecture.md)

---

## Navigation

**Previous**

- [08 Logging](08%20Logging.md)

**Next**

- [10 Strong Identifiers](10%20Strong%20Identifiers.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
