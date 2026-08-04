# Books and Workflows Structure

This initiative captures the refinement that makes `books/` and `workflows/` first-class parts of the Nestgrid Engineering Operating System.

## Context

After the operating-system restructure, the repository used `handbook/` for canonical handbook books.

Further review identified two improvements:

- the folder should describe the physical contents as books, while the Engineering Handbook remains the concept;
- workflows should become first-class operating-system artefacts that describe how agents, Sentinel and approval gates coordinate.

## Objective

Rename `handbook/` to `books/`, introduce `workflows/`, keep top-level folders lowercase, and document Knowledge, Practice and Automation as conceptual categories rather than physical nesting.

## Scope

- Rename the canonical handbook folder to `books/`.
- Add a standard workflow catalogue.
- Update links and prompt samples.
- Record the structural decision.
- Preserve product repository guidance that product handbooks live under `docs/handbooks/`.
- Keep reviews as first-class artefacts without adding a root `reviews/` folder.

## Outputs

- [ADR-003: Adopt Books and Workflows Structure](../../decisions/ADR-003-adopt-books-and-workflows-structure.md)
- [Implementation Report](artefacts/03%20Implementation/Implementation%20Report.md)
- [Workflows](../../../workflows/README.md)

## Status

Complete.

## Navigation

**Initiatives**

- [Initiatives](../README.md)

**Repository**

- [Nestgrid Engineering Operating System](../../../README.md)
