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

### Document Endpoint Metadata

API endpoints are first-class product interfaces. Their OpenAPI metadata should describe the endpoint clearly enough for a consumer to understand its purpose and contract without reading the implementation.

For public and internal application endpoints, provide appropriate metadata using the framework's OpenAPI support. In ASP.NET Core Minimal APIs, this normally includes:

- `WithName` for a stable operation name;
- `WithTags` for logical grouping;
- `WithSummary` for a concise purpose;
- `WithDescription` for behaviour, constraints and important usage notes; and
- explicit response metadata such as `Produces`, status codes and problem responses.

The level of detail should be proportionate to the endpoint. Health checks and private infrastructure endpoints may use brief descriptions, while public or partner-facing APIs require complete, consumer-oriented documentation.

Endpoint metadata must remain accurate as behaviour changes. It should not claim authorisation, response types, status codes or constraints that the implementation does not enforce.

### Provide an Interactive Development Reference

ASP.NET Core API products should expose their generated OpenAPI document during development. Scalar is the preferred interactive reference UI where appropriate.

The OpenAPI document and Scalar UI should normally be mapped only in Development or another explicitly approved non-production environment. Interactive API documentation must not be exposed in production by default.

The UI helps engineers and consumers explore the contract, but it does not replace accurate endpoint metadata, automated API tests or consumer-facing documentation.

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
- Endpoints should have clear, accurate OpenAPI metadata.
- API products should provide an interactive OpenAPI reference during development where appropriate.
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
