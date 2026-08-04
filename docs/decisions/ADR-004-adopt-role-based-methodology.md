# ADR-004: Adopt Role-Based Methodology

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

The Nestgrid Engineering Operating System now contains handbook books, workflows, templates, roles and profiles.

Early workflow documentation referred directly to named agents such as Evelyn, Gideon, Mason, Harper, Morgan, Rowan and Sentinel. That was useful while establishing the operating model, but it coupled the methodology to the current agent roster.

The methodology should be usable by humans, agents, automation or mixed teams.

## Decision

The Engineering Operating System methodology will use role names in handbook books, templates and workflows.

Named profiles are implementations of those roles, not the methodology itself.

Standard roles are:

- Project Sponsor
- Product Owner
- Solution Architect
- Software Engineer
- Quality Engineer
- Security Engineer
- Platform Engineer
- Independent Reviewer

Agent documents may continue to use agent names and should map each agent to the role it fulfils.

## Rationale

Role-based language keeps the methodology durable, professional and independent of execution mechanism.

It allows the same workflow to be followed by:

- human specialists;
- named profiles;
- automation;
- or mixed human and agent teams.

It also makes workflows clearer for downstream execution because each participant is identified by responsibility rather than persona.

## Alternatives Considered

### Keep Agent Names in the Methodology

This was rejected because it makes the handbook appear dependent on the current agent roster.

### Remove Agent Names Entirely

This was rejected because profiles are useful execution guidance. Profile names should remain in `profiles/`, prompt samples and historical records where they provide operational context.

## Consequences

Handbook books, templates and workflows should refer to roles rather than named agents.

The profiles catalogue becomes the mapping layer between canonical role responsibility and named execution guidance.

Review artefacts should use `Independent Review` as the standard artefact name. Sentinel remains the current Independent Reviewer agent profile.

Historical decision records and initiative artefacts may retain agent names when they describe work that already occurred.

## Related Decisions

- [ADR-003: Adopt Books and Workflows Structure](ADR-003-adopt-books-and-workflows-structure.md)

## Related Documentation

- [Roles and Responsibilities](../../books/15%20Engineering%20Workflow/02%20Roles%20and%20Responsibilities.md)
- [Roles](../../roles/README.md)
- [Profiles](../../profiles/README.md)
- [Workflows](../../workflows/README.md)
- [Independent Review Template](../../templates/artefacts/Independent%20Review.Template.md)

---

## Navigation

**Decision Index**

- [Decisions](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
