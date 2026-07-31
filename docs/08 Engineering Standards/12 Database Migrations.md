# Database Migrations

> Part of the **[Engineering Standards](README.md)**.

## Purpose

Database migration standards define how schema changes should be produced, reviewed and validated.

## Guidance

Schema changes should be reviewable and repeatable.

Migration work should not be considered complete when schema generation is deferred unless that deferral is explicit and accepted.

### Produce Reviewable Migrations

Database-backed features should include migrations or equivalent schema artefacts when persistence changes.

The migration should be understandable in review and aligned with the intended data model.

### Validate Provider Behaviour

Tests that use in-memory persistence do not prove relational mappings, provider behaviour, generated schema, precision, indexes or constraints.

Where those concerns matter, use provider-backed integration tests.

### Use Provider-Appropriate Database Naming

Database object naming should follow the standard convention for the selected database provider.

For PostgreSQL, database objects should use `snake_case`.

This applies to:

- Tables
- Columns
- Primary keys
- Foreign keys
- Indexes
- Constraints
- Sequences

.NET code should continue to use PascalCase for types and members.

Entity Framework Core mappings should translate .NET names to the provider-appropriate database naming convention explicitly.

Do not rely on accidental provider naming behaviour where a name is part of the database contract.

When a product uses a non-standard database provider, the Architecture Pack should define the database naming convention for that provider.

### Handle Configuration Safely

Default configuration should not contain committed local database credentials.

Connection strings and credentials should be managed through appropriate environment configuration or secret management.

## Key Takeaways

- Schema changes should be reviewable and repeatable.
- Deferred migrations must be documented explicitly.
- In-memory tests do not validate relational provider behaviour.
- Database object naming should follow the selected provider convention.
- PostgreSQL database objects should use `snake_case`.
- Default configuration should not contain local database credentials.

## Related Reading

- [Data Architecture](../05%20Architecture/05%20Data%20Architecture.md)
- [Integration Testing](../09%20Testing/03%20Integration%20Testing.md)
- [Configuration and Secrets](../10%20Deployment/04%20Configuration%20and%20Secrets.md)

---

## Navigation

**Previous**

- [11 API Contracts](11%20API%20Contracts.md)

**Next**

- [Testing](../09%20Testing/README.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
