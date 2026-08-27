# Artefacts

This directory demonstrates the standard product-repository locations for lifecycle artefacts. The folders remain present even when a stage is not required or has not started.

## Lifecycle Artefact Folders

| Stage | Typical owner | Typical outputs |
| --- | --- | --- |
| `01 Discovery/` | Product Owner | Product Brief, Architecture Handover |
| `02 Architecture/` | Solution Architect | Architecture Recommendation, Architecture Pack |
| `03 Implementation/` | Software Engineer | Implementation Plan, Implementation Report, Engineering Assurance |
| `04 Quality/` | Quality Engineer | Test Strategy, Release Readiness Report |
| `05 Security/` | Security Engineer | Security Assessment |
| `06 Platform/` | Platform Engineer | Deployment Guide, Operational Readiness Review |
| `07 Release/` | Project Sponsor with lifecycle recommendations | Release Report |

The primary approved artefact and its associated gate normally perform the handover. A separate handover document is only needed when it adds useful context.

## Cross-Cutting Records

- Decisions live in `docs/decisions/` or, when scoped, inside the relevant initiative.
- Independent reviews live in `docs/reviews/` at product scope or in an initiative's `reviews/` directory.
- Operationalisation is considered from Discovery onwards and is realised during Platform. It may mean package publication, installation, configuration, service registration, upgrades, documentation and validation depending on the product type.

## Proportionality

Not every initiative needs every artefact at full depth. The required evidence depends on scope, risk, product type and the changes being made. A small change may need a short brief, focused tests and a release note; a new product may need the complete set.

## Navigation

**Sample**

- [Lifecycle Mini Sample](../../README.md)

**Engineering Artefacts**

- [Engineering Artefacts](../../../../books/16%20Engineering%20Artefacts/README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../../README.md)
