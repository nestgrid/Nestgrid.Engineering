# ADR-005: Adopt Roles and Profiles Separation

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

The Engineering Operating System methodology is role-based. The previous repository structure kept named agent documents under `agents/`, which made the execution profiles and canonical engineering disciplines appear to be the same thing.

The methodology should remain agnostic of whether work is performed by humans, named agents, automation or mixed teams.

## Decision

Separate roles and profiles into distinct top-level directories.

The repository will use:

```text
roles/
profiles/
```

`roles/` contains canonical engineering disciplines and is authoritative for responsibilities, authority, inputs, outputs, artefacts, working process and Definition of Done.

`profiles/` contains named implementations of roles and is authoritative only for profile style, tone, behavioural emphasis and execution preferences.

## Role and Profile Definitions

Role means canonical engineering discipline, responsibility, authority, inputs, outputs, artefacts, working process and Definition of Done.

Profile means implementation style, personality, tone, behavioural guidance and specialist bias for executing a role.

When role guidance and profile guidance overlap, the role is authoritative.

## Rationale

This keeps the methodology durable and independent of the current profile roster.

A Software Engineer role can be fulfilled by a human engineer, Mason, another future profile or automation without changing the handbook or workflows.

Profiles can evolve independently without changing the canonical role responsibilities.

## Alternatives Considered

### Keep `agents/`

This was rejected because `agents/` over-emphasises the current execution mechanism.

### Use `agents/roles/` and `agents/profiles/`

This was rejected because roles are not agent-specific. They belong at the top level of the operating system.

## Consequences

Handbook books, templates and workflows should reference roles.

Prompt samples should reference both roles and profiles.

Named execution guidance should read the role first and the profile second.

The previous `agents/` directory is replaced by `roles/` and `profiles/`.

Historical records may retain `agents/` language where they describe past repository states or earlier decisions.

## Related Decisions

- [ADR-004: Adopt Role-Based Methodology](ADR-004-adopt-role-based-methodology.md)

## Related Documentation

- [Roles](../../roles/README.md)
- [Profiles](../../profiles/README.md)
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
