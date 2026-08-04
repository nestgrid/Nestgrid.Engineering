# TDR-001: Number Lifecycle Artefact Directories

> Decision record for **Technical**.

## Status

Accepted

## Type

Technical

Use the appropriate decision prefix:

- `BDR` for Business Decision Record.
- `PDR` for Product Decision Record.
- `TDR` for Technical Decision Record.
- `ADR` for Architectural Decision Record.

## Date

2026-07-22

## Owners

- Nestgrid Engineering

## Context

Nestgrid Engineering Operating System defines a standard project repository structure for product teams.

After applying the first iteration of the Engineering Handbook to Nestgrid.Finance, the lifecycle artefact directories were found to be clearer when ordered by lifecycle stage rather than by plain, unnumbered names.

The previous convention used unnumbered directory names:

```text
docs/
  artefacts/
    Discovery/
    Architecture/
    Implementation/
    Quality/
    Security/
    Platform/
    Release/
```

This structure described the stages, but did not make the intended lifecycle order visually obvious when browsing a repository.

## Decision

Lifecycle artefact directories in product repositories will use numbered names that reflect engineering workflow order:

```text
docs/
  artefacts/
    01 Discovery/
    02 Architecture/
    03 Implementation/
    04 Quality/
    05 Security/
    06 Platform/
    07 Release/
```

The numbering reflects the lifecycle sequence:

```text
Discovery
  -> Architecture
  -> Implementation
  -> Quality
  -> Security
  -> Platform
  -> Release
```

## Rationale

Numbered lifecycle artefact directories improve consistency with the handbook book structure.

They make the workflow order visible in file browsers, terminals and repository views.

They also reduce ambiguity for teams, contributors and tooling that need to locate lifecycle artefacts consistently.

## Alternatives Considered

### Keep Unnumbered Directories

This would avoid a small naming change, but lifecycle order would remain less obvious and folder order would vary by file browser or alphabetical sorting.

### Use Alphabetical Ordering

This was rejected because alphabetical ordering does not represent the engineering lifecycle.

The artefact structure should communicate workflow order, not lexical order.

## Consequences

Product repositories should create lifecycle artefact directories using the numbered convention.

Existing repositories using unnumbered lifecycle artefact directories should be aligned when practical.

Templates, samples and documentation should use the numbered directory names.

The lifecycle stages and artefact meanings are unchanged.

## Related Decisions

- [ADR-001: Use Markdown-First Documentation](ADR-001-use-markdown-first-documentation.md)

## Related Documentation

- [Repository Structure](../../handbook/07%20Solution%20Structure/01%20Repository%20Structure.md)
- [Repository Storage](../../handbook/16%20Engineering%20Artefacts/04%20Repository%20Storage.md)
- [Starting a Project Repository](../../handbook/16%20Engineering%20Artefacts/06%20Starting%20a%20Project%20Repository.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)