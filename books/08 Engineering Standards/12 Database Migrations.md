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

### Apply Development Migrations Explicitly

Development environments may apply pending Entity Framework Core migrations automatically on application startup when explicitly enabled through configuration.

This supports a better developer experience for local development, fresh clones and integration-style testing.

The behaviour must be controlled by configuration rather than hidden environment-only code.

Example intent:

```text
Development
ApplyMigrationsOnStartup = true

Production
ApplyMigrationsOnStartup = false
```

When enabled, startup migration should:

- use `Migrate` or `MigrateAsync`, not `EnsureCreated`;
- log when migration application starts;
- log when there are no pending migrations;
- log each applied migration where practical;
- fail clearly when migration application fails;
- and remain disabled by default for production.

Do not use `EnsureCreated` for migrated relational databases because it bypasses the migration history model.

Production environments must never apply migrations automatically from application startup.

Production schema changes are part of the controlled deployment process and should be planned, reviewed, backed up and validated through Platform and Release.

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
- Development startup migration may be enabled explicitly through configuration.
- Production startup migration must remain disabled.
- Production schema changes belong to the deployment process.
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

- [13 Implementation Planning](13%20Implementation%20Planning.md)

**Book**

- [Engineering Standards](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
