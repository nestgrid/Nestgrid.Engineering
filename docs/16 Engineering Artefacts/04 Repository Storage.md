# Repository Storage

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Repository storage defines where handbook content and project artefacts should live inside product repositories.

## Guidance

The Nestgrid Engineering methodology is stored in this repository.

Completed artefacts for a product or solution should live with the product repository they describe.

### Recommended Product Repository Structure

```text
docs/
  handbooks/
    01 Philosophy/
    02 Language/
    03 Discovery/
    04 Domain Modelling/
    05 Architecture/
    06 Decisions/
    07 Solution Structure/
    08 Coding Standards/
    09 Testing/
    10 Deployment/
    11 Operations/
    12 Documentation/
  artefacts/
    discovery/
    architecture/
    implementation/
    quality/
    security/
    platform/
    release/
```

### Handbook

`docs/handbooks/` contains enduring product knowledge.

Examples:

- Product philosophy
- Ubiquitous language
- Domain model
- Architecture overview
- Solution structure
- Operational model

### Artefacts

`docs/artefacts/` contains lifecycle outputs and evidence of engineering work.

Examples:

- Product Brief
- Architecture Pack
- Implementation Plan
- Test Strategy
- Security Assessment
- Deployment Guide
- Release Report

### Decisions

Product decisions may live under `docs/handbooks/06 Decisions/` or `docs/decisions/`.

The repository should choose one location and link to it consistently.

## Key Takeaways

- Product artefacts belong in the product repository.
- `docs/handbooks/` contains enduring knowledge.
- `docs/artefacts/` contains lifecycle outputs.
- Structure should make handover documents easy to find.

## Related Reading

- [Repository Structure](../07%20Solution%20Structure/01%20Repository%20Structure.md)
- [05 Artefact Lifecycle](05%20Artefact%20Lifecycle.md)

---

## Navigation

**Previous**

- [03 Artefact Metadata](03%20Artefact%20Metadata.md)

**Next**

- [05 Artefact Lifecycle](05%20Artefact%20Lifecycle.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
