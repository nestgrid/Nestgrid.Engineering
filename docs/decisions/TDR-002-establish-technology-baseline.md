# TDR-002: Establish Technology Baseline

> Decision record for **Technical**.

## Status

Accepted

## Type

Technical

## Date

2026-07-24

## Owners

- Nestgrid Engineering

## Context

Nestgrid Engineering Operating System defines the methodology and standards used across Nestgrid products.

Product teams need a default technology baseline so new products can start quickly, remain consistent and share engineering practices across repositories.

Without a baseline, each product would repeatedly decide core runtime, database, validation, testing and logging technologies, increasing divergence and maintenance cost.

## Decision

Nestgrid products will use the standard technology baseline defined in [Technology Baseline](../../handbook/08%20Engineering%20Standards/01%20Technology%20Baseline.md).

The baseline includes `.NET`, C#, PostgreSQL, Entity Framework Core, ASP.NET Core Minimal APIs, Nestgrid.Response, FluentValidation, xUnit, Shouldly, NSubstitute and Microsoft.Extensions.Logging.

Products should follow the baseline by default. Deviations must be justified and documented through the appropriate decision record, usually a `TDR` or `ADR`.

## Rationale

A shared baseline improves consistency, onboarding, reuse, review and operational support.

It allows Nestgrid products to share implementation patterns, testing approaches, deployment expectations and troubleshooting knowledge.

The baseline remains flexible enough to allow justified deviations when product context requires a different choice.

## Alternatives Considered

### Choose Technology Per Product

This maximises local flexibility but increases divergence, review complexity and long-term maintenance cost.

It also makes it harder to reuse patterns, samples and operational knowledge across products.

### Define Architecture Without Technology Defaults

This keeps the handbook more abstract, but leaves important product-start decisions unresolved.

The handbook should provide enough default guidance to reduce unnecessary decision-making while still allowing documented deviations.

## Consequences

New Nestgrid products have a clear default stack.

Shared templates, samples and implementation guidance should align with the baseline.

Product teams must record deviations when the baseline is not appropriate.

The baseline should be reviewed when platform support, product needs or operational experience justify change.

## Related Decisions

- [ADR-001: Use Markdown-First Documentation](ADR-001-use-markdown-first-documentation.md)

## Related Documentation

- [Technology Baseline](../../handbook/08%20Engineering%20Standards/01%20Technology%20Baseline.md)
- [Engineering Standards](../../handbook/08%20Engineering%20Standards/README.md)
- [Testing](../../handbook/09%20Testing/README.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
