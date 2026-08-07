# Discovery Note

```yaml
title: Commandable Engineering Operating System
version: 0.1
status: Proposed
owner: Nestgrid Engineering
contributors:
  - Project Sponsor
  - Codex
produced_by: Product Owner
consumed_by: Project Sponsor, Solution Architect, Software Engineer
date: 2026-08-07
supersedes:
related_decisions:
related_work_items:
related_repositories:
  - engineering
```

## Summary

The Nestgrid Engineering Operating System has reached a strong written-methodology state.

The next possible refinement is to make the EOS commandable before making it fully runnable.

Commandable means humans and agents can invoke standard lifecycle actions using consistent prompts or commands while the Project Sponsor still controls approval and progression.

## Insight

The EOS should not copy agent workflow tools wholesale.

However, workflow tools demonstrate the value of clear commands that reduce friction when starting, progressing or reviewing work.

Nestgrid can adopt that ergonomics while preserving its stronger role-based, artefact-led operating model.

## Proposed Direction

Introduce a command layer as a future EOS capability.

Commands should:

- be role-based rather than profile-specific;
- identify required inputs;
- state expected outputs;
- respect approval gates;
- preserve artefact locations;
- read prior reviews and decisions;
- be usable manually before automation exists;
- and be structured enough for a future Runner to execute.

## Candidate Evolution

```text
v1.0 Written EOS
Roles, profiles, books, templates, workflows and artefacts.

v1.5 Commandable EOS
Standard commands and prompts for invoking lifecycle actions consistently.

v2.0 Runnable EOS
A Runner can inspect repositories, select workflows, create artefacts and manage gates.

v3.0 Orchestrated EOS
Roles, profiles and Independent Reviews coordinate with reduced manual handover.
```

## Candidate Commands

- `start-opportunity`
- `run-discovery`
- `architecture-recommend`
- `architecture-execute`
- `engineering-plan`
- `engineering-execute`
- `quality-review`
- `security-review`
- `platform-readiness`
- `sentinel-review`
- `release-check`

## Recommendation

Keep this initiative proposed until more real product usage confirms the command set.

Do not implement Runner behaviour yet.

The next useful step is to design a small command catalogue and test it manually against active products such as Nestgrid.Diagnostics and Nestgrid.Finance.
