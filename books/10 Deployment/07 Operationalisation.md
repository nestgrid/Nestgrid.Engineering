# Operationalisation

> Part of the **[Deployment](README.md)**.

## Purpose

Operationalisation turns engineered software into a product that can be delivered, consumed, installed, configured, upgraded, supported and validated in its target environment.

It is broader than deployment.

A product is not operationally ready until its intended users, consumers or operators can reliably use it in the way the product requires.

## Guidance

Operationalisation is product-agnostic.

It applies differently depending on what is being delivered:

- A library may need package publication, versioning, consumer documentation and package-consumption validation.
- A web application or API may need hosting, configuration, health checks, deployment automation and rollback.
- A service or worker may need publication, installation, service registration, logs, upgrades, uninstall and smoke tests.
- A command-line tool may need executable packaging, installation guidance, configuration defaults and validation commands.
- A mobile application may need signing, distribution, update strategy, platform permissions and store readiness.

The Platform Engineer owns final operationalisation, but the concern must be carried through the lifecycle.

### Discovery Captures Operational Requirements

Discovery should identify how the product is expected to be delivered, consumed, installed, configured, upgraded, supported and validated.

These become Operational Requirements in the Product Brief.

### Architecture Designs the Operational Model

Architecture should define the operational model where it affects system shape, packaging, distribution, hosting, configuration, security, observability, upgrade, rollback, portability or support.

The operational model belongs in the Architecture Pack.

### Engineering Implements Operationalisation

Engineering should implement the packageable, deployable or consumable shape required by the approved operational model.

This may include package metadata, publish profiles, installers, service registration assets, configuration defaults, validation commands, documentation hooks or consumer examples.

### Quality Validates Operational Scenarios

Quality should validate operational scenarios that materially affect release confidence.

Examples include package consumption, clean install, configuration changes, upgrade, rollback, uninstall, smoke tests and recovery.

### Security Reviews Operational Security

Security should review the security aspects of operationalisation.

Examples include service identity, runtime permissions, package integrity, signing, secrets, configuration, distribution channels and least privilege.

### Platform Realises the Operational Package

Platform should turn the engineered product into a repeatable operational package or delivery process.

This may include publication, deployment automation, installation guidance, service registration, environment configuration, observability, operational documentation, upgrade approach and readiness validation.

## Key Takeaways

- Operationalisation is a product requirement, not only a platform concern.
- Platform owns final realisation, but should not discover the operational strategy at the end of the lifecycle.
- The form of operationalisation depends on the product type.
- Operational requirements should appear in Discovery and be shaped by Architecture.
- Operational scenarios should be implemented, tested, secured and validated before release.

## Related Reading

- [03 Discovery - Requirements](../03%20Discovery/04%20Requirements.md)
- [15 Engineering Workflow - Lifecycle Flow](../15%20Engineering%20Workflow/03%20Lifecycle%20Flow.md)
- [05 Deployment Validation](05%20Deployment%20Validation.md)
- [06 Rollback and Recovery](06%20Rollback%20and%20Recovery.md)
- [Operations](../11%20Operations/README.md)

---

## Navigation

**Previous**

- [06 Rollback and Recovery](06%20Rollback%20and%20Recovery.md)

**Next**

- [Operations](../11%20Operations/README.md)

**Book**

- [Deployment](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
