# Repository Structure

> Part of the **[Solution Structure](README.md)**.

## Purpose

Repository structure defines the top-level organisation of a codebase or documentation repository.

It helps contributors find the right artefacts quickly and understand the purpose of the repository.

## Guidance

A repository should be understandable from its root.

The top-level files and folders should reveal what the repository contains, how it is governed and how contributors should work with it.

### Keep the Root Intentional

The repository root should contain only high-value entry points and standard governance files.

Common examples include `README.md`, lifecycle or overview documents, license files, contribution guidance and primary folders.

### Separate Major Artefact Types

Source code, tests, documentation, samples, templates and tools should have clear locations.

This separation reduces confusion and makes automation easier.

### Make Documentation Discoverable

Documentation should be easy to find from the root README.

Important lifecycle or methodology documents should not be buried where readers cannot discover them.

### Avoid Root Clutter

The root should not become a dumping ground for temporary files, experiments or scattered notes.

Unstructured root clutter makes repositories harder to understand and maintain.

### Match Repository Purpose

The exact structure should reflect the repository's purpose.

A documentation repository, product repository, library repository and tooling repository may need different root folders.

### Separate Handbook and Artefacts

Product repositories should separate long-lived product knowledge from lifecycle artefacts.

Recommended structure:

```text
src/
tests/
docs/
  handbooks/
  artefacts/
    01 Discovery/
    02 Architecture/
    03 Implementation/
    04 Quality/
    05 Security/
    06 Platform/
    07 Release/
  decisions/
samples/        optional
assets/         optional
scripts/        optional
tools/          optional
.github/        optional
```

`src/` should contain production code.

`tests/` should contain automated tests.

`docs/handbooks/` should contain enduring product documentation such as philosophy, language, domain model, architecture and operations.

`docs/artefacts/` should contain workflow outputs such as Product Briefs, Architecture Packs, Implementation Reports, Test Strategies, Security Assessments and Deployment Guides.

Lifecycle artefact folders should be numbered by workflow order rather than sorted alphabetically.

`docs/decisions/` should contain decision records. The product handbook may explain how decisions are governed, but the decision records themselves should live in `docs/decisions/`.

Optional folders such as `samples/`, `assets/`, `scripts/`, `tools/` and `.github/` should be added when the repository needs examples, supporting assets, automation, internal tooling or GitHub-specific workflows.

## Key Takeaways

- The repository root should communicate purpose quickly.
- Major artefact types should have clear locations.
- Documentation should be discoverable.
- Root clutter should be avoided.
- Structure should match repository purpose.
- Handbook content and lifecycle artefacts should be separated in product repositories.

## Related Reading

- [02 Source Structure](02%20Source%20Structure.md)
- [04 Naming and Organisation](04%20Naming%20and%20Organisation.md)
- [Engineering Artefacts](../16%20Engineering%20Artefacts/README.md)

---

## Navigation

**Previous**

- [Solution Structure](README.md)

**Next**

- [02 Source Structure](02%20Source%20Structure.md)

**Book**

- [Solution Structure](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
