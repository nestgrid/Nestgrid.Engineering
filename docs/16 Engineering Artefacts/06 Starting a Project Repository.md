# Starting a Project Repository

> Part of the **[Engineering Artefacts](README.md)**.

## Purpose

This page defines the baseline structure for starting a product or project repository using Nestgrid Engineering.

## Guidance

Start with a lean repository structure before adding detailed content.

The structure should make source code, tests, enduring knowledge, lifecycle artefacts and decision records easy to find.

## Standard Structure

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

## What Goes Where

`src/` contains production code.

`tests/` contains automated tests.

`docs/handbooks/` contains enduring product knowledge.

`docs/artefacts/` contains workflow outputs created during delivery.

`docs/decisions/` contains decision records.

`samples/` contains reference examples, sample applications, sample data or demo usage.

`assets/` contains images, diagrams, logos, screenshots and static supporting files.

`scripts/` contains repeatable local or CI helper scripts.

`tools/` contains custom internal tooling.

`.github/` contains GitHub workflows, issue templates, pull request templates and contribution automation.

## Starting Steps

1. Create `src/`, `tests/` and `docs/`.
2. Create `docs/handbooks/`, `docs/artefacts/` and `docs/decisions/`.
3. Add a README to each major folder explaining its purpose.
4. Add the initial handbook books needed by the project.
5. Copy standard artefact templates when the first workflow artefacts are produced.
6. Create the decision index under `docs/decisions/README.md`.
7. Add optional folders only when the repository needs them.

## Key Takeaways

- Start with a lean standard structure before detailed content.
- Keep source code and tests clearly separated.
- Keep handbook pages, artefacts and decision records separate.
- Decision governance belongs in the handbook.
- Decision records belong in `docs/decisions/`.
- Optional folders should be added only when they have a clear purpose.

## Related Reading

- [04 Repository Storage](04%20Repository%20Storage.md)
- [Repository Structure](../07%20Solution%20Structure/01%20Repository%20Structure.md)
- [Lifecycle Mini Sample](../../samples/lifecycle-mini-sample/README.md)

---

## Navigation

**Previous**

- [05 Artefact Lifecycle](05%20Artefact%20Lifecycle.md)

**Next**

- [Engineering Workflow](../15%20Engineering%20Workflow/README.md)

**Book**

- [Engineering Artefacts](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
