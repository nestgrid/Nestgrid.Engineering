# Discovery Note

```yaml
title: EOS Extensibility: Roles and Capabilities
version: 0.1
status: Proposed
owner: Nestgrid Engineering
contributors:
  - Project Sponsor
  - Codex
produced_by: Product Owner
consumed_by: Project Sponsor, Solution Architect
date: 2026-08-08
supersedes:
related_decisions:
related_work_items:
related_repositories:
  - engineering
```

## Summary

The Nestgrid Engineering Operating System is becoming a general-purpose engineering methodology rather than an internal Nestgrid-only handbook.

As it moves toward open source use and possible commercial execution tooling, it needs a controlled way to evaluate additional roles, cross-cutting concerns and reusable capabilities.

## Current Assessment

The current EOS is strong in:

- engineering philosophy;
- lifecycle structure;
- role and profile separation;
- workflow;
- governance;
- artefact discipline;
- and extensibility.

The remaining work is not primarily about correcting mistakes.

It is about broadening the EOS without making it complicated.

## Candidate Evolution Dimensions

### More Roles

The current roles cover core engineering delivery.

Future optional roles may cover organisational or specialist needs:

- Product Designer;
- Technical Writer;
- Data Engineer;
- Performance Engineer;
- Developer Experience Engineer;
- Data Protection or Compliance Specialist;
- Site Reliability Engineer.

These should remain optional unless a workflow or product genuinely needs them.

### Cross-Cutting Concerns

The EOS should continue to make cross-cutting concerns visible early rather than discovering them at the end.

Candidate concerns include:

- Observability;
- Performance;
- Accessibility;
- Localisation;
- Privacy;
- Compliance;
- Resilience;
- Cost efficiency;
- Developer experience;
- documentation quality.

Operationalisation has already been formalised and provides a useful model.

### Executable Engineering

The long-term direction appears to be:

```text
Books
  -> Roles
  -> Profiles
  -> Capabilities
  -> Runner
```

Capabilities or Skills may become reusable execution units that sit between the methodology and a future Runner.

This keeps the EOS platform-independent because the same capability could be executed by a human, Codex, ChatGPT, Claude or another tool.

## Important Constraint

Avoid technology-specific roles.

The EOS should not create roles such as UI Agent, Database Agent, API Agent, React Agent or EF Agent.

Those belong in standards, samples, technical decisions or implementation guidance.

## Recommendation

Keep this initiative Proposed.

When resumed, Discovery should first assess whether to add Product Designer as an optional specialist role.

The next broader exploration should consider a Skills or Capability Model, but only after commandable workflows have been validated against real product work.
