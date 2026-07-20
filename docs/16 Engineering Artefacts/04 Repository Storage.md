# Repository Storage

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Repository storage defines where handbook content and project artefacts should live inside product repositories.

## Guidance

The Nestgrid Engineering methodology is stored in this repository.

Completed artefacts for a product or solution should live with the product repository they describe.

### Recommended Product Repository Structure

```text
src/
tests/
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
  decisions/
samples/        optional
assets/         optional
scripts/        optional
tools/          optional
.github/        optional
```

### Source

`src/` contains production code.

### Tests

`tests/` contains automated tests.

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

Product decision records should live under `docs/decisions/`.

The product handbook may include `docs/handbooks/06 Decisions/` to explain decision governance, decision types and how decisions are reviewed.

The records themselves should remain in `docs/decisions/`.

### Optional Folders

`samples/` contains reference examples, sample applications, sample data or demo usage.

`assets/` contains images, diagrams, logos, screenshots and static supporting files.

`scripts/` contains repeatable local or CI helper scripts.

`tools/` contains custom internal tooling.

`.github/` contains GitHub workflows, issue templates, pull request templates and contribution automation.

## Key Takeaways

- Product artefacts belong in the product repository.
- `src/` contains production code.
- `tests/` contains automated tests.
- `docs/handbooks/` contains enduring knowledge.
- `docs/artefacts/` contains lifecycle outputs.
- `docs/decisions/` contains decision records.
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
