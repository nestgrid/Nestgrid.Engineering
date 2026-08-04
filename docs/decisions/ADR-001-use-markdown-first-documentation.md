# ADR-001: Use Markdown-First Documentation

> Decision record for **Architecture**.

## Status

Accepted

## Type

Architecture

## Date

2026-07-19

## Owners

- Nestgrid Engineering Operating System maintainers

## Context

Nestgrid Engineering Operating System defines the methodology, standards and practices used across Nestgrid software engineering.

The repository needs documentation that is easy to read, review, version, search and maintain. It should work well in GitHub, local IDEs and AI-assisted engineering workflows without requiring a dedicated documentation platform from day one.

The team considered whether to use a documentation framework immediately or keep the repository Markdown-first.

## Decision

Nestgrid Engineering Operating System will use Markdown-first documentation with GitHub as the source of truth.

Documentation will be organised as plain Markdown files. The canonical handbook lives under `handbook/`, operating-system decisions and initiatives live under `docs/`, reusable templates live under `templates/`, and examples live under `samples/`.

A generated website or documentation portal may be added later as a presentation layer, but Markdown remains the source content.

## Rationale

Markdown keeps the repository simple, portable and easy to maintain.

It supports review through normal pull requests, works naturally in GitHub and IDEs, and avoids early operational overhead from documentation frameworks.

This approach also makes the operating system easier for engineers and AI tools to consume directly from the repository.

## Alternatives Considered

### Documentation Framework from the Start

Frameworks such as static site generators can provide navigation, themes, search and publishing workflows.

This was not chosen initially because the handbook first needs stable content, structure and standards. Introducing a framework too early would add maintenance before the content model is proven.

### Wiki-Based Documentation

A repository wiki can be quick to start, but it separates documentation from the normal repository workflow.

This weakens review, versioning and alignment with templates, samples and repository governance.

## Consequences

The repository remains lightweight and easy to contribute to.

Navigation must be maintained through clear README files and explicit Markdown links.

Markdown validation should be automated to reduce broken links and preserve trust.

If a website is needed later, it should be generated from the existing Markdown rather than replacing it.

## Related Decisions

- None

## Related Documentation

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)
- [Documentation](../../handbook/12%20Documentation/README.md)
- [Templates](../../handbook/13%20Templates/README.md)
- [Samples](../../handbook/14%20Samples/README.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
