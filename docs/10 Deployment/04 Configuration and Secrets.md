# Configuration and Secrets

> Part of the **[Deployment](README.md)**.

## Purpose

Configuration and secrets define how environment-specific settings and sensitive values are supplied during deployment and runtime.

They help keep deployments secure, portable and predictable.

## Guidance

Configuration should be separated from deployable artefacts where practical.

Secrets should be protected throughout their lifecycle and never treated as ordinary configuration.

### Externalise Environment Values

Values that differ by environment should be provided through configuration mechanisms rather than hardcoded into the artefact.

This supports consistent artefacts across environments.

### Protect Secrets

Secrets should be stored and delivered through approved secret-management mechanisms.

They should not appear in source control, logs, build output or documentation examples.

### Validate Required Settings

Applications should fail clearly when required configuration is missing or invalid.

Silent misconfiguration can be more dangerous than a failed startup.

### Keep Configuration Understandable

Configuration names and documentation should explain purpose.

Unclear settings create operational risk.

### Rotate and Revoke

Secrets should be rotatable and revocable.

Teams should understand how to respond when a secret is exposed or no longer needed.

## Key Takeaways

- Environment values should be externalised.
- Secrets require approved protection mechanisms.
- Missing configuration should fail clearly.
- Configuration should be understandable.
- Secrets should support rotation and revocation.

## Related Reading

- [03 Environment Management](03%20Environment%20Management.md)
- [Security Architecture](../05%20Architecture/07%20Security%20Architecture.md)

---

## Navigation

**Previous**

- [03 Environment Management](03%20Environment%20Management.md)

**Next**

- [05 Deployment Validation](05%20Deployment%20Validation.md)

**Book**

- [Deployment](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
