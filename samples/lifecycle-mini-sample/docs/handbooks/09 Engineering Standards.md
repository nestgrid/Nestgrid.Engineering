# Engineering Standards

> Part of the **[Lifecycle Mini Sample](../../README.md)**.

## Purpose

This page demonstrates how a product records the standards relevant to its approved technology and product type. It does not replace the global Engineering Standards book.

## General Standards

- Organise code and documentation by meaningful responsibility.
- Keep one top-level type per source file, including internal types.
- Keep commands, results and use cases discoverable as first-class artefacts.
- Prefer concrete abstractions unless genuine substitutability or an architectural boundary requires one.
- Record meaningful logging, validation, exception, recovery and testing expectations.
- Use published Nestgrid libraries through packages when a published package is the approved dependency.

## API Products

When the product exposes an ASP.NET Core API:

- publish an OpenAPI document;
- provide clear endpoint metadata such as names, tags, summaries, descriptions and response metadata;
- provide an interactive OpenAPI UI such as Scalar in Development or another explicitly approved non-production environment;
- protect or disable interactive documentation in Production unless its exposure is an approved requirement.

## Data and Development

For a product using EF Core:

- use the approved provider's database naming convention;
- map .NET PascalCase explicitly to provider-appropriate database names;
- allow development migrations to apply on startup only when explicitly enabled through configuration;
- never apply migrations automatically in Production; schema changes are part of the controlled deployment process.

These are examples of product-relevant standards, not assumptions that every sample or product must use .NET, an API or a relational database.

## Related Reading

- [Engineering Standards](../../../../books/08%20Engineering%20Standards/README.md)
- [Architecture](05%20Architecture.md)
- [Operationalisation](08%20Operationalisation.md)

---

## Navigation

**Previous**

- [Operationalisation](08%20Operationalisation.md)

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../../README.md)
