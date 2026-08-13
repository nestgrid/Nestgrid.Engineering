# Operationalisation

> Part of the **[Lifecycle Mini Sample](../../README.md)**.

## Purpose

Operationalisation is the process of making an engineered product usable in its target environment. It is broader than DevOps operations and is considered throughout the lifecycle.

## Across the Lifecycle

- **Product Owner:** captures who uses the product, where it must run, how it is installed or obtained, how it is configured and what upgrade or recovery expectations exist.
- **Solution Architect:** designs the packaging, configuration, service, distribution, observability, rollback and recovery model.
- **Software Engineer:** implements the approved operational behaviour and supporting documentation.
- **Quality Engineer:** verifies installation, configuration, upgrade, uninstall, smoke and recovery scenarios where relevant.
- **Security Engineer:** reviews identities, permissions, secrets, data protection and least privilege.
- **Platform Engineer:** realises the operational package and deployment experience.
- **Project Sponsor:** approves material operational commitments and the final release.

## Product-Type Examples

| Product type | Operationalisation may include |
| --- | --- |
| Library or SDK | Package publication, versioning, consumer guidance and compatibility validation |
| Web or API application | Hosting, configuration, health checks, deployment and rollback |
| Service or worker | Publication, installation, service registration, logging, upgrades and uninstall |
| Console tool | Packaging, installation, configuration and command validation |
| Mobile application | Signing, distribution, permissions, upgrades and store readiness |

The product type determines the concrete evidence. The principle applies to all products: a product is not ready merely because its source code builds.

## Sample Application

Team Tasks is assumed to be a small internal application. Its operational package would need to explain:

- how to install it;
- how to configure its owned data store;
- how to verify that it is healthy;
- how to upgrade it safely;
- how to recover or roll back a failed deployment;
- how to support the people using it.

The sample does not prescribe whether the final product is a web application, service or another application type. That is an Architecture decision informed by the approved operational requirements.

## Related Reading

- [Architecture](05%20Architecture.md)
- [Engineering Standards](09%20Engineering%20Standards.md)
- [Platform Artefacts](../artefacts/06%20Platform/README.md)
- [Deployment Guidance](../../../../books/10%20Deployment/README.md)
- [Operations Guidance](../../../../books/11%20Operations/README.md)

---

## Navigation

**Previous**

- [Engineering Workflow](07%20Engineering%20Workflow.md)

**Next**

- [Engineering Standards](09%20Engineering%20Standards.md)

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../../README.md)
