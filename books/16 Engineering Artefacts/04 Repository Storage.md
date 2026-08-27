# Repository Storage

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

Repository storage defines where handbook content and project artefacts should live inside product repositories.

## Guidance

The Nestgrid Engineering methodology is stored in this repository.

Completed artefacts for a product or solution should live with the product repository they describe.

### Recommended Product Repository Structure

This is the standard target structure for a product repository.

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
    08 Engineering Standards/
    09 Testing/
    10 Deployment/
    11 Operations/
    12 Documentation/
  guides/
  artefacts/
    01 Discovery/
    02 Architecture/
    03 Implementation/
    04 Quality/
    05 Security/
    06 Platform/
    07 Release/
  decisions/
  reviews/
  initiatives/
samples/        optional
assets/         optional
scripts/        optional
tools/          optional
.github/        optional
```

During pure Discovery and Architecture, a product repository may remain documentation-first.

`src/` and `tests/` become required when Engineering begins and implementation work is planned.

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

Lifecycle artefact folders should be numbered by workflow order:

```text
01 Discovery
02 Architecture
03 Implementation
04 Quality
05 Security
06 Platform
07 Release
```

Examples:

- Product Brief
- Architecture Handover
- Architecture Recommendation
- Architecture Pack
- Implementation Plan
- Test Strategy
- Security Assessment
- Deployment Guide
- Release Report

### Guides

`docs/guides/` contains durable product documentation for consumers, contributors or other audiences.

Examples include:

- API Usage Guide
- Contribution Guide
- Integration Guide

Guides explain how to use or contribute to a product. They are not lifecycle artefacts and should not be placed under `docs/artefacts/`.

### Decisions

Product decision records should live under `docs/decisions/`.

The product handbook may include `docs/handbooks/06 Decisions/` to explain decision governance, decision types and how decisions are reviewed.

The records themselves should remain in `docs/decisions/`.

### Reviews

Independent review artefacts should live under `docs/reviews/`.

Independent Reviews are recognised engineering artefacts, but they are not mandatory lifecycle stage outputs.

They provide independent evidence about lifecycle readiness, repository quality, unresolved findings and opportunities to improve the Engineering Handbook.

Use one stable scope-based name for each review series. The review date and version belong inside the document:

```text
docs/
  reviews/
    Finance Architecture Independent Review.md
```

For an initiative-specific review:

```text
docs/
  initiatives/
    <initiative-name>/
      reviews/
        Read Model Independent Review.md
```

Update the canonical document for follow-up reviews. Increment its version, preserve stable finding IDs and append to its Review History. Do not create date-stamped competing copies for the same scope.

Downstream roles should review relevant Independent Reviews before continuing work.

Findings should be resolved, accepted or explicitly deferred by the responsible role.

### Initiatives

`docs/initiatives/` contains scoped lifecycle runs for major features, enhancements, migrations, platform work and other engineering initiatives.

Initiative artefacts should not be mixed into product-level `docs/artefacts/`.

Each initiative should be self-contained:

```text
docs/
  initiatives/
    <yyyy-mm>-<initiative-name>/
      README.md
      artefacts/
        01 Discovery/
        02 Architecture/
        03 Implementation/
        04 Quality/
        05 Security/
        06 Platform/
        07 Release/
      decisions/
      reviews/
```

When an initiative completes, enduring product knowledge should be promoted into `docs/handbooks/`, enduring product decisions should be promoted or linked from `docs/decisions/`, and initiative artefacts should remain as historical evidence.

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
- `docs/reviews/` contains independent review artefacts.
- `docs/initiatives/` contains scoped lifecycle runs.
- Structure should make handover documents easy to find.

## Related Reading

- [Repository Structure](../07%20Solution%20Structure/01%20Repository%20Structure.md)
- [05 Artefact Lifecycle](05%20Artefact%20Lifecycle.md)
- [07 Initiative Artefacts](07%20Initiative%20Artefacts.md)

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

- [Nestgrid Engineering Operating System](../../README.md)
