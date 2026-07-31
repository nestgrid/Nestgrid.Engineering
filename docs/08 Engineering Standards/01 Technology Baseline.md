# Technology Baseline

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Technology baseline defines the default engineering stack for Nestgrid products.

It provides consistency across products, reduces repeated technology selection and allows teams to share patterns, tooling and operational knowledge.

## Guidance

Nestgrid products should follow the baseline unless there is a clear reason to deviate.

The baseline is not intended to prevent good judgement. It defines the default starting point so deviations are deliberate, justified and documented.

### When to Follow the Baseline

Products should follow the baseline when building standard Nestgrid applications, APIs, services, libraries and supporting tools.

Following the baseline is expected when the product has no unusual technical, regulatory, operational or integration constraint that requires a different choice.

### When Deviations Are Acceptable

Deviations are acceptable when the baseline does not fit the product context.

Examples may include a platform constraint, integration requirement, specialist workload, operational limitation or a strong product-specific reason.

Deviations must be justified and documented through the appropriate decision record, usually a `TDR` or `ADR`.

### Runtime

Nestgrid products should use `.NET` with the latest LTS version unless otherwise agreed.

C# is the standard implementation language.

### Database

PostgreSQL is the standard relational database.

Products should use a different database only when the domain, workload, hosting model or operational constraint justifies it.

### Data Access

Entity Framework Core is the standard data access technology.

Products should use it consistently unless there is a documented reason to use another approach for a specific boundary or workload.

### API

ASP.NET Core Minimal APIs are the standard approach for HTTP APIs.

Products may use other ASP.NET Core styles where the product context clearly benefits from them.

### Result Pattern

Nestgrid.Response is the standard result model for Nestgrid products.

Products should use the standard Nestgrid result model for consistent success, failure, status and error handling across APIs, application flows and integrations.

### Validation

FluentValidation is recommended for request validation.

Request validation belongs in the Application layer. Domain validation belongs in the Domain Model. Database constraints remain the final protection of persistence.

### Testing

xUnit, Shouldly and NSubstitute are the standard testing libraries.

Products should use these libraries unless there is a justified reason to deviate.

### Logging

Microsoft.Extensions.Logging with `ILogger` is the standard logging abstraction.

Products should prefer this abstraction so logging remains consistent with the .NET hosting and dependency injection model.

### General Standards

Nestgrid products should enable Nullable Reference Types and treat warnings as errors.

Products should use file-scoped namespaces, primary constructors where appropriate and async-first development for I/O-bound work.

Dependencies should be provided through dependency injection. Code should depend on abstractions at architectural boundaries and where substitution, testing or decoupling provides clear value.

Products should prefer framework capabilities before introducing third-party libraries.

## Key Takeaways

- Nestgrid products should follow the technology baseline by default.
- Deviations are acceptable when justified and recorded.
- `.NET`, C#, PostgreSQL, EF Core and ASP.NET Core Minimal APIs form the current baseline.
- Nestgrid.Response is the standard result model.
- FluentValidation is recommended for request validation in the Application layer.
- Domain validation belongs in the Domain Model.
- xUnit, Shouldly and NSubstitute are the standard testing libraries.
- Framework capabilities should be preferred before third-party libraries.

## Related Reading

- [TDR-002: Establish Technology Baseline](../decisions/TDR-002-establish-technology-baseline.md)
- [02 Readability](02%20Readability.md)
- [07 Application Response Model](07%20Application%20Response%20Model.md)
- [Testing](../09%20Testing/README.md)

---

## Navigation

**Previous**

- [Engineering Standards](README.md)

**Next**

- [02 Readability](02%20Readability.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
