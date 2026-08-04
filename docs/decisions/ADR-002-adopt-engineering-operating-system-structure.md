# ADR-002: Adopt Engineering Operating System Structure

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

Nestgrid Engineering Operating System has evolved from a handbook into a broader operating model for engineering work.

The repository now contains handbook guidance, engineering agents, artefact templates, samples, decisions and lifecycle initiatives. Keeping the handbook books directly under `docs/` made the repository appear to be only a documentation handbook, while the agents lived outside the repository even though they had become part of the operating model.

The repository needs a structure that reflects the full operating system while preserving the product repository convention where product-specific handbook content lives under `docs/handbooks/`.

## Decision

The Nestgrid Engineering Operating System repository will use the following top-level structure:

```text
agents/
handbook/
docs/
  decisions/
  initiatives/
templates/
samples/
scripts/
```

Engineering agent documents will live under `agents/`.

The canonical global handbook will live under `handbook/`.

The `docs/` directory will contain durable records about the operating system itself, including `docs/decisions/` and `docs/initiatives/`.

Product repositories will continue to use `docs/handbooks/` for product-specific handbook knowledge.

## Rationale

This structure makes the operating system explicit.

Agents are no longer separate prompt documents outside the repository. They are part of the same operating model as the handbook, templates, samples and lifecycle records.

Moving the global handbook to `handbook/` separates canonical methodology from operating-system decisions and initiatives.

Keeping product repositories on `docs/handbooks/` preserves the established product convention and avoids confusing product documentation with the global operating-system handbook.

## Alternatives Considered

### Keep Handbook Books Under `docs/`

This was rejected because `docs/` had become overloaded. It contained both canonical handbook books and records about the evolution of the repository.

### Keep Agents in a Separate Repository or Folder

This was rejected because the agents are now part of the operating system. Keeping them separate weakens discoverability, versioning and traceability.

### Move Product Repository Convention to `handbook/`

This was rejected because product repositories are not operating-system repositories. Their enduring product knowledge should continue to live under `docs/handbooks/`.

## Consequences

The repository now communicates that it is an engineering operating system rather than only a handbook.

Links to handbook books must use `handbook/` instead of `docs/`.

Agents, handbook standards, decisions, initiatives, templates and samples can now evolve together in one repository.

Documentation validation remains important because structural changes affect many relative links.

## Related Decisions

- [ADR-001: Use Markdown-First Documentation](ADR-001-use-markdown-first-documentation.md)

## Related Documentation

- [Engineering Handbook](../../handbook/README.md)
- [Engineering Agents](../../agents/README.md)
- [Repository Structure](../../handbook/07%20Solution%20Structure/01%20Repository%20Structure.md)
- [Engineering Artefacts](../../handbook/16%20Engineering%20Artefacts/README.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
