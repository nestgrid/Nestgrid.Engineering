# ADR-003: Adopt Books and Workflows Structure

> Decision record for **Architecture**.

## Status

Accepted

## Type

Architecture

## Date

2026-08-04

## Owners

- Nestgrid Engineering Operating System maintainers

## Context

The Nestgrid Engineering Operating System repository now contains agents, handbook guidance, templates, samples, decisions, initiatives and early Runner vision.

After moving the canonical handbook content from `docs/` to `handbook/`, the repository structure became clearer but still carried some conceptual awkwardness. The handbook is the overall standards concept, while the numbered directories are the individual books that compose it.

The operating system also needs an explicit place for repeatable workflows. Agents define responsibilities, the handbook defines standards, and templates define artefact shape. Workflows define how those pieces are coordinated for common kinds of work.

## Decision

The Nestgrid Engineering Operating System repository will use lowercase top-level folders.

The canonical handbook books will live under `books/`.

The Engineering Handbook remains the concept used in documentation.

A new top-level `workflows/` directory will define repeatable operating paths.

The top-level structure is:

```text
agents/
books/
docs/
  decisions/
  initiatives/
templates/
samples/
scripts/
workflows/
```

Reviews are recognised as first-class engineering artefacts, but they are not introduced as a root operating-system folder yet. Product-level reviews belong in product repositories under `docs/reviews/`. Initiative-specific reviews belong in the relevant initiative's `reviews/` folder.

## Rationale

Lowercase top-level folders are easier to use with Git, URLs, automation, shells and cross-platform filesystems.

`books/` describes the physical structure more accurately than `handbook/`. The Engineering Handbook remains an important concept, but the repository contains the books that make up that handbook.

`workflows/` fills the gap between role definitions and future automation. It describes which agents participate, in what order, which artefacts are expected, and where review or approval gates occur.

Keeping reviews as artefact outputs avoids adding a root folder before operating-system-level reviews become regular enough to justify it.

## Alternatives Considered

### Keep `handbook/`

This was rejected because it makes the folder and concept identical even though the folder contains individual books.

### Use Title Case Top-Level Folders

This was rejected because Title Case top-level folders create more friction for automation, links and command-line usage.

### Add `reviews/` as a Top-Level Folder Immediately

This was deferred. Reviews are important, but they should remain close to the product or initiative they review until operating-system-level reviews become regular.

### Introduce `knowledge/`, `practice/` and `automation/` Folders

This was rejected for now. Those categories are useful for documentation, but physical nesting would add indirection without enough operational value.

## Consequences

Links to canonical handbook books must use `books/`.

Reusable prompts should point Engineering Agents to `/engineering/books` when identifying the Engineering Handbook.

Workflows can now evolve as durable operating-system artefacts and later become inputs to a Runner.

Product repository guidance remains unchanged: product-specific handbook knowledge continues to live under `docs/handbooks/`.

## Related Decisions

- [ADR-001: Use Markdown-First Documentation](ADR-001-use-markdown-first-documentation.md)
- [ADR-002: Adopt Engineering Operating System Structure](ADR-002-adopt-engineering-operating-system-structure.md)

## Related Documentation

- [Engineering Handbook](../../books/README.md)
- [Engineering Agents](../../agents/README.md)
- [Workflows](../../workflows/README.md)
- [Repository Structure](../../books/07%20Solution%20Structure/01%20Repository%20Structure.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
